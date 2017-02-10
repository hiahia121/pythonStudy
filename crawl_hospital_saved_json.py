# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
from lxml import etree
import StringIO, gzip
import json

fp = open('hospital.json','w')

def gzdecode(data):
    compressedstream = StringIO.StringIO(data)
    gziper = gzip.GzipFile(fileobj=compressedstream)
    data2 = gziper.read()  # 读取解压缩后数据
    return data2


def getHtml(url):
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'__utma=118505753.1899325020.1486551615.1486551615.1486604972.2; __utmc=118505753; __utmz=118505753.1486551615.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        'Host':'www.a-hospital.com',
        'Referer':'http://www.a-hospital.com/w/%E5%8C%97%E4%BA%AC%E5%B8%82%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    }
    request = urllib2.Request(url,headers = headers)
    html = urllib2.urlopen(request).read()
    html = gzdecode(html)
    return html

def parseHtml(html):

    content = etree.HTML(html)

    countUl = len(content.xpath('//ul[3]/li'))

    for i in range(countUl):
        data = []
        hospitalName = content.xpath('//ul[3]/li[' + str(i+1) + ']/b/a/text()')

        countLi = len(content.xpath('//ul[3]/li[' + str(i+1) + ']/ul/li'))
        for j in range(countLi):
            for q in range(1):
                try:
                    key = content.xpath('//ul[3]/li[' + str(i+1) + ']/ul/li[' + str(j+1) + ']/b/text()')
                    value = content.xpath('//ul[3]/li[' + str(i+1) + ']/ul/li[' + str(j+1) + ']/text()')
                    print key[0]

                    if key[0] == '医院网站':
                        value = content.xpath('//ul[3]/li[' + str(i+1) + ']/ul/li[' + str(j+1) + ']//a/text()')

                    print value[0]
                    break
                except:
                    value = ['缺失']
            data.append({"key":"医院名称","value":hospitalName[0]})
            data.append({"key":key[0].encode('utf-8'),"value":value[0].encode('utf-8')})
        result = json.dumps(data,ensure_ascii=False)
        fp.write(result + '\n')



if __name__ == '__main__':
    url = 'http://www.a-hospital.com/w/%E5%8C%97%E4%BA%AC%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8'
    html = getHtml(url)
    parseHtml(html)

    print "============================================================================="

    fp.close()

