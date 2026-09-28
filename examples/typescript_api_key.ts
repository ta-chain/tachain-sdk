// Install the generated package and set TAC_BASE_URL, TAC_API_KEY, TAC_API_SECRET.
// Keep API secrets in a server-side environment; do not bundle them into browser code.
import {
  ApiEnumApi,
  Configuration,
  signatureMiddleware,
} from '@ta-chain/tachain-sdk'

const basePath = process.env.TAC_BASE_URL
const apiKey = process.env.TAC_API_KEY
const apiSecret = process.env.TAC_API_SECRET
if (!basePath || !apiKey || !apiSecret) {
  throw new Error('Set TAC_BASE_URL, TAC_API_KEY and TAC_API_SECRET')
}

const configuration = new Configuration({
  basePath,
  middleware: [signatureMiddleware(apiKey, apiSecret)],
})
const api = new ApiEnumApi(configuration)
api.getV1EnumGetList({ xCredentialType: 'API Key' })
  .then(console.log)
  .catch((error: unknown) => {
    console.error('API request failed', error)
    process.exitCode = 1
  })
