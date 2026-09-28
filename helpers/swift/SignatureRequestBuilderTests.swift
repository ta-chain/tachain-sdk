import Foundation
import XCTest
@testable import TachainSDK

#if canImport(FoundationNetworking)
import FoundationNetworking
#endif

final class SignatureRequestBuilderTests: XCTestCase {
    private let apiKey = "demo-key"
    private let apiSecret = "demo-secret"
    private let timestamp = "1790586000"

    func testBackendSignatureVectors() {
        let plain = URL(string: "https://api.example.com/v1/enum/GetList?b=z&x=%2B+&b=a&A=1")!
        XCTAssertEqual(TachainSignature.normalizeQuery(url: plain), "A=1&b=a&b=z&x=+ ")
        XCTAssertEqual(
            TachainSignature.computeSignature(apiKey: apiKey, apiSecret: apiSecret, timestamp: timestamp, url: plain),
            "a4283936739171659a2b1be9e098c62f9b9e7a5a92430e76e6dd42f260a3110e"
        )

        let unicode = URL(string: "https://api.example.com/v1/enum/GetList?a=%EE%80%80&a=%F0%90%80%80")!
        XCTAssertEqual(TachainSignature.normalizeQuery(url: unicode), "a=𐀀&a=")
        XCTAssertEqual(
            TachainSignature.computeSignature(apiKey: apiKey, apiSecret: apiSecret, timestamp: timestamp, url: unicode),
            "cffe13c9fa916b79d7f2ccacb4403c0bd5af1b5221414564a4571581b3b152eb"
        )

        let mixedCase = URL(string: "https://api.example.com/v1/enum/GetList?a=1&A=2")!
        XCTAssertEqual(TachainSignature.normalizeQuery(url: mixedCase), "a=1&a=2")
    }

    func testSignsFinalEncodedURLAndReplacesBearerHeader() throws {
        TachainSignature.configure(apiKey: apiKey, apiSecret: apiSecret)
        defer { TachainSignature.disable() }

        let builder = SignedURLSessionRequestBuilder<String>(
            method: "GET",
            URLString: "https://api.example.com/v1/enum/GetList",
            parameters: nil,
            headers: ["Authorization": "Bearer stale"],
            requiresAuthentication: true
        )
        let request = try builder.createURLRequest(
            urlSession: URLSession.shared,
            method: .get,
            encoding: AppendingQuery(),
            headers: [:]
        )

        let finalURL = try XCTUnwrap(request.url)
        XCTAssertEqual(finalURL.query, "b=z&x=%2B+&b=a&A=1")
        XCTAssertNil(request.value(forHTTPHeaderField: "Authorization"))
        XCTAssertEqual(request.value(forHTTPHeaderField: "X-Credential-Type"), "API Key")
        XCTAssertEqual(request.value(forHTTPHeaderField: "X-API-Key"), apiKey)
        let signedTimestamp = try XCTUnwrap(request.value(forHTTPHeaderField: "X-Timestamp"))
        XCTAssertNotNil(Int64(signedTimestamp))
        XCTAssertEqual(
            request.value(forHTTPHeaderField: "X-Signature"),
            TachainSignature.computeSignature(
                apiKey: apiKey,
                apiSecret: apiSecret,
                timestamp: signedTimestamp,
                url: finalURL
            )
        )
    }
}

private struct AppendingQuery: ParameterEncoding {
    func encode(_ urlRequest: URLRequest, with parameters: [String: Any]?) throws -> URLRequest {
        var result = urlRequest
        result.url = URL(string: "https://api.example.com/v1/enum/GetList?b=z&x=%2B+&b=a&A=1")
        return result
    }
}
