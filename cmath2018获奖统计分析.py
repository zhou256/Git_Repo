# -*- coding: utf-8 -*-
"""
     ����Ч�����Բο����˲��͵�Ч��չʾ:
	 https://blog.csdn.net/jp_zhou256/article/details/83959856
"""
"""2018�껪Ϊ����ģս��ͳ��"""
import pandas as pd
import xlwt
import numpy as np
file_path=r'C:/Users/Administrator/Desktop/AAA/'
data_A=pd.read_excel(file_path+'2018�����ջ�����_A��.xls',encode='gbk')
len(data_A)
data_A.columns.tolist()
data_B=pd.read_excel(file_path+'2018�����ջ�����_B��.xls',encode='gbk')
len(data_B)
data_C=pd.read_excel(file_path+'2018�����ջ�����_C��.xls',encode='gbk')
len(data_C)
data_D=pd.read_excel(file_path+'2018�����ջ�����_D��.xls',encode='gbk')
len(data_D)
data_E=pd.read_excel(file_path+'2018�����ջ�����_E��.xls',encode='gbk')
len(data_E)
data_F=pd.read_excel(file_path+'2018�����ջ�����_F��.xls',encode='gbk')
len(data_F)
data_all=pd.concat([data_A,data_B,data_C,data_D,data_E,data_F],axis=0) #�����з���ƴ��
print(data_all.head(10))
sum([len(data_A),len(data_B),len(data_C),len(data_D),len(data_E),len(data_F)])
columnnum=len(data_A.columns.tolist())
len(data_all)
#data_all.to_excel(file_path+'2018��ģ�ɼ�����.xls',encoding='gbk')
data_SMU=data_all[((data_all['�ӳ����ڵ�λ']=='���ϴ�ѧ')|
                                    (data_all['��һ�������ڵ�λ']=='���ϴ�ѧ')|
                                    (data_all['�ڶ��������ڵ�λ']=='���ϴ�ѧ'))]
data_SMU.to_excel(file_path+'���ϴ�ѧ2018�о�����ģ�ɼ�����.xls',encoding='gbk')

#�Ϻ����´�ѧ����δ������ռ��
#1.�񽱶���
prized=data_SMU[~(data_SMU['����']=='�ɹ����뽱')]
#2.δ�񽱶���
unprized=data_SMU[data_SMU['����']=='�ɹ����뽱']
prized['����'].value_counts()  #�ֱ����������������,Ĭ���ǽ���
"""
���Ƚ�    63
���Ƚ�    30
һ�Ƚ�     3
"""
prizedCount=prized['����'].value_counts(ascending=True)
"""
һ�Ƚ�     3
���Ƚ�    30
���Ƚ�    63
"""
unprizedCount=unprized['����'].value_counts() #����ɹ����뽱�Ļ�����
#�ɹ����뽱    139
#2018��Ϊ��ȫ���о�����ѧ��ģ,�Ϻ����´�ѧ����
prizedsum=np.sum(prizedCount[:])
prizeate=np.sum(prizedCount)/(np.sum(unprizedCount)+prizedsum) # 0.4393063583815029
prizeate # 0.4393063583815029
#���´�ѧ������ռ2018�������������
rate=sum(sum(prizedCount)+unprizedCount)/data_all.shape[0] #����������=12207
rate #0.019251249283198164

#ͳ�Ƹ�����У�Ļ�Ƶ��
#prize_freq=data_all.groupby(['���','����']).agg('sum')
#2018��ѡ��ѡ�����һ����,�����������
"""1.����������: һ�Ƚ�����Ϊ���� һ�Ƚ�ͬ��,����ȥ��,ʹ��������ʽ�����ַ����滻"""
#str1='zhoujianpeng'
#str1.replace('jian', '��')
#��̵��ַ���ֱ���滻�ͺ���.
data_all['����']=data_all['����'].apply(lambda x:x.replace('һ�Ƚ�����Ϊ��','һ�Ƚ�'))
#������������û����ȫ��ȥ�سɹ�(����һ�Ƚ���Ȼ��ͬ��û�кϲ�)
"""
import re
s = 'obj_Temp:28.41 ref_Temp:39.24'
a = re.search(r'obj_Temp:([\d.]+)', s) #ȡ��ָ���ַ����е�����
a.group(1)
"""
chooses,category=[data_all['���'].value_counts(ascending=True),data_all['����'].value_counts(ascending=True)]
chooses
category
totalNum=data_all.shape[0]
prize1_rate,prize2_rate,prize3_rate,unprize_rate=category/totalNum
print('\nһ�Ƚ�: ',prize1_rate,'\n���Ƚ�: ',prize2_rate,'\n���Ƚ�: ',prize3_rate,'\n�ɹ����뽱: ',unprize_rate)
#������&δ������ռ��
lucky_count=sum(category[:3]) #������:4358
success_join_count=totalNum-lucky_count #δ������:7849
print('2018�껪Ϊ����ѧ��ģ����: ',prize1_rate+(prize2_rate+prize3_rate))



#��У�����б�
import pandas as pd
university_list=list(pd.concat([data_all['�ӳ����ڵ�λ'],data_all['��һ�������ڵ�λ'],data_all['�ڶ��������ڵ�λ']]).unique())
university_list #2018�걾�ڲ�����ѧ��ģ�����Ĵ�ѧ����
data_SMU=data_all[((data_all['�ӳ����ڵ�λ']=='�Ϻ����´�ѧ')|
                                    (data_all['��һ�������ڵ�λ']=='�Ϻ����´�ѧ')|
                                    (data_all['�ڶ��������ڵ�λ']=='�Ϻ����´�ѧ'))]


#university=[] #��������ѧ��Ⱥ
university={} #��������ѧ��Ⱥ
totalNum=data_all.shape[0] #����������֧��
for i in range(len(university_list)):
    #grade.append(university_list[i]+str(i))
    del data_SMU
    data_SMU=data_all[((data_all['�ӳ����ڵ�λ']==university_list[i])|(data_all['��һ�������ڵ�λ']==university_list[i])|(data_all['�ڶ��������ڵ�λ']==university_list[i]))].reset_index(drop=True)
    del data_SMU['���']
    university[university_list[i]]=data_SMU
#�ֱ�ͳһÿһ����ѧ�ĸ���������Ŀ


"""
xuexiao1={'ѧУ����':ͬ�ô�ѧ,
          '��������':1000,
          '��������':480,
          'δ������':1000-480,
          'ѧУ����񽱱���':[1,2,3,4,5,6],
          'ѧУ�񽱱�':480/1000
          '�����':{
          'A':{'һ�Ƚ�':10,'���Ƚ�':20,'���Ƚ�':50,'�ɹ����뽱':200,'ѡ������֧��':280,'��Ƶ��':80,'δ��Ƶ��':200,'�񽱱���':18.5%}
          'B':{'һ�Ƚ�':10,'���Ƚ�':20,'���Ƚ�':50,'�ɹ����뽱':200,'ѡ������֧��':280,'��Ƶ��':80,'δ��Ƶ��':200,'�񽱱���':18.5%}
          'C':{'һ�Ƚ�':10,'���Ƚ�':20,'���Ƚ�':50,'�ɹ����뽱':200,'ѡ������֧��':280,'��Ƶ��':80,'δ��Ƶ��':200,'�񽱱���':18.5%}
          'D':{'һ�Ƚ�':10,'���Ƚ�':20,'���Ƚ�':50,'�ɹ����뽱':200,'ѡ������֧��':280,'��Ƶ��':80,'δ��Ƶ��':200,'�񽱱���':18.5%}
          'E':{'һ�Ƚ�':10,'���Ƚ�':20,'���Ƚ�':50,'�ɹ����뽱':200,'ѡ������֧��':280,'��Ƶ��':80,'δ��Ƶ��':200,'�񽱱���':18.5%}
          'F':{'һ�Ƚ�':10,'���Ƚ�':20,'���Ƚ�':50,'�ɹ����뽱':200,'ѡ������֧��':280,'��Ƶ��':80,'δ��Ƶ��':200,'�񽱱���':18.5%}
            }
          }
"""

    
#totalUniv=[]
totalUniv={}
saiti_list=['A','B','C','D','E','F']
for i in range(len(university)):
#for i in range(5):
    #print(university[university_list[0]]) #universityΪ�ֵ�,ѧУ����Ϊkey
    xiexiao={}
     #xiexiao1=university[university_list[3]]
    xiexiao1=university[university_list[i]]
    #xiexiao1=university[university_list[77]] #3--ͬ�ô�ѧ��77--���´�ѧ
    #ѧУ����(�����е�����)
    zhongshu=pd.concat([xiexiao1['�ӳ����ڵ�λ'],xiexiao1['��һ�������ڵ�λ'],xiexiao1['�ڶ��������ڵ�λ']]) #Series
    xiexiao['ѧУ����']= zhongshu.value_counts().index[0] #value_countsĬ���ǽ���,ѡ��������Ӧ������ֵ��ΪѧУ.
    #chooses=xiexiao1['���'].value_counts(ascending=True) #��Ӧ����ѡ������֧��
    ##A=xiexiao1[xiexiao1['���']].value_counts()
    #prizeoption=xiexiao1['����'].unique()
    #1.������������
    xiexiao['��������']=len(xiexiao1)
    #totalUniv[university_list[3]]=xiexiao
    #totalUniv[university_list[i]]=xiexiao
    #2.������ѧУ�ĸ�������������
    #2.1.ѡ��A������
    #xiexiao1[xiexiao1['���']=='A']['����'].value_counts(ascending=True) #����A�����Ӧ�Ļ����
    #2.2.����������Ի����һ����
    """
    zhou=[1,2,4,5],zhou[-1],zhou[:-1]
    """
    timu={}#�������������Զ�Ӧ�Ļ����
    sum_prize1=0
    award_prize=0
    for ii in range(len(saiti_list)):
        #print(saiti_list[ii])
        #things=things.index
        #�����things���г�ʼ��,��Ȼ�е�ѧУû��һ�Ƚ�things[0]�ʹ�λ��,�ͳ�����.
        things=xiexiao1[xiexiao1['���']==saiti_list[ii]]['����'].value_counts(ascending=True)
        #����ͬ�ô�ѧ��B,����B��Ŀû��һ�Ƚ�
        #things=xiexiao1[xiexiao1['���']==saiti_list[ii]]['����'].value_counts(ascending=True)
        ##����ֵ,��Ϊÿ������һ������.
        one_rate1=0
        two_rate1=0
        three_rate1=0
        non_rate1=0
        prized_rate1=0
        try:
            #һ�Ƚ�������
            try:
                if ~things[things.index=='һ�Ƚ�'].empty:
                    #print('1')
                    one_prize1=things[things.index=='һ�Ƚ�'] #type(one_prize1)=Series
                    if len(one_prize1)==0:
                        one_prize1=0
                    elif len(one_prize1)==1:
                        #one_prize1=one_prize1.values[0,0] #��Seriesת��Ϊ��ά����
                        one_prize1=list(one_prize1)[0] #��Seriesת��Ϊlist��ȡֵҲ����
                else:
                    one_prize1=0
            except  :
                pass
            finally:
                print('one_prize1����������������������������')    
            #���Ƚ�����
            try:
                if ~things[things.index=='���Ƚ�'].empty:
                    two_prize1=things[things.index=='���Ƚ�']
                    if len(two_prize1)==0:
                        two_prize1=0
                    elif len(two_prize1)==1:
                        #one_prize1=one_prize1.values[0,0] #��Seriesת��Ϊ��ά����
                        two_prize1=list(two_prize1)[0] #��Seriesת��Ϊlist��ȡֵҲ����
                else:
                    two_prize1=0
            except  :
                pass
            finally:
                print('two_prize1����������������������������')  
            #���Ƚ�������
            try:
                if ~things[things.index=='���Ƚ�'].empty:
                    three_prize1=things[things.index=='���Ƚ�']
                    if len(three_prize1)==0:
                        three_prize1=0
                    elif len(three_prize1)==1:
                        #one_prize1=one_prize1.values[0,0] #��Seriesת��Ϊ��ά����
                        three_prize1=list(three_prize1)[0] #��Seriesת��Ϊlist��ȡֵҲ����
                else:
                    three_prize1=0
            except  :
                pass
            finally:
                print('three_prize1����������������������������')
            #�ɹ����뽱������===δ������
            try:
                if ~things[things.index=='�ɹ����뽱'].empty:
                    non_prize1=things[things.index=='�ɹ����뽱']
                    if len(non_prize1)==0:
                        non_prize1=0
                    elif len(non_prize1)==1:
                        #one_prize1=one_prize1.values[0,0] #��Seriesת��Ϊ��ά����
                        non_prize1=list(non_prize1)[0] #��Seriesת��Ϊlist��ȡֵҲ����
                else:
                    non_prize1=0
            except  :
                pass
            finally:
                print('non_prize1����������������������������')
            #�񽱶�������
            award_prize=sum(things[:-1])
            #ĳ������Ĳ����ܶ�����
            sum_prize1=sum(things)
            #һ�Ƚ�������������������������ռ��
            one_rate1=one_prize1/sum_prize1
            #���Ƚ�������������������������ռ��
            two_rate1=two_prize1/sum_prize1
            #���Ƚ�������������������������ռ��
            three_rate1=three_prize1/sum_prize1
            #δ�񽱶�����������������������ռ��
            non_rate1=non_prize1/sum_prize1
            #�񽱶�����������������������ռ��
            prized_rate1=award_prize/sum_prize1
            timu[saiti_list[ii]]={
                    'һ�Ƚ�������':one_prize1,
                    'һ�Ƚ��񽱱���':one_rate1,
                    '���Ƚ�������':two_prize1,
                    '���Ƚ��񽱱���':two_rate1,
                    '���Ƚ�������':three_prize1,
                    '���Ƚ��񽱱���':three_rate1,
                    '�ɹ����뽱������':non_prize1,'δ�񽱱���':non_rate1,
                    '�񽱶�����':award_prize,'�񽱱���':prized_rate1}
            #del things
        except  :
            pass
        #finally:
        #     print('����������������������������')
    #3.��������
    try:
        total_queue=0
        for i1 in range(len(timu)):
            try:
                total_queue+=timu[saiti_list[i1]]['�񽱶�����']
            except:
                continue
        xiexiao['���ܶ�����']=total_queue
    except:
            pass
    #4.δ��������
    try:
        un_num=0
        for i1 in range(len(timu)):
            try:
                un_num+=timu[saiti_list[i1]]['�ɹ����뽱������']
            except:
                continue
        xiexiao['δ���ܶ�����']=un_num
    except:
            pass
    #5.ĳ��������������Ϊһ��list=[]����
    try:
        rate_list={}
        for i1 in range(len(timu)):
            rate_list[saiti_list[i1]]=timu[saiti_list[i1]]['�񽱱���']
        xiexiao['ѧУ����񽱱���']=rate_list
    except:
            pass
    #5.ѧУ����������ɻ����
    try:
        xiexiao['ѧУ�������ϸ']=timu
    except:
            pass
    #5.ѧУ�񽱱�
    try:
        xx_rate=total_queue/len(xiexiao1) #ѧУ�Ĳ��뾺��������
        xiexiao['ѧУ�񽱱�']=xx_rate
    except:
            pass
    #totalUniv.append(xiexiao)
    totalUniv[university_list[i]]=xiexiao
    del xiexiao1
#�����ֵ�����:ʹ��DataFrame
import pandas as pd
data=pd.DataFrame(totalUniv,columns=totalUniv.keys()).T
columns_name=data.columns.tolist()
#������ֵ�����������������������
#data.columns=[['��������', 'ѧУ�������ϸ', 'ѧУ����񽱱���', 'ѧУ����', 'ѧУ�񽱱�', 'δ���ܶ�����', '���ܶ�����']]
#�������������Ⱥ�˳����λ�ñ仯
data=pd.DataFrame(totalUniv,columns=totalUniv.keys()).T
#����ָ���е�˳��
data=data[['ѧУ����','��������', '���ܶ�����', 'δ���ܶ�����','ѧУ�������ϸ', 'ѧУ����񽱱���',  'ѧУ�񽱱�']]
#data[data['ѧУ����']=='�Ϻ����´�ѧ']
data.to_csv('E:/jianpengzhou.csv',index=False)
#���ղ����������ֵ��������
join_party={}
for i in range(len(university_list)):
#for i in range(5):
    #print(university[university_list[0]]) #universityΪ�ֵ�,ѧУ����Ϊkey
    try:
        xiexiao1=totalUniv[university_list[i]]
        num=int(xiexiao1['��������'])
        join_party[str(university_list[i])]=num
        print(xiexiao1)
    except:
        continue
univ_totalnum=list(sorted(join_party.items(),key=lambda x:x[1],reverse=True)) #Ĭ������,TrueΪ����.
#�Ϻ�������Ч��������ֱ��ͼ
#ɸѡ���Ϻ��ĸ�У
shanghai_univ=[]
for i in range(len(univ_totalnum)):
    for item in ['�Ϻ�','����','����','ͬ��','����','��ž��ڶ���ҽ']:
        if item in univ_totalnum[i][0]:
            shanghai_univ.append(univ_totalnum[i])
        else:
            continue
#ɾ����Ⱥ����Ϻ��ĸ�У
#del shanghai_univ[9]  #ɾ���й�ʯ�ʹ�ѧ(����)---�ൺ
#del shanghai_univ[12] #������ͨ��ѧ----����  
#����Ϻ���У�б�34��
#����ֱ��ͼ
import matplotlib.pyplot as plt
plt.subplots(figsize=(10,6))
plt.rcParams['font.sans-serif'] = ['SimHei']  #������ʾ����
plt.bar(range(len(shanghai_univ)),[shanghai_univ[i][1] for i in range(len(shanghai_univ))],color='blue',align='center')
plt.title("�Ϻ�����У2018��'��Ϊ��'ȫ���о�����ѧ��ģ������������ֱ��ͼ")
plt.xticks(range(len(shanghai_univ)),[shanghai_univ[i][0] for i in range(len(shanghai_univ))],rotation=90)
plt.xlim([-1,len(shanghai_univ)])
plt.xlabel("�Ϻ���У")
plt.ylabel("������")
plt.tight_layout()
plt.show()            
shanghai_university=shanghai_univ
type(shanghai_university[0][0])
type(shanghai_university[0][1])


#1.���Ϻ���У�����ݿⱣ��
import sqlite3
conn=sqlite3.connect('E:/������ϰ��256/MathModel/cmath2018.sqlite')
curs=conn.cursor()
#conn.close()
#��Python��һ���ֺ�����һ�����,curs.execute(sql(i))ִֻ��һ�����
curs.execute("drop table if EXISTS unives_shanghai");
#curs.close()
curs.execute("create table unives_shanghai(uid varchar(10) PRIMARY KEY,univ_name varchar(30),groupe_num int)")
#curs.execute("insert into unives_shanghai(uid,univ_name,groupe_num) values('123456','�й���ѧ������ѧ',240)") #% ('123456','�й���ѧ������ѧ',240))

id1='10247'+str(1)
name1=shanghai_university[1][0]
num1=shanghai_university[1][1]
print("ͳ�Ƶ���ѧ===(%s,%s,%d)" % (id1,name1,num1))
#curs.execute("insert into unives_shanghai(uid,univ_name,groupe_num) values('%s','%s','%d')" % (id1,name1,num1)) #% ('123456','�й���ѧ������ѧ',240))

curs.execute("select * from unives_shanghai")
df1=curs.fetchall()

#for i in range(2,len(shanghai_university)):
for i in range(len(shanghai_university)):
    try:
        curs.execute("insert into unives_shanghai(uid,univ_name,groupe_num) values('%s','%s','%d')" % ('10247'+str(i),shanghai_university[i][0],shanghai_university[i][1]))
    except Exception as ex:  #�쳣���׳�
        print("Exception: ", str(ex))
        pass

curs.execute("select * from unives_shanghai")
df1=curs.fetchall()
#��ѡ�����Ϻ���������������>=100��ѧУ
curs.execute("select * from unives_shanghai where groupe_num>=100")
df1=curs.fetchall()

#ɸѡ�����Ϻ�������У�Ļ����
shanghai_get={}
for i in range(len(shanghai_university)):
    shanghai_get[shanghai_university[i][0]]=totalUniv[shanghai_university[i][0]]
#�����񽱸�У�񽱶�����ֱ��ͼ
#����ǰ    
import matplotlib.pyplot as plt
plt.subplots(figsize=(10,6))
plt.rcParams['font.sans-serif'] = ['SimHei']  #������ʾ����
#for i in shanghai_get:
#    print(i)
plt.bar(range(len(shanghai_get)),[shanghai_get[i]['���ܶ�����'] for i in shanghai_get],color='blue',align='center')
plt.title("�Ϻ�����У2018��'��Ϊ��'ȫ���о�����ѧ��ģ�����񽱶���ֱ��ͼ")
plt.xticks(range(len(shanghai_get)),[shanghai_get[i]['ѧУ����'] for i in shanghai_get],rotation=90)
plt.xlim([-1,len(shanghai_get)])
plt.xlabel("�Ϻ���У")
plt.ylabel("�񽱶�����")
plt.tight_layout()
plt.show() 
#�����:���ݸ��Ӳ���Ū,����ȡ������������,�򻯲�������
namename={}
for i in shanghai_get:
    namename[i]=shanghai_get[i]['���ܶ�����']
zhouzhou=sorted(namename.items(),key=lambda x:x[1],reverse=True)
import matplotlib.pyplot as plt
plt.subplots(figsize=(10,6))
plt.rcParams['font.sans-serif'] = ['SimHei']  #������ʾ����
plt.bar(range(len(zhouzhou)),[zhouzhou[i][1] for i in range(len(zhouzhou))],color='blue',align='center')
plt.title("�Ϻ�����У2018��'��Ϊ��'ȫ���о�����ѧ��ģ�����񽱶���ֱ��ͼ")
plt.xticks(range(len(zhouzhou)),[zhouzhou[i][0] for i in  range(len(zhouzhou))],rotation=90)
plt.xlim([-1,len(zhouzhou)])
plt.xlabel("�Ϻ���У")
plt.ylabel("�񽱶�����")
plt.tight_layout()
plt.show()
import pandas as pd
data2=pd.DataFrame(shanghai_get,columns=shanghai_get.keys()).T
columns2=data2.columns.tolist()
data2=data2[[ 'ѧУ����','��������', '���ܶ�����', 'δ���ܶ�����', 'ѧУ�񽱱�', 'ѧУ����񽱱���']]
data2.to_csv('E:/�Ϻ���У��ģ��_data.csv',index=False)

#ȫ�������
shouzhou=sorted(join_party.items(),key=lambda x:x[1],reverse=True)
import pandas as pd
data2=pd.DataFrame(shouzhou,columns=['ѧУ','����������'])
columns2=data2.columns.tolist()
data2.to_csv('E:/ȫ����У��ģ��������_data.csv',index=True)
#ȫ����ʵ����Ч�Ļ����
import pandas as pd
data2=pd.DataFrame([totalUniv[i] for i in totalUniv],index=totalUniv.keys())
columns2=data2.columns.tolist()
data2=data2[['ѧУ����', '��������', '���ܶ�����','δ���ܶ�����', 'ѧУ����񽱱���', 'ѧУ�񽱱�']]
#data2.reindex(range(len(data2.index.tolist()))) #ֱ�Ӵ�����Ҫ����index���ɡ����Ǻܶණ��û��
data2.to_csv('E:/ȫ����ģ�񽱸�Уս��ͳ��_data.csv',index=False)
