package tachainsdk

import (
    "crypto/hmac"
    "crypto/sha256"
    "encoding/hex"
    "net/http"
    "net/url"
    "sort"
    "strconv"
    "strings"
    "time"
    "unicode/utf16"
)

func ordinalLess(a, b string) bool {
    left, right := utf16.Encode([]rune(a)), utf16.Encode([]rune(b))
    for i := 0; i < len(left) && i < len(right); i++ {
        if left[i] != right[i] { return left[i] < right[i] }
    }
    return len(left) < len(right)
}

// NormalizeQuery matches the Tactic Chain server's decoded, ordinal-sorted query.
func NormalizeQuery(u *url.URL) string {
    type group struct { key string; values []string }
    groups := map[string]*group{}
    for _, item := range strings.Split(u.RawQuery, "&") {
        if item == "" { continue }
        pair := strings.SplitN(item, "=", 2)
        key, err := url.QueryUnescape(pair[0])
        if err != nil { key = pair[0] }
        value := ""
        if len(pair) > 1 {
            value, err = url.QueryUnescape(pair[1])
            if err != nil { value = pair[1] }
        }
        folded := strings.ToLower(key)
        if groups[folded] == nil { groups[folded] = &group{key: key} }
        groups[folded].values = append(groups[folded].values, value)
    }
    sorted := make([]*group, 0, len(groups))
    for _, item := range groups { sorted = append(sorted, item) }
    sort.Slice(sorted, func(i, j int) bool { return ordinalLess(sorted[i].key, sorted[j].key) })
    parts := make([]string, 0)
    for _, item := range sorted {
        sort.Slice(item.values, func(i, j int) bool { return ordinalLess(item.values[i], item.values[j]) })
        for _, value := range item.values { parts = append(parts, item.key+"="+value) }
    }
    return strings.Join(parts, "&")
}

// ComputeSignature signs the final request URL. The JSON body is not signed.
func ComputeSignature(apiKey, apiSecret, timestamp string, u *url.URL) string {
    mac := hmac.New(sha256.New, []byte(apiSecret))
    mac.Write([]byte(apiKey + timestamp + NormalizeQuery(u)))
    return hex.EncodeToString(mac.Sum(nil))
}

// SignatureTransport wraps Configuration.HTTPClient.Transport.
type SignatureTransport struct {
    APIKey string
    APISecret string
    Base http.RoundTripper
    Now func() time.Time
}

func (s *SignatureTransport) RoundTrip(request *http.Request) (*http.Response, error) {
    base := s.Base
    if base == nil { base = http.DefaultTransport }
    now := s.Now
    if now == nil { now = time.Now }
    timestamp := strconv.FormatInt(now().Unix(), 10)
    signed := request.Clone(request.Context())
    signed.Header.Del("Authorization")
    signed.Header.Set("X-Credential-Type", "API Key")
    signed.Header.Set("X-API-Key", s.APIKey)
    signed.Header.Set("X-Timestamp", timestamp)
    signed.Header.Set("X-Signature", ComputeSignature(s.APIKey, s.APISecret, timestamp, signed.URL))
    return base.RoundTrip(signed)
}
