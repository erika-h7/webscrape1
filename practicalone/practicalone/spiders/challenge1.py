#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 13:18:50 2021

@author: infinitypencil
"""

import scrapy

class PracticaloneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    in_stock = scrapy.Field()
    
    pass


class SolutionSpider(scrapy.Spider):
    name = "Solution"
    # allowed_domains[]
    start_urls = [
        
        "https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html",
        "https://books.toscrape.com/catalogue/a-year-in-provence-provence-1_421/index.html",
        "https://books.toscrape.com/catalogue/the-third-wave-an-entrepreneurs-vision-of-the-future_862/index.html",
        "https://books.toscrape.com/catalogue/made-to-stick-why-some-ideas-survive-and-others-die_715/index.html",
        
        ]
    
    def parse(self, response):
        item = PracticaloneItem()
        
        item['category'] = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
        
        item['title'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        
        item['in_stock'] = response.xpath("normalize-space(//p[@class='instock availability']/i/following::node()[1])").get()
        
        
        return item
    
    
    
    