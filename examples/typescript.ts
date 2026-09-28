// After publishing/installing @ta-chain/tachain-sdk.
// Set TAC_BASE_URL and TAC_TOKEN in the server-side environment.
import { ApiEnumApi, Configuration } from '@ta-chain/tachain-sdk'

const basePath = process.env.TAC_BASE_URL
const token = process.env.TAC_TOKEN
if (!basePath || !token) {
  throw new Error('Set TAC_BASE_URL and TAC_TOKEN before running this example')
}

const api = new ApiEnumApi(new Configuration({ basePath, accessToken: token }))

async function main() {
  const result = await api.getV1EnumGetList({ xCredentialType: 'Token' })
  console.log(result)
}

main().catch((error: unknown) => {
  console.error('API request failed', error)
  process.exitCode = 1
})
