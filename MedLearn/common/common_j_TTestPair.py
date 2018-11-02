#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:10:09 2018

@author: charleshen
"""




'''

dfx #定量，

tsy(定类) #固定 

'''


#pair t-test https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html
#但样本https://stackoverflow.com/questions/44947229/one-sided-one-sample-t-test-python


from scipy.stats import ttest_rel
import pandas as pd

from MedLearn.utils.pandastool import ParseDFtypes
from MedLearn.utils.modelbase import ModelBase
from MedLearn.dataset import load_MedExp


import coloredlogs,logging
coloredlogs.install()




class TTestPair(ModelBase):

    """
    配对T检验: 用于配对定量数据之间的差异对比关系,需要输入dfx,dfy两个dataframe，并且具有相同的列
    并且dfx,dfy都必须是数字型数据
    
    方法
    -------
    get_info : 
        获取该模型的信息， 返回一个字典，包含‘id’和‘name’, 'description','limited'关键字
        含义分别为：模型的id, 模型的名称，模型的描述，模型的适用范围


    run:  
        参数
        ----------
        dfx: pandas DataFrame
            需要每列的数据都是数字型数据，不能是字符串或者object
        
        dfy: pandas Series
             需要每列的数据都是数字型数据，不能是字符串或者object,并且和dfx的列数一样
            
            
        返回结果
        ----------        
            返回一个字典，带有‘result’关键字，F-值、p-值等等系数组成的dataframe

    """
    
    
    
    def __init__(self, 
                 model_id = None, 
                 model_limiation = None,
                 ):
        
        self._id_ = model_id
        self._limitation_ = model_limiation

        
        
    def get_info(self):
        
        return {'id': self._id, 
                'name': self._name, 
                'description': self._description,
                'limited':self._limitation
                }
    
    
    def run(self, 
            dfx, 
            dfy): 

        
            
            msg = {}
            
            xl = len(dfx)
            yl = len(dfy)
            if  xl != yl:
                logging.error('the length of input X:%s is not equal the length of Y: %s ! ' % (xl,yl))
                msg['error'] = '输入的dfx的长度为:%s 不等于输入的dfy的长度: %s  ' % (xl,yl)
                return  {'result':pd.DataFrame(), 'msg':msg}
            
        
            x_numer_cols, x_cate_cols = ParseDFtypes(dfx)
            y_numer_cols, y_cate_cols = ParseDFtypes(dfy)

            
            if (x_cate_cols !=[]) or (y_cate_cols != []):
                logging.error('input x or y has non-numeric data, please check your input data')
                msg['error'] = '输入的dfx或者dfy所有的列都不是数值型数据，请检查输入数据'
                return  {'result':pd.DataFrame(), 'msg':msg}            
            
            
            if  len(x_numer_cols) != len(y_numer_cols):
                logging.error('the number of columns for input X:%s is not equal Y: %s ! ' % (x_numer_cols,y_numer_cols))
                msg['error'] = '输入的dfx的可用的列为:%s ，这和输入的dfy可用的列: %s 在列数数量上不相等 ' % (x_numer_cols,y_numer_cols)
                return  {'result':pd.DataFrame(), 'msg':msg}            
            
        
            
            else:
                
                
                rr = []
                for i, j in zip(x_numer_cols, y_numer_cols):
                    
                    idx = '%s-配对-%s' %(i,j)
                    F, p = ttest_rel(dfx[i],dfy[j])
                
                    m1 = dfx[i].mean()
                    s1 = dfx[i].std()
                    
                    
                    m2 = dfy[j].mean()
                    s2 = dfy[j].std()
                    
                    r1 = '%s±%s' % (round(m1,3),round(s1,3))
                    r2 = '%s±%s' % (round(m2,3),round(s2,3))
                    
                    
                    e = m1 - m2
                    columns = ['配对1(平均值±标准差)', '配对2(平均值±标准差)','差值(配对1-配对2)', 't-值', 'p-值']
                    dfr = pd.DataFrame([r1,r2,e,F,p],index=columns, columns = [idx]).T.round(5)
                    rr.append(dfr)
                    
                    
                res = pd.concat(rr)
                    
                res['p-值'] = res['p-值'].apply(lambda x:'{:.5f}'.format(x))
                
                return {'result':res, 'msg':msg}
            
        
        
            

if __name__ == '__main__':
    
    #读取数据
    
    
    
    df =load_MedExp()

    testdata = load_MedExp()
    dfx = df[['med','age']]
    
    dfy = df[['educdec','ndisease']]
    
    
    #类的初始化
    O = TTestPair()

    #打印该类描述的信息
    print(O.get_info().get('description'))
    
    #执行运算，传入tsx、tsy参数
    dict_res = O.run(dfx,dfy)
    
    #获取返回的字典
    dict_res.get('result')
















