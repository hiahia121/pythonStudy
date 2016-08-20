# -*- coding:utf-8 -*-


import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from lxml import etree

url = 'http://www.qiushibaike.com/'
files = open("data.txt","wb")
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')
tree = etree.HTML(content)
con = tree.xpath('//div[@class="content"]/text()')
for i in con:
	files.write(i + '\n')
