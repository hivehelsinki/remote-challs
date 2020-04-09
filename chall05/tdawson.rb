#!/usr/bin/env ruby
#ruby 2.5.1p57

require 'open-uri'
require 'nokogiri'

$WIKI_URL = String.new("https://en.wikipedia.org/wiki/")
$seen_links = []
$counter = 0

def is_seen(page)
	return $seen_links.include?(page)
end

def open_URL(url)
	begin
		file = open(url)
	rescue
		abort("no wikipedia page for this word!")
	end
end

def next_wiki_link(links, i)
	until links[i].to_s.match(/^\/wiki\/[^\/#.:]+$/) do
		i += 1
		if (i >= links.size)
			abort("no valid Wikipedia link found!")
		end
	end
	return i
end	

def find_philosophy(page)
	doc = Nokogiri::HTML.parse(open_URL($WIKI_URL + page))
	attrs = doc.xpath('//p//a/@href', '//li//a/@href')
	attrs.map {|attr| attr.value}
	i = next_wiki_link(attrs, 0)
	page = attrs[i].to_s.split('/')[2]
	if page.eql?("Philosophy")
		puts "!!! Reach Philosophy !!!"
		exit
	end
	until not is_seen(page) do
		puts "Skip #{page}, already seen this one"
		i = next_wiki_link(attrs, i+1)
		page = attrs[i].to_s.split('/')[2]
	end
	$seen_links << page
	$counter += 1
	puts "\tGoing to #{page} (counter: #{$counter})"
	find_philosophy(page)
end

find_philosophy(ARGV[0])
