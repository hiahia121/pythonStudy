#coding:utf-8

import urllib2
from lxml import etree
import json
from urllib import unquote
import multiprocessing
import time




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
    countLi = len(content.xpath('//div[@itemprop="address"]/ul//li'))

    contactInfoKey.append(content.xpath('//div[@itemprop="address"]/ul/li[' + str(countLi-1) + ']/b/text()')[0])
    contactInfoKey.append(content.xpath('//div[@itemprop="address"]/ul/li[' + str(countLi) + ']/b/text()')[0])

    try:
        contactInfoVal.append(content.xpath('//table[@style="width:100%;"]/tr[6]/td[1]/ul/li[1]/span/text()')[0])
    except:
        contactInfoVal.append('empty')
    try:
        contactInfoVal.append(content.xpath('//table[@style="width:100%;"]/tr[6]/td[1]/ul/li[3]/span/text()')[0])
    except:
        contactInfoVal.append('empty')
    try:
        contactInfoVal.append(content.xpath('//div[@itemprop="address"]/ul/li[' + str(countLi-1) + ']/span/text()')[0])
    except:
        contactInfoVal.append('empty')
    try:
        contactInfoVal.append(content.xpath('//div[@itemprop="address"]/ul/li[' + str(countLi) + ']//span/text()')[0])
    except:
        contactInfoVal.append('empty')

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

    return result


def getData():
    urlList = []
    urlSplitedList = []
    for url in open(filename + '.txt', 'r'):
        urlList.append(url)
    count = len(urlList) / 10
    for i in range(10):
        urlSplitedList.append(urlList[count * i: count * (i + 1)])

    return urlSplitedList


def run(url_list,j):
    print j
    count = 1
    fjson = open(filename+str(j)+'.json','w')
    for url in url_list:
        print count
        print url
        try:
            html = getHtml(url)
            basicInfo_key, basicInfo_val, industryInfo_Key, industryInfo_val, contactInfo_key, contactInfo_val = parseHtml(
                html)
            result = saveJson(basicInfo_key, basicInfo_val, industryInfo_Key, industryInfo_val, contactInfo_key,
                              contactInfo_val)
            jsonContent = json.dumps(result, ensure_ascii=False)
            fjson.write(jsonContent + '\n')
        except:
            print 'Error'
        count +=1


if __name__ == '__main__':
    filename = unquote('%E5%BB%B6%E5%BA%86%E5%8E%BF')
    urls = getData()
    for j in range(10):
        p = multiprocessing.Process(target=run,args=(urls[j],j,))
        p.start()



    print 'over!!!!!!'


