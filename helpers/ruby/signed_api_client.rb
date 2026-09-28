# frozen_string_literal: true

require 'cgi'
require 'uri'
require 'openssl'
require 'tachain-sdk/api_client'

module TachainSdk
  # Signs Typhoeus' fully serialized URL immediately before it sends the request.
  class SignedApiClient < ApiClient
    attr_reader :api_key

    def initialize(config = Configuration.default, api_key:, api_secret:, clock: -> { Time.now.to_i })
      super(config)
      # OpenAPI `form` + `explode: true` arrays must become repeated keys.
      @config.params_encoding ||= :multi
      @api_key = api_key
      @api_secret = api_secret
      @clock = clock
    end

    def self.normalize_query(url)
      query = URI.parse(url).query.to_s
      groups = {}
      query.split('&').each do |part|
        next if part.empty?

        raw_key, raw_value = part.split('=', 2)
        key = CGI.unescape(raw_key)
        value = CGI.unescape(raw_value.to_s)
        # QueryHelpers.ParseQuery uses a case-insensitive dictionary and keeps
        # the first spelling when the same key appears with another casing.
        lookup = key.downcase
        groups[lookup] ||= { key: key, values: [] }
        groups[lookup][:values] << value
      end
      ordinal = ->(text) { text.encode(Encoding::UTF_16BE).b }
      groups.values.sort_by { |group| ordinal.call(group[:key]) }.flat_map do |group|
        group[:values].sort_by { |value| ordinal.call(value) }.map do |value|
          "#{group[:key]}=#{value}"
        end
      end.join('&')
    end

    def self.compute_signature(api_key, api_secret, timestamp, url)
      content = api_key + timestamp + normalize_query(url)
      OpenSSL::HMAC.hexdigest('SHA256', api_secret, content)
    end

    def build_request(http_method, path, opts = {})
      request = super
      timestamp = @clock.call.to_i.to_s
      headers = request.options[:headers]
      %w[Authorization X-Credential-Type X-API-Key X-Timestamp X-Signature].each do |name|
        headers.delete(name)
        headers.delete(name.to_sym)
      end
      headers['X-Credential-Type'] = 'API Key'
      headers['X-API-Key'] = @api_key
      headers['X-Timestamp'] = timestamp
      headers['X-Signature'] = self.class.compute_signature(@api_key, @api_secret, timestamp, request.url)
      request
    end
  end
end
