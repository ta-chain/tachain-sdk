// Add generated/swift as a local Swift package, or use the split repository after release.
import Foundation
import TachainSDK

@main
struct EnumList {
    static func main() {
        let environment = ProcessInfo.processInfo.environment
        guard let baseURL = environment["TAC_BASE_URL"],
              let token = environment["TAC_TOKEN"] else {
            fatalError("Set TAC_BASE_URL and TAC_TOKEN")
        }
        TachainSDKAPI.basePath = baseURL
        TachainSDKAPI.customHeaders["Authorization"] = "Bearer \(token)"
        let done = DispatchSemaphore(value: 0)
        _ = ApiEnumAPI.getV1EnumGetList(
            xCredentialType: .token,
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
