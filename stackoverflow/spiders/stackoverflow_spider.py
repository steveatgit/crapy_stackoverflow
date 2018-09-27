import scrapy
from stackoverflow.items import StackoverflowItem


class StackOverflowSpider(scrapy.Spider):
    name = 'stack'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        item = StackoverflowItem()
        item['title'] = response.css('h1 a::text').extract()[0]
        item['votes'] = response.css('.question .vote-count-post::text').extract()[0]
        item['body'] = response.css('.question .post-text').extract()[0]
        item['tags'] = response.css('.question .post-tag::text').extract()
        item['link'] = response.url
        yield item
