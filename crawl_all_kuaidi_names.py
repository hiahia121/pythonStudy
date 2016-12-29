# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
from lxml import etree


def get_html(url):
    html = urllib2.urlopen(url).read()
    return html


def parse_html(html):
    content = etree.HTML(html)
    get_data1 = [i.encode('utf-8') for i in content.xpath('//div[@class="column-1 column-list"]//a/text()')]
    get_data2 = [j.encode('utf-8') for j in content.xpath('//div[@class="column-2 column-list"]//a/text()')]
    get_data = get_data1 + get_data2

    return get_data

def save_data(get_data):
    f = open('all_kuaidi_names.txt', 'w')
    for data in get_data:
        f.write(data)
        f.write('\n')

    f.close()

def main():
    url = "https://www.kuaidi100.com/all/index.shtml?from=newindex"
    html = get_html(url)
    get_data = parse_html(html)
    save_data(get_data)

if __name__ == "__main__":

    main()
    print "all has been crawled!!!!"
