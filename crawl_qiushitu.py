import urllib2
import urllib
from lxml import etree

url = 'http://www.qiushibaike.com/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
content = response.read()
tree = etree.HTML(content)
con = tree.xpath('//img/@src')
x = 0
for i in con:
	urllib.urlretrieve(i,'%s.jpg' % x)
	x+=1
