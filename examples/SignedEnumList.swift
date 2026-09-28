// Add generated/swift as a local Swift package, or use the split repository.
// Keep API secrets in the server-side environment.
import Foundation
import TachainSDK

@main
struct SignedEnumList {
    static func main() {
        let environment = ProcessInfo.processInfo.environment
        guard let baseURL = environment["TAC_BASE_URL"],
              let apiKey = environment["TAC_API_KEY"],
              let apiSecret = environment["TAC_API_SECRET"] else {
            fatalError("Set TAC_BASE_URL, TAC_API_KEY, and TAC_API_SECRET")
        }

        TachainSDKAPI.basePath = baseURL
        TachainSignature.configure(apiKey: apiKey, apiSecret: apiSecret)

        let done = DispatchSemaphore(value: 0)
        _ = ApiEnumAPI.getV1EnumGetList(
            xCredentialType: .apiKey,
            apiResponseQueue: .global()
        ) { data, error in
            if let error = error {
                fputs("API request failed: \(error)\n", stderr)
            } else if let data = data {
                print(data)
            }
            done.signal()
        }
        done.wait()
    }
}
