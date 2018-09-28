# coding:utf8
import rdflib

# graph = rdflib.Graph('Sleepycat')

# first time create the store:
# graph.open('myRDFLibStore.rdf', create = True)

graph = rdflib.Graph()

s = rdflib.URIRef('牛膝')
p = rdflib.URIRef('功效属性')
o = rdflib.URIRef('活血')

graph.add((s, p, o))
# 以n3格式存储
graph.serialize('zhongyao.rdf', format='n3')

s = rdflib.URIRef('http://www.example.org/牛膝')
p = rdflib.URIRef('http://www.example.org/功效属性')
o = rdflib.URIRef('http://www.example.org/活血')

g1 = rdflib.Graph()
g1.add((s, p, o))
g1.serialize('zhongyao1.rdf')  # 默认以'xml'格式存储

g2 = rdflib.Graph()
g2.parse('zhongyao1.rdf', format='xml')  # 解析rdf文件时，需要指定格式
subject = g2.subjects(p, o)
for i in subject:
	print(i)
