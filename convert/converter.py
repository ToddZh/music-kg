# -*- encoding: utf-8 -*-
import sys
import json
import re
import rdflib

class converte(object):
	def __init__(self):
		pass

	def saveGraphXML(self, graph, subjects, predicates, objects):
		graph_ = rdflib.Graph()
		for i, j in zip(predicates, objects):
			s = rdflib.URIRef('musicsong/' + subjects)
			p = rdflib.URIRef("http://www.zhutong.com/knowledge_graph/vocab/" + i)
			o = rdflib.URIRef(j)
			graph_.add((s, p, o))
		# 以n3格式存储
		# 默认以'xml'格式存储
		graph_.serialize(graph, format='xml')

	def saveGraphNT(self, graph, subjects, predicates, objects):
		graph_ = rdflib.Graph()
		for i, j in zip(predicates, objects):
			s = rdflib.URIRef('musicsong/' + subjects)
			p = rdflib.URIRef("http://www.zhutong.com/knowledge_graph/vocab/" + i)
			o = rdflib.URIRef(j)
			graph_.add((s, p, o))
		# 以n3格式存储
		# 默认以'xml'格式存储
		graph_.serialize(graph, format='nt')

	def parseGraph(self, graph, graph_format):
		graph_ = rdflib.Graph()
		'''
		format: 'rdf/xml' 'xml', 'n3', 'nt', 'trix', 'rdfa'
		'''
		graph_.parse(graph, format=graph_format)
		self.show(graph_)

	# 读取大文件有问题
	def xml2nt(self, graph, graph_format, graph_save, graph_save_format):
		graph_ = rdflib.Graph()
		graph_.parse(graph, format=graph_format)
		graph_.serialize(graph_save, format=graph_save_format)
		pass

	def xml3json(self):
		pass

	def show(self, graph):
		# 打印图的大小
		print(len(graph))  # prints 2
		# 遍历所有三元组
		import pprint
		for stmt in graph:
			pprint.pprint(stmt)

	def removeBlank(self, list):
		res = []
		for i in list:
			r = ''
			if i.find(' ') > 0:
				r = i.replace(' ', '/')
				res.append(r)
			else:
				res.append(i)
		return res

if __name__ == "__main__":
	# instantiate class
	converter = converte()
	converter.xml2nt("../test/data/musicknowledgegraph.rdf", "xml", "../test/data/musicknowledgegraph.nt", "nt")

	# predicates = ['song_lyric', 'song_id', 'song_recommends', 'song_sub_title', 'song_comments'
	# 	, 'song_original_name', 'label', 'song_name']
	# objects = ['第一千个昼夜游鸿明 miracle_1989 云停了下来 在半空里保持着静止状态 我眨一眨眼 往日情怀 飞了过来 时光很奇怪 让和我有了爱然后分开 嘿 九霄云外 谁在叫我 翻阅回忆的字典 也解释不清爱 第一千个昼夜 忽然我醒来 我不会忘记那天 那一夜 陪我流下的泪 黎明前 吻着 抱着风 把孤单推过来 最后那一眼 烙在我的脑海 一千个夜也不能 把最爱偷回来 我想要回到那天 那一夜 但时间不肯后退 往前走 多少天 多少年 我把心停下来 带走那一夜 将永远留给我 在多年以后 爱石沉大海 时光很奇怪 让和我有了爱然后分开 嘿 九霄云外 谁在叫我 翻阅回忆的字典 也解释不清爱 第一千个昼夜 忽然我醒来 我不会忘记那天 那一夜 陪我流下的泪 黎明前 吻着 抱着风 把孤单推过来 最后那一眼 烙在我的脑海 一千个夜也不能 把最爱偷回来 我不会忘记那天 那一夜 陪我流下的泪 黎明前 吻着 抱着风 把孤单推过来 最后那一眼 烙在我的脑海 一千个夜也不能 把最爱偷回来 我想要回到那天 那一夜 但时间不肯后退 往前走 多少天 多少年 我把心停下来 带走那一夜 将永远留给我 在多年以后 爱石沉大海 在多年以后 爱石沉大海 我会记得你说得话 我只想要有你的未来 给舟'
	# 	, '401597', '1', '', '0', '第一千个昼夜', 'song #401597', '第一千个昼夜']
	# converter.saveGraphXML('../test/data/zhutong.rdf', "401597", predicates, converter.removeBlank(objects))

	# predicates = ['song_lyric', 'song_id', 'song_recommends', 'song_sub_title', 'song_comments'
	# 	, 'song_original_name', 'label', 'song_name', 'song_word_writer', 'song_composer']
	# objects = ['谁的年轻 不曾是骄傲 可又多少无畏骄傲 在风雨中衰老 谁的天空 不曾有痴狂 可又多少年少痴狂 在岁月中苍凉 在妥协中奔忙 在诱惑前迷茫 你温软的微笑 给我昂起头颅的力量 向梦想出发 绽放青春的花 即使不会到达 谁又会在乎 为梦想坚持 就是最真勇士 即使不会到达 谁又会在乎 走我们的路 时光坚硬 梦想如此柔软 现实太泥泞 不断跌倒 不断跌倒 还继续吗 在妥协中奔忙 在诱惑前迷茫 你温暖的微笑 给我昂起头颅的力量 向梦想出发 绽青春的花 心中不灭希望 是指引方向的光 为梦想坚持 就是最真勇士 即使不会到达 谁又会在乎 走我们的路 梦想的路 向梦想出发 绽青春的花 心中不灭希望 是指引方向的光 为梦想坚持 就是最真勇士 即使不会到达 谁又会在乎 走我们的路 梦想的路 走我们的路 梦想的路 走我们的路'
	# 	, '533832', '78', '电影《与时尚同居》主题曲', '20', '我们的路', 'song #533832', '我们的路'
	# 		   , '徐闻 尹丽川', '菊地圭介']
	## 保存 rdf
	# converter.saveGraphXML('../test/data/zhutong.rdf', "533832", predicates, converter.removeBlank(objects))
	# converter.saveGraphNT('../test/data/zhutong.nt', "533832", predicates, converter.removeBlank(objects))

	print("pass")
