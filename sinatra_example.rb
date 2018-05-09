#!/Users/hugo/.rbenv/versions/2.2.3/bin/ruby

require 'sinatra/base'

class MyApp < Sinatra::Base
    get '/' do
        'Hello, World!'
    end
end

Rack::Handler::CGI.run MyApp.new