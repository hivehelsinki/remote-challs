#!/usr/bin/env ruby
#ruby 2.5.1p57

require 'open-uri'

def go_to(url, visited, counter, seen)
    start_url = "https://en.wikipedia.org/wiki/"
    if url == "Philosophy"
        puts "!!! Reach Philosophy !!!"
        exit
    end
    begin
        file = open(start_url.concat(url))
    rescue
        puts "no wikipedia page for this word!"
        exit
    end
    content = file.read()
    content = content.slice(content.index('<p>')..-1)
    link = content.slice(content.index('<a href="/wiki')..-1)
    while seen != 0
        link = link.slice(10..-1)
        link = link.slice(link.index('<a href="/wiki')..-1)
        seen -= 1
    end
    path = link.slice(link.index('"/wiki/')..link.index('" '))
    our_path = path.slice(7..-2)
    if !visited.include? our_path
        counter += 1
        puts "\tGoing to " + our_path  + " (counter: " + counter.to_s + ")"
        visited.push(our_path)
        go_to(our_path, visited, counter, seen)
    else
        puts "Skip " + our_path  + ", already seen this one"
        go_to(url, visited, counter, seen + 1)
    end
end

def main()
    visited = []
    if (ARGV[0])
        go_to(ARGV[0], visited, 0, 0)
    else
        puts "missing argument!"
    end
end

main()

