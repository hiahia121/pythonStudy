# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
from lxml import etree

def get_html(url):
    headers = {
            'Accept':'text/html,application/xhtml+xml,'
            'application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie':'_hc.v="\"4d3d1a80-cc41-48d6-a663-a82fe36dc029.1467209186\""; PHOENIX_ID=0a010889-15954078f61-7634e8e; _tr.u=NPKejoJKIxP5DtPi;_tr.s=NKSirD4taOE5C7bF; s_ViewType=1; JSESSIONID=7E919F0D338C669EB846B197C5885AE7; aburl=1; cy=435; cye=yanqing',
            'Host':'www.dianping.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    request = urllib2.Request(url,headers=headers)
    html = urllib2.urlopen(request).read()
    return html


if __name__ == '__main__':
	 url = "http://www.dianping.com/yanqing/hotel"
	 html = get_html(url)
	 print html
