require 'uri'
require 'tachain-sdk'

base_url = URI(ENV.fetch('TAC_BASE_URL'))
TachainSdk.configure do |config|
  config.scheme = base_url.scheme
  config.host = base_url.host
  config.base_path = base_url.path
end

client = TachainSdk::SignedApiClient.new(
  api_key: ENV.fetch('TAC_API_KEY'),
  api_secret: ENV.fetch('TAC_API_SECRET')
)
puts TachainSdk::ApiEnumApi.new(client).get_v1_enum_get_list('API Key')
