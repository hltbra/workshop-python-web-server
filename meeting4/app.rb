#!/Users/hugo/.rbenv/versions/2.2.3/bin/ruby

require 'sinatra/base'

class MyApp < Sinatra::Base
    get '/' do
        'Hello from Ruby!'
    end

    post '/p' do
        params.inspect
    end
end

Rack::Handler::CGI.run MyApp.new