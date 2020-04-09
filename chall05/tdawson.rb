#!/usr/bin/env ruby
#ruby 2.5.1p57

require 'open-uri'
require 'nokogiri'

$WIKI_URL = String.new("https://en.wikipedia.org/wiki/")
$seen_links = []
$counter = 0

def open_URL(url)
	begin
		file = open(url)
	rescue
		abort("no wikipedia page for this word!")
	end
end

def next_wiki_link(links, i)
	until links[i].to_s.match(/^\/wiki\/.+$/) do
		i += 1
	end
	return i
end	

def find_philosophy(article)
	doc = Nokogiri::HTML.parse(open_URL($WIKI_URL + article))
	attrs = doc.xpath('//p//a/@href') 
	attrs.map {|attr| attr.value}
	i = 0
	i = next_wiki_link(attrs, i)
	article = attrs[i].to_s.split('/')[2]
	if article.eql?("Philosophy")
		puts "!!! Reach Philosophy !!!"
		exit
	end
	if ($seen_links.include?(article))
		puts "Skip #{article}, already seen this one"
		i = next_wiki_link(attrs, i)
		article = attrs[i].to_s.split('/')[2]
	else
		$seen_links << article
	end
	$counter += 1
	puts "\tGoing to #{article} (counter: #{$counter})"
	find_philosophy(article)
end

start = ARGV[0]
find_philosophy(start)