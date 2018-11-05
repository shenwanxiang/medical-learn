
from ..common.common_e_CorrStat import CorrStat
from ..common.common_a_CountFreq import CountFreq
from ..common.common_b_ChiSquareCrossTab import ChiSquareCrossTab
from ..common.common_c_DescripStat import DescripStat
from ..common.common_d_GroupByStat import GroupByStat
from ..common.common_e_CorrStat import CorrStat
from ..common.common_f_OlsLinearReg import OlsLinearReg
from ..common.common_g_OnewayAnova import OnewayAnova
from ..common.common_h_TTestInd import TTestInd
from ..common.common_i_TTest1Samp import TTest1Samp
from ..common.common_j_TTestPair import TTestPair
from ..common.common_k_NormalityTest import NormalityTest
from ..common.common_l_NonparametricStat import NonparametricStat
from ..common.common_m_HOVTest import HOVTest
CorrStat_conf = CorrStat().get_info()

GlobalConf = [
    {"id": "comman",
     "name": "通用方法",
        "children": [
            CorrStat().get_info(),
            CountFreq().get_info(),
            DescripStat().get_info(),
            GroupByStat().get_info(),
            OnewayAnova().get_info(),
            TTestInd().get_info(),
            TTest1Samp().get_info(),
            TTestPair().get_info(),
            NormalityTest().get_info(),
            NonparametricStat().get_info(),
            HOVTest().get_info()
            ]
     }

]
