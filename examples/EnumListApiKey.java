// Install the generated Java client and set TAC_BASE_URL, TAC_API_KEY, TAC_API_SECRET.
import com.tachain.sdk.api.ApiEnumApi;
import com.tachain.sdk.client.ApiClient;
import com.tachain.sdk.client.ApiException;
import com.tachain.sdk.client.SignatureInterceptor;

public final class EnumListApiKey {
    public static void main(String[] args) throws ApiException {
        String baseUrl = System.getenv("TAC_BASE_URL");
        String apiKey = System.getenv("TAC_API_KEY");
        String apiSecret = System.getenv("TAC_API_SECRET");
        if (baseUrl == null || apiKey == null || apiSecret == null) {
            throw new IllegalStateException("Set TAC_BASE_URL, TAC_API_KEY and TAC_API_SECRET");
        }
        ApiClient client = new ApiClient();
        client.setBasePath(baseUrl);
        client.setHttpClient(client.getHttpClient().newBuilder()
            .addInterceptor(new SignatureInterceptor(apiKey, apiSecret)).build());
        System.out.println(new ApiEnumApi(client).getV1EnumGetList("API Key", null));
    }
}
