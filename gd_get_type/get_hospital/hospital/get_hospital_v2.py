# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag
file = r'D:\learn_python\gd_get_type\get_hospital\hospital\\hospital.html'
soup = BeautifulSoup(open(file),"html5lib")
def th_txt(str):
    return str.replace('：'.decode("UTF-8"),'').replace(' ','')
# 找到 li 标签下所有的数据
for x in soup.find_all('li'):
    # 找到 li 下 标签 a 的所有数据
    for hospital_name in x.find_all('a'):
        if hospital_name.string:
            print ''
            # 打印出 a 标签的字符串
            print '%s|'% th_txt(hospital_name.string),
    for hospital_other_str in x.find_all('li'):
        for address_phone in hospital_other_str:
            if isinstance(address_phone,NavigableString):
                print '%s|' % th_txt(address_phone),

        
        # if isinstance(hospital_name,NavigableString):
        #     print hospital_name
