#!/usr/bin/ruby
#version: 2.5.1p57

require 'net/http'

def get_wiki(article)
	net = Net::HTTP.new("en.wikipedia.org", 443)
	net.use_ssl = true
	response = net.get("/wiki/" + article)
	if (response.code.match?(/^3\d\d$/) && response.header['location'])
		redirected = response.header['location'].match(/\/([\w_()%]*$)/)[1]
		response = get_wiki(redirected)
	end
	abort("No wikipedia page for " + article + "!") if response.code == "404"
	abort("Error") if response.code != "200"
	return response
end

def get_next(visited, response)
	content = response.body.match(/<p>.*/m)
	links = content[0].scan(/<a href="\/wiki\/([\w_%()]*)"/m)
	i = 0
	loop do
		break if !visited.include?(links[i][0])
		puts "Skip " + URI.unescape(links[i][0]) + ", already seen this one"
		i += 1
	end
	return links[i][0]
end

abort("Enter starting article as argument!") if ARGV.length != 1
response = get_wiki(ARGV[0])
visited = Array.new
visited.push(ARGV[0])
counter = 1
loop do
	article = get_next(visited, response)
	visited.push(article)
	if article == "Philosophy"
		puts "!!! Reach Philosophy !!!"
		break
	end
	puts "\tGoing to " + URI.unescape(article) + " (counter: " + counter.to_s + ")"
	counter += 1
	response = get_wiki(article)
end
