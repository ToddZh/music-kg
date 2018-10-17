import requests
import json
import  bs4
from bs4 import BeautifulSoup
from music_163 import save_as_json
from urllib.parse import urljoin

# https://baike.baidu.com/item/中文内容

def entity_labeling(self, label):
    if label is None:
        return None
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    #            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9,image/webp, * / *;q = 0.8'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'content-type': 'application/json',
               'Content-Encoding': 'deflate'}
    s = json.dumps(label)
    url = 'https://aip.baidubce.com/rpc/2.0/kg/v1/cognitive/entity_annotation?access_token=24.874a79e13df6c5e405ba01ff7c6a789b.2592000.1541819315.282335-14277744'
    response = requests.post(url,headers=headers,timeout=10,data=s)
    response.encoding = 'utf-8'
    if response.status_code != 200:
        return None
    # response = BeautifulSoup(response.text, 'lxml')
    return response.text

def baidubaike_download(target, type):
    url = "https://baike.baidu.com/item/" + target
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    #            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9,image/webp, * / *;q = 0.8'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Content-Encoding': 'deflate'}
    response = requests.get(url, headers=headers, timeout=10)
    response.encoding = 'utf-8'
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        if type == 'artist':
            data = get_artist(soup)
        elif type == 'album':
            data = get_album(soup)
        elif type == 'music':
            data = get_music(soup)
        else:
            return not None
        return data
    except:
        return not None


def get_artist(soup):
    # 主题——artist
    title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').text
    # 简介
    introduction_node = soup.find(class_='lemma-summary').text[1:]

    # 去掉引用
    introduction_node_findn1 = -1
    introduction_node_findn2 = 0

    while (introduction_node.find('\n', introduction_node_findn2)):
        introduction_node_findn1 = introduction_node_findn2
        introduction_node_findn2 = introduction_node.find('\n', introduction_node_findn2 + 1)
        # print(introduction_node)
        if introduction_node_findn2 < 0 or introduction_node_findn2 == (len(introduction_node) - 1):
            break
        width = introduction_node_findn2 - introduction_node_findn1
        if width < 10 and introduction_node_findn1 != -1:
            introduction_node = introduction_node[:introduction_node_findn1] + introduction_node[
                                                                               introduction_node_findn2 + 1:]
            introduction_node_findn1 -= 1
            introduction_node_findn2 -= (width + 1)
    print(introduction_node)

    # 基本信息
    basic_name_node = soup.findAll('dt', class_='basicInfo-item name')
    basic_value_node = soup.findAll('dd', class_='basicInfo-item value')
    basic_node = {}
    for i, j in zip(basic_name_node, basic_value_node):
        name = i.text.replace('\xa0', '')
        if j.text[1:-1].find('、'):
            value = j.text[1:-1].split('、')
        # elif j.text.find('\n',1,-1):
        #     value = j.text.split('\n')
        else:
            value = j.text[1:-1]
        basic_node[name] = value

    # 专辑
    music_album_node = []
    music_album = soup.findAll('li', class_='album-item')
    if music_album == []:
        music_album_table = soup.find('table', class_='musicAlbum-table')
        for row in music_album_table.findAll("td", class_='with-padding'):
            # print(row)
            album = row.text.strip('\n')
            music_album_node.append(album)
            save_as_json.save_entity_album(album)
    else:
        for j in music_album:
            album_name = j.text.split('\n')
            for i in album_name:
                if i != '':
                    try:
                        int(i)
                        continue
                    except:
                        music_album_node.append(i)
                        save_as_json.save_entity_album(i)

    print(music_album_node)
    data_json = {
        'title_node': title_node,
        'introduction_node': introduction_node,
        'basic_node': basic_node,
        'music_album_node': music_album_node
    }
    return data_json

def get_album(soup):
    # 主题——album
    title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').text
    # 简介
    introduction_node = soup.find(class_='lemma-summary').text[1:]

    # 去掉引用
    introduction_node_findn1 = -1
    introduction_node_findn2 = 0

    while (introduction_node.find('\n', introduction_node_findn2)):
        introduction_node_findn1 = introduction_node_findn2
        introduction_node_findn2 = introduction_node.find('\n', introduction_node_findn2 + 1)
        # print(introduction_node)
        if introduction_node_findn2 < 0 or introduction_node_findn2 == (len(introduction_node) - 1):
            break
        width = introduction_node_findn2 - introduction_node_findn1
        if width < 10 and introduction_node_findn1 != -1:
            introduction_node = introduction_node[:introduction_node_findn1] + introduction_node[
                                                                               introduction_node_findn2 + 1:]
            introduction_node_findn1 -= 1
            introduction_node_findn2 -= (width + 1)
    print(introduction_node)

    # 基本信息
    basic_name_node = soup.findAll('dt', class_='basicInfo-item name')
    basic_value_node = soup.findAll('dd', class_='basicInfo-item value')
    basic_node = {}
    for i, j in zip(basic_name_node, basic_value_node):
        name = i.text.replace('\xa0', '')
        if j.text[1:-1].find('、'):
            value = j.text[1:-1].split('、')
        # elif j.text.find('\n',1,-1):
        #     value = j.text.split('\n')
        else:
            value = j.text[1:-1]
        basic_node[name] = value

    # 专辑歌曲
    music_node = []
    music_table = soup.find('table', class_='table-view log-set-param')
    for row in music_table.findAll("tr"):
        cells = row.findAll("td")
        if len(cells) >= 2 and cells[1] != None:
            music = cells[1].text.strip('\n')
            music_node.append(music)
            save_as_json.save_entity_music(music)
    data_json = {
        'title_node': title_node,
        'introduction_node': introduction_node,
        'basic_node': basic_node,
        'music_node': music_node
    }
    return data_json

def get_music(soup):
    # 主题——music
    title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').text
    # 简介
    introduction_node = soup.find(class_='lemma-summary').text[1:]

    # 去掉引用
    introduction_node_findn1 = -1
    introduction_node_findn2 = 0

    while (introduction_node.find('\n', introduction_node_findn2)):
        introduction_node_findn1 = introduction_node_findn2
        introduction_node_findn2 = introduction_node.find('\n', introduction_node_findn2 + 1)
        # print(introduction_node)
        if introduction_node_findn2 < 0 or introduction_node_findn2 == (len(introduction_node) - 1):
            break
        width = introduction_node_findn2 - introduction_node_findn1
        if width < 10 and introduction_node_findn1 != -1:
            introduction_node = introduction_node[:introduction_node_findn1] + introduction_node[
                                                                               introduction_node_findn2 + 1:]
            introduction_node_findn1 -= 1
            introduction_node_findn2 -= (width + 1)
    print(introduction_node)

    # 基本信息
    basic_name_node = soup.findAll('dt', class_='basicInfo-item name')
    basic_value_node = soup.findAll('dd', class_='basicInfo-item value')
    basic_node = {}
    for i, j in zip(basic_name_node, basic_value_node):
        name = i.text.replace('\xa0', '')
        if j.text[1:-1].find('、'):
            value = j.text[1:-1].split('、')
        # elif j.text.find('\n',1,-1):
        #     value = j.text.split('\n')
        else:
            value = j.text[1:-1]
        basic_node[name] = value
    # 歌词信息
    music_title = soup.findAll('div')
    music_lyric_node = ""
    lyric_begin = False
    message1 = title_node.text + "歌曲鉴赏"
    message2 = title_node.text + "歌曲歌词"
    for i in  range(len(music_title)):
        value = music_title[i].text.replace('\n','')
        if value.find(message1) >=0 and len(value) < 50 :
            break
        if lyric_begin == True:
            para = value
            music_lyric_node += " " + para
        if value.find(message2) >= 0 and len(value) < 50 :
            lyric_begin = True
    print (music_lyric_node)

    # music_lyric_node = basic_lyric.findAll('div', class_='para').text
    data_json = {
        'title_node': title_node.text,
        'introduction_node': introduction_node,
        'basic_node': basic_node,
        'music_lyric_node': music_lyric_node
    }
    return data_json

def _save_new_data(self, soup):
    #error items
    title_node =''
    try:
        title_node=soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').text
    except:
        return not res_data
    #second title
    title_sub__text=''
    try:
        title_sub__text = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h2').get_text()
    except:
        title_sub__text=''
    filename = title_node.get_text() + title_sub__text
    path='../webpages/'#custom diectory for webpages
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + filename.replace('/',''), 'wb') as f:
        f.write(html_cont) #.decode('utf-8')
        print('Save to disk filename:'+f.name+"")
    return res_data



