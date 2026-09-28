<?php
// Run composer install in generated/php before using this local example.
require __DIR__ . '/../generated/php/vendor/autoload.php';

$baseUrl = getenv('TAC_BASE_URL');
$token = getenv('TAC_TOKEN');
if (!$baseUrl || !$token) {
    throw new RuntimeException('Set TAC_BASE_URL and TAC_TOKEN');
}

$config = TachainSdk\Configuration::getDefaultConfiguration()
    ->setHost($baseUrl)
    ->setAccessToken($token);
$api = new TachainSdk\Api\ApiEnumApi(new GuzzleHttp\Client(), $config);
print_r($api->getV1EnumGetList('Token'));
