#!/usr/bin/env ruby
# ruby 2.5.3p105

require 'net/http'
require 'json'

# Outputs a printed route to Philosophy article given start search word
class WikiPhilosophy
  def initialize(keyword)
    @base_url = 'https://en.wikipedia.org/w/api.php'
    @search = keyword
    @current_page = nil
    @current_links = nil
    @counter = 0
    @path = []
  end

  def print_philosophy_path
    search_wiki_url
    puts 'no wikipedia page for this word!' if @current_page.nil?
    search_philosophy_path while @current_page != 'Philosophy'
    puts '!!! Reach Philosophy !!!'
  end

  # private

  def set_current_links
    url = "#{@base_url}?action=parse&format=json&page=#{@current_page}&prop=text&formatversion=2"
    body = http_get(url)
    unless body['error'].nil?
      puts "Error: #{@current_page} not found."
      @current_page = @current_links.shift
      return set_current_links
    end
    @current_links = parse_links_from_body body
    set_current_links if @current_links.nil?
  end

  def search_philosophy_path(set_links = true)
    set_current_links if set_links
    first = @current_links.shift
    first = @current_links.shift while @path.include? first
    @path.unshift first
    @current_page = first
    @counter += 1
    puts "Going to #{first} (counter: #{@counter})"
  end

  def parse_links_from_body(body)
    puts body['parse']['text'].scan(/(?<=<p>).*?(?=<\/p>)/).flatten.join('')
    matches = body['parse']['text'].scan(/(?<=<p>).*?(?=<\/p>)/).flatten.join('')
                                   .scan(/(?<=href=").*?(?=")/).flatten
    if matches
      return matches.select do |link|
        link.start_with?('#') && !link.start_with?('#cite_note')
      end.map { |link| link.split('#').last }
    end
    nil
  end

  def search_wiki_url
    results = http_get("#{@base_url}?action=opensearch&search=#{@search}")
    @current_page = results.first(1).first
  end

  def http_get(full_url)
    uri = URI(full_url)
    response = Net::HTTP.get_response(uri)
    JSON.parse(response.body)
  end
end

WikiPhilosophy.new('Markdown').print_philosophy_path
