# -*-coding:utf8-*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
import json
import time
import string



f = open("all_music2_saved.txt","w")
def crawl_all_model_music():                     #爬下所有风格下，所有模块下的音乐＋喜欢数
    count_style_music = 0
    for up_up_up_i in range(2,18):
        time.sleep(10)
        up_up_url = "https://douban.fm/j/v2/songlist/explore?type=hot&genre={0}&limit=20&sample_cnt=5".format(up_up_up_i)
        crawl_one_model_music(up_up_url)
        count_style_music += 1
        print "###################################### " +count_style_music+ " style music has been crawled ###########################################"

def crawl_one_model_music(up_up_url):                                                #爬下一个风格下，所有模块下的音乐名字＋喜欢数

    up_up_get_json = json.loads(urllib2.urlopen(up_up_url).read())
    for up_up_i in range(len(up_up_get_json)):
        up_url = "https://douban.fm/j/v2/songlist/{0}/?kbps=192".format(up_up_get_json[up_up_i]['id'])
        crawl_one_class_music(up_url)



def crawl_one_class_music(up_url):                                        #爬取一个模块下的所有音乐名字＋喜欢数
    save_music_list = []
    up_html = urllib2.urlopen(up_url).read()
    up_json = json.loads(up_html)
    count = up_json['count']

    for i in range(0,count):
        sid = up_json["songs"][i]["sid"]
        ssid = up_json["songs"][i]["ssid"]
        last_str = sid + "g" + ssid
        url = "https://douban.fm/j/v2/song/"+ last_str
        crawl_onemusic(save_music_list,url)

    for music in save_music_list:
        f.write(music)

    print " **********************  this models has been crawled " + str(count) + " songs    *************************************"
    time.sleep(20)

def crawl_onemusic(save_music_list,url):               #爬取一首歌,并保存到列表中

    html = get_html(url)
    music_title, liked_count = parse_html(html)
    save_music_list.append(music_title)
    save_music_list.append('\t')
    save_music_list.append(liked_count)
    save_music_list.append('\n')
    print music_title + '\n'


def get_html(url):   #获取网页文本

    html = urllib2.urlopen(url).read()
    return html

def parse_html(html):  #解析网页，获取想要的音乐名字和喜欢数的内容

    data_by_json = json.loads(html)
    music_title = data_by_json['title']
    liked_count = str(data_by_json['liked_count'])

    return music_title , liked_count

if __name__ == '__main__':
    crawl_all_model_music()
    f.close()
    print "all has been crawled!!!"

