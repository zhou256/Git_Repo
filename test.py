import sys
#导入某个文件夹下的源码文件可以这么写代码
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
#删除无用的列:DataFrame中沿着列方向是axis=1
df1=df.drop(['ID','TARGET'],axis=1) 
#1.数据诊断:
#1.1.均值、中位数、max、min、众数等等
#1.2.计数类
#1.3.缺失值、方差等，方差=0说明这个属性没有区分度,可以直接删除。
#1.4.分位点、值的频数等;分位点:均匀，每个值都会出现一下；分位点：值分布都一样。
#值的频数：最经常出现的值及比例。
"""1.统计指标--计数类"""
###Version 0###
start=time.time()
df_eda_summary= eda_analysis.eda_analysis_v1(missSet=[np.nan,9999999999,-999999],df=df1.iloc[:,0:3])
print("EDA Running Time: {0:.2f} Seconds".format(time.time()-start)) #0.34s


