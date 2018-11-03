# -*- coding: utf-8 -*-
#Python�����ת������:ʹ��ǿ���pandas����ȡgbk,Ȼ��ת�뱣���utf-8.
#matlab��cell2str(str2int(jinpeng))��Ƕ��ʹ��.

#import os 
#import pandas as pd #��Ҫ���ļ��ĳɱ���ĸ�ʽ�������Լ���ʱ�޸ģ�
#�������������塷dict�з�utf-8��������utf-8
#file_dir = 'C:/Users/Administrator/Desktop/people_name/dict.txt' 
#df1 = pd.read_csv(file_dir, encoding='gbk') 
#df1.to_csv('C:/Users/Administrator/Desktop/people_name/dict1.txt', encoding='utf-8',index=None) 

#������ö�����д�������ļ������Ļ���������д���'0x1A'����ֻ������ļ���һ���֣�
#ʹ��'rb'��һֱ��ȡ�ļ�ĩβ��




import os, sys
import jieba, codecs, math
import jieba.posseg as pseg


names = {}			# �����ֵ�
relationships = {}	# ��ϵ�ֵ�
lineNames = []		# ÿ���������ϵ

# count names
jieba.load_userdict("C:/Users/Administrator/Desktop/people_name/dict.txt")		# �����ֵ�
with codecs.open("C:/Users/Administrator/Desktop/people_name/���������1.txt", "rb", "utf-8") as f:
	for line in f.readlines():
		poss = pseg.cut(line)		# �ִʲ����ظôʴ���
		lineNames.append([])		# Ϊ�¶����һ��������������б�
		for w in poss:
			if w.flag != "nr" or len(w.word) < 2:
				continue			# ���ִʳ���С��2��ôʴ��Բ�Ϊnrʱ��Ϊ�ôʲ�Ϊ����
			lineNames[-1].append(w.word)		# Ϊ��ǰ�εĻ�������һ������
			if names.get(w.word) is None:
				names[w.word] = 0
				relationships[w.word] = {}
			names[w.word] += 1					# ��������ִ����� 1

# explore relationships
for line in lineNames:					# ����ÿһ��
	for name1 in line:					
		for name2 in line:				# ÿ���е�����������
			if name1 == name2:
				continue
			if relationships[name1].get(name2) is None:		# ��������δͬʱ�������½���
				relationships[name1][name2]= 1
			else:
				relationships[name1][name2] = relationships[name1][name2]+ 1		# ���˹�ͬ���ִ����� 1

# output
#with codecs.open("C:/Users/Administrator/Desktop/ʵ��¥/���ڹ�����ȡ����ɽ�С������ϵ/output/busan_node.txt", "w", "gbk") as f:
#	f.write("Id Label Weight\r\n")
#	for name, times in names.items():
#		f.write(name + " " + name + " " + str(times) + "\r\n")
list_node=[]
import pandas as pd
for name, times in names.items():
    #print('name1: ',name,'name2: ',name,'Ƶ��: ',times)
    list_node.append([name,name,times])
df1=pd.DataFrame(list_node,columns=['Id','Label','weight'])
df1.to_csv('C:/Users/Administrator/Desktop/people_name/output/node.csv',index=False)
#
#with codecs.open("C:/Users/Administrator/Desktop/ʵ��¥/���ڹ�����ȡ����ɽ�С������ϵ/output/busan_edge.txt", "w", "gbk") as f:
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



