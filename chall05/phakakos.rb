#!/usr/bin/env ruby
# ruby version 2.6.6p146
$VERBOSE = nil

require 'HTTParty'
require 'Nokogiri'

def base_url
	"https://en.wikipedia.org"
end

cmd_argv = ARGV

if (ARGV.length == 2)
	exit()
end
start = "/wiki/" + ARGV[0]
$goal = "/wiki/Philosophy"
$history = [""]
$step = 0
$loops = 0
$dup = 0


class Reader

	def initialize(url)
		doc = HTTParty.get(url)
		if (doc.body.nil? || doc.body.empty?)
			return
		end
		@read_page ||= Nokogiri::HTML(doc)
	end

	def try_bad_link
		wiki_content.css(".noarticletext") { |page| page.text }
	end
	
	def get_links
		wiki_content.css("p").css("a[href]") { |link| link.text }
	end
	
	def get_list_links
		wiki_content.css("li").css("a[href]") { |link| link.text }
	end
	
	def wiki_content
		@read_page.css("#bodyContent").css("#mw-content-text")
	end
end

class MainLoop

	def initialize(url)
		if (url == $goal)
			puts "!!! Reach Philosophy !!!"
			exit()
		end
		pname = url.split("/wiki/")
		if ($history.index(url) != nil)
			puts "Skip #{pname[-1]}, already seen this one"
			$dup = 1
			return()
		else
			if ($step > 0)
				puts "\tGoing to #{pname[-1]} (counter: #{$step})"
			end
			$history.push(url)
			$step += 1
		end
	end
	
	def find
		if ($dup == 1)
			$dup = 0
			return()
		end
		reader = Reader.new(base_url + $history[-1])
		bad = reader.try_bad_link
		if (bad[0] && $loops == 0)
			puts "Bad link"
			exit()
		elsif (bad[0])
			puts "Bad link, going back"
			return()
		else
			links = reader.get_links
			if (links.length < 1)
				links = reader.get_list_links
				if(links.length > 0 && $step == 1)
					$step -= 1
					MainLoop.new(links[0]["href"]).find
				end
			end
			if (links.length < 1 && $loops > 0)
				puts "No found links, going back"
				return
			elsif (links.length < 1)
				puts "No found links"
				exit()
			end
			(0...links.size).each do |index|
				if (links[index]["href"].match('^/wiki/*') && !links[index]["href"].match(':'))
					$loops += 1
					MainLoop.new(links[index]["href"]).find
					$loops -= 1
				end
			end
		end
	end
end
MainLoop.new(start).find
puts "Could not find a connection"