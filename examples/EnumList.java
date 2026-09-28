// Add the generated Java client to your project before compiling this file.
// Set TAC_BASE_URL and TAC_TOKEN in the server-side environment.
import com.tachain.sdk.api.ApiEnumApi;
import com.tachain.sdk.client.ApiClient;
import com.tachain.sdk.client.ApiException;
import com.tachain.sdk.client.auth.HttpBearerAuth;

public final class EnumList {
    public static void main(String[] args) throws ApiException {
        String baseUrl = System.getenv("TAC_BASE_URL");
        String token = System.getenv("TAC_TOKEN");
        if (baseUrl == null || token == null) {
            throw new IllegalStateException("Set TAC_BASE_URL and TAC_TOKEN");
        }
        ApiClient client = new ApiClient();
        client.setBasePath(baseUrl);
        ((HttpBearerAuth) client.getAuthentication("BearerToken")).setBearerToken(token);
        System.out.println(new ApiEnumApi(client).getV1EnumGetList("Token", null));
    }
}
