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


def get_category(page)
	base = 'https://en.wikipedia.org/w/api.php?action=query&prop=categories&titles='
	url = '%s%s%s' % [base, page, '&format=json']
	uri = URI(url)
	return Net::HTTP.get_response(uri)
end


def check_category(page)
	begin
		res = get_category(page)
		key, value = JSON.parse(res.body)['query']['pages'].first
		categories = value['categories']
		categories.each { |category|
			if category['title'].downcase.include? "philosophy"
				puts "!!! Reach Philosophy !!!"
				exit
			end
		}
	rescue
		return
	end
end


def aristotle(arg, counter)
	check_category(arg)
	res = make_request(arg)
	VISITED << arg
	link = get_first_link(res)
	counter += 1
	puts "Going to %s (counter: %d)" % [link, counter]
	aristotle(link, counter)
end


def main()
	if ARG
		puts "Road to Philosophy... CTRL+C to exit"
		aristotle(ARG.capitalize(), 0)
	else
		puts "Please specify a wiki page"
	end
end


main()
