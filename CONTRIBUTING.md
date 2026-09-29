# Contributing

1. Open an issue or pull request describing the API change or generator problem.
2. Import a fresh backend export with `python3 scripts/import_openapi.py /path/to/full-openapi-export.json`. The script removes internal endpoints before writing `source/openapi.json`.
3. Run `python3 scripts/generate.py` and inspect `openapi/tactic-chain-public.json` and the eight generated clients.
4. Put custom authentication code in `helpers/`; the generator copies it into supported packages. Do not hand-edit generated code.
5. Run the available local builds and the shared signature vector checks before submitting.

Do not commit credentials, release tokens, private keys, or a downloaded generator JAR. Package publishing is handled by the manual release workflow after maintainers configure the registries. NuGet.org publishing uses Trusted Publishing; configure the `package-release` environment secret `NUGET_USER` with the NuGet.org profile name (not an email address), and configure the NuGet policy for this repository's `publish.yml` workflow and `package-release` environment.
