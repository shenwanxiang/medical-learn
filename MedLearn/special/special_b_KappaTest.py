#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 2 20:07:26 2018

@author: charleshen

Kappa test
"""


import sys
sys.path.insert(0,'/home/shenwanxiang/wuhan_software/medical-learn') #改成你的路径

import os
import pandas as pd
import scipy.stats as stats
import numpy as np


from MedLearn.dataset import load_MedExp
from MedLearn.utils.modelbase import ModelBase
from MedLearn.utils.pandastool import isCategory, isSeries
from MedLearn.docs import common_doc
from MedLearn.utils import logtools
from statsmodels.stats.inter_rater import cohens_kappa


#filename = os.path.basename(__file__)
filename = 'special_b_KappaTest.py'
ABSTRACT = '''在诊断试验中，研究者希望考察不同的诊断方法在诊断结果上是否具有一致性。如：评价两种诊断试验方法对同一个样本或研究对象的化验结果的一致性。此时，Kappa值可以作为评价判断的一致性程度的指标。'''
DOC = common_doc.DOC(filename=filename)

def core(tsx,tsy = None, method = 'simple_kappa'):
    
    '''
    input
    --------
      tsx: 定类型数据
      tsy: 定类型数据
      method: 方法，下拉菜单
    '''
    
    msg = {}
    
    methods = {"simple_kappa":"简单kappa", 
               "weight_kappa":"加权kappa" 
              }

    table = pd.crosstab(tsx,tsy)
    
    if method == 'simple_kappa':
        res = cohens_kappa(table, return_results=True)
    
    else:
        res = cohens_kappa(table, wt = 'linear', return_results=True)

    columns = {'名称':'%s & %s' % (tsx.name, tsy.name) ,
               'Kappa值':res.get('kappa'),
               'Z值':res.get('z_value'),
               'P值':res.get('pvalue_two_sided'),
               '95%CI(下限)':round(res.get('kappa_low'),5),
               '95%CI(上限)':round(res.get('kappa_upp'),5),
                'ASE':round(res.get('std_kappa0'),5),
              '类型':res.get('kind')}

        
    return pd.DataFrame([columns]).set_index('名称'), msg



#df = load_MedExp()
#tsx = df.child
#tsy = df.physlim
#core(tsx,tsy)[0] 
