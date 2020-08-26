from symbol import except_clause

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SpiderSpider(CrawlSpider):
    name = 'spider1'
    allowed_domains = ['shironet.mako.co.il']
    start_urls = ['https://shironet.mako.co.il/artist?type=works&lang=1&prfid=3963']
    base_url = 'https://shironet.mako.co.il/artist?type=works&lang=1&prfid=396'
    rules = [Rule(LinkExtractor(allow=''),
                  callback='parse_hacol', follow=True)]

    def parse_hacol(self, response):
        lyrics = response.xpath('//span[@class="artist_lyrics_text"]/text()').extract()
        author = response.xpath('//a[@class="artist_singer_title"]/text()').extract()
        title = response.xpath('//h1[@class="artist_song_name_txt"]/text()').extract()
        URL = response.request.url


        yield {
            "lyrics": lyrics,
            "author": author,
            "url": URL,
            "title": title
        }