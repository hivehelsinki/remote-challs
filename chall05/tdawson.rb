#!/usr/bin/env ruby
#ruby 2.5.1p57

require 'open-uri'
require 'nokogiri'

$WIKI_URL = String.new("https://en.wikipedia.org/wiki/")
$seen_pages = []
$counter = 0

def open_URL(url)
	begin
		file = open(url)
	rescue
		abort("no wikipedia page for this word!")
	end
end

def next_wiki_link(links, i)
	until links[i].to_s.match(/^\/wiki\/[^\/:]+$/) do
		i += 1
		if (i >= links.size)
			abort("Error: No valid Wikipedia link found!")
		end
	end
	return i
end	

def find_philosophy(page)
	doc = Nokogiri::HTML.parse(open_URL($WIKI_URL + page))
	links = doc.css('div.mw-content-ltr p a[href]', 'div.mw-content-ltr li a[href]').map {|element| element['href']}
	i = next_wiki_link(links, 0)
	page = links[i].to_s.split('/')[-1]
	if page.eql?("Philosophy")
		puts "!!! Reach Philosophy !!!"
		exit
	end
	until not $seen_pages.include?(page) do
		puts "Skip #{page}, already seen this one"
		i = next_wiki_link(links, i+1)
		page = links[i].to_s.split('/')[-1]
	end
	$seen_pages << page
	$counter += 1
	puts "\tGoing to #{page} (counter: #{$counter})"
	find_philosophy(page)
end

if ARGV.empty? or ARGV[0].empty?
	abort("Error: No argument given!")
end
find_philosophy(ARGV[0])
