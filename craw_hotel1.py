# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib2, httplib
import time
import StringIO, gzip
from lxml import etree
count = 1
sleep_count = 1
url_list = []
f = open('all_jining_hotel.txt','w')
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
            'Cookie':'_hc.v=da9ed1e5-2c7e-b59e-6df7-f18e385184b3.1483090213; __utma=205923334.377081170.1483420878.1483420878.1483420878.1; __utmc=205923334; __utmz=205923334.1483420878.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHOENIX_ID=0a017918-1596366d5a9-12d911bd; __mta=147673992.1483495506032.1483526448192.1483581336242.17; s_ViewType=1; JSESSIONID=617D7DE4821C99E72393B91F0D62D942; aburl=1; cy=149; cye=weifang',
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
    city_list = ['jining']
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
            sleep_count +=1
            if sleep_count % 5 == 0:
                time.sleep(5)
            elif sleep_count % 25 == 0:
                time.sleep(25)
        print "##################################################  " + city + "  has been crawled #######################################"
        time.sleep(5)
    print "all has been crawled!!!"
    f.close()
