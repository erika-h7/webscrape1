#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:42:11 2021

@author: infinitypencil
"""
import time
import requests
import smtplib
from selenium import webdriver
from bs4 import BeautifulSoup

# OPTION 1
# setting our instance
#driver = webdriver.Chrome()

# going in to the website
#driver.get('https://pastebin.com/Mfc9txQV')

#def closing_pop_up():
    #time.sleep(5)
    #driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()

#closing_pop_up()

#while True:
    # add parser
    #page_source = driver.page_source
    #soup = BeautifulSoup(page_source, 'lxml')

    # scraping into our data
    #if str(soup).find("Key") == -1:
        
        #time.sleep(500)
        
        #continue
    
    #else:
        
        #print("ALERT")
        
        #break
        
        
# OPTION 2, its a quicker and better option
while True:
    url = 'https://pastebin.com/Mfc9txQV'
    headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'Accept-Language': 'en-US, en;q=0.5'})
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    if str(soup).find("Key") == -1:
        
        time.sleep(500)
        
        continue
    
    else:
        
        create_email = 'Subject: CHECK PASTEBIN ---FOUND KEY---'
        from_address = 'from address' #paste in sender email address
        to_address = 'to address' #paste in reciever email address
        # highly recomend using SSL
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.starttls()
        mail.login("USERNAME", "PASSWORD") # add your username and password
        # sending the email
        mail.sendmail(from_address, to_address, create_email)
        mail.close()
        
        print("ALERT")
        
        break
        
        
