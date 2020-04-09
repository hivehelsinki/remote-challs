#!/usr/bin/env ruby
#ruby 2.5.1p57

require 'open-uri'
require 'nokogiri'
require 'set'

$WIKI_URL = String.new("https://en.wikipedia.org/wiki/")
$seen_pages = Set.new

def get_page_links(page)
	file = open($WIKI_URL + page) rescue abort("no wikipedia page for this word!")
	links = Nokogiri::HTML.parse(file)
		.css('div.mw-content-ltr p a[href]', 'div.mw-content-ltr li a[href]')
		.map { |elem| elem['href'] }
end

def next_wiki_page(links)
	links.each { |link|
		if link.match(/^\/wiki\/[^\/:]+$/) 
			page = link.split('/')[-1]
			(puts "Skip #{page}, already seen this one"; next) if $seen_pages.include?(page)
			return page
		end
	}
	abort("No valid wikipedia page link found!")
end

def find_philosophy(page, counter)
	links = get_page_links(page)
	page = next_wiki_page(links)
	(puts "!!! Reach Philosophy !!!"; exit) if page.eql?("Philosophy")
	$seen_pages << page;
	puts "\tGoing to #{page} (counter: #{counter})"
	find_philosophy(page, counter += 1)
end

if ARGV.empty? then start = "" else start = ARGV[0] end #start from main page if no arg given :D
(puts "!!! Reach Philosophy !!!"; exit) if ARGV[0].eql?("Philosophy")
find_philosophy(start, 1)
