# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2, httplib
import time
import StringIO, gzip
from lxml import etree
count = 1
url_list = []
f = open('three_city_hotel.txt','w')
# 解压gzip
def gzdecode(data):
    compressedstream = StringIO.StringIO(data)
    gziper = gzip.GzipFile(fileobj=compressedstream)
    data2 = gziper.read()  # 读取解压缩后数据
    return data2

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
    html = gzdecode(html)
    return html

def get_one_hotel_html(one_url):
    one_hotel_html = urllib2.urlopen(one_url).read()
    return one_hotel_html

def parse_one_hotel_html(one_hotel_html):
    content = etree.HTML(one_hotel_html)
    get_data1 = content.xpath('//h1[@class="shop-name"]/text()')
    get_data2 = content.xpath('//p[@class="info shop-star"]//span[@class="item"]/text()')
    get_data = get_data1
    get_data.append('\t')
    get_data += get_data2
    get_data.append('\n')
    get_data[0] = get_data[0].replace("\n", "").replace(" ", "")
    get_data[2] = get_data[2].replace("(", "").replace(")", "")
    return get_data

def parse_html(html):
    content = etree.HTML(html)
    print "********************************crawling "+str(count)+" module************************************************"
    get_data = content.xpath('//a[@class="hotel-name-link"]/@href')
    for data in get_data:
        one_url = 'http://www.dianping.com' + data
        one_hotel_html = get_one_hotel_html(one_url)
        get_data = parse_one_hotel_html(one_hotel_html)
        for data in get_data:
            f.write(data)


if __name__ == '__main__':
    city_list = ['beijing','tianjin','shanghai']
    for city in city_list:
        url = "http://www.dianping.com/{0}/hotel/".format(city)
        html = get_html(url)
        parse_html(html)
        count +=1
        for i in range(2,51):
            url = "http://www.dianping.com/{0}/hotel/p{1}".format(city,i)
            html = get_html(url)
            parse_html(html)
            count +=1
        print "##################################################  " + city + "  has been crawled #######################################"
        time.sleep(5)
    print "all has been crawled!!!"
    f.close()
