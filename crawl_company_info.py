#coding:utf-8

import urllib2
from lxml import etree
import json


def getHtml(url):
    html = urllib2.urlopen(url).read().decode('utf-8','ignore').encode('utf-8')
    return html

def getBasicInfo(content):
    basicInfoKey = content.xpath('//td[@style="width:70%; vertical-align:top;"]/ul//li/b/text()')
    countLi = len(content.xpath('//td[@style="width:70%; vertical-align:top;"]/ul//li'))

    basicInfoVal = []
    basicInfoVal.append(content.xpath('//span[@itemprop="name"]/text()')[0].strip())

    for i in range(countLi):
        if basicInfoKey[i] == u'机构类型：':
            index = basicInfoKey.index(u'机构类型：')
            for q in range(1):
                try:
                    basicInfoVal.append(content.xpath(
                        '//td[@style="width:70%; vertical-align:top;"]/ul/li[' + str(index + 1) + ']/a/text()')[0])
                    break
                except:
                    basicInfoVal.append('empty')

        elif basicInfoKey[i] == u'经营范围：':
            index1 = basicInfoKey.index(u'经营范围：')
            for q in range(1):
                try:
                    basicInfoVal.append(content.xpath(
                        '//td[@style="width:70%; vertical-align:top;"]/ul/li[' + str(index1 + 1) + ']/text()')[1])
                    break
                except:
                    basicInfoVal.append('empty')

        elif basicInfoKey[i] == u'经济类型：':
            index2 = basicInfoKey.index(u'经济类型：')
            for q in range(1):
                try:
                    basicInfoVal.append(content.xpath(
                        '//td[@style="width:70%; vertical-align:top;"]/ul/li[' + str(index2 + 1) + ']/a/text()')[0])
                    break
                except:
                    basicInfoVal.append('empty')

        elif basicInfoKey[i] == u'注册日期：':
            index3 = basicInfoKey.index(u'注册日期：')
            for q in range(1):
                try:
                    basicInfoVal.append(content.xpath(
                        '//td[@style="width:70%; vertical-align:top;"]/ul/li[' + str(index3 + 1) + ']/text()')[1])
                    break
                except:
                    basicInfoVal.append('empty')
        elif basicInfoKey[i] == u'注册资金：':
            index4 = basicInfoKey.index(u'注册资金：')
            for q in range(1):
                try:
                    basicInfoVal.append(content.xpath(
                        '//td[@style="width:70%; vertical-align:top;"]/ul/li[' + str(index4 + 1) + ']/text()')[1])
                    break
                except:
                    basicInfoVal.append('empty')

        elif basicInfoKey[i] == u'职工人数：':

            index5 = basicInfoKey.index(u'职工人数：')

            for q in range(1):
                try:
                    basicInfoVal.append(content.xpath(
                        '//td[@style="width:70%; vertical-align:top;"]/ul/li[' + str(index5 + 1) + ']/text()')[1])
                    break
                except:
                    basicInfoVal.append('empty')

    basicInfoVal.append('')
    basicInfoVal[-1] = content.xpath('//span[@itemprop="description"]/text()')[0]

    return basicInfoKey , basicInfoVal

def getIndustryInfo(content):
    industryInfoKey = []
    industryInfoVal = []
    industryInfoVal.append(content.xpath('//table[@style="width:100%;"]/tr[4]/td[1]/ul/li/text()')[1].strip())
    industryInfoKey.append(content.xpath('//table[@style="width:100%;"]/tr[4]/td[1]/ul/li/b/text()')[0])


    countLi = len(content.xpath('//table[@style="width:100%;"]/tr[4]/td[1]/ul/li/ul//li/b/text()'))
    for i in range(countLi):
        industryInfoKey.append(content.xpath('//table[@style="width:100%;"]/tr[4]/td[1]/ul/li/ul/li[' + str(i + 1) + ']/b/text()')[0])
        industryInfoVal.append(content.xpath('//table[@style="width:100%;"]/tr[4]/td[1]/ul/li/ul/li[' + str(i + 1) + ']/a/text()')[0])

    return industryInfoKey , industryInfoVal

def getContactInfo(content):
    contactInfoKey = []
    contactInfoVal = []

    contactInfoKey.append(content.xpath('//table[@style="width:100%;"]/tr[6]/td[1]/ul/li[1]/b/text()')[0])
    contactInfoKey.append(content.xpath('//table[@style="width:100%;"]/tr[6]/td[1]/ul/li[3]/b/text()')[0])
    contactInfoKey.append(content.xpath('//div[@itemprop="address"]/ul/li[5]/b/text()')[0])
    contactInfoKey.append(content.xpath('//div[@itemprop="address"]/ul/li[6]/b/text()')[0])

    contactInfoVal.append(content.xpath('//table[@style="width:100%;"]/tr[6]/td[1]/ul/li[1]/span/text()')[0])
    contactInfoVal.append(content.xpath('//table[@style="width:100%;"]/tr[6]/td[1]/ul/li[3]/span/text()')[0])
    contactInfoVal.append(content.xpath('//div[@itemprop="address"]/ul/li[5]/span/text()')[0])
    contactInfoVal.append(content.xpath('//div[@itemprop="address"]/ul/li[6]//span/text()')[0])


    return contactInfoKey , contactInfoVal

def parseHtml(html):
    content = etree.HTML(html)
    basicInfo_key, basicInfo_val = getBasicInfo(content)
    industryInfo_Key, industryInfo_val = getIndustryInfo(content)
    contactInfo_key, contactInfo_val =getContactInfo(content)

    return basicInfo_key , basicInfo_val ,industryInfo_Key ,industryInfo_val , contactInfo_key , contactInfo_val



def saveJson(basicInfo_key,basicInfo_val,industryInfo_Key,industryInfo_val,contactInfo_key,contactInfo_val):
    result1 = []
    result2 = []
    result3 = []

    for i in range(len(basicInfo_key)):
        result1.append({"value":basicInfo_val[i].encode('utf-8'),"key":basicInfo_key[i].encode('utf-8')})

    for i in range(len(industryInfo_Key)):
        result2.append({"value":industryInfo_val[i].encode('utf-8'),"key":industryInfo_Key[i].encode('utf-8')})

    for i in range(len(contactInfo_key)):
        result3.append({"value":contactInfo_val[i].encode('utf-8'),"key":contactInfo_key[i].encode('utf-8')})


    result = {"basicInfo":{"thisCompany":result1},"industryInfo":{"thisCompany":result2},"contactInfo":{"thisCompany":result3}}

    print result
    jsonContent = json.dumps(result, ensure_ascii=False)
    f = open('first.json','w')
    f.write(jsonContent)
    f.close()

if __name__ == '__main__':
    url5 = 'https://beijing.mingluji.com/%E3%80%8A%E4%B8%96%E7%95%8C%E6%96%B0%E9%97%BB%E6%8A%A5%E3%80%8B%E7%A4%BE'
    url = 'https://beijing.mingluji.com/%E3%80%8A%E4%B8%96%E7%95%8C%E6%96%B0%E9%97%BB%E6%8A%A5%E3%80%8B%E7%A4%BE'
    url1 = 'https://beijing.mingluji.com/%E3%80%8A%E4%B8%AD%E5%9B%BD%E5%8D%B0%E5%88%B7%E3%80%8B%E6%9D%82%E5%BF%97%E7%A4%BE'
    url2 = 'https://beijing.mingluji.com/%E4%B8%8A%E6%B5%B7%E6%97%A5%E4%B8%B0%E7%AE%A1%E4%B8%9A%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%8C%97%E4%BA%AC%E9%94%80%E5%94%AE%E5%88%86%E5%85%AC%E5%8F%B8'
    url3 = 'https://beijing.mingluji.com/%E4%B8%8A%E6%B5%B7%E5%8A%AA%E5%A5%A5%E7%BD%97%E6%95%A3%E7%83%AD%E5%99%A8%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%8C%97%E4%BA%AC%E5%88%86%E5%85%AC%E5%8F%B8'
    url4 = 'https://beijing.mingluji.com/%E5%85%89%E5%A4%A7%E5%9B%BD%E9%99%85%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%80%BB%E5%85%AC%E5%8F%B8%E7%AC%AC%E4%B9%9D%E5%B7%A5%E7%A8%8B%E5%A4%84'
    html = getHtml(url2)
    basicInfo_key, basicInfo_val, industryInfo_Key, industryInfo_val, contactInfo_key, contactInfo_val =parseHtml(html)
    saveJson(basicInfo_key, basicInfo_val, industryInfo_Key, industryInfo_val, contactInfo_key, contactInfo_val)

