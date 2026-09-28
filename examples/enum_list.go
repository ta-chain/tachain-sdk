// Install the generated Go module or add a local replace directive before running.
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	tachainsdk "github.com/ta-chain/tachain-sdk/generated/go"
)

func main() {
	baseURL := os.Getenv("TAC_BASE_URL")
	token := os.Getenv("TAC_TOKEN")
	if baseURL == "" || token == "" {
		log.Fatal("set TAC_BASE_URL and TAC_TOKEN")
	}

	config := tachainsdk.NewConfiguration()
	config.Servers = tachainsdk.ServerConfigurations{{URL: baseURL}}
	client := tachainsdk.NewAPIClient(config)
	ctx := context.WithValue(context.Background(), tachainsdk.ContextAccessToken, token)
	result, _, err := client.ApiEnumAPI.GetV1EnumGetList(ctx).XCredentialType("Token").Execute()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(result)
}
