import scrapy

class ShiroNet(scrapy.Spider):
    name = 'ShiroNet'
    allowed_domains = ['shironet.mako.co.il']
    start_urls = ['https://shironet.mako.co.il/artist?type=works&lang=1&prfid=1920']

    def parse(self, response):
        i=1
        while i in range(1,30):
            links = response.xpath(
                    '/html/body/table[2]/tr/td/table/tr/td[2]/table/tr/td/table/tr/td[1]/table/tr/td[2]/table/tr[5]/td/table/tr[{}]/td/a/@href'.format(i)).get()
            i +=1
            yield {
                "links": links
            }
        # lirycs = response.xpath('//span[@class="artist_lyrics_text"]/text()').extract()
        # author = response.xpath('//a[@class="artist_singer_title"]/text()').extract()
