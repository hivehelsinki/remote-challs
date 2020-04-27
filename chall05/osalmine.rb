#!/usr/bin/env ruby

# ruby version 2.6.3p62

require 'nokogiri'
require 'open-uri'
require "net/http"

str = ARGV[0]

fail("Usage: enter one wikipedia page name") if ARGV.length() != 1

url = URI.parse("https://en.wikipedia.org/wiki/#{str}")
req = Net::HTTP.new(url.host, url.port)
req.use_ssl = true
res = req.request_head(url.path)

if res.code.to_i == 404
    abort("no wikipedia page for this word!")
end

next_page_name = str

def get_first_link(first_p, url)
    hrefs = first_p.css("a").map do |link|
        if (href = link.attr("href")) && !href.empty?
            URI::join(url, href)
        end
        rescue
            nil
    end
    return (hrefs)
end

i = 0

visited = []

while next_page_name != "Philosophy"
    i += 1
    doc = Nokogiri::HTML(open(url))
    ind = 0
    first_p = doc.at_css('[id="mw-content-text"]').css('p')
    urls = get_first_link(first_p, url)
    ind = 0
    url = urls[0]
    while (urls[ind] == nil)
        ind += 1
        url = urls[ind]
    end
    while (visited.include?(urls[ind]))
        puts("Skip " + urls[ind].to_s.split('/')[-1] + ", already seen this one")
        ind += 1
        url = urls[ind]
    end
    next_page_name = url.to_s.split('/')[-1]
    visited << url
    if next_page_name == "Philosophy"
        puts("!!! Reach Philosophy !!!")
        exit
    end
    puts("\tGoing to #{next_page_name} (counter: #{i})")
end
