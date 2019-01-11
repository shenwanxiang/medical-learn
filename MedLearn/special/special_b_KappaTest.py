#https://www.statsmodels.org/dev/generated/statsmodels.stats.inter_rater.cohens_kappa.html


'''
一致性检验


'''


from statsmodels.stats.inter_rater import cohens_kappa


cohens_kappa(table, weights=None, return_results=True, wt=None)

wt:   None, 'linear', 'quadratic'
如果为None， weights无作用， linear 为线性加权， 

table (array_like, 2-Dim) – square array with results of two raters, one rater in rows, second rater in columns  





import logging
import os

import coloredlogs
import pandas as pd
# import researchpy as rp

from ..dataset import load_MedExp
from ..utils.modelbase import ModelBase
from ..utils.pandastool import isCategory, isSeries
from ..docs import common_doc
from ..utils import crosstab


coloredlogs.install()

filename = os.path.basename(__file__)
ABSTRACT = '''相关分析用于研究定量数据之间的关系情况,包括是否有关系,以及关系紧密程度等.此分析方法通常用于回归分析之前;相关分析与回归分析的逻辑关系为:先有相关关系,才有可能有回归关系。'''
DOC = common_doc.DOC(filename=filename)

