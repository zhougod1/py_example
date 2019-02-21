#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


chrome_option = Options()
chrome_option.add_argument('--headless')

# chrome_option.add_argument("--proxy-server=http://" + ip：port)
# chrome_option.add_argument('user-agent= '你想修改成的User-Agent')

chrome = webdriver.Chrome(chrome_options=chrome_option)

chrome.get('https://cuiqingcai.com/2599.html')

html = chrome.page_source 

soup = BeautifulSoup(html, 'lxml')

soup.select("")


chrome.close()
