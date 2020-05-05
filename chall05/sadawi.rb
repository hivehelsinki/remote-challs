#!/usr/bin/env ruby
#ruby 2.5.1p57

require 'open-uri'
begin
file = open('https://en.wikipedia.org/wiki/' + ARGV[0])
rescue
	puts "no wikipedia page for this word!"
	exit
end
contents = file.read
main = contents.match(/(?<=<p>)(?<!<\/p>)[\s\S]*?((?<=wiki\/)[a-zA-Z_()]*?(?="))[\s\S]*?<\/a>/)[1]
visited = []
count = 1
puts "	Going to " + main + " (counter: " + count.to_s + ")"
visited.push(main)

while main != "Philosophy"
	count += 1
	file = open('https://en.wikipedia.org/wiki/' + main)
	contents = file.read
	main = contents.match(/(?<=<p>)(?<!<\/p>)[\s\S]*?((?<=wiki\/)[a-zA-Z_()]*?(?="))[\s\S]*?<\/a>/)[1]
	if visited.include? main
		puts "Loop detected, stopping."
		break
	end
	visited.push(main)
	if main == "Philosophy"
		puts "!!! Reach Philosophy !!!"
	else
		puts "	Going to " + main + " (counter: " + count.to_s + ")"
	end
end