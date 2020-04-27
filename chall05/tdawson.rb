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
		.css('div#mw-content-text p a[href]', 'div#mw-content-text li a[href]')
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

def find_philosophy(page, counter = 1)
	links = get_page_links(page)
	next_page = next_wiki_page(links)
	(puts "!!! Reach Philosophy !!!"; exit) if next_page.eql?("Philosophy")
	$seen_pages << next_page;
	puts "\tGoing to #{next_page} (counter: #{counter})"
	find_philosophy(next_page, counter += 1)
end

if ARGV.empty? then start_page = "" else start_page = ARGV[0] end #start from main page if no arg given :D
(puts "!!! Reach Philosophy !!!"; exit) if start_page.eql?("Philosophy")
find_philosophy(start_page)
