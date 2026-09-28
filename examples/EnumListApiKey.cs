// Add a reference to the generated SDK package and set the environment variables.
using System;
using System.Net.Http;
using System.Threading.Tasks;
using Tachain.Sdk.Api;
using Tachain.Sdk.Client;

public static class EnumListApiKey
{
    public static async Task Main()
    {
        var baseUrl = Environment.GetEnvironmentVariable("TAC_BASE_URL")
            ?? throw new InvalidOperationException("Set TAC_BASE_URL");
        var apiKey = Environment.GetEnvironmentVariable("TAC_API_KEY")
            ?? throw new InvalidOperationException("Set TAC_API_KEY");
        var apiSecret = Environment.GetEnvironmentVariable("TAC_API_SECRET")
            ?? throw new InvalidOperationException("Set TAC_API_SECRET");
        using var httpClient = new HttpClient(
            new SignatureHandler(apiKey, apiSecret, new HttpClientHandler()));
        var api = new ApiEnumApi(httpClient, new Configuration { BasePath = baseUrl });
        Console.WriteLine(await api.GetV1EnumGetListAsync("API Key"));
    }
}
