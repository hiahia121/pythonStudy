# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib2
from lxml import etree
import time
import random


f = open('info_taiyuan2_hotels.txt','w')
f1 = open('taiyuan_url.txt','w')
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
    get_data.append('\n')
    get_data[0] = get_data[0].replace("\n", "").replace(" ", "")
    get_data[2] = get_data[2].replace("(", "").replace(")", "")
    return get_data


def run():
    count = 1
    url_list = []
    for url in open('hotels_taiyuan.txt'):
        url_list.append(url)

    for i in url_list[0:]:

        print i
        f1.write(i)

        for j in range(3):
            time.sleep(j*5)
            try:
                html = get_html(i)
                data = parse_html(html)
                for aim_data in data:
                    f.write(aim_data)
                print count
                count +=1
                print "+++++++++++++++++++++++++++++++++++++++++++"
                j = 0
                break
            except:
                print 'error'






if __name__ == '__main__':
    run()
    f.close()
    f1.close()
    print "all has been crawled and saved"
