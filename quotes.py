# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        self.log('I just visited' + response.url)
        item =  {
        'author_name': response.css('span.text::text').extract(),
        'text': response.css('span.text::text')[0].extract(),
        }
        yield item
        # pagination
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        next_page_url = response.urljoin(next_page_url)
        
