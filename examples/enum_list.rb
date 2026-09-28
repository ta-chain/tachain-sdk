# Install the generated gem or add generated/ruby/lib to RUBYLIB first.
require 'uri'
require 'tachain-sdk'

base_url = ENV.fetch('TAC_BASE_URL')
token = ENV.fetch('TAC_TOKEN')
uri = URI(base_url)

TachainSdk.configure do |config|
  config.scheme = uri.scheme
  config.host = uri.host
  config.base_path = uri.path
  config.access_token = token
end

puts TachainSdk::ApiEnumApi.new.get_v1_enum_get_list('Token')
