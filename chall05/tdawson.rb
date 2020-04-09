#!/usr/bin/env ruby
#ruby 2.5.1p57

require 'open-uri'
require 'nokogiri'
require 'set'

$WIKI_URL = String.new("https://en.wikipedia.org/wiki/")
$seen_pages = Set.new

def open_URL(url)
	file = open(url) rescue abort("no wikipedia page for this word!")
end

def next_wiki_page(links)
	links.each { |link|
		if link.match(/^\/wiki\/[^\/:]+$/) 
			page = link.split('/')[-1]
			if $seen_pages.include?(page)
				puts "Skip #{page}, already seen this one"
				next
			end
			return page
		end
	}
	abort("No valid wikipedia page link found!")
end

def find_philosophy(page, counter)
	doc = Nokogiri::HTML.parse(open_URL("#{$WIKI_URL}#{page}"))
	links = doc.css('div.mw-content-ltr p a[href]', 'div.mw-content-ltr li a[href]').map { |element| element['href'] }
	page = next_wiki_page(links)
	if page.eql?("Philosophy")
		puts "!!! Reach Philosophy !!!"; exit
	end
	$seen_pages << page;
	puts "\tGoing to #{page} (counter: #{counter})"
	find_philosophy(page, counter += 1)
end

#if no argument is given, start from Wikipedia main page :D
if ARGV.empty? then start = "" else start = ARGV[0] end
find_philosophy(start, 1)
