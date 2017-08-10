
# import requests
# from bs4 import BeautifulSoup
# import os

# headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
# all_url = 'http://qt.qq.com/php_cgi/news/php/varcache_article.php?id=33185'
# start_url = requests.get(all_url, headers = headers)
# Soup = BeautifulSoup(start_url.text, 'lxml')
# center_list = Soup.find_all('center')
# for center in center_list:
#     title = center.get_text()
#     print(title)

import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os
 
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'http://www.mzitu.com/all'  ##开始的URL地址
start_html = requests.get(all_url,  headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
Soup = BeautifulSoup(start_html.text, 'lxml')
all_a = Soup.find('div', class_ = 'all').find_all('a')
for a in all_a:
    title = a.get_text()
    path = str(title).strip()
    os.makedirs(os.path.join("D:\mzitu", path))
    os.chdir("D:\mzitu\\"+path)
    href = a['href']
    html = requests.get(href, headers=headers)
    html_Soup = BeautifulSoup(html.text, 'lxml')
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1, int(max_span)+1):
        page_url = href + '/' + str(page)
        img_html = requests.get(page_url, headers=headers)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_='main-image').find('img')['src']
        name = img_url[-9:-4]
        img = requests.get(img_url, headers=headers)
        f = open(name+'.jpg', 'ab')
        f.write(img.content)
        f.close()
        