import sys
#����ĳ���ļ����µ�Դ���ļ�������ôд����
sys.path.append('C:/Users/Administrator/userSatisfy/')
import eda_analysis
import time
# -*- coding: utf-8 -*-
from __future__ import division
import pandas as pd
import numpy as np
from scipy import stats
df=pd.read_csv('F:/Datasets/Kaggle/santander-customer-satisfaction/train.csv')
columns_name=df.columns.tolist()
label=df['TARGET']
#ɾ�����õ���:DataFrame�������з�����axis=1
df1=df.drop(['ID','TARGET'],axis=1) 
#1.�������:
#1.1.��ֵ����λ����max��min�������ȵ�
#1.2.������
#1.3.ȱʧֵ������ȣ�����=0˵���������û�����ֶ�,����ֱ��ɾ����
#1.4.��λ�㡢ֵ��Ƶ����;��λ��:���ȣ�ÿ��ֵ�������һ�£���λ�㣺ֵ�ֲ���һ����
#ֵ��Ƶ����������ֵ�ֵ��������
"""1.ͳ��ָ��--������"""
###Version 0###
start=time.time()
df_eda_summary= eda_analysis.eda_analysis_v1(missSet=[np.nan,9999999999,-999999],df=df1.iloc[:,0:3])
print("EDA Running Time: {0:.2f} Seconds".format(time.time()-start)) #0.34s


