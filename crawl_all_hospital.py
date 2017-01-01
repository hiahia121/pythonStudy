# -*- coding:utf-8 -*-
from __future__ import division
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
import json
import math


f = open('all_hospital_info.txt','w')
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

def get_list_count(url):
    html = urllib2.urlopen(url).read()
    get_json = json.loads(html)
    total = int(math.ceil(get_json["data"]["total"]/10))
    return total

if __name__ == '__main__':
    out_url_list = ['https://yi.baidu.com/pc/hospital/list?key=%E5%AE%89%E5%BE%BD&cityId=0&provId=9&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483261242440761&seed=seed_1483261451178',
                    'https://yi.baidu.com/pc/hospital/list?key=%E5%8C%97%E4%BA%AC&cityId=1&provId=1&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483261279000017&seed=seed_1483261487910',
                    'https://yi.baidu.com/pc/hospital/list?key=%E9%87%8D%E5%BA%86&cityId=33&provId=33&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483261958503381&seed=seed_1483262167296',
                    'https://yi.baidu.com/pc/hospital/list?key=%E7%A6%8F%E5%BB%BA&cityId=0&provId=5&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262056312348&seed=seed_1483262264893',
                    'https://yi.baidu.com/pc/hospital/list?key=%E7%94%98%E8%82%83&cityId=0&provId=11&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262123563462&seed=seed_1483262331944',
                    'https://yi.baidu.com/pc/hospital/list?key=%E5%B9%BF%E4%B8%9C&cityId=0&provId=4&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262163889705&seed=seed_1483262371925',
                    'https://yi.baidu.com/pc/hospital/list?key=%E5%B9%BF%E8%A5%BF&cityId=0&provId=12&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262198175022&seed=seed_1483262406420',
                    'https://yi.baidu.com/pc/hospital/list?key=%E8%B4%B5%E5%B7%9E&cityId=0&provId=10&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262223169692&seed=seed_1483262431524',
                    'https://yi.baidu.com/pc/hospital/list?key=%E6%B5%B7%E5%8D%97&cityId=0&provId=8&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262258556305&seed=seed_1483262467394',
                    'https://yi.baidu.com/pc/hospital/list?key=%E6%B2%B3%E5%8C%97&cityId=0&provId=13&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262281683512&seed=seed_1483262490416',
                    'https://yi.baidu.com/pc/hospital/list?key=%E6%B2%B3%E5%8D%97&cityId=0&provId=14&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262304515892&seed=seed_1483262513517',
                    'https://yi.baidu.com/pc/hospital/list?key=%E9%BB%91%E9%BE%99%E6%B1%9F&cityId=0&provId=15&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262342948776&seed=seed_1483262551072',
                    'https://yi.baidu.com/pc/hospital/list?key=%E6%B9%96%E5%8C%97&cityId=0&provId=16&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262374681732&seed=seed_1483262583635',
                    'https://yi.baidu.com/pc/hospital/list?key=%E6%B9%96%E5%8D%97&cityId=0&provId=17&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262394243092&seed=seed_1483262603219',
                    'https://yi.baidu.com/pc/hospital/list?key=%E5%90%89%E6%9E%97&cityId=0&provId=18&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262425286028&seed=seed_1483262634064',
                    'https://yi.baidu.com/pc/hospital/list?key=%E6%B1%9F%E8%8B%8F&cityId=0&provId=19&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262487345914&seed=seed_1483262695678',
                    'https://yi.baidu.com/pc/hospital/list?key=%E6%B1%9F%E8%A5%BF&cityId=0&provId=20&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262512343724&seed=seed_1483262720534',
                    'https://yi.baidu.com/pc/hospital/list?key=%E8%BE%BD%E5%AE%81&cityId=0&provId=21&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262543406237&seed=seed_1483262751738',
                    'https://yi.baidu.com/pc/hospital/list?key=%E5%86%85%E8%92%99%E5%8F%A4&cityId=0&provId=22&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262566185977&seed=seed_1483262774555',
                    'https://yi.baidu.com/pc/hospital/list?key=%E5%AE%81%E5%A4%8F&cityId=0&provId=23&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262589241588&seed=seed_1483262798070',
                    'https://yi.baidu.com/pc/hospital/list?key=%E9%9D%92%E6%B5%B7&cityId=0&provId=24&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262611790894&seed=seed_1483262820714',
                    'https://yi.baidu.com/pc/hospital/list?key=%E5%B1%B1%E4%B8%9C&cityId=0&provId=25&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262637764418&seed=seed_1483262845774',
                    'https://yi.baidu.com/pc/hospital/list?key=%E5%B1%B1%E8%A5%BF&cityId=0&provId=26&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262667741922&seed=seed_1483262876420',
                    'https://yi.baidu.com/pc/hospital/list?key=%E9%99%95%E8%A5%BF&cityId=0&provId=27&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262693266589&seed=seed_1483262901294',
                    'https://yi.baidu.com/pc/hospital/list?key=%E5%9B%9B%E5%B7%9D&cityId=0&provId=28&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262728363606&seed=seed_1483262937233',
                    'https://yi.baidu.com/pc/hospital/list?key=%E4%B8%8A%E6%B5%B7&cityId=2&provId=2&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262753007997&seed=seed_1483262961453',
                    'https://yi.baidu.com/pc/hospital/list?key=%E8%A5%BF%E8%97%8F&cityId=0&provId=29&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262776910289&seed=seed_1483262985715',
                    'https://yi.baidu.com/pc/hospital/list?key=%E6%96%B0%E7%96%86&cityId=0&provId=30&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262802343618&seed=seed_1483263010327',
                    'https://yi.baidu.com/pc/hospital/list?key=%E5%A4%A9%E6%B4%A5&cityId=3&provId=3&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262823567766&seed=seed_1483263031527',
                    'https://yi.baidu.com/pc/hospital/list?key=%E4%BA%91%E5%8D%97&cityId=0&provId=31&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262847513049&seed=seed_1483263055669',
                    'https://yi.baidu.com/pc/hospital/list?key=%E6%B5%99%E6%B1%9F&cityId=0&provId=32&regionId=0&pageSize=10&sortType=1&isInsurance=0&hospitalType=0&hospitalLvl=0&serviceType=0&isRecommend=0&page=1&zt=pcdyyy&zt_ext=&pvid=1483262869553863&seed=seed_1483263078278']
    for out_url in out_url_list:
        count = get_list_count(out_url)
        for j in range(1,count+1):
            url = out_url.replace("page=1","page={0}".format(j))
            html = get_html(url)
            parse_html(html)
    f.close()
