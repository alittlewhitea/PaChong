# -*- coding:utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://qt.qq.com/php_cgi/news/php/varcache_article.php?id=33185'
start_url = requests.get(all_url, headers = headers)
Soup = BeautifulSoup(start_url.text, 'lxml')
# center_list = Soup.find_all('center')
artical_center = Soup.find_all('center')
for center in artical_center:
    ni = center['alt']
    print (ni)