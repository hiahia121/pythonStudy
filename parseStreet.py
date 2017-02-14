# -*- coding:gbk -*-
import sys
reload(sys)
sys.setdefaultencoding('gbk')
import urllib2
from lxml import etree
import json
import os

def getHtml(url):

    html = urllib2.urlopen(url).read().decode('gbk', 'ignore').encode('utf-8')
    return html



def parseHtml(html):
    data = []
    data1 = []
    content = etree.HTML(html)
    count_tr = len(content.xpath('//div[@style="float:right "]/table//tr'))


    areaName = content.xpath('//div[@style="float:right "]/table/tr[1]/td/a/text()')

    for i in range(count_tr-1):
        data.append(content.xpath('//div[@style="float:right "]/table//tr[' + str(i + 1) + ']/td/strong/text()'))
        data1.append(content.xpath('//div[@style="float:right "]/table//tr[' + str(i + 1) + ']/td/text()'))

    return data , data1 , areaName


def savedJson(data,data1 ,areaName):
    result = []
    for index in range(len(data)-1):
        for q in range(1):
            try:
                result.append({"key": data[index][0].encode('utf-8'), "value": data1[index][0].encode('utf-8')})
                if index == 0:
                    result.append({"key": data[index][1].encode('utf-8'), "value": areaName[0].encode('utf-8')})
                else:
                    result.append({"key": data[index][1].encode('utf-8'), "value": data1[index][1].encode('utf-8')})
                break

            except:
                print 'error'

    result.append({"key":data[-1][0].encode('utf-8'),"value":data1[-1][0].encode('utf-8')})

    jsonContent = json.dumps(result,ensure_ascii=False)

    return jsonContent

if __name__ == '__main__':
    count = 1
    area_path = './streetUrl/'
    files = os.listdir(area_path)
    for file in files:
        file_name = os.path.splitext(file)[0].strip()
        print file_name

        fileJson = open('./resultJson/' + file_name + '.json' , 'w')
        for url in open(area_path + file_name + '.txt','r'):
            print count

            for q in range(3):
                try:
                    html = getHtml(url)
                    result1 , result2 ,area_name = parseHtml(html)
                    json_content = savedJson(result1,result2 ,area_name)
                    fileJson.write(json_content + '\n')
                    count +=1
                    break
                except:
                    print 'Error'
        fileJson.close()





