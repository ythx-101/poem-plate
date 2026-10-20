import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compose_bw  # installs column_tight + clean_petals
import compose_lib as L
from PIL import Image
SP='\u3000'
TAG='白妈{0}蓝妈{0}红妈{0}其{1}'
P={
 'sylphy_cl':dict(n='一',src='cl_sylphy_a.png',cols=[('希露菲','big',20),(f'青丝一夜化霜华{SP}墨镜藏眸入帝家','mid',10),(f'莫道重逢人不识{SP}春风原是旧时花','mid',16),('《无职转生》','small',0)],kw=dict(bleed=('bottom','right','top'),scale=1.667,ox=110,oy=0)),
 'roxy_cl':dict(n='二',src='cl_roxy_b.png',cols=[('洛琪希','big',20),(f'心声难解别家乡{SP}一骑携童出院墙','mid',10),(f'弟子焚香尊若圣{SP}十年笑约作新娘','mid',16),('《无职转生》','small',0)],kw=dict(bleed=('bottom','right','top'),scale=1.667,ox=110,oy=0)),
 'eris_cl':dict(n='三',src='cl_eris_a.png',cols=[('艾莉丝','big',20),(f'赤焰飞扬意气高{SP}留书断发入风涛','mid',10),(f'霜锋磨尽圣门雪{SP}未诉相思先拔刀','mid',16),('《无职转生》','small',0)],kw=dict(bleed=('bottom','right','top'),scale=1.667,ox=110,oy=0)),
}
for k in (sys.argv[1:] or P):
    p=P[k]; print('==',k)
    L.compose(p['src'],f'final_{k}.png',p['cols'],TAG.format(SP,p['n']),**p['kw'])
