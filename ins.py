#-*- coding: utf-8 -*-
"""douban_Top250"""
import urllib2
import string
import re
import csv
from BeautifulSoup import BeautifulSoup
import sys
import wget

# 书名 URL 作者 简介 封面下载

reload(sys)
sys.setdefaultencoding('utf8')

def clean_html(html):
    '''清除html文本中的相关转义符号'''
    html = re.sub('&nbsp;', ' ', html)
    html = re.sub('&ensp;', ' ', html)
    html = re.sub('&emsp;', ' ', html)
    html = re.sub('&amp;', '&', html)
    html = re.sub('&lt;', '<', html)
    html = re.sub('&gt;', '>', html)
    html = re.sub('&quot;', '"', html)
    return html    

def ins():
    BASE_URL = "https://www.instagram.com/ravaray/"
    soup = BeautifulSoup(urllib2.urlopen(BASE_URL))
    for items in soup.findAll('img',{'class':'_icyx7'}):
        picpath = items['src']
        print picpath
        wget.download(picpath,"insimg/")

if __name__ == '__main__':
    ins()
