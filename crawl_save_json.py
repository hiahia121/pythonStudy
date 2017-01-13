# -*- coding:utf-8 -*-


import urllib2
from lxml import etree
import json

url = "http://beijing.mingluji.com/%E3%80%8A%E7%A7%91%E5%AD%A6%E4%B8%96%E7%95%8C%E3%80%8B%E6%9D%82%E5%BF%97%E7%A4%BE"


html = urllib2.urlopen(url).read().decode('utf-8')

content = etree.HTML(html)


gettd = content.xpath('//td[@style="width:70%; vertical-align:top;"]//b/following-sibling::*[1]/text()')

gettd1 = content.xpath('//td[@style="width:70%; vertical-align:top;"]//li/text()')

data ={
    '机构名称：':gettd[0].encode('utf-8'),
    '机构类型：':gettd[1].encode('utf-8'),
    '经营范围：':gettd1[5].encode('utf-8'),
    '经济类型：':gettd[2].encode('utf-8'),
    '注册日期：':gettd1[10].encode('utf-8'),
    '注册资金：':gettd1[12].encode('utf-8'),
    '职工人数：':gettd1[14].encode('utf-8'),
    '补充说明：':gettd[3].encode('utf-8')
}

data1 = json.dumps(data,ensure_ascii=False)
print data1
print ("++++++++++++++++++++++++++++++++++++s")

fp = open("first.json", "w")
fp.write(data1)








