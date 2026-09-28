import Foundation
import CommonCrypto

#if canImport(FoundationNetworking)
import FoundationNetworking
#endif

/// API Key + Secret authentication for the generated URLSession client.
///
/// Install this factory before making API calls. The Swift 5 generated client
/// uses process-wide configuration, so one credential is active at a time.
public enum TachainSignature {
    private struct Credential {
        let apiKey: String
        let apiSecret: String
    }

    private static let lock = NSLock()
    private static var credential: Credential?

    public static func configure(apiKey: String, apiSecret: String) {
        lock.lock()
        credential = Credential(apiKey: apiKey, apiSecret: apiSecret)
        lock.unlock()

        TachainSDKAPI.customHeaders.removeValue(forKey: "Authorization")
        TachainSDKAPI.requestBuilderFactory = SignatureRequestBuilderFactory()
    }

    /// Restore the generated client's default request builder before using Token auth.
    public static func disable() {
        lock.lock()
        credential = nil
        lock.unlock()
        TachainSDKAPI.requestBuilderFactory = URLSessionRequestBuilderFactory()
    }

    /// Match the backend's decoded query, including duplicate keys and values.
    public static func normalizeQuery(url: URL) -> String {
        let rawQuery = URLComponents(url: url, resolvingAgainstBaseURL: false)?.percentEncodedQuery ?? ""
        var groups: [(key: String, values: [String])] = []

        for segment in rawQuery.split(separator: "&", omittingEmptySubsequences: true) {
            let text = String(segment)
            let separator = text.firstIndex(of: "=")
            let key = decode(separator.map { String(text[..<$0]) } ?? text)
            let value = decode(separator.map { String(text[text.index(after: $0)...]) } ?? "")

            // QueryHelpers.ParseQuery groups names with OrdinalIgnoreCase and
            // keeps the spelling of the first occurrence.
            if let index = groups.firstIndex(where: { sameQueryKey($0.key, key) }) {
                groups[index].values.append(value)
            } else {
                groups.append((key, [value]))
            }
        }

        groups.sort { ordinalLess($0.key, $1.key) }
        return groups.flatMap { group in
            group.values.sorted(by: ordinalLess).map { "\(group.key)=\($0)" }
        }.joined(separator: "&")
    }

    /// The backend signs the final URL query. It does not sign the JSON body.
    public static func computeSignature(apiKey: String, apiSecret: String, timestamp: String, url: URL) -> String {
        let message = Array((apiKey + timestamp + normalizeQuery(url: url)).utf8)
        let secret = Array(apiSecret.utf8)
        var digest = [UInt8](repeating: 0, count: Int(CC_SHA256_DIGEST_LENGTH))

        secret.withUnsafeBytes { keyBytes in
            message.withUnsafeBytes { messageBytes in
                digest.withUnsafeMutableBytes { digestBytes in
                    CCHmac(
                        CCHmacAlgorithm(kCCHmacAlgSHA256),
                        keyBytes.baseAddress,
                        secret.count,
                        messageBytes.baseAddress,
                        message.count,
                        digestBytes.baseAddress
                    )
                }
            }
        }
        return digest.map { String(format: "%02x", $0) }.joined()
    }

    fileprivate static func sign(_ original: URLRequest) throws -> URLRequest {
        guard let url = original.url else { throw SignatureError.missingURL }
        lock.lock()
        let active = credential
        lock.unlock()
        guard let active = active else { throw SignatureError.credentialMissing }

        let timestamp = String(Int64(Date().timeIntervalSince1970))
        var request = original
        request.setValue(nil, forHTTPHeaderField: "Authorization")
        request.setValue("API Key", forHTTPHeaderField: "X-Credential-Type")
        request.setValue(active.apiKey, forHTTPHeaderField: "X-API-Key")
        request.setValue(timestamp, forHTTPHeaderField: "X-Timestamp")
        request.setValue(
            computeSignature(apiKey: active.apiKey, apiSecret: active.apiSecret, timestamp: timestamp, url: url),
            forHTTPHeaderField: "X-Signature"
        )
        return request
    }

    private static func decode(_ value: String) -> String {
        let spaces = value.replacingOccurrences(of: "+", with: " ")
        return spaces.removingPercentEncoding ?? spaces
    }

    private static func ordinalLess(_ left: String, _ right: String) -> Bool {
        left.utf16.lexicographicallyPrecedes(right.utf16)
    }

    private static func sameQueryKey(_ left: String, _ right: String) -> Bool {
        (left as NSString).compare(right, options: [.caseInsensitive, .literal]) == .orderedSame
    }
}

public enum SignatureError: Error {
    case missingURL
    case credentialMissing
}

public final class SignatureRequestBuilderFactory: RequestBuilderFactory {
    public init() {}

    public func getNonDecodableBuilder<T>() -> RequestBuilder<T>.Type {
        SignedURLSessionRequestBuilder<T>.self
    }

    public func getBuilder<T: Decodable>() -> RequestBuilder<T>.Type {
        SignedURLSessionDecodableRequestBuilder<T>.self
    }
}

public final class SignedURLSessionRequestBuilder<T>: URLSessionRequestBuilder<T> {
    override public func createURLRequest(
        urlSession: URLSessionProtocol,
        method: HTTPMethod,
        encoding: ParameterEncoding,
        headers: [String: String]
    ) throws -> URLRequest {
        try TachainSignature.sign(super.createURLRequest(
            urlSession: urlSession, method: method, encoding: encoding, headers: headers
        ))
    }
}

public final class SignedURLSessionDecodableRequestBuilder<T: Decodable>: URLSessionDecodableRequestBuilder<T> {
    override public func createURLRequest(
        urlSession: URLSessionProtocol,
        method: HTTPMethod,
        encoding: ParameterEncoding,
        headers: [String: String]
    ) throws -> URLRequest {
        try TachainSignature.sign(super.createURLRequest(
            urlSession: urlSession, method: method, encoding: encoding, headers: headers
        ))
    }
}
