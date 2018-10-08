# -*- coding: utf-8 -*-
"""��Ϲ��ߴ�������"""
from __future__ import division
import pandas as pd
import numpy as np
from scipy import stats
#����ĳ���ļ����µ�Դ���ļ�������ôд����

def file_fre_top_5(x):
    if len(x)<=5:
        new_array=np.full(5,np.nan)
        new_array[0:len(x)]=x
        return new_array
#�ڵ�ǰ�ļ������������Ч,���ǲ����ں����ļ�����óɹ�.
#def to_frame(columnsname):
#    #����ǰ���ö��󷵻س�һ��DataFrame.
#        return pd.DataFrame(self,columns=columnsname)

def eda_analysis_v1(missSet=[np.nan,9999999999,-999999],df=pd.Series()):
    ##1.Count
    #df=df1.iloc[:,0:3] #���벻ͨ��,ֱ���ڲ�����.
    count_un=df.apply(lambda x:len(x.unique()))
    #count_un=count_un.to_frame('count')
    count_un=pd.DataFrame(count_un,columns=['count'])
    ##2.Count Zero
    count_zero=df.apply(lambda x:np.sum(x==0))
    #count_zero=count_zero.to_frame('count_zero')
    count_zero=pd.DataFrame(count_zero,columns=['count_zero'])
    ##3.Mean
    df_mean=df.apply(lambda x:np.mean(x[~np.isin(x,missSet)]))
    #df_mean=df_mean.to_frame('mean')
    df_mean=pd.DataFrame(df_mean,columns=['mean'])
    ##4.median
    df_median=df.apply(lambda x:np.median(x[~np.isin(x,missSet)]))
    #df_median=df_median.to_frame('median')
    df_median=pd.DataFrame(df_median,columns=['median'])
    ##5.Mode
    df_mode=df.apply(lambda x:stats.mode(x[~np.isin(x,missSet)])[0][0])
    #df_mode=df_mode.to_frame('mode')
    df_mode=pd.DataFrame(df_mode,columns=['mode'])
    ##6.Mode Percentage
    df_mode_count=df.apply(lambda x:stats.mode(x[~np.isin(x,missSet)])[1][0])
    #df_mode_count=df_mode_count.to_frame('mode_count')
    df_mode_count=pd.DataFrame(df_mode_count,columns=['mode_count'])
    df_mode_perct=df_mode_count/df.shape[0]
    #df_mode_perct=df_mode_perct.to_frame('mode_percent')
    df_mode_perct=pd.DataFrame(df_mode_perct,columns=['mode_percent'])
    
    ##7.min
    df_min=df.apply(lambda x:np.min(x[~np.isin(x,missSet)]))
    #df_min=df_min.to_frame('min')
    df_min=pd.DataFrame(df_min,columns=['min'])
    ##8.max
    df_max=df.apply(lambda x:np.max(x[~np.isin(x,missSet)]))
    #df_max=df_max.to_frame('max')
    df_max=pd.DataFrame(df_max,columns=['max'])
    ##9.quantile
    json_quantile={}
    for i,name in enumerate(df.columns):
        #print('the {} columns: {}'.format(i,name))
        json_quantile[name]=np.percentile(df[name][~np.isin(df[name],missSet)],(1,5,25,50,75,95,99)) #ȥ��ȱʧֵ�ٷ��ظ�����λ��
    df_quantile=pd.DataFrame(json_quantile)[df.columns].T
    df_quantile.columns=['quan01','quan05','quan25','quan50','quan75','quan95','quan99']
    ##10.Frequence
    json_fre_name={}
    json_fre_count={}
    for i,name in enumerate(df.columns):
        #1.Index name
        index_name=df[name][~np.isin(df[name],missSet)].value_counts().iloc[0:5,].index.values
        #1.1 If the length of array is less than 5
        index_name=file_fre_top_5(index_name)
        json_fre_name[name]=index_name
        #2.value count
        value_count=df[name][~np.isin(df[name],missSet)].value_counts().iloc[0:5,].values
        #2.1.if the length of array is less than 5
        value_count=file_fre_top_5(value_count)
        json_fre_count[name]=value_count
    #ת��
    df_fre_name=pd.DataFrame(json_fre_name)[df.columns].T
    df_fre_count=pd.DataFrame(json_fre_count)[df.columns].T
    df_fre=pd.concat([df_fre_name,df_fre_count],axis=1) #axis=1��ʾ�����еķ���ƴ��
    df_fre.columns=['value1','value2','value3','value4','value5','freq1','freq2','freq3','freq4','freq5']
    ##11.Miss Value Count
    df_miss=df.apply(lambda x:np.sum(np.isin(x,missSet))) #apply����ÿһ��������ȱʧֵ�����
    #df_miss=df_miss.to_frame('freq_miss')
    df_miss=pd.DataFrame(df_miss,columns=['freq_miss'])
    ######12.Comnbine API informations#########
    #���ؽ����һ������ƴ��һ��
    df_eda_summay=pd.concat([count_un,count_zero,df_mean,df_median,
                df_mode,df_mode_count,df_mode_perct,df_min,df_max,
                df_fre,df_miss],axis=1) 
    return df_eda_summay