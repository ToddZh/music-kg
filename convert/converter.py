# -*- encoding: utf-8 -*-
import sys
import codecs
import os
import json
import re
import rdflib
import pprint

class converte(object):
	def __init__(self):
		pass

	def outputPredicateObjects(self,file, graph_format,subjects):
		graph = self.parseGraph(file,graph_format)
		# self.show(graph)
		s = rdflib.URIRef('http://www.unisound.com/knowledge_graph/musicsong_tag/429904')
		predicate_objects = graph.predicate_objects(s)
		# subject_predicates = graph.subject_predicates(401597)
		# objects = graph.objects(subjects,"401597")
		for stmt in predicate_objects:
			pprint.pprint(stmt)
			p = stmt[0]
			o = stmt[1]
			print(str(p))


	def saveGraph(self, graph, subjects, predicates, objects):
		s = rdflib.URIRef('musicsong/' + subjects)
		p = rdflib.URIRef(predicates)
		o = rdflib.URIRef(objects)
		graph.add((s, p, o))


	def saveGraphXML(self, file, subjects, predicates, objects):
		graph_ = rdflib.Graph()
		for i, j in zip(predicates, objects):
			s = rdflib.URIRef('musicsong/' + subjects)
			p = rdflib.URIRef("http://www.zhutong.com/knowledge_graph/vocab/" + i)
			o = rdflib.URIRef(j)
			graph_.add((s, p, o))
		# 默认以'xml'格式存储
		graph_.serialize(file, format='xml')

	def saveGraphN3(self, file, subjects, predicates, objects):
		if os.path.exists(file):
			graph_ = rdflib.Graph()
			graph_.parse(file, format='n3')

			s = rdflib.URIRef(subjects)
			p = rdflib.URIRef(predicates)
			o = rdflib.URIRef(objects)
			graph_.add((s, p, o))
			# 以n3格式存储
			graph_.serialize(file, format='n3')
		else:
			# print('文件不存在')
			with codecs.open(file, 'w', 'utf-8') as f:
				graph_ = rdflib.Graph()
				graph_.parse(file, format='n3')

				s = rdflib.URIRef(subjects)
				p = rdflib.URIRef(predicates)
				o = rdflib.URIRef(objects)
				graph_.add((s, p, o))
				# 以n3格式存储
				graph_.serialize(file, format='n3')




	def saveGraphNT(self, file, subjects, predicates, objects):
		graph_ = rdflib.Graph()
		for i, j in zip(predicates, objects):
			s = rdflib.URIRef('musicsong/' + subjects)
			p = rdflib.URIRef("http://www.zhutong.com/knowledge_graph/vocab/" + i)
			o = rdflib.URIRef(j)
			graph_.add((s, p, o))
		graph_.serialize(file, format='nt')

	def parseGraph(self, file, graph_format):
		graph_ = rdflib.Graph()
		'''
		format: 'rdf/xml' 'xml', 'n3', 'nt', 'trix', 'rdfa'
		'''
		graph_.parse(file, format=graph_format)
		# self.show(graph_)
		return graph_

	def xml2nt(self, file, graph_format, file_save, graph_save_format):
		graph_ = rdflib.Graph()
		graph_.parse(file, format=graph_format)
		graph_.serialize(file_save, format=graph_save_format)
		pass

	def xml2json(self):
		pass

	def musicjson2nt(self, json):
		graph_ = rdflib.Graph()
		pass

	def show(self,graph):
		# 打印图的大小
		print(len(graph))  # prints 2
		# 遍历所有三元组
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
	converter.show(converter.parseGraph('../test/data/zhutong.rdf','n3'))
	# converter.xml2nt("../test/data/musicknowledgegraph.rdf", "xml", "../test/data/musicknowledgegraph.nt", "nt")
	# converter.outputPredicateObjects("../test/data/musicknowledgegraph.rdf", "xml", "musicalbum/39375")


	# graph = rdflib.Graph()
    #
	# s = rdflib.URIRef('牛膝')
	# p = rdflib.URIRef('功效属性')
	# o = rdflib.URIRef('活血')
    #
	# graph.add((s, p, o))
	# # 以n3格式存储
	# graph.serialize('../test/data/zhutong.rdf', format='n3')

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
