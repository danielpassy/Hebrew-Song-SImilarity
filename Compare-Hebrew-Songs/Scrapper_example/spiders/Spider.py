import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'QuoteToScrap'
    start_urls = ['http://quotes.toscrape.com/']
    allowed_domains = ["quotes.toscrape.com"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, meta={'dont_redirect': True})


    def parse(self, response):

        ##css é equivalente a xpath, só uma outra forma de direcionar o parser, mas ambos são válidos
        title = response.css('title::text').extract()
        yield {"titletext": title}
