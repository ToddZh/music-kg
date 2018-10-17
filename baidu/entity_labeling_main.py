import json
import codecs
import rdflib
from baidu import html_downloader
from convert import converter

if __name__ == '__main__':
    html = html_downloader.HtmlDownloader()
    # label = {"data": "张杰"}
    # data = html.entity_labeling(label)
    # data_json = json.loads(data)
    # entity_annotation = data_json['entity_annotation']
    # print(len(entity_annotation))
    # print(entity_annotation)

    with codecs.open('../test/data/entity.txt', 'r','utf-8') as f:
        line = f.readline()
        trans = converter.converte()
        graph = rdflib.Graph()
        while line:
            print(line)
            label = {"data": line}
            data = html.entity_labeling(label)
            data_json = json.loads(data)
            entity_annotation = data_json['entity_annotation']
            size = len(entity_annotation)
            if size == 0:
                continue
            if line != entity_annotation[0]['mention']:
                continue

            bdbkKgId = entity_annotation[0]['_bdbkKgId']
            name = entity_annotation[0]['mention']
            tag = entity_annotation[0]['concept']['level1']
            Introduction = entity_annotation[0]['desc']

            line = f.readline()
        file = "../test/data/baiduEntityAPI.rdf"
        graph.serialize(file, format='nt')