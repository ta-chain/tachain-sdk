const assert = require('node:assert/strict');
const sdk = require('../generated/typescript/dist/index.js');

(async () => {
  const requests = [];
  const fetchApi = async (url, init) => {
    requests.push({ url, init });
    return new Response(JSON.stringify({ code: 200, data: { fileId: 'uploaded-file' } }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  };
  const tokenConfig = new sdk.Configuration({
    basePath: 'https://api.example.com', accessToken: 'test-token', fetchApi,
  });
  await new sdk.ApiOrderApi(tokenConfig).postV1OrderCreate({
    xCredentialType: 'Token',
    tacticChainApiServiceControllersApiIntegrationV1ApiOrderCreateRequest: {
      orderNumber: 'PO-001', orderDate: new Date('2026-10-09T00:00:00Z'), scopeCode: 'T3',
      orderLines: [{ lineNumber: '10', materialCode: 'MAT-001', quantity: 100, unit: 'kg' }],
    },
  });
  const order = requests.pop();
  assert.equal(order.url, 'https://api.example.com/v1/order/Create');
  assert.equal(new Headers(order.init.headers).get('Authorization'), 'Bearer test-token');
  assert.equal(new Headers(order.init.headers).get('X-Credential-Type'), 'Token');
  assert.deepEqual(JSON.parse(order.init.body).orderLines, [
    { lineNumber: '10', materialCode: 'MAT-001', quantity: 100, unit: 'kg' },
  ], 'Repaired array references must serialize the actual line fields');

  const signedConfig = new sdk.Configuration({
    basePath: 'https://api.example.com', accessToken: 'must-be-removed', fetchApi,
    middleware: [sdk.signatureMiddleware('test-key', 'test-secret')],
  });
  await new sdk.ApiReferenceApi(signedConfig).getV1ReferenceMappings({
    xCredentialType: 'API Key', mappedTable: 'Material', externalValue: 'MAT +中', page: 2,
  });
  const reference = requests.pop();
  const headers = new Headers(reference.init.headers);
  assert.equal(new URL(reference.url).searchParams.get('externalValue'), 'MAT +中');
  assert.equal(headers.get('Authorization'), null);
  assert.equal(headers.get('X-Signature'), await sdk.computeSignature(
    'test-key', 'test-secret', headers.get('X-Timestamp'), reference.url,
  ), 'Sign the final encoded reference-query URL');

  const uploadResult = await new sdk.ApiDeclarationUploadApi(signedConfig).postV1DeclarationUploadFile({
    xCredentialType: 'API Key', file: new Blob(['file contents'], { type: 'application/pdf' }),
  });
  const upload = requests.pop();
  assert.equal(upload.url, 'https://api.example.com/v1/declaration/UploadFile');
  assert.equal(upload.init.method, 'POST');
  assert.ok(upload.init.body instanceof FormData);
  assert.equal(await upload.init.body.get('file').text(), 'file contents');
  assert.equal(new Headers(upload.init.headers).get('Content-Type'), null,
    'The fetch implementation must set the multipart boundary');
  assert.equal(new Headers(upload.init.headers).get('X-Credential-Type'), 'API Key');
  assert.equal(uploadResult.data.fileId, 'uploaded-file');
  console.log('TypeScript request serialization, signed reference query and multipart upload passed');
})().catch((error) => { console.error(error); process.exitCode = 1; });
