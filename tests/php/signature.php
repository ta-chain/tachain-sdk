<?php

declare(strict_types=1);

require __DIR__ . '/../../generated/php/vendor/autoload.php';

use GuzzleHttp\Client;
use GuzzleHttp\HandlerStack;
use GuzzleHttp\Promise\Create;
use GuzzleHttp\Psr7\Response;
use Psr\Http\Message\RequestInterface;
use TachainSdk\Api\ApiEnumApi;
use TachainSdk\Auth\SignatureMiddleware;
use TachainSdk\Configuration;

foreach (['signature-vector.json', 'signature-unicode-vector.json', 'signature-case-vector.json'] as $name) {
    $vector = json_decode(file_get_contents(__DIR__ . '/../' . $name), true, 512, JSON_THROW_ON_ERROR);
    if (SignatureMiddleware::normalizeQuery($vector['url']) !== $vector['normalizedQuery']) {
        throw new RuntimeException('Normalization mismatch: ' . $name);
    }
    if (SignatureMiddleware::computeSignature($vector['apiKey'], $vector['apiSecret'], $vector['timestamp'], $vector['url']) !== $vector['signature']) {
        throw new RuntimeException('Signature mismatch: ' . $name);
    }
}

$captured = null;
$stack = HandlerStack::create(static function (RequestInterface $request, array $options) use (&$captured) {
    $captured = $request;
    return Create::promiseFor(new Response(200, [], '{}'));
});
$stack->push(SignatureMiddleware::create('demo-key', 'demo-secret', static fn (): int => 1790586000));
$client = new Client(['handler' => $stack]);
$config = (new Configuration())->setHost('https://api.example.com');
$api = new ApiEnumApi($client, $config);
$request = $api->getV1EnumGetListRequest('API Key', ['Unit', 'Supplier'])
    ->withHeader('Authorization', 'Bearer stale');
$client->send($request);
if (!$captured || $captured->getHeaderLine('Authorization') !== '') {
    throw new RuntimeException('Signed request kept stale Bearer auth');
}
if ($captured->getHeaderLine('X-Credential-Type') !== 'API Key' || $captured->getHeaderLine('X-API-Key') !== 'demo-key') {
    throw new RuntimeException('API Key headers missing');
}
if ($captured->getHeaderLine('X-Signature') !== SignatureMiddleware::computeSignature('demo-key', 'demo-secret', '1790586000', (string) $captured->getUri())) {
    throw new RuntimeException('Final URI signature mismatch');
}

echo "PHP signature vectors and signed GET passed\n";
