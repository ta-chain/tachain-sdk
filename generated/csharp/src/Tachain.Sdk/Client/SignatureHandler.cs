using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Tachain.Sdk.Client
{
    /// <summary>Signs the final HttpRequestMessage URI before transmission.</summary>
    public sealed class SignatureHandler : DelegatingHandler
    {
        private readonly string _apiKey;
        private readonly string _apiSecret;

        /// <summary>Creates a signer for requests sent through <paramref name="innerHandler"/>.</summary>
        public SignatureHandler(string apiKey, string apiSecret, HttpMessageHandler innerHandler)
            : base(innerHandler)
        {
            _apiKey = apiKey;
            _apiSecret = apiSecret;
        }

        /// <summary>Normalizes the final URI query using the backend's ordinal ordering.</summary>
        public static string NormalizeQuery(Uri uri)
        {
            var values = new Dictionary<string, (string Key, List<string> Values)>(StringComparer.OrdinalIgnoreCase);
            var raw = uri.Query.TrimStart('?');
            foreach (var item in raw.Split('&', StringSplitOptions.RemoveEmptyEntries))
            {
                var pair = item.Split('=', 2);
                var key = Uri.UnescapeDataString(pair[0].Replace('+', ' '));
                var value = Uri.UnescapeDataString((pair.Length > 1 ? pair[1] : "").Replace('+', ' '));
                if (!values.TryGetValue(key, out var group))
                {
                    group = (key, new List<string>());
                    values[key] = group;
                }
                group.Values.Add(value);
            }
            return string.Join("&", values.Values.OrderBy(group => group.Key, StringComparer.Ordinal).SelectMany(group =>
                group.Values.OrderBy(value => value, StringComparer.Ordinal)
                    .Select(value => group.Key + "=" + value)));
        }

        /// <summary>Computes lowercase HMAC-SHA256 for the supplied timestamp and URI.</summary>
        public static string ComputeSignature(string apiKey, string apiSecret, string timestamp, Uri uri)
        {
            var message = apiKey + timestamp + NormalizeQuery(uri);
            using var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(apiSecret));
            return Convert.ToHexString(hmac.ComputeHash(Encoding.UTF8.GetBytes(message))).ToLowerInvariant();
        }

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            if (request.RequestUri == null) throw new InvalidOperationException("Request URI is required for signing.");
            var timestamp = DateTimeOffset.UtcNow.ToUnixTimeSeconds().ToString(System.Globalization.CultureInfo.InvariantCulture);
            request.Headers.Authorization = null;
            request.Headers.Remove("X-Credential-Type");
            request.Headers.Remove("X-API-Key");
            request.Headers.Remove("X-Timestamp");
            request.Headers.Remove("X-Signature");
            request.Headers.TryAddWithoutValidation("X-Credential-Type", "API Key");
            request.Headers.TryAddWithoutValidation("X-API-Key", _apiKey);
            request.Headers.TryAddWithoutValidation("X-Timestamp", timestamp);
            request.Headers.TryAddWithoutValidation("X-Signature", ComputeSignature(_apiKey, _apiSecret, timestamp, request.RequestUri));
            return base.SendAsync(request, cancellationToken);
        }
    }
}
