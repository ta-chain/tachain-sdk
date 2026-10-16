# Tachain SDK

Open source clients for the **public Tactic Chain integration API**. The [main SDK source repository](https://github.com/ta-chain/tachain-sdk) pins [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) **7.25.0**, tracks the source OpenAPI export, and commits generated clients for eight languages. Each client can be built from source.

## Clients and package targets

| Language | Generator | Code | Intended package | Registry |
| --- | --- | --- | --- | --- |
| TypeScript | `typescript-fetch` | [`generated/typescript`](generated/typescript) | `@ta-chain/tachain-sdk` | npm |
| Python | `python` | [`generated/python`](generated/python) | `tachain-sdk` | PyPI |
| Java | `java` | [`generated/java`](generated/java) | `com.tachain:tachain-sdk` | Maven Central |
| C# | `csharp` | [`generated/csharp`](generated/csharp) | `Tachain.Sdk` | NuGet |
| Go | `go` | [`generated/go`](generated/go) | `github.com/ta-chain/tachain-sdk/generated/go` | Go modules |
| PHP | `php` | [`generated/php`](generated/php) · [standalone repository](https://github.com/ta-chain/tachain-sdk-php) | `ta-chain/tachain-sdk` | Packagist, via a split repository |
| Ruby | `ruby` | [`generated/ruby`](generated/ruby) | `tachain-sdk` | RubyGems |
| Swift | `swift5` | [`generated/swift`](generated/swift) · [standalone repository](https://github.com/ta-chain/tachain-sdk-swift) | `TachainSDK` | Swift Package Manager, via a split repository |

The main repository contains all eight generated clients. PHP and Swift also have standalone repositories with their package manifests at the repository root, so they can be used directly with Composer and Swift Package Manager. `sdk.config.json` is the single place to edit package coordinates and the release version. For a new version, edit it, regenerate, review and commit the resulting code, then manually dispatch the release workflow. Choose a version that is not already in the target registry.

## Regenerate

Requirements: Python 3.10+, Java 11+, and network access for the pinned generator JAR on first use. The JAR is downloaded from Maven Central to `.cache/` and checked against a pinned SHA-256 digest. It is not committed. To update the API contract, import a fresh full export from a path outside this repository, then regenerate:

```sh
python3 scripts/import_openapi.py /path/to/full-openapi-export.json
python3 scripts/generate.py
python3 scripts/sync_frontend_spec.py
```

The import script saves only `/v1/` integration operations and their reachable schemas to `source/openapi.json`; internal `/api/` endpoints from the upstream export are never committed. The generation script adds stable operation IDs and the actual authentication requirements, validates the public OpenAPI document, generates all eight SDKs, then applies the small maintained signature helpers and package metadata. Current input yields **45 public operations and 95 reachable schemas**, including material, product and process-route maintenance, reference mappings, declaration file upload, declaration verification and pending receipts. `openapi/tactic-chain-public.json` is the distributable contract.

The normalizer repairs known Apifox array-item references using the corresponding exported request models, converts nullable type arrays to OpenAPI 3.0 syntax, and exposes schema examples through `example` while preserving all exported examples in `x-export-examples`. Impossible object/string composition branches from the export are retained in `x-export-invalid-composition`; valid composition rules, required fields and conditional field descriptions remain in the contract. Unknown dangling references still fail validation.

The pinned generator's Python template needs a small generation-time fallback for composed request models. It keeps `FileId`/Base64 fields during dictionary conversion and leaves omitted alternatives absent, so uploaded files survive nested declaration submission. This workaround lives in `scripts/generate.py`; generated code remains reproducible. CI checks those round trips and TypeScript's signed reference queries and multipart uploads without calling a live API.

The sync script copies that contract to the sibling frontend's `public/openapi/tactic-chain-public.json`, which powers the SDK page and its AI prompt link. Run `python3 scripts/sync_frontend_spec.py --check` before publishing to detect drift. Supply `--frontend-root` when the projects are checked out in different locations.

Regenerate one language with `python3 scripts/generate.py typescript`. Generated directories are replaced by the script; put hand-maintained code in `helpers/`, `examples/`, or `scripts/`. CI reruns generation and checks for differences.

## Authentication

Create a credential in the Tactic Chain Token page and grant it access to the specific API methods. Set the SDK base URL to **your API service origin**, not the placeholder `https://api.example.com`. Each generated operation requires the `X-Credential-Type` argument:

- **Single Token:** pass `Token`, and configure standard bearer auth. The request must contain `Authorization: Bearer <token>` and `X-Credential-Type: Token`.
- **API Key + Secret:** pass `API Key`, and sign the **final URL** immediately before sending. The request must contain `X-API-Key`, `X-Timestamp` (Unix seconds), `X-Signature`, and `X-Credential-Type: API Key`. The server accepts timestamps within the endpoint's configured window (300 seconds by default).

For API Key mode, the server computes:

```text
normalizedQuery = decoded query keys grouped case-insensitively (first spelling retained),
                  then sorted ordinal;
                  for each key, decoded values sorted ordinal;
                  join key=value pairs with & (without re-encoding)
message = apiKey + timestamp + normalizedQuery
signature = lowercase_hex(HMAC_SHA256(UTF8(apiSecret), UTF8(message)))
```

The body is **not** included in the current backend signature. Duplicate query keys are retained. The signature must be calculated after the generated client has serialized query parameters. The shared tests cover ASCII, Unicode, and mixed-case keys in [`tests/`](tests).

All eight clients include maintained signing adapters that hook into the final network request:

| Client | Adapter | How to attach |
| --- | --- | --- |
| TypeScript | `signatureMiddleware` | `Configuration({ middleware: [signatureMiddleware(key, secret)] })` |
| Python | `SignedRESTClient` | `api_client.rest_client = SignedRESTClient(config, key, secret)` |
| Java | `SignatureInterceptor` | `apiClient.setHttpClient(apiClient.getHttpClient().newBuilder().addInterceptor(...).build())` |
| C# | `SignatureHandler` | Construct `HttpClient(new SignatureHandler(key, secret, new HttpClientHandler()))` and pass it to the API class |
| Go | `SignatureTransport` | Set `Configuration.HTTPClient` to an `http.Client` using the transport |
| PHP | `TachainSdk\Auth\SignatureMiddleware` | Push `SignatureMiddleware::create($key, $secret)` onto a Guzzle `HandlerStack` |
| Ruby | `TachainSdk::SignedApiClient` | Pass `SignedApiClient.new(config, api_key: key, api_secret: secret)` to the generated API class |
| Swift | `TachainSignature` | Call `TachainSignature.configure(apiKey: ..., apiSecret: ...)` before invoking the generated API |

For PHP, create a `HandlerStack`, push `SignatureMiddleware::create($key, $secret)`, construct a `GuzzleHttp\Client(['handler' => $stack])`, then pass that client to `new TachainSdk\Api\ApiEnumApi($client, $config)`. Swift's signer uses Apple `CommonCrypto` and the `URLSession` request builder; its package currently targets Apple SPM platforms. See [`examples/`](examples) for complete Token and API Key calls.

## Local builds

Clone the main source repository, then run the commands for your language from its root:

```sh
git clone https://github.com/ta-chain/tachain-sdk.git
cd tachain-sdk
```

```sh
npm install --prefix generated/typescript && npm run build --prefix generated/typescript
python3 -m pip install ./generated/python
mvn -f generated/java/pom.xml test
dotnet build generated/csharp/src/Tachain.Sdk/Tachain.Sdk.csproj
go -C generated/go test ./...
composer install --working-dir=generated/php
(cd generated/ruby && gem build tachain-sdk.gemspec)
swift build --package-path generated/swift
```

To build from the standalone package repositories instead, run either sequence from a directory outside the main checkout:

PHP ([source](https://github.com/ta-chain/tachain-sdk-php)):

```sh
git clone https://github.com/ta-chain/tachain-sdk-php.git
composer install --working-dir=tachain-sdk-php
```

Swift ([source](https://github.com/ta-chain/tachain-sdk-swift)):

```sh
git clone https://github.com/ta-chain/tachain-sdk-swift.git
swift build --package-path tachain-sdk-swift
```

Run only the commands for toolchains installed on your machine. The `examples/` directory shows per-language use against an API base URL and credential supplied through environment variables.

## Publishing

Release is manual through `.github/workflows/publish.yml`. In GitHub Actions, open **Publish SDK packages** and select **Run workflow**. Check **Publish all eight SDKs** to release every package in one run, or check any combination of language boxes to release a subset. Enter the version committed in `sdk.config.json` and type `publish` in the confirmation field. Leave **Publish all eight SDKs** unchecked when selecting individual languages; an empty or conflicting selection fails before publishing. Each selected package is built and published independently after the shared preflight. If only some packages fail, rerun the workflow with just those languages selected.

Publishing jobs use the GitHub `package-release` environment. **Configure required reviewers for that environment in repository settings** before publishing. The maintainers must verify the `ta-chain` npm scope, PyPI project ownership, Maven Central `com.tachain` namespace, NuGet ID, RubyGems name, Packagist vendor, and GitHub organization/repositories. Configure npm and PyPI trusted publishing for the workflow, and add `CENTRAL_USERNAME`, `CENTRAL_PASSWORD`, `MAVEN_GPG_PRIVATE_KEY`, `MAVEN_GPG_PASSPHRASE`, `NUGET_USER`, `RUBYGEMS_API_KEY`, and `SPLIT_REPO_TOKEN` as the relevant GitHub Actions secrets. Never commit registry tokens or GPG keys.

Go is a nested module and uses tags such as `generated/go/v0.1.0`. Packagist expects `composer.json` at a repository root, and Swift Package Manager expects `Package.swift` at a repository root. Consequently the generated PHP and Swift directories are mirrored into the [PHP](https://github.com/ta-chain/tachain-sdk-php) and [Swift](https://github.com/ta-chain/tachain-sdk-swift) release repositories and tagged there with the release version (for example, `v0.1.0`). Continue publishing them only from this repository's subtree history. The main monorepo URL is **not** a direct Composer or SPM package URL.

Maven Central publishing uses Sonatype's Central Publishing Maven plugin, attached sources/Javadoc, and the generated `sign-artifacts` GPG profile. Central Portal namespace verification and a user token are required for publishing. The release workflow does not run on ordinary commits or pull requests.

## License and contributions

The SDK and maintained helpers are MIT licensed; see [LICENSE](LICENSE). Generated files carry upstream OpenAPI Generator notices. Please make API contract updates through `source/openapi.json` and `scripts/generate.py`, with a focused review of the public spec and any changed client behavior. See [CONTRIBUTING.md](CONTRIBUTING.md).
