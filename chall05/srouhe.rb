#!/usr/bin/ruby
# ruby 2.5.1p57

require 'json'
require 'net/http'

VISITED = []
ARG = ARGV[0]


def shut_down
	puts "\nNo patience, huh?"
	sleep 1
end


Signal.trap("INT") { 
  shut_down 
  exit
}


def get_first_link(res)
	begin
		i = res.body.index('<p>')
		main = res.body.slice(i..-1)
		links = main.scan(/(?<=<a href="\/wiki\/).[^"]*/)
		links.each { |link|
			if not link.include? ":"
				if VISITED.include? link
					puts "Skip %s, already seen this one" % link
				else
					return link
				end
			end
		}
	rescue
		return ARG
	end
end
  

def make_request(page)
	base = 'https://en.wikipedia.org/wiki/'
	url = '%s%s' % [base, page]
	uri = URI(url)
	res = Net::HTTP.get_response(uri)
	if res.code == "200"
		return res
	else
		puts "no wikipedia page for this word!: %s" % page
		exit
	end
end


def aristotle(arg, counter)
	res = make_request(arg)
	VISITED << arg
	link = get_first_link(res)
	if link == "Philosophy"
		puts "!!! Reach Philosophy !!!"
		exit
	end
	counter += 1
	puts "Going to %s (counter: %d)" % [link, counter]
	aristotle(link, counter)
end


def main()
	if ARG
		if ARG.downcase == "philosophy"
			puts "You're already there"
			exit
		end
		puts "Road to Philosophy... CTRL+C to exit"
		aristotle(ARG.capitalize(), 0)
	else
		puts "Please specify a wiki page"
	end
end


main()
