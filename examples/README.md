# Integration examples

The examples use generated API classes and call `GET /v1/enum/GetList`.
Set `TAC_BASE_URL` to your API service origin and create a credential with
permission for that endpoint and HTTP method. Read secrets from the server-side
environment; never put a Token or API Secret in a browser bundle.

| Language | Token | API Key + Secret |
| --- | --- | --- |
| TypeScript | [`typescript.ts`](typescript.ts) | [`typescript_api_key.ts`](typescript_api_key.ts) |
| Python | [`python.py`](python.py) | [`python_api_key.py`](python_api_key.py) |
| Java | [`EnumList.java`](EnumList.java) | [`EnumListApiKey.java`](EnumListApiKey.java) |
| C# | [`EnumList.cs`](EnumList.cs) | [`EnumListApiKey.cs`](EnumListApiKey.cs) |
| Go | [`enum_list.go`](enum_list.go) | [`enum_list_api_key.go`](enum_list_api_key.go) |
| PHP | [`enum_list.php`](enum_list.php) | [`enum_list_api_key.php`](enum_list_api_key.php) |
| Ruby | [`enum_list.rb`](enum_list.rb) | [`enum_list_api_key.rb`](enum_list_api_key.rb) |
| Swift | [`EnumList.swift`](EnumList.swift) | [`SignedEnumList.swift`](SignedEnumList.swift) |

All eight generated clients include signing adapters for API Key + Secret.
The adapters sign the final serialized URL as described in the repository README.

Install a published package or build the client from source before running an
example. The [main source repository](https://github.com/ta-chain/tachain-sdk)
contains all eight clients under `generated/<language>`; see its
[local build commands](../README.md#local-builds). PHP and Swift also have
standalone package repositories: [PHP](https://github.com/ta-chain/tachain-sdk-php)
and [Swift](https://github.com/ta-chain/tachain-sdk-swift).
Each example is standalone; for languages with two example files, run one at a
time.
