package tachainsdk

import (
    "net/url"
    "testing"
)

func TestSignatureVectors(t *testing.T) {
    cases := []struct { raw, normalized, signature string }{
        {"https://api.example.com/v1/enum/GetList?b=z&x=%2B+&b=a&A=1", "A=1&b=a&b=z&x=+ ", "a4283936739171659a2b1be9e098c62f9b9e7a5a92430e76e6dd42f260a3110e"},
        {"https://api.example.com/v1/enum/GetList?a=%EE%80%80&a=%F0%90%80%80", "a=𐀀&a=", "cffe13c9fa916b79d7f2ccacb4403c0bd5af1b5221414564a4571581b3b152eb"},
        {"https://api.example.com/v1/enum/GetList?a=2&A=1", "a=1&a=2", "6e9e61ed01c34368c2534b52037712c112ae0f7bb1045e3e81a25eb1b5a44f51"},
    }
    for _, test := range cases {
        parsed, err := url.Parse(test.raw)
        if err != nil { t.Fatal(err) }
        if got := NormalizeQuery(parsed); got != test.normalized { t.Errorf("normalize %q: got %q", test.raw, got) }
        if got := ComputeSignature("demo-key", "demo-secret", "1790586000", parsed); got != test.signature { t.Errorf("sign %q: got %q", test.raw, got) }
    }
}
