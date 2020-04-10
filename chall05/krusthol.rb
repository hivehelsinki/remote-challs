#!/usr/bin/env ruby
#ruby 2.5.1p57
require 'open-uri'

counter = 0
checked_pages = []
starting_point = 'https://en.wikipedia.org/wiki/' + ARGV[0]
begin
contents = open(starting_point).read
rescue
        puts "no wikipedia page for this word!"
        exit
end
split_p = contents.split('<p>')
road = split_p[1].scan(/(?<=<a href="\/wiki\/).[^"]*/)
checked_pages.push(road[0])
counter = counter + 1
puts ("Going to " + road[0] + " (counter: #{counter})")
while !checked_pages.include?('Philosophy') do
    contents = open('https://en.wikipedia.org/wiki/' + checked_pages.last).read
    split_open = contents.split('<p>')
    road = split_open[1].scan(/(?<=<a href="\/wiki\/).[^"]*/)
    i = 0
    while checked_pages.include?(road[i]) do
        i = i + 1    
    end
    checked_pages.push(road[i])
    counter = counter + 1
    puts ("Going to " + road[0] + " (counter: #{counter})")
end
puts ("!!! Reach Philosophy !!!")