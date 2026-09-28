# frozen_string_literal: true

require 'json'
$LOAD_PATH.unshift(File.expand_path('../generated/ruby/lib', __dir__))
require_relative '../generated/ruby/lib/tachain-sdk'

signer = TachainSdk::SignedApiClient
%w[signature-vector.json signature-unicode-vector.json signature-case-vector.json].each do |filename|
  vector = JSON.parse(File.read(File.join(__dir__, filename)))
  actual_query = signer.normalize_query(vector.fetch('url'))
  raise "normalization mismatch: #{filename}" unless actual_query == vector.fetch('normalizedQuery')

  actual_signature = signer.compute_signature(
    vector.fetch('apiKey'), vector.fetch('apiSecret'), vector.fetch('timestamp'), vector.fetch('url')
  )
  raise "signature mismatch: #{filename}" unless actual_signature == vector.fetch('signature')
end

config = TachainSdk::Configuration.new
client = signer.new(config, api_key: 'demo-key', api_secret: 'demo-secret', clock: -> { 1_790_586_000 })
request = client.build_request(
  :GET, '/v1/enum/GetList',
  query_params: { 'enumTypes' => %w[Unit Supplier] },
  header_params: { :'X-Credential-Type' => 'API Key', :'Authorization' => 'Bearer stale' }
)
raise 'array parameters were not exploded' unless request.url.include?('enumTypes=Unit&enumTypes=Supplier')
raise 'API Key header absent' unless request.options[:headers]['X-API-Key'] == 'demo-key'
raise 'duplicate credential type header' if request.options[:headers].key?(:'X-Credential-Type')
raise 'stale bearer header' if request.options[:headers].key?(:Authorization) || request.options[:headers].key?('Authorization')
raise 'wrong final URL signature' unless request.options[:headers]['X-Signature'] == signer.compute_signature('demo-key', 'demo-secret', '1790586000', request.url)

Typhoeus.stub(/api\.example\.com/).and_return(Typhoeus::Response.new(code: 200, body: '{}'))
_data, status, _headers = client.call_api(:GET, '/v1/enum/GetList', query_params: { 'enumTypes' => %w[Unit Supplier] })
raise 'stubbed GET failed' unless status == 200

puts 'Ruby signature vectors and signed GET passed'
