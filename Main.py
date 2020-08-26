from lxml import html, etree
import pandas as pd
import requests
import scrapy

page = requests.get('https://shironet.mako.co.il/artist?type=lyrics&lang=1&prfid=1920&wrkid=11096')
tree = html.fromstring(page.content)


lirycs = tree.xpath('//span[@class="artist_lyrics_text"]/text()')
prices = tree.xpath('//a[@class="artist_singer_title"]/text()')
other_links = tree.xpath('/html/body/table[2]/tr/td/table/tr/td[2]/table/tr/td/table/tr/td[1]/table/tr/td[2]/table/tr[3]/td/table/tr/td[2]/table[1]/tr[1]/td/table/tr/td/a/img')
# response.xpath('//span[@class="artist_lyrics_text"]/text()')
# response.xpath('//a[@class="artist_singer_title"]/text()')
print(prices)
print(lirycs)
print(other_links)
# x = open("milim.txt", 'w+', encoding='utf-8')
# x.write('author: ' + prices[0] + '\n')
# for i in lirycs:
#     x.write(i)
# x.close()