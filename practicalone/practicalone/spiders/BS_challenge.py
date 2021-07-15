#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 05:29:40 2021

@author: infinitypencil
"""

import requests
from bs4 import BeautifulSoup
import pandas
import time

# we will use a class with headers because we dont want to red flag their server, and it will prevent from amazon blocking our request and ban our api, this will emulate a browser request
def review_count_scrape():
    url= 'https://amazon.com/bestsellers'
    
    # we accquire the browser emulator link from : networkinghowtos.com/howto/common-user-agent-list/
    headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
        
    # this will make the request to the url   
    r = requests.get(url, headers=headers)
    
    # this will 
    soup = BeautifulSoup(r.text, 'lxml')
    
    # this will print the status code of our connection
    print(r.status_code)
    
    product_total_review = [i.text for i in soup.findAll('a', {'class': 'a-size-small a-link-normal'})]
    
    # we want to assign it to a data frame
    df = pandas.DataFrame(product_total_review)
    # alway good to see
    print(df)
    
    # add timer for every 60 seconds
    time.sleep(60)
    
# we need to run only 2 times for 2 minute total, because we dont want to span their server and run into issues
end_timer = time.time() + 60 * 2
while time.time() < end_timer:
    review_count_scrape()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                