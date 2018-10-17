#coding:utf-8
import json
import os
import codecs

def read_json():
    with codecs.open('../test/data/savejson.json', 'r','utf-8') as f:
        message = '[' + f.read() + ']'
        # message = f.read()
        # print(message)
        data = json.loads(message)
        # print(data)
        print(data[0])
        # json.dump(data, f)
        return data

def save_json(data):
    json_str = json.dumps(data, ensure_ascii=False)
    with codecs.open('../test/data/savejson.json', 'w') as f:
        f.write('[' + json_str + ']')

def add_json(data):
    json_str = json.dumps(data, ensure_ascii=False)
    file = '../test/data/savejson.json'
    print(json_str)
    if os.path.exists(file):
        if os.path.getsize(file):
            # print('文件存在且不为空')
            with codecs.open(file, 'a' , 'utf-8') as f:
                s = "," + "\n" + json_str
                f.write(s)
        else:
            # print('文件存在且为空')
            with codecs.open(file, 'a', 'utf-8') as f:
                f.write(json_str)
    else:
        # print('文件不存在')
        with codecs.open(file, 'w', 'utf-8') as f:
            f.write(json_str)


def save_entity(data):
    file = '../test/data/entity.txt'
    if os.path.exists(file):
        if os.path.getsize(file):
            # print('文件存在且不为空')
            with codecs.open(file, 'a', 'utf-8') as f:
                f.write('\n')
                f.write(data)
        else:
            # print('文件存在且为空')
            with codecs.open(file, 'a', 'utf-8') as f:
                f.write(data)
    else:
        # print('文件不存在')
        with codecs.open(file, 'w', 'utf-8') as f:
            f.write(data)

def save_entity_album(data):
    file = '../test/data/entity_album.txt'
    if os.path.exists(file):
        if os.path.getsize(file):
            # print('文件存在且不为空')
            with codecs.open(file, 'a', 'utf-8') as f:
                f.write('\n')
                f.write(data)
        else:
            # print('文件存在且为空')
            with codecs.open(file, 'a', 'utf-8') as f:
                f.write(data)
    else:
        # print('文件不存在')
        with codecs.open(file, 'w', 'utf-8') as f:
            f.write(data)

def save_entity_music(data):
    file = '../test/data/entity_music.txt'
    if os.path.exists(file):
        if os.path.getsize(file):
            # print('文件存在且不为空')
            with codecs.open(file, 'a', 'utf-8') as f:
                f.write('\n')
                f.write(data)
        else:
            # print('文件存在且为空')
            with codecs.open(file, 'a', 'utf-8') as f:
                f.write(data)
    else:
        # print('文件不存在')
        with codecs.open(file, 'w', 'utf-8') as f:
            f.write(data)

if __name__ == '__main__':
    data = {
        'name': '朱彤',
        'shares': 100,
        'price': 542.23
    }
    read_json()
