#!/usr/bin/env ruby
#ruby 2.5.1p57
require 'open-uri'

counter = 0
checked_pages = []
if ARGV[0] != nil
    starting_point = 'https://en.wikipedia.org/wiki/' + ARGV[0]
else
    puts "Road to Philosophy script usage: ./krusthol.rb [Wikipedia article]"
    exit
end
begin
contents = open(starting_point).read
rescue
        puts "no wikipedia page for this word!"
        exit
end
split_p = contents.split('<p>')
i = 1
road = split_p[i].scan(/(?<=<a href="\/wiki\/).[^"]*/)
while road[0] == nil do
    i = i + 1
    road = split_p[i].scan(/(?<=<a href="\/wiki\/).[^"]*/)    
end
checked_pages.push(road[0])
counter = counter + 1
puts ("Going to " + road[0] + " (counter: #{counter})")
while !checked_pages.include?('Philosophy') do
    contents = open('https://en.wikipedia.org/wiki/' + checked_pages.last).read
    split_p = contents.split('<p>')
    i = 1
    road = nil
    while road == nil do
        road = split_p[i].scan(/(?<=<a href="\/wiki\/).[^"]*/)
        i = i + 1
    end
    i = 0
    while checked_pages.include?(road[i]) do
        puts ("Skip " + road[i] + ", already seen this one")
        i = i + 1    
    end
    checked_pages.push(road[i])
    counter = counter + 1
    puts ("Going to " + road[0] + " (counter: #{counter})")
end
puts ("!!! Reach Philosophy !!!")
