# -*- coding: utf-8 -*-
# py2.7.13
from bs4 import BeautifulSoup
from bs4 import Tag
from bs4 import NavigableString
import re
# 使用bs4用html5lib解析网页
soup = BeautifulSoup(open(r"D:\learn_python\gd_get_type\get_university\get_hospital_2\hospital.html"),"html5lib")
# for each_hospital in soup.find('title'):
#     print each_hospital

# aa = '<li><b>56789900</b>1234567878</li>'
# soup1 = BeautifulSoup(aa,"html5lib")
# for i in soup1.li:
#     if isinstance(i,NavigableString):
#         print i
    
    # print type(i),i
# print unicode(str(soup.find_all('li')), encoding="utf-8")
# ,href=re.compile("//w")
for i in soup.find_all('li'):
    for x in i.find_all('a'):
        print unicode(x.string),
    for y in i:
        for d in y:
            if isinstance(d, NavigableString):
                print unicode(y),
    print ''
    # print i.string
    # for x in i.find_all('li'):
    # # print i.string
    #     for y in x.find_all('b'):
    #         print y.string
    #     print unicode(str(y), encoding="utf-8")
    # print '-'*20
