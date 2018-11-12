# -*- coding: utf-8 -*-
"""
     具体效果可以参看个人博客的效果展示:
	 https://blog.csdn.net/jp_zhou256/article/details/83959856
"""
"""2018年华为杯数模战况统计"""
import pandas as pd
import xlwt
import numpy as np
file_path=r'C:/Users/Administrator/Desktop/AAA/'
data_A=pd.read_excel(file_path+'2018年最终获奖名单_A题.xls',encode='gbk')
len(data_A)
data_A.columns.tolist()
data_B=pd.read_excel(file_path+'2018年最终获奖名单_B题.xls',encode='gbk')
len(data_B)
data_C=pd.read_excel(file_path+'2018年最终获奖名单_C题.xls',encode='gbk')
len(data_C)
data_D=pd.read_excel(file_path+'2018年最终获奖名单_D题.xls',encode='gbk')
len(data_D)
data_E=pd.read_excel(file_path+'2018年最终获奖名单_E题.xls',encode='gbk')
len(data_E)
data_F=pd.read_excel(file_path+'2018年最终获奖名单_F题.xls',encode='gbk')
len(data_F)
data_all=pd.concat([data_A,data_B,data_C,data_D,data_E,data_F],axis=0) #沿着列方向拼接
print(data_all.head(10))
sum([len(data_A),len(data_B),len(data_C),len(data_D),len(data_E),len(data_F)])
columnnum=len(data_A.columns.tolist())
len(data_all)
#data_all.to_excel(file_path+'2018建模成绩汇总.xls',encoding='gbk')
data_SMU=data_all[((data_all['队长所在单位']=='东南大学')|
                                    (data_all['第一队友所在单位']=='东南大学')|
                                    (data_all['第二队友所在单位']=='东南大学'))]
data_SMU.to_excel(file_path+'东南大学2018研究生建模成绩汇总.xls',encoding='gbk')

#上海海事大学获奖与未获奖人数占比
#1.获奖队伍
prized=data_SMU[~(data_SMU['奖项']=='成功参与奖')]
#2.未获奖队伍
unprized=data_SMU[data_SMU['奖项']=='成功参与奖']
prized['奖项'].value_counts()  #分别计算各个奖项获奖人数,默认是降序
"""
三等奖    63
二等奖    30
一等奖     3
"""
prizedCount=prized['奖项'].value_counts(ascending=True)
"""
一等奖     3
二等奖    30
三等奖    63
"""
unprizedCount=unprized['奖项'].value_counts() #计算成功参与奖的获奖人数
#成功参与奖    139
#2018华为杯全国研究生数学建模,上海海事大学获奖率
prizedsum=np.sum(prizedCount[:])
prizeate=np.sum(prizedCount)/(np.sum(unprizedCount)+prizedsum) # 0.4393063583815029
prizeate # 0.4393063583815029
#海事大学总人数占2018年参赛人数比重
rate=sum(sum(prizedCount)+unprizedCount)/data_all.shape[0] #参赛总人数=12207
rate #0.019251249283198164

#统计各个高校的获奖频数
#prize_freq=data_all.groupby(['题号','奖项']).agg('sum')
#2018年选手选题情况一览表,获奖情况分区数
"""1.发现数据中: 一等奖（华为）和 一等奖同名,考虑去重,使用正则表达式或者字符串替换"""
#str1='zhoujianpeng'
#str1.replace('jian', '周')
#顽固的字符串直接替换就好了.
data_all['奖项']=data_all['奖项'].apply(lambda x:x.replace('一等奖（华为）','一等奖'))
#上述方法还是没有完全的去重成功(两个一等奖依然是同名没有合并)
"""
import re
s = 'obj_Temp:28.41 ref_Temp:39.24'
a = re.search(r'obj_Temp:([\d.]+)', s) #取到指定字符串中的数字
a.group(1)
"""
chooses,category=[data_all['题号'].value_counts(ascending=True),data_all['奖项'].value_counts(ascending=True)]
chooses
category
totalNum=data_all.shape[0]
prize1_rate,prize2_rate,prize3_rate,unprize_rate=category/totalNum
print('\n一等奖: ',prize1_rate,'\n二等奖: ',prize2_rate,'\n三等奖: ',prize3_rate,'\n成功参与奖: ',unprize_rate)
#获奖人数&未获奖人数占比
lucky_count=sum(category[:3]) #获奖人数:4358
success_join_count=totalNum-lucky_count #未获奖人数:7849
print('2018年华为杯数学建模获奖率: ',prize1_rate+(prize2_rate+prize3_rate))



#高校名称列表
import pandas as pd
university_list=list(pd.concat([data_all['队长所在单位'],data_all['第一队友所在单位'],data_all['第二队友所在单位']]).unique())
university_list #2018年本期参与数学建模竞赛的大学名单
data_SMU=data_all[((data_all['队长所在单位']=='上海海事大学')|
                                    (data_all['第一队友所在单位']=='上海海事大学')|
                                    (data_all['第二队友所在单位']=='上海海事大学'))]


#university=[] #将各个大学分群
university={} #将各个大学分群
totalNum=data_all.shape[0] #参赛队伍总支数
for i in range(len(university_list)):
    #grade.append(university_list[i]+str(i))
    del data_SMU
    data_SMU=data_all[((data_all['队长所在单位']==university_list[i])|(data_all['第一队友所在单位']==university_list[i])|(data_all['第二队友所在单位']==university_list[i]))].reset_index(drop=True)
    del data_SMU['序号']
    university[university_list[i]]=data_SMU
#分别统一每一个大学的各个赛题数目


"""
xuexiao1={'学校名称':同济大学,
          '参赛人数':1000,
          '获奖总人数':480,
          '未获奖人数':1000-480,
          '学校各题获奖比率':[1,2,3,4,5,6],
          '学校获奖比':480/1000
          '获奖情况':{
          'A':{'一等奖':10,'二等奖':20,'三等奖':50,'成功参与奖':200,'选做队伍支数':280,'获奖频数':80,'未获奖频数':200,'获奖比率':18.5%}
          'B':{'一等奖':10,'二等奖':20,'三等奖':50,'成功参与奖':200,'选做队伍支数':280,'获奖频数':80,'未获奖频数':200,'获奖比率':18.5%}
          'C':{'一等奖':10,'二等奖':20,'三等奖':50,'成功参与奖':200,'选做队伍支数':280,'获奖频数':80,'未获奖频数':200,'获奖比率':18.5%}
          'D':{'一等奖':10,'二等奖':20,'三等奖':50,'成功参与奖':200,'选做队伍支数':280,'获奖频数':80,'未获奖频数':200,'获奖比率':18.5%}
          'E':{'一等奖':10,'二等奖':20,'三等奖':50,'成功参与奖':200,'选做队伍支数':280,'获奖频数':80,'未获奖频数':200,'获奖比率':18.5%}
          'F':{'一等奖':10,'二等奖':20,'三等奖':50,'成功参与奖':200,'选做队伍支数':280,'获奖频数':80,'未获奖频数':200,'获奖比率':18.5%}
            }
          }
"""

    
#totalUniv=[]
totalUniv={}
saiti_list=['A','B','C','D','E','F']
for i in range(len(university)):
#for i in range(5):
    #print(university[university_list[0]]) #university为字典,学校名称为key
    xiexiao={}
     #xiexiao1=university[university_list[3]]
    xiexiao1=university[university_list[i]]
    #xiexiao1=university[university_list[77]] #3--同济大学，77--海事大学
    #学校名称(三列中的众数)
    zhongshu=pd.concat([xiexiao1['队长所在单位'],xiexiao1['第一队友所在单位'],xiexiao1['第二队友所在单位']]) #Series
    xiexiao['学校名称']= zhongshu.value_counts().index[0] #value_counts默认是降序,选择众数对应的索引值即为学校.
    #chooses=xiexiao1['题号'].value_counts(ascending=True) #对应赛题选做队伍支数
    ##A=xiexiao1[xiexiao1['题号']].value_counts()
    #prizeoption=xiexiao1['奖项'].unique()
    #1.分析获奖总人数
    xiexiao['参赛队伍']=len(xiexiao1)
    #totalUniv[university_list[3]]=xiexiao
    #totalUniv[university_list[i]]=xiexiao
    #2.分析该学校的各个赛题完成情况
    #2.1.选做A题的情况
    #xiexiao1[xiexiao1['题号']=='A']['奖项'].value_counts(ascending=True) #返回A赛题对应的获奖情况
    #2.2.六道赛题各自获奖情况一览表
    """
    zhou=[1,2,4,5],zhou[-1],zhou[:-1]
    """
    timu={}#存放六道赛题各自对应的获奖情况
    sum_prize1=0
    award_prize=0
    for ii in range(len(saiti_list)):
        #print(saiti_list[ii])
        #things=things.index
        #必须对things进行初始化,不然有的学校没有一等奖things[0]就错位了,就出错了.
        things=xiexiao1[xiexiao1['题号']==saiti_list[ii]]['奖项'].value_counts(ascending=True)
        #发现同济大学有B,但是B题目没有一等奖
        #things=xiexiao1[xiexiao1['题号']==saiti_list[ii]]['奖项'].value_counts(ascending=True)
        ##赋初值,因为每个奖不一定都有.
        one_rate1=0
        two_rate1=0
        three_rate1=0
        non_rate1=0
        prized_rate1=0
        try:
            #一等奖队伍数
            try:
                if ~things[things.index=='一等奖'].empty:
                    #print('1')
                    one_prize1=things[things.index=='一等奖'] #type(one_prize1)=Series
                    if len(one_prize1)==0:
                        one_prize1=0
                    elif len(one_prize1)==1:
                        #one_prize1=one_prize1.values[0,0] #将Series转换为二维数组
                        one_prize1=list(one_prize1)[0] #将Series转换为list在取值也可以
                else:
                    one_prize1=0
            except  :
                pass
            finally:
                print('one_prize1出错啦！！！！！！！！！！！')    
            #二等奖人数
            try:
                if ~things[things.index=='二等奖'].empty:
                    two_prize1=things[things.index=='二等奖']
                    if len(two_prize1)==0:
                        two_prize1=0
                    elif len(two_prize1)==1:
                        #one_prize1=one_prize1.values[0,0] #将Series转换为二维数组
                        two_prize1=list(two_prize1)[0] #将Series转换为list在取值也可以
                else:
                    two_prize1=0
            except  :
                pass
            finally:
                print('two_prize1出错啦！！！！！！！！！！！')  
            #三等奖队伍数
            try:
                if ~things[things.index=='三等奖'].empty:
                    three_prize1=things[things.index=='三等奖']
                    if len(three_prize1)==0:
                        three_prize1=0
                    elif len(three_prize1)==1:
                        #one_prize1=one_prize1.values[0,0] #将Series转换为二维数组
                        three_prize1=list(three_prize1)[0] #将Series转换为list在取值也可以
                else:
                    three_prize1=0
            except  :
                pass
            finally:
                print('three_prize1出错啦！！！！！！！！！！！')
            #成功参与奖队伍数===未获奖人数
            try:
                if ~things[things.index=='成功参与奖'].empty:
                    non_prize1=things[things.index=='成功参与奖']
                    if len(non_prize1)==0:
                        non_prize1=0
                    elif len(non_prize1)==1:
                        #one_prize1=one_prize1.values[0,0] #将Series转换为二维数组
                        non_prize1=list(non_prize1)[0] #将Series转换为list在取值也可以
                else:
                    non_prize1=0
            except  :
                pass
            finally:
                print('non_prize1出错啦！！！！！！！！！！！')
            #获奖队伍总数
            award_prize=sum(things[:-1])
            #某道赛题的参赛总队伍数
            sum_prize1=sum(things)
            #一等奖队伍与该赛题参赛队伍总数的占比
            one_rate1=one_prize1/sum_prize1
            #二等奖队伍与该赛题参赛队伍总数的占比
            two_rate1=two_prize1/sum_prize1
            #三等奖队伍与该赛题参赛队伍总数的占比
            three_rate1=three_prize1/sum_prize1
            #未获奖队伍与该赛题参赛队伍总数的占比
            non_rate1=non_prize1/sum_prize1
            #获奖队伍与该赛题参赛队伍总数的占比
            prized_rate1=award_prize/sum_prize1
            timu[saiti_list[ii]]={
                    '一等奖队伍数':one_prize1,
                    '一等奖获奖比率':one_rate1,
                    '二等奖队伍数':two_prize1,
                    '二等奖获奖比率':two_rate1,
                    '三等奖队伍数':three_prize1,
                    '三等奖获奖比率':three_rate1,
                    '成功参与奖队伍数':non_prize1,'未获奖比率':non_rate1,
                    '获奖队伍数':award_prize,'获奖比率':prized_rate1}
            #del things
        except  :
            pass
        #finally:
        #     print('出错啦！！！！！！！！！！！')
    #3.获奖总人数
    try:
        total_queue=0
        for i1 in range(len(timu)):
            try:
                total_queue+=timu[saiti_list[i1]]['获奖队伍数']
            except:
                continue
        xiexiao['获奖总队伍数']=total_queue
    except:
            pass
    #4.未获奖总人数
    try:
        un_num=0
        for i1 in range(len(timu)):
            try:
                un_num+=timu[saiti_list[i1]]['成功参与奖队伍数']
            except:
                continue
        xiexiao['未获奖总队伍数']=un_num
    except:
            pass
    #5.某赛题获奖情况本质上为一个list=[]对象
    try:
        rate_list={}
        for i1 in range(len(timu)):
            rate_list[saiti_list[i1]]=timu[saiti_list[i1]]['获奖比率']
        xiexiao['学校各题获奖比率']=rate_list
    except:
            pass
    #5.学校各道赛题完成获奖情况
    try:
        xiexiao['学校各题获奖明细']=timu
    except:
            pass
    #5.学校获奖比
    try:
        xx_rate=total_queue/len(xiexiao1) #学校的参与竞赛总人数
        xiexiao['学校获奖比']=xx_rate
    except:
            pass
    #totalUniv.append(xiexiao)
    totalUniv[university_list[i]]=xiexiao
    del xiexiao1
#保存字典数据:使用DataFrame
import pandas as pd
data=pd.DataFrame(totalUniv,columns=totalUniv.keys()).T
columns_name=data.columns.tolist()
#各列数值不变的条件下来重命名各列
#data.columns=[['参赛队伍', '学校各题获奖明细', '学校各题获奖比率', '学校名称', '学校获奖比', '未获奖总队伍数', '获奖总队伍数']]
#各列随着名称先后顺序发生位置变化
data=pd.DataFrame(totalUniv,columns=totalUniv.keys()).T
#重新指定列的顺序
data=data[['学校名称','参赛队伍', '获奖总队伍数', '未获奖总队伍数','学校各题获奖明细', '学校各题获奖比率',  '学校获奖比']]
#data[data['学校名称']=='上海海事大学']
data.to_csv('E:/jianpengzhou.csv',index=False)
#按照参赛人数对字典进行排序
join_party={}
for i in range(len(university_list)):
#for i in range(5):
    #print(university[university_list[0]]) #university为字典,学校名称为key
    try:
        xiexiao1=totalUniv[university_list[i]]
        num=int(xiexiao1['参赛队伍'])
        join_party[str(university_list[i])]=num
        print(xiexiao1)
    except:
        continue
univ_totalnum=list(sorted(join_party.items(),key=lambda x:x[1],reverse=True)) #默认升序,True为降序.
#上海各个高效参赛队伍直方图
#筛选出上海的高校
shanghai_univ=[]
for i in range(len(univ_totalnum)):
    for item in ['上海','华东','东华','同济','复旦','解放军第二军医']:
        if item in univ_totalnum[i][0]:
            shanghai_univ.append(univ_totalnum[i])
        else:
            continue
#删除离群点非上海的高校
#del shanghai_univ[9]  #删除中国石油大学(华东)---青岛
#del shanghai_univ[12] #华东交通大学----江西  
#获得上海高校列表34所
#画出直方图
import matplotlib.pyplot as plt
plt.subplots(figsize=(10,6))
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来显示中文
plt.bar(range(len(shanghai_univ)),[shanghai_univ[i][1] for i in range(len(shanghai_univ))],color='blue',align='center')
plt.title("上海各高校2018年'华为杯'全国研究生数学建模竞赛参赛队伍直方图")
plt.xticks(range(len(shanghai_univ)),[shanghai_univ[i][0] for i in range(len(shanghai_univ))],rotation=90)
plt.xlim([-1,len(shanghai_univ)])
plt.xlabel("上海高校")
plt.ylabel("队伍数")
plt.tight_layout()
plt.show()            
shanghai_university=shanghai_univ
type(shanghai_university[0][0])
type(shanghai_university[0][1])


#1.将上海高校入数据库保存
import sqlite3
conn=sqlite3.connect('E:/代码练习区256/MathModel/cmath2018.sqlite')
curs=conn.cursor()
#conn.close()
#在Python中一个分号算是一条语句,curs.execute(sql(i))只执行一条语句
curs.execute("drop table if EXISTS unives_shanghai");
#curs.close()
curs.execute("create table unives_shanghai(uid varchar(10) PRIMARY KEY,univ_name varchar(30),groupe_num int)")
#curs.execute("insert into unives_shanghai(uid,univ_name,groupe_num) values('123456','中国科学技术大学',240)") #% ('123456','中国科学技术大学',240))

id1='10247'+str(1)
name1=shanghai_university[1][0]
num1=shanghai_university[1][1]
print("统计的数学===(%s,%s,%d)" % (id1,name1,num1))
#curs.execute("insert into unives_shanghai(uid,univ_name,groupe_num) values('%s','%s','%d')" % (id1,name1,num1)) #% ('123456','中国科学技术大学',240))

curs.execute("select * from unives_shanghai")
df1=curs.fetchall()

#for i in range(2,len(shanghai_university)):
for i in range(len(shanghai_university)):
    try:
        curs.execute("insert into unives_shanghai(uid,univ_name,groupe_num) values('%s','%s','%d')" % ('10247'+str(i),shanghai_university[i][0],shanghai_university[i][1]))
    except Exception as ex:  #异常的抛出
        print("Exception: ", str(ex))
        pass

curs.execute("select * from unives_shanghai")
df1=curs.fetchall()
#挑选出来上海地区参赛队伍数>=100的学校
curs.execute("select * from unives_shanghai where groupe_num>=100")
df1=curs.fetchall()

#筛选出来上海各个高校的获奖情况
shanghai_get={}
for i in range(len(shanghai_university)):
    shanghai_get[shanghai_university[i][0]]=totalUniv[shanghai_university[i][0]]
#画出获奖高校获奖队伍数直方图
#排序前    
import matplotlib.pyplot as plt
plt.subplots(figsize=(10,6))
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来显示中文
#for i in shanghai_get:
#    print(i)
plt.bar(range(len(shanghai_get)),[shanghai_get[i]['获奖总队伍数'] for i in shanghai_get],color='blue',align='center')
plt.title("上海各高校2018年'华为杯'全国研究生数学建模竞赛获奖队伍直方图")
plt.xticks(range(len(shanghai_get)),[shanghai_get[i]['学校名称'] for i in shanghai_get],rotation=90)
plt.xlim([-1,len(shanghai_get)])
plt.xlabel("上海高校")
plt.ylabel("获奖队伍数")
plt.tight_layout()
plt.show() 
#排序后:数据复杂不好弄,单独取出来再做分析,简化操作过程
namename={}
for i in shanghai_get:
    namename[i]=shanghai_get[i]['获奖总队伍数']
zhouzhou=sorted(namename.items(),key=lambda x:x[1],reverse=True)
import matplotlib.pyplot as plt
plt.subplots(figsize=(10,6))
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来显示中文
plt.bar(range(len(zhouzhou)),[zhouzhou[i][1] for i in range(len(zhouzhou))],color='blue',align='center')
plt.title("上海各高校2018年'华为杯'全国研究生数学建模竞赛获奖队伍直方图")
plt.xticks(range(len(zhouzhou)),[zhouzhou[i][0] for i in  range(len(zhouzhou))],rotation=90)
plt.xlim([-1,len(zhouzhou)])
plt.xlabel("上海高校")
plt.ylabel("获奖队伍数")
plt.tight_layout()
plt.show()
import pandas as pd
data2=pd.DataFrame(shanghai_get,columns=shanghai_get.keys()).T
columns2=data2.columns.tolist()
data2=data2[[ '学校名称','参赛队伍', '获奖总队伍数', '未获奖总队伍数', '学校获奖比', '学校各题获奖比率']]
data2.to_csv('E:/上海高校数模获奖_data.csv',index=False)

#全国的情况
shouzhou=sorted(join_party.items(),key=lambda x:x[1],reverse=True)
import pandas as pd
data2=pd.DataFrame(shouzhou,columns=['学校','参赛队伍数'])
columns2=data2.columns.tolist()
data2.to_csv('E:/全国高校数模参赛人数_data.csv',index=True)
#全国有实力高效的获奖情况
import pandas as pd
data2=pd.DataFrame([totalUniv[i] for i in totalUniv],index=totalUniv.keys())
columns2=data2.columns.tolist()
data2=data2[['学校名称', '参赛队伍', '获奖总队伍数','未获奖总队伍数', '学校各题获奖比率', '学校获奖比']]
#data2.reindex(range(len(data2.index.tolist()))) #直接传入想要的新index即可。但是很多东西没了
data2.to_csv('E:/全国数模获奖高校战果统计_data.csv',index=False)
