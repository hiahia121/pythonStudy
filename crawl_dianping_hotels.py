# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib2, httplib
import time
import StringIO, gzip
from lxml import etree

sleep_count = 1
entry_url = []
f = open('hotels_changchun.txt','w')
def gzdecode(data):
    compressedstream = StringIO.StringIO(data)
    gziper = gzip.GzipFile(fileobj=compressedstream)
    data2 = gziper.read()  # 读取解压缩后数据
    return data2

def get_html(url):                                                  #获取url网页信息
    headers = {
        'Accept': 'text/html,application/xhtml+xml,'
                  'application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_hc.v=da9ed1e5-2c7e-b59e-6df7-f18e385184b3.1483090213; __utma=205923334.377081170.1483420878.1483420878.1483420878.1; __utmc=205923334; __utmz=205923334.1483420878.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHOENIX_ID=0a017918-1596366d5a9-12d911bd; __mta=147673992.1483495506032.1484022837275.1484024188239.22; s_ViewType=1; JSESSIONID=CC359CAB58603541AB3A62BC729F73B4; aburl=1; cy=70; cye=changchun',
        'Host': 'www.dianping.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    }
    request = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(request).read()
    html = gzdecode(html)
    return html

def parse_html(html):                                           #解析url="http://www.dianping.com/beijing/hotel/"网页信息
    content = etree.HTML(html)
    get_data = content.xpath('//div[@class="nav-2nd J_choice-trigger-wrap-downtown"]/a/@href')
    return get_data

def packge_url(url_part):                                       #组装成新的url,并追加到entry_url列表中
    for data in url_part:
        data = "http://www.dianping.com"+data
        entry_url.append(data)

def parse_aim_url_html(html):                                  #爬去目标网页中的数据信息，宾馆名＋点评量
    content = etree.HTML(html)
    get_data1 = content.xpath('//h1[@class="shop-name"]/text()')
    get_data2 = content.xpath('//p[@class="info shop-star"]//span[@class="item"]/text()')
    get_data = get_data1
    get_data.append('\t')
    get_data += get_data2
    get_data.append('\n')
    get_data[0] = get_data[0].replace("\n", "").replace(" ", "")
    get_data[2] = get_data[2].replace("(", "").replace(")", "")
    return get_data

def parse_next_floor_url_html(html):                           #解析下一层url网页信息，并爬去单个网页中的数据
    content = etree.HTML(html)
    get_data = content.xpath('//a[@class="hotel-name-link"]/@href')
    for data in get_data:
        url = 'http://www.dianping.com' + data
        html = get_html(url)
        get_aim_data = parse_aim_url_html(html)
        for aim_data in get_aim_data:
            f.write(aim_data)


def parse_html_and_get_count(html):                                     #获取列总表数
    content = etree.HTML(html)
    get_data = content.xpath('//a[@class="next"]/preceding-sibling::*[1]/text()')
    data = int(get_data[0])
    return data


if __name__ == '__main__':
    url = "http://www.dianping.com/changchun/hotel/"
    get_out_floor_html = get_html(url)
    get_data = parse_html(get_out_floor_html)
    packge_url(get_data)                                                #准备好中间层url列表
    print entry_url
    print len(entry_url)
    new_list_url = entry_url[0:len(entry_url)]
    print new_list_url
    for one_entry_url in new_list_url:                                     #one_entry_url表示一个区的url
        entry_url_html = get_html(one_entry_url)
        count = parse_html_and_get_count(entry_url_html)
        print count
        print one_entry_url
        print "++++++++++++++++++++++++++++++++++++++++++"
        get_next_floor_url_html = get_html(one_entry_url)
        parse_next_floor_url_html(get_next_floor_url_html)
        for index in range(2,count+1):
            time.sleep(2)
            list_url = one_entry_url + "p{0}".format(index)
            print list_url
            get_list_url_html = get_html(list_url)
            #print get_list_url_html
            parse_next_floor_url_html(get_list_url_html)
            sleep_count += 1
            if sleep_count % 5 == 0:
                time.sleep(30)
            print "++++++++++++++++++++++++++++++++++++++++++"
        time.sleep(50)
    f.close()

