<?php

declare(strict_types=1);

namespace TachainSdk\Auth;

use Psr\Http\Message\RequestInterface;

/** Signs the final Guzzle request URI for API Key + Secret credentials. */
final class SignatureMiddleware
{
    public static function normalizeQuery(string $url): string
    {
        $query = parse_url($url, PHP_URL_QUERY);
        if ($query === null || $query === false || $query === '') {
            return '';
        }

        // QueryHelpers.ParseQuery groups keys case-insensitively and retains the
        // spelling of the first occurrence. Do not use parse_str: it discards
        // duplicate keys and changes dots/spaces in parameter names.
        $groups = [];
        foreach (explode('&', $query) as $part) {
            if ($part === '') {
                continue;
            }
            $pair = explode('=', $part, 2);
            $key = urldecode($pair[0]);
            $value = urldecode($pair[1] ?? '');
            $lookup = strtolower($key);
            if (!isset($groups[$lookup])) {
                $groups[$lookup] = ['key' => $key, 'values' => []];
            }
            $groups[$lookup]['values'][] = $value;
        }

        $ordinal = static function (string $a, string $b): int {
            return strcmp(
                mb_convert_encoding($a, 'UTF-16BE', 'UTF-8'),
                mb_convert_encoding($b, 'UTF-16BE', 'UTF-8')
            );
        };
        $entries = array_values($groups);
        usort($entries, static fn (array $a, array $b): int => $ordinal($a['key'], $b['key']));
        $parts = [];
        foreach ($entries as $entry) {
            usort($entry['values'], $ordinal);
            foreach ($entry['values'] as $value) {
                $parts[] = $entry['key'] . '=' . $value;
            }
        }
        return implode('&', $parts);
    }

    public static function computeSignature(string $apiKey, string $apiSecret, string $timestamp, string $url): string
    {
        return hash_hmac('sha256', $apiKey . $timestamp . self::normalizeQuery($url), $apiSecret);
    }

    /**
     * Push the returned middleware onto a Guzzle HandlerStack and pass its
     * Client to a generated API class. $clock allows deterministic tests.
     */
    public static function create(string $apiKey, string $apiSecret, ?callable $clock = null): callable
    {
        $clock = $clock ?? static fn (): int => time();
        return static function (callable $handler) use ($apiKey, $apiSecret, $clock): callable {
            return static function (RequestInterface $request, array $options) use ($handler, $apiKey, $apiSecret, $clock) {
                $timestamp = (string) $clock();
                $url = (string) $request->getUri();
                $request = $request->withoutHeader('Authorization')
                    ->withHeader('X-Credential-Type', 'API Key')
                    ->withHeader('X-API-Key', $apiKey)
                    ->withHeader('X-Timestamp', $timestamp)
                    ->withHeader('X-Signature', self::computeSignature($apiKey, $apiSecret, $timestamp, $url));
                return $handler($request, $options);
            };
        };
    }
}
