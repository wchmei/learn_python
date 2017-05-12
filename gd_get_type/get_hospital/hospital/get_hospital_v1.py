# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag
# 查看工作目录
# print os.getcwd()
# file = r'D:\learn_python\gd_get_type\get_hospital\hospital\\hospital.html'
# soup = BeautifulSoup(open(file),"html5lib")
test = '''
<li><b><a href="/w/%E5%8C%97%E4%BA%AC466%E5%8C%BB%E9%99%A2" title="北京466医院">北京466医院</a>（空军航空医学研究所附属医院）</b>
<ul>
<li><b>医院地址</b>：北京市海淀区北洼路北口（香格里拉饭店南100米路东）</li>
<li><b>联系电话</b>：010-81988888；4000466120（咨询）</li>
</ul>
</li>
<li><b><a href="/w/%E5%8C%97%E4%BA%AC%E6%9C%9D%E9%98%B3%E5%8C%BB%E9%99%A2%E4%BA%AC%E8%A5%BF%E9%99%A2%E5%8C%BA" title="北京朝阳医院京西院区">北京朝阳医院京西院区</a></b>
<ul>
<li><b>医院地址</b>：北京市石景山区京原路5号</li>
<li><b>联系电话</b>：010-85231000（总机）；51718135（咨询）；51718027(医务处）；51718199（急救）；51718602（急诊）；51718159（值班）</li>
</ul>
</li>
'''.decode("UTF-8")
soup = BeautifulSoup(test,'html5lib')
def tH_txt(str):
    return str.replace('：'.decode("UTF-8"),'').replace(' ','')
# 找到 li 标签下所有的数据
for x in soup.find_all('li'):
    # 找到 li 下 标签 a 的所有数据
    for hospital_name in x.find_all('a'):
        # 打印出 a 标签的字符串
        print '%s|'% tH_txt(hospital_name.string),
    for hospital_other_str in x.find_all('li'):
        for address_phone in hospital_other_str:
            if isinstance(address_phone,NavigableString):
                print '%s|' % tH_txt(address_phone),
    print ''
        
        # if isinstance(hospital_name,NavigableString):
        #     print hospital_name
