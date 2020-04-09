#!/usr/bin/env ruby
# ruby version 2.5.2.3

require 'open-uri'

$array = Array.new
$counter = 0

def getArticleSource(string)
	url = 'https://en.wikipedia.org/wiki/'
	source = open(url + string).read
    rescue
		puts 'no wikipedia page for this word!'
        exit
    else
    	GetFirstLink(source)
end

def GetFirstLink(source)
	# Get content part of article
	pattern = /<p>[\s\S]+?<\/p>/
	paragraphs = source.scan(pattern)
	if !paragraphs[0]
		puts 'no wikipedia page for this word!'
		exit
	end

    # Get wikipedia links from content and loop to find first link
	pattern = /a href="\/wiki\/([\s\S]*?)["]/
    paragraphs.each{ |paragraph|
		links = paragraph.scan(pattern)
        links.each{ |link|
			if (link[0] == 'Philosophy')
				puts '!!! Reach Philosophy !!!'
				exit
			elsif ($array[0] and $array.include? link[0])
                puts "Skip " + link[0] + ", already seen this one"
            elsif
                link[0].match(":")
			else
				$array << link[0]
				$counter += 1
				puts "\tGoing to " + link[0] + " (counter: #{$counter})"
				getArticleSource(link[0])
			end
		}
	}
	puts "Can't reach Philosophy"
	exit
end

if ARGV[0]
    getArticleSource(ARGV[0])
end