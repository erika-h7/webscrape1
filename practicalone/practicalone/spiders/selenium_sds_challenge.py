#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:26:19 2021

@author: infinitypencil
"""

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# cool little tricks
#options = webdriver.ChromeOptions()
#options.add_argument('--incognito')

# setting our instance
driver = webdriver.Chrome()

time.sleep(2)

# website
def sds_scrape_1():
    driver.get('https://sdsclub.com/')
    driver.find_element_by_xpath('//*[@id="menu-item-456"]/a').click()
    
# closing pop ups    
def closing_pop_up():
    time.sleep(10)
    driver.find_element_by_class_name('close-icon').click()
    

sds_scrape_1()

closing_pop_up()


# select a carrier path
driver.find_element_by_xpath('//*[@id="category-career"]/div/div[2]/div[4]/div/figure/a').click()

closing_pop_up()

# add parser
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

# scraping into our data
# returning list
scrape_one = [i.text for i in soup.findAll('span', {'class': 'desc'})]
# returning list
scrape_two = [i.text for i in soup.findAll('div', {'class': 'single-path-article-content'})]
# return instructor list
scrape_three = [i.text for i in soup.findAll('p', {'class': 'name'})]
    

# create data frames
df = pd.DataFrame(scrape_one)
df_two = pd.DataFrame(scrape_two)
df_three = pd.DataFrame(scrape_three)

# printing our data
print(df, df_two, df_three)

time.sleep(10)

driver.quit()

df_scrape_one_clean = df.replace('\n', ' ', )
df_scrape_two_clean = df_two.replace('\n', ' ', )
df_scrape_three_clean = df_three.replace('\n', ' ', )
clean_stack = pd.concat([df_scrape_one_clean, df_scrape_two_clean, df_scrape_three_clean], axis=1)






