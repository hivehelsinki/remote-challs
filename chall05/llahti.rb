#!/usr/bin/ruby -w
#ruby 2.3.7p456

require 'net/http'

if ARGV.length == 0
    exit
end

uri = URI("https://en.wikipedia.org/wiki/#{ARGV[0]}")
visited = [ARGV[0]]

while uri.path != '/wiki/Philosophy'

    res = Net::HTTP.get_response(uri)

    if res.code != '200'
        puts 'no wikipedia page for this word!'
        exit
    end

    startSearch = res.body.index('<p>')

    while true
        startLink = res.body[startSearch..-1].index('<a href="/wiki/') + 15
        linkLen = res.body[startSearch+startLink..-1].index('"') - 1
        nextPage = res.body[startSearch+startLink..startSearch+startLink+linkLen].split('#')[0]
        
        if visited.include?(nextPage)
            puts "Skip #{nextPage}, already seen this one"
        elsif !nextPage.start_with?("Help:IPA") && !nextPage.start_with?("File:")
            break
        end
        startSearch = startSearch + startLink
    end

    uri.path = "/wiki/#{nextPage}"
    visited << nextPage
    if uri.path != '/wiki/Philosophy'
        puts "\tGoing to #{nextPage} (counter: #{visited.length - 1})"
    end
end

puts '!!! Reach Philosophy !!!'