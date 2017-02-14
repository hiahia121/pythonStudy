# -*- coding:gbk -*-
import sys
reload(sys)
sys.setdefaultencoding('gbk')
import urllib2
from lxml import etree


def getHtml(url):
    html = unicode(urllib2.urlopen(url).read(),'gbk').encode('utf-8')
    return html


def parseHtml(html):
    content = etree.HTML(html)
    count_tr = len(content.xpath('//div[@id="page_left"]/table[1]//tr'))
    print count_tr-1
    for i in range(2,count_tr+1):
        areaName = content.xpath('//div[@id="page_left"]/table[1]/tr[' + str(i) + ']/td[1]//a/text()')
        streetUrl = content.xpath('//div[@id="page_left"]/table[1]/tr[' + str(i) + ']/td[6]//a/@href')
        f = open('./streetUrl/' + areaName[0].strip() + '.txt' , 'w')
        for j in streetUrl:
            f.write('http://www.tcmap.com.cn' + j +'\n')
        f.close()



if __name__ == '__main__':
    url = 'http://www.tcmap.com.cn/tianjin/'
    html = getHtml(url)
    parseHtml(html)