# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# -*- coding: utf-8 -*-
import scrapy
import requests


class ShiroNet(scrapy.Spider):
    name = 'ShiroasdNet'
    start_urls = ['https://shironet.mako.co.il/artist?type=lyrics&lang=1&prfid=3706&wrkid=32905']

    def parse(self, response):
        lirycs = response.xpath('//span[@class="artist_lyrics_text"]/text()').extract()
        author = response.xpath('//a[@class="artist_singer_title"]/text()').extract()

        yield {
            "lirycs": lirycs,
            "prices": author
        }