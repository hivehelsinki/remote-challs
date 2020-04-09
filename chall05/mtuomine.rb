#!/usr/bin/env ruby

#ruby 2.5.1p57

require 'net/http'

uri = URI("https://en.wikipedia.org/wiki/" + ARGV[0])
counter = 0
visited = []

def traverse(visited, uri, counter)
	html = Net::HTTP.get(uri)
	if html.empty?
		puts "no wikipedia page for this word!"
		exit
	end

	content = html.split("<p>", 2)
	linksArr = content[1].scan(/href\s*=\s*"([^"]*)"/)

	# Bubblegum, couldn't combine with regex on tpo
	res = []
	linksArr.each { |link|
		if link[0].match(/^\/wiki\//)
			res.append(link[0])
		end
	}

	res.each { |link|
		trimmed = link.split('/').last
		if trimmed.eql? "Philosophy"
			puts "!!! Reach Philosophy !!!"
			exit
		elsif visited.include? trimmed
			puts "Skip #{trimmed}, already seen this one"
		else
			puts "\tGoing to #{trimmed} (counter: #{counter})"
			visited.append(trimmed)
			return link
		end
	}
	return ""
end

while
	counter += 1
	link = traverse(visited, uri, counter)
	uri = URI("https://en.wikipedia.org"+ link)
end
