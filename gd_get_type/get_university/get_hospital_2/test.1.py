# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from bs4 import Tag
from bs4 import NavigableString

hospital = '''
<li><b><a href="/w/%E7%A7%A6%E7%9A%87%E5%B2%9B%E5%B8%82%E7%AC%AC%E4%B8%80%E5%8C%BB%E9%99%A2" title="秦皇岛市第一医院">秦皇岛市第一医院</a></b>
<ul>
<li><b>医院地址</b>：河北省秦皇岛市海港区文化路258号</li>
<li><b>联系电话</b>：0335-3032042</li>
</ul>
</li>
'''
soup = BeautifulSoup(hospital,"html5lib")
# print soup
for i in soup.li:
    print unicode(i,encoding="utf-8")