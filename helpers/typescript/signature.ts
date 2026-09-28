import type { Middleware } from './runtime';

/** Match SignatureHelper.NormalizeQueryString in the Tactic Chain API. */
export function normalizeQuery(url: string): string {
    const values = new Map<string, { key: string; values: string[] }>();
    for (const [key, value] of new URL(url).searchParams) {
        const folded = key.toLowerCase();
        const group = values.get(folded);
        if (group) group.values.push(value);
        else values.set(folded, { key, values: [value] });
    }
    const parts: string[] = [];
    for (const group of [...values.values()].sort((a, b) => a.key < b.key ? -1 : a.key > b.key ? 1 : 0)) {
        for (const value of group.values.sort()) {
            parts.push(`${group.key}=${value}`);
        }
    }
    return parts.join('&');
}

/** Lowercase hex HMAC-SHA256(apiKey + unixSeconds + normalizedQuery). */
export async function computeSignature(
    apiKey: string,
    apiSecret: string,
    timestamp: string,
    url: string,
): Promise<string> {
    const encoder = new TextEncoder();
    const key = await crypto.subtle.importKey(
        'raw', encoder.encode(apiSecret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign'],
    );
    const content = apiKey + timestamp + normalizeQuery(url);
    const digest = await crypto.subtle.sign('HMAC', key, encoder.encode(content));
    return [...new Uint8Array(digest)].map((byte) => ('0' + byte.toString(16)).slice(-2)).join('');
}

/** Sign the final generated URL immediately before fetch; never sign the JSON body. */
export function signatureMiddleware(apiKey: string, apiSecret: string): Middleware {
    return {
        pre: async ({ url, init }) => {
            const timestamp = String(Math.floor(Date.now() / 1000));
            const headers = new Headers(init.headers);
            headers.delete('Authorization');
            headers.set('X-Credential-Type', 'API Key');
            headers.set('X-API-Key', apiKey);
            headers.set('X-Timestamp', timestamp);
            headers.set('X-Signature', await computeSignature(apiKey, apiSecret, timestamp, url));
            return { url, init: { ...init, headers } };
        },
    };
}
