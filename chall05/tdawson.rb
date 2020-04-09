#!/usr/bin/ruby

require 'open-uri'
require 'nokogiri'
require "net/http"

$wikiURL = String.new("https://en.wikipedia.org/wiki/")
$seen_links = []
$counter = 0

def next_link(article)
	doc = Nokogiri::HTML.parse(open($wikiURL + article))
	attrs = doc.xpath('//p//a/@href') 
	attrs.map {|attr| attr.value} 
	article = attrs[0].to_s.split('/')[2]
	if article.eql?("Philosophy")
		puts "!!! Reach Philosophy !!!"
		exit
	end
	if ($seen_links.include?(article))
		puts "Skip " + article + ", already seen this one"
		article = attrs[1].to_s.split('/')[2]
	else
		$seen_links << article
	end
	$counter += 1
	puts "Going to " + article + " (counter: " + $counter.to_s + ")"
	next_link(article)
end

start = ARGV[0]
puts "START: " + $wikiURL + start

response = Net::HTTP.get_response(URI.parse($wikiURL + start))
if (response.code == 404)
	abort("no wikipedia page for this word!")
end

next_link(start)