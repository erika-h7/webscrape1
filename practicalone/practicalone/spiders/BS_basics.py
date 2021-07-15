#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 05:07:49 2021

@author: infinitypencil
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('http://quotes.toscrape.com/')

soup = BeautifulSoup(r.content, 'lxml')

quotes = soup.find_all("div", class_="quote")
for x in quotes:
    print(x.find("span").text)
    

tags = soup.find_all("div", class_="tags")
for x in tags:
    print(x.text)