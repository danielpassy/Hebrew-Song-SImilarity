import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class QuotetutorialItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    pass

class testSpider(CrawlSpider):
    name = "aranha"
    start_urls = ['https://stackoverflow.com/questions/37380588/performing-a-scrapy-broad-crawl-with-high-concurrency-and-low-request-rate-on-ea']
    rules = [Rule(LinkExtractor(allow=''),
                  callback='parse', follow=True)]

    def parse(self, response):
        oi = QuotetutorialItem()
        yield oi