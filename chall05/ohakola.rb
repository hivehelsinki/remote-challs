#!/usr/bin/env ruby
# ruby 2.5.3p105

require 'net/http'
require 'json'

# Outputs a printed route to Philosophy article given start search word
class WikiPhilosophyPath
  def initialize(keyword)
    @base_url = 'https://en.wikipedia.org/w/api.php'
    @search = keyword
    @current_page = nil
    @current_links = nil
    @counter = 0
    @path = []
  end

  def run
    search_wiki_url
    puts 'no wikipedia page for this word!' if @current_page.nil?
    puts "First search result #{@current_page} with given search word" unless @current_page.nil?
    while @current_page != 'Philosophy' && !@current_page.nil?
      puts "Going to #{@current_page} (counter: #{@counter})"
      go_to_current_page
      set_new_current_page
    end
    puts '!!! Reach Philosophy !!!' unless @current_page.nil?
  end

  # private

  def go_to_current_page
    url = "#{@base_url}?action=parse&format=json&page=#{@current_page}&prop=text&formatversion=2"
    body = http_get(url)
    unless body['error'].nil?
      puts "Error: #{@current_page} not found."
      return puts 'No links left, stopping' if @current_links.nil?

      @current_page = @current_links.shift
      return go_to_current_page
    end
    @current_links = parse_links_from_body body
    go_to_current_page if @current_links.nil?
  end

  def set_new_current_page
    return if @current_links.nil?

    first = @current_links.shift
    while @path.include? first
      puts "Skip #{first}, already seen this one"
      first = @current_links.shift
    end
    @path.unshift first
    @current_page = first
    @counter += 1
  end

  def parse_links_from_body(body)
    return nil if body['parse']['text'].nil?

    content = body['parse']['text'].split('<p>')
    content.shift
    content = content.join('')
    matches = content.scan(/(?<=href=").*?(?=")/).flatten
    if matches
      return matches.select do |link|
               link.start_with?('/wiki/') && !link.include?(':') &&
               !link.include?('#')
             end.map { |link| link.split('/').last }
    end
    nil
  end

  def search_wiki_url
    results = http_get("#{@base_url}?action=opensearch&search=#{@search}")
    @current_page = results[1].first
  end

  def http_get(full_url)
    uri = URI(full_url)
    response = Net::HTTP.get_response(uri)
    JSON.parse(response.body)
  end
end

if !ARGV[0].nil?
  WikiPhilosophyPath.new(ARGV[0]).run
else
  puts 'No arguments given.'
end
