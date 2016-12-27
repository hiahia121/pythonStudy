# -*-coding:gbk-*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
import json
import time

full_url = []
target_data = []
url = "https://douban.fm/j/v2/songlist/explore?type=hot&genre=0&limit=20&sample_cnt=5"

pages = urllib2.urlopen(url).read()
get_json = json.loads(pages)


for t in range(len(get_json)):
    full_url.append('https://douban.fm/j/v2/songlist/{0}/?kbps=192'.format(get_json[t]["id"]))


for x in full_url:
    print x
    url_last_str = []
    time.sleep(10)
    html = urllib2.urlopen(x).read()

    hjson = json.loads(html)
    count = hjson['count']

    for i in range(0, count):
        sid = hjson["songs"][i]["sid"]
        ssid = hjson["songs"][i]["ssid"]
        last_str = sid + "g" + ssid
        url_last_str.append(last_str)

    for j in range(len(url_last_str)):
        url_last_str[j] = "https://douban.fm/j/v2/song/" + url_last_str[j]

    for q in url_last_str:
        pages = urllib2.urlopen(q).read()
        njson = json.loads(pages)

        print pages
        print "============================="
        music_title = njson['title']
        liked_count = str(njson['liked_count'])
        target_data.append(music_title)
        target_data.append('\t')
        target_data.append(liked_count)
        target_data.append('\n')

        file_music = open('testmusic.txt', 'w')
        for m in range(len(target_data)):
            file_music.write(target_data[m])

    time.sleep(5)
file_music.close()
