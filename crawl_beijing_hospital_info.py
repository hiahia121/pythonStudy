# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
import json
f = open('hospital_info.txt','w')
def get_html(url):
    html = urllib2.urlopen(url).read()
    return html

def parse_html(html):
    get_json = json.loads(html)
    count = len(get_json["data"]["hospitalList"])
    for i in range(count):
        print get_json["data"]["hospitalList"][i]["name"]
        print get_json["data"]["hospitalList"][i]["level"]
        print get_json["data"]["hospitalList"][i]["grade"]

        f.write(get_json["data"]["hospitalList"][i]["name"])
        f.write('\t')
        f.write(get_json["data"]["hospitalList"][i]["level"])
        f.write('\t')
        f.write(get_json["data"]["hospitalList"][i]["grade"])
        f.write('\n')
if __name__ == '__main__':
    for j in range(1,25):
        url = "https://yi.baidu.com/pc/hospital/list?key=%E5%8C%97%E4%BA%AC&cityId=1&provId=1&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page={0}&zt=pcdyyy&zt_ext=&pvid=1483186557077732&seed=seed_1483187442402".format(j)
        html = get_html(url)
        parse_html(html)
    f.close()
