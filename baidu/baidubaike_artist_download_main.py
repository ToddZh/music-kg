import codecs
import rdflib
from baidu import html_downloader
from convert import converter
from kg import insert_to_neo4j


if __name__ == '__main__':
    # data = html_downloader.baidubaike_download('预谋邂逅','album')
    # neo4j = insert_to_neo4j.GraphNeo4j()
    # neo4j.add_artist_node(data)

    neo4j = insert_to_neo4j.GraphNeo4j()

    # 爬取歌手信息
    with codecs.open('../test/data/entity_artist.txt', 'r','utf-8') as f:
        line = f.readline().strip()
        while line:
            if len(line) == 0:
                continue
            print(line)
            try:
                list = line.split("$$")
                id = list[0]
                target = list[1]
                data = html_downloader.baidubaike_download(target, 'artist')
                if data == True:
                    pass
                else:
                    for i in data:
                        neo4j.add_artist_node(data, id)
            except Exception as e:
                print(e)
            line = f.readline().strip()
        # file = "../test/data/baiduEntityAPI.rdf"
        # graph.serialize(file, format='nt')

    # 爬取专辑信息
    with codecs.open('../test/data/entity_album.txt', 'r','utf-8') as f:
        line = f.readline().strip()
        while line:
            if len(line) == 0:
                continue
            print(line)
            try:
                list = line.split("$$")
                id = list[0]
                target = list[2]
                data = html_downloader.baidubaike_download(target, 'album')
                if data == True:
                    pass
                else:
                    for i in data:
                        neo4j.add_album_node(data, id)

                line = f.readline().strip()
            except:
                print("add album error!")
    # 爬取歌曲信息
    with codecs.open('../test/data/entity_music.txt', 'r', 'utf-8') as f:
        line = f.readline().strip()
        while line:
            if len(line) == 0:
                continue
            print(line)
            try:
                list = line.split("$$")
                id = list[0]
                target = list[2]
                data = html_downloader.baidubaike_download(target, 'music')
                if data == True:
                    pass
                else:
                    for i in data:
                        neo4j.add_music_node(data, id)

                line = f.readline().strip()
            except:
                print("add music error!")