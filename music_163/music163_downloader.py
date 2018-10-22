"""
下载网易云中华语音乐信息
保存在data文件夹中
"""
import requests
from bs4 import BeautifulSoup
import time
import json
import re
from music_163 import save_as_json
from kg import insert_to_neo4j
from convert import converter

class Music(object):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '_ntes_nnid=7eced19b27ffae35dad3f8f2bf5885cd,1476521011210; _ntes_nuid=7eced19b27ffae35dad3f8f2bf5885cd; usertrack=c+5+hlgB7TgnsAmACnXtAg==; Province=025; City=025; NTES_PASSPORT=6n9ihXhbWKPi8yAqG.i2kETSCRa.ug06Txh8EMrrRsliVQXFV_orx5HffqhQjuGHkNQrLOIRLLotGohL9s10wcYSPiQfI2wiPacKlJ3nYAXgM; P_INFO=hourui93@163.com|1476523293|1|study|11&12|jis&1476511733&mail163#jis&320100#10#0#0|151889&0|g37_client_check&mailsettings&mail163&study&blog|hourui93@163.com; _ga=GA1.2.1405085820.1476521280; JSESSIONID-WYYY=fb5288e1c5f667324f1636d020704cab2f27ee915622b114f89027cbf60c38be2af6b9cbef2223c1f2581e3502f11b86efd60891d6f61b6f783c0d55114f8269fa801df7352f5cc4c8259876e563a6bd0212b504a8997723a0593b21d5b3d9076d4fa38c098be68e3c5d36d342e4a8e40c1f73378cec0b5851bd8a628886edbdd23a7093%3A1476623819662; _iuqxldmzr_=25; __utma=94650624.1038096298.1476521011.1476610320.1476622020.10; __utmb=94650624.14.10.1476622020; __utmc=94650624; __utmz=94650624.1476521011.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        'DNT': '1',
        'Host': 'music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    def __init__(self):
        self.graph_ = insert_to_neo4j.GraphNeo4j()
        self.converter_ = converter.converte()


    def save_artist(self, group_id, initial):
        params = {'id': group_id, 'initial': initial}
        r = requests.get('http://music.163.com/discover/artist/cat', headers=self.headers, params=params)
        # 网页解析
        soup = BeautifulSoup(r.content.decode(), 'html.parser')
        body = soup.body

        hot_artists = soup.find_all('a', attrs={'class': 'msk'})
        artists = body.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})
        save_id = str(group_id) + str(initial)
        # for artist in hot_artists + artists:
        for artist in hot_artists:
            artist_id = artist['href'].replace('/artist?id=', '').strip()
            artist_name = artist['title'].replace('的音乐', '')
            try:
                # 根据 artist_id 与 artist_name 进行专辑爬取
                data = artist_id + "$$" + artist_name
                save_as_json.save_entity(data, '../test/data/entity_artist.txt')
                self.graph_.driver_add_properties_id(artist_name, "歌手", {"id":artist_id}, [])
                self.converter_.saveGraphN3("../test/data/"+save_id+".rdf", "歌手/" + artist_name,'id',artist_id)
                self.save_albums(artist_id, artist_name, save_id)
            except Exception as e:
                # 打印错误日志
                print(e)




    def save_albums(self, artist_id, artist_name, save_id):
        params = {'id': artist_id, 'limit': '200'}
        # 获取歌手个人主页
        r = requests.get('http://music.163.com/artist/album', headers=self.headers, params=params)
        # 网页解析
        soup = BeautifulSoup(r.content.decode(), 'html.parser')
        body = soup.body
        albums = body.find_all('a', attrs={'class': 'tit s-fc0'})  # 获取所有专辑
        for album in albums:
            albume_id = album['href'].replace('/album?id=', '')
            albums_name = album.getText()
            data = artist_name + "$$" + albume_id + "$$" + albums_name
            try:
                save_as_json.save_entity(data, '../test/data/entity_album.txt')
                self.graph_.driver_add_properties_id(albums_name, "专辑", {"id": albume_id}, [])
                self.graph_.driver_add_relation_id(artist_id, artist_name, "歌手", "专辑", albume_id, albums_name, "专辑")
                self.converter_.saveGraphN3("../test/data/"+save_id+".rdf", "歌手/" + artist_name,'专辑',albums_name)
                self.converter_.saveGraphN3("../test/data/"+save_id+".rdf", "专辑/" + albums_name,'id',albume_id)
                self.save_music(albume_id, albums_name, save_id)
            except Exception as e:
                # 打印错误日志
                print(e)

    def save_music(self, album_id, albums_name, save_id):
        params = {'id': album_id}
        # 获取专辑对应的页面
        r = requests.get('http://music.163.com/album', headers=self.headers, params=params)

        # 网页解析
        soup = BeautifulSoup(r.content.decode(), 'html.parser')
        body = soup.body
        musics = body.find('ul', attrs={'class': 'f-hide'}).find_all('li')  # 获取专辑的所有音乐
        for music in musics:
            music = music.find('a')
            music_id = music['href'].replace('/song?id=', '')
            music_name = music.getText()
            data = albums_name + "$$" + music_id + "$$" + music_name
            try:
                save_as_json.save_entity(data, '../test/data/entity_music.txt')
                self.graph_.driver_add_properties_id(music_name, "歌曲", {"id": music_id}, [])
                self.graph_.driver_add_relation_id(album_id, albums_name, "专辑", "歌曲", music_id, music_name, "歌曲")
                self.converter_.saveGraphN3("../test/data/"+save_id+".rdf", "专辑/" + albums_name,'歌曲',music_name)
                self.converter_.saveGraphN3("../test/data/"+save_id+".rdf", "歌曲/" + music_name,'id',music_id)
                self.save_lyric(music_id, music_name, save_id)
            except Exception as e:
                # 打印错误日志
                print(e)

    def save_lyric(self, music_id, music_name, save_id):
        # 获取歌词，链接为网易云音乐API
        url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=1'
        try:
            response = requests.get(url, headers=self.headers)
            html = response.text
        except:
            print('request error')
        # 载入json数据
        json_obj = json.loads(html)
        # 匹配Json字段
        initial_lyric = json_obj['lrc']['lyric']
        # 正则匹配时间字符串
        regex = re.compile(r'\[.*\]')
        # 正则替换时间字符串
        final_lyric = re.sub(regex, '', initial_lyric).strip()

        data = music_name + "$$" + final_lyric
        try:
            save_as_json.save_entity(data, '../test/data/entity_lyric.txt')
            self.graph_.driver_add_properties(music_name, "歌曲", {"id": music_id}, [])
            self.graph_.driver_add_properties(music_name, "歌曲", {"歌词": final_lyric}, [])
            self.converter_.saveGraphN3("../test/data/"+save_id+".rdf", "歌曲/" + music_name,'歌词',final_lyric)
            # self.save_music(albume_id, albums_name, save_id)
        except Exception as e:
            # 打印错误日志
            print(e)

if __name__ == '__main__':
    id_range = [1001, 1002, 1003]
    music = Music()
    for i in range(65, 91):
        for j in id_range:
            music.save_artist(j, i)
    # music = Music()
    # music.save_lyric(573426358,'Are You Ready (Live)',1)
