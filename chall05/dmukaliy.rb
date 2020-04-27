#!/usr/bin/env ruby
#ruby 2.5.1p57

require 'open-uri'

def get_path(content, skip)
    content = content.slice(content.index('<p>')..-1)
    link = content.slice(content.index('<a href="/wiki')..-1)
    while skip != 0
        link = link.slice(10..-1)
        link = link.slice(link.index('<a href="/wiki')..-1)
        skip -= 1
    end
    path = link.slice(link.index('"/wiki/')..link.index('" '))
    our_path = path.slice(7..-2)
    return our_path
end

def go_to(url, visited, counter, skip)
    start_url = "https://en.wikipedia.org/wiki/"
    begin
        file = open(start_url.concat(url))
    rescue
        puts "no wikipedia page for this word!"
        exit
    end
    content = file.read()
    our_path = get_path(content, skip)
    if our_path == "Philosophy"
        puts "!!! Reach Philosophy !!!"
        exit
    end
    if our_path.include? "Help:IPA/"
        go_to(url, visited, counter, skip + 1)
    end
    if !visited.include? our_path
        counter += 1
        skip = 0
        puts "\tGoing to " + our_path  + " (counter: " + counter.to_s + ")"
        visited.push(our_path)
        go_to(our_path, visited, counter, skip)
    else
        puts "Skip " + our_path  + ", already seen this one"
        go_to(url, visited, counter, skip + 1)
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

