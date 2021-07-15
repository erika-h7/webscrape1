#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 10:00:20 2021

@author: infinitypencil
"""

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.superdatascience.com')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div[1]/div/nav/ul/li[7]/a').click()



time.sleep(5)
driver.quit()