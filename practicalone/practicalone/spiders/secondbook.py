#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:16:34 2021

@author: infinitypencil
"""

import scrapy
#from practicalone.items import PracticaloneItem

class PracticaloneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    price = scrapy.Field()
    
    pass


class SecondSpider(scrapy.Spider):
    name = "Books2"
    start_urls = [
        
        "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
        
        ]
    
    def parse(self, response):
        item = PracticaloneItem()
        #item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').extract()
        #item['price'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').extract()
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        
        return item
    
