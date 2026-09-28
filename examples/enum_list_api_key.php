<?php

use GuzzleHttp\Client;
use GuzzleHttp\HandlerStack;
use TachainSdk\Api\ApiEnumApi;
use TachainSdk\Auth\SignatureMiddleware;
use TachainSdk\Configuration;

require __DIR__ . '/../generated/php/vendor/autoload.php';

$baseUrl = getenv('TAC_BASE_URL') ?: throw new RuntimeException('Set TAC_BASE_URL');
$apiKey = getenv('TAC_API_KEY') ?: throw new RuntimeException('Set TAC_API_KEY');
$apiSecret = getenv('TAC_API_SECRET') ?: throw new RuntimeException('Set TAC_API_SECRET');

$stack = HandlerStack::create();
$stack->push(SignatureMiddleware::create($apiKey, $apiSecret));
$http = new Client(['handler' => $stack]);
$config = Configuration::getDefaultConfiguration()->setHost($baseUrl);
$api = new ApiEnumApi($http, $config);
print_r($api->getV1EnumGetList('API Key'));
