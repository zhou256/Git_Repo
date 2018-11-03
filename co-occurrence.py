# -*- coding: utf-8 -*-
#Python里面的转码问题:使用强大的pandas来读取gbk,然后转码保存成utf-8.
#matlab中cell2str(str2int(jinpeng))的嵌套使用.

#import os 
#import pandas as pd #需要把文件改成编码的格式（可以自己随时修改）
#将《人名的名义》dict中非utf-8编码变成是utf-8
#file_dir = 'C:/Users/Administrator/Desktop/people_name/dict.txt' 
#df1 = pd.read_csv(file_dir, encoding='gbk') 
#df1.to_csv('C:/Users/Administrator/Desktop/people_name/dict1.txt', encoding='utf-8',index=None) 

#如果你用二进制写入再用文件读出的话，如果其中存在'0x1A'，就只会读出文件的一部分，
#使用'rb'会一直读取文件末尾。




import os, sys
import jieba, codecs, math
import jieba.posseg as pseg


names = {}			# 姓名字典
relationships = {}	# 关系字典
lineNames = []		# 每段内人物关系

# count names
jieba.load_userdict("C:/Users/Administrator/Desktop/people_name/dict.txt")		# 加载字典
with codecs.open("C:/Users/Administrator/Desktop/people_name/人民的名义1.txt", "rb", "utf-8") as f:
	for line in f.readlines():
		poss = pseg.cut(line)		# 分词并返回该词词性
		lineNames.append([])		# 为新读入的一段添加人物名称列表
		for w in poss:
			if w.flag != "nr" or len(w.word) < 2:
				continue			# 当分词长度小于2或该词词性不为nr时认为该词不为人名
			lineNames[-1].append(w.word)		# 为当前段的环境增加一个人物
			if names.get(w.word) is None:
				names[w.word] = 0
				relationships[w.word] = {}
			names[w.word] += 1					# 该人物出现次数加 1

# explore relationships
for line in lineNames:					# 对于每一段
	for name1 in line:					
		for name2 in line:				# 每段中的任意两个人
			if name1 == name2:
				continue
			if relationships[name1].get(name2) is None:		# 若两人尚未同时出现则新建项
				relationships[name1][name2]= 1
			else:
				relationships[name1][name2] = relationships[name1][name2]+ 1		# 两人共同出现次数加 1

# output
#with codecs.open("C:/Users/Administrator/Desktop/实验楼/基于共现提取《釜山行》人物关系/output/busan_node.txt", "w", "gbk") as f:
#	f.write("Id Label Weight\r\n")
#	for name, times in names.items():
#		f.write(name + " " + name + " " + str(times) + "\r\n")
list_node=[]
import pandas as pd
for name, times in names.items():
    #print('name1: ',name,'name2: ',name,'频数: ',times)
    list_node.append([name,name,times])
df1=pd.DataFrame(list_node,columns=['Id','Label','weight'])
df1.to_csv('C:/Users/Administrator/Desktop/people_name/output/node.csv',index=False)
#
#with codecs.open("C:/Users/Administrator/Desktop/实验楼/基于共现提取《釜山行》人物关系/output/busan_edge.txt", "w", "gbk") as f:
#	f.write("Source Target Weight\r\n")
#	for name, edges in relationships.items():
#		for v, w in edges.items():
#			if w > 3:
#				f.write(name + " " + v + " " + str(w) + "\r\n")
list_edge=[]
for name, edges in relationships.items():
    for v, w in edges.items():
        if w > 3:
            list_edge.append([name, v ,str(w)])
df2=pd.DataFrame(list_edge,columns=['Source','Target','weight'])
df2.to_csv('C:/Users/Administrator/Desktop/people_name/output/edge.csv',index=False)



