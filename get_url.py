#coding:utf-8
import urllib2
from lxml import etree
from urllib import unquote

def getHtml(url):
    html = urllib2.urlopen(url).read()
    return html

def getUrls(content):

    urlList = content.xpath('//div[@class="mw-category"]//ul//li/a/@href')

    for index in range(len(urlList)):
        urlList[index] = 'https://beijing.mingluji.com' + urlList[index]
    return urlList

def getNextPage(content):
    tagAText = content.xpath('//div[@id="mw-pages"]/a[2]/text()')
    tagAUrl = content.xpath('//div[@id="mw-pages"]/a[2]/@href')
    tagAUrl[0] = 'https://beijing.mingluji.com' + tagAUrl[0]
    return tagAText, tagAUrl

def parseHtml(html):
    content = etree.HTML(html)
    urlList = getUrls(content)

    tagAText , tagAUrl = getNextPage(content)

    return urlList , tagAText ,tagAUrl

def crawl(f,url):
    html = getHtml(url)
    url_list, tag_a_text, tag_a_url = parseHtml(html)
    for url in url_list:
        f.write(url + '\n')
    return tag_a_text ,tag_a_url

if __name__ == '__main__':
    url = 'https://beijing.mingluji.com/%E5%88%86%E7%B1%BB:%E5%BB%B6%E5%BA%86%E5%8E%BF'
    file_name = url.split(':')[2]
    count = 1
    f = open(unquote(file_name) +'.txt','w')
    tagA_text , tagA_url = crawl(f,url)
    print tagA_text[0]
    while(tagA_text[0] == u'下一页'):
        new_url = tagA_url[0]
        tagA_text, tagA_url = crawl(f, new_url)
        print count
        count +=1
    f.close()
    print "over!!!!!!"