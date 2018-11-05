### 三、整体介绍：

#### 以下三个模块分别为通用统计分析（common模块），高级机器学习分析（advance模块）和医学统计中特殊场景的分析（special模块）

#### 导入模块
`>>> from MedProc import common,advance,special`

1.common模块：

    1.1 频数：common.a_CountFreq
    1.2 交叉（卡方）：common.b_ChiSquareCrossTab
    1.3 描述：common.c_DescripStat
    1.4 分类汇总：common.d_GroupByStat
    1.5 相关：common.e_CorrStat
    1.6 回归：common.f_OlsLinearReg
    1.7 单因素方差：common.g_OnewayAnova
    1.8 T检验：common.h_TTestInd
    1.9 单样本T检验：common.i_TTest1Samp
    1.10 配对T检验：common.j_TTestPair
    1.11 正态性检验：common.k_NormalityTest
    1.12 非参数检验：common.l_NonparametricStat
    1.13 方差齐检验：common.m_HOVTest


2.advance模块：

    2.1 聚类：advance_Cluster  
    2.2 因子:advance_FA
    2.3 主成分:advance:PCA
    2.4 事后检验:advance_PostHocTest
    2.5 逐步回归:advance_StepwiseReg
    2.6 分层回归: advance_HierarchicalReg
    2.7 双因素方差: advance_TwowayAnova
    2.8 二元Logit分析: 未做 binary logistic regression
    2.9 多分类Logit分析: 未做
    2.10 岭回归分析: 未做

3.special模块：

    3.1 卡方检验: 未做
    3.2 Kappa一致性检验: 未做
    3.3 二元Probit回归分析: 未做
    3.4 Poisson回归分析: 未做
    3.5 多因素方差分析: 未做