// Add a reference to the generated Tachain.Sdk package first.
using System;
using System.Net.Http;
using System.Threading.Tasks;
using Tachain.Sdk.Api;
using Tachain.Sdk.Client;

public static class EnumList
{
    public static async Task Main()
    {
        var baseUrl = Environment.GetEnvironmentVariable("TAC_BASE_URL")
            ?? throw new InvalidOperationException("Set TAC_BASE_URL");
        var token = Environment.GetEnvironmentVariable("TAC_TOKEN")
            ?? throw new InvalidOperationException("Set TAC_TOKEN");
        var configuration = new Configuration { BasePath = baseUrl, AccessToken = token };
        using var httpClient = new HttpClient();
        var api = new ApiEnumApi(httpClient, configuration);
        Console.WriteLine(await api.GetV1EnumGetListAsync("Token"));
    }
}
