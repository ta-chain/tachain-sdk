package com.tachain.sdk.client;

import java.nio.charset.StandardCharsets;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Locale;
import java.util.Map;
import java.util.List;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import okhttp3.HttpUrl;
import okhttp3.Interceptor;
import okhttp3.Request;
import okhttp3.Response;
import java.io.IOException;

/** Signs the final OkHttp URL immediately before transmission. */
public final class SignatureInterceptor implements Interceptor {
    private final String apiKey;
    private final String apiSecret;

    public SignatureInterceptor(String apiKey, String apiSecret) {
        this.apiKey = apiKey;
        this.apiSecret = apiSecret;
    }

    public static String normalizeQuery(HttpUrl url) {
        Map<String, QueryGroup> groups = new LinkedHashMap<>();
        for (int index = 0; index < url.querySize(); index++) {
            String key = url.queryParameterName(index);
            String value = url.queryParameterValue(index);
            groups.computeIfAbsent(key.toLowerCase(Locale.ROOT), ignored -> new QueryGroup(key))
                .values.add(value == null ? "" : value);
        }
        List<QueryGroup> sorted = new ArrayList<>(groups.values());
        sorted.sort((left, right) -> left.key.compareTo(right.key));
        List<String> parts = new ArrayList<>();
        for (QueryGroup group : sorted) {
            Collections.sort(group.values);
            for (String value : group.values) parts.add(group.key + "=" + value);
        }
        return String.join("&", parts);
    }

    private static final class QueryGroup {
        final String key;
        final List<String> values = new ArrayList<>();
        QueryGroup(String key) { this.key = key; }
    }

    public static String computeSignature(String apiKey, String apiSecret, String timestamp, HttpUrl url) {
        try {
            Mac mac = Mac.getInstance("HmacSHA256");
            mac.init(new SecretKeySpec(apiSecret.getBytes(StandardCharsets.UTF_8), "HmacSHA256"));
            byte[] digest = mac.doFinal((apiKey + timestamp + normalizeQuery(url)).getBytes(StandardCharsets.UTF_8));
            StringBuilder hex = new StringBuilder(digest.length * 2);
            for (byte b : digest) hex.append(String.format("%02x", b & 0xff));
            return hex.toString();
        } catch (Exception error) {
            throw new IllegalStateException("Unable to sign API request", error);
        }
    }

    @Override
    public Response intercept(Chain chain) throws IOException {
        Request original = chain.request();
        String timestamp = Long.toString(Instant.now().getEpochSecond());
        Request signed = original.newBuilder()
            .removeHeader("Authorization")
            .header("X-Credential-Type", "API Key")
            .header("X-API-Key", apiKey)
            .header("X-Timestamp", timestamp)
            .header("X-Signature", computeSignature(apiKey, apiSecret, timestamp, original.url()))
            .build();
        return chain.proceed(signed);
    }
}
