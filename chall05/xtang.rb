#!/usr/bin/ruby
# ruby 2.5.1p57

require 'net/http'

abort ("Usage: ./xtang.rb <wrod>") if ARGV.length != 1

visited = [ARGV[0]]

uri = URI("https://en.wikipedia.org/wiki/#{ARGV[0]}")

 while uri.path != '/wiki/Philosophy'
    response = Net::HTTP.get_response(uri)
    abort("no wikipedia page") if response.code != '200'

    startSearch = response.body.index('<p>')

    while true
        startLink = response.body[startSearch.. -1].index('<a href="/wiki/') + 15
     
        linklen = response.body[startSearch + startLink.. -1].index('"') - 1

        nextPage = response.body[startSearch + startLink..startSearch+startLink + linklen].split('#')[0]


        if visited.include?(nextPage)
            puts "Skip #{nextPage}, already seen this one"
        elsif !nextPage.start_with?("Help:IPA") && !nextPage.start_with?("File:")
            break;
        end;

        startSearch = startSearch + startLink
   end

    uri.path = "/wiki/#{nextPage}"


    visited << nextPage

    if uri.path != '/wiki/Philosophy'
     #   puts "\tGoing to #{nextPage} (counter: #{visited.length - 1})"
       puts "\tGoing to #{nextPage} (counter: #{visited.length - 1})"
    end

end

puts '!!! Reach Philosophy !!!'
