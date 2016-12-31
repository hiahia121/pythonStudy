# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
from lxml import etree

def get_html(url):
    html = urllib2.urlopen(url).read()
    return html

def parse_html(html):
    content = etree.HTML(html)
    get_data1 = content.xpath('//h1[@class="shop-name"]/text()')
    get_data2 = content.xpath('//p[@class="info shop-star"]//span[@class="item"]/text()')
    get_data = get_data1
    get_data.append('\t')
    get_data += get_data2
    get_data[0] = get_data[0].replace("\n","").replace(" ","")
    get_data[2] = get_data[2].replace("(","").replace(")","")
    print get_data
    return get_data

def save_data(get_data):
    f = open('hotel.txt','w')
    for data in get_data:
        f.write(data)
    f.close()

if __name__ == '__main__':
    url = "http://www.dianping.com/shop/10658976"
    html = get_html(url)
    get_data = parse_html(html)
    save_data(get_data)
    print "has been crawled one hotel info !!!!!!"
