// Install the generated Go module or add a local replace directive before running.
package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"

	tachainsdk "github.com/ta-chain/tachain-sdk/generated/go"
)

func main() {
	baseURL := os.Getenv("TAC_BASE_URL")
	apiKey := os.Getenv("TAC_API_KEY")
	apiSecret := os.Getenv("TAC_API_SECRET")
	if baseURL == "" || apiKey == "" || apiSecret == "" {
		log.Fatal("set TAC_BASE_URL, TAC_API_KEY and TAC_API_SECRET")
	}
	config := tachainsdk.NewConfiguration()
	config.Servers = tachainsdk.ServerConfigurations{{URL: baseURL}}
	config.HTTPClient = &http.Client{Transport: &tachainsdk.SignatureTransport{
		APIKey: apiKey, APISecret: apiSecret,
	}}
	client := tachainsdk.NewAPIClient(config)
	result, _, err := client.ApiEnumAPI.GetV1EnumGetList(context.Background()).
		XCredentialType("API Key").Execute()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(result)
}
