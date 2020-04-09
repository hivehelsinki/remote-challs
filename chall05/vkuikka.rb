#!/usr/bin/ruby
#ruby 2.5.5p157

require 'open-uri'

if (!article = ARGV[0])
	return
end
url = "https://en.wikipedia.org/wiki/"
begin
file = open(url + article)
rescue
	puts "No wikipedia page for this word"
	return
end
visited = []
while (article != "Philosophy")
	file = open(url + article)
	content = file.read
	matches = content.scan(/(?<=(<p>)|(<h[0-9])).+?<a href=\"\/wiki\/([^\":]*)"/mu).drop(1)
	for items in matches
		if !visited.include? items[2]
			article = items[2]
			break
		else
			puts "skip " + items[2] + " already visited"
		end
	end
	visited << article
	puts "	Going to " + article
end
puts "Found Philosophy!"
