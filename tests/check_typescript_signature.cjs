const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const { normalizeQuery, computeSignature } = require('../generated/typescript/dist/signature.js');

(async () => {
  for (const name of ['signature-vector.json', 'signature-unicode-vector.json', 'signature-case-vector.json']) {
    const vector = JSON.parse(fs.readFileSync(path.join(__dirname, name), 'utf8'));
    assert.equal(normalizeQuery(vector.url), vector.normalizedQuery, name);
    assert.equal(
      await computeSignature(vector.apiKey, vector.apiSecret, vector.timestamp, vector.url),
      vector.signature,
      name,
    );
  }
  console.log('TypeScript signature vectors passed');
})().catch((error) => { console.error(error); process.exitCode = 1; });
