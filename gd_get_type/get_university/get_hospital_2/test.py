# -*- coding:utf-8 -*-
import re
with open(r"D:\learn_python\gd_get_type\get_university\get_hospital_2\hospital.html") as flo:
    data = flo.read()
    # print(data)


# url, 名称
pattern = '<a href="(/w.*?)"[.\s\S]*?">(.*?)</a>'
for i in re.findall(pattern, data):
    url, name = i
    # if u'医'.decode('utf-8') in name:
    print(url,  unicode(name, encoding="utf-8"))
    pass

# url, 地址，电话
# pattern = '<a href="(/w.*?)"[\s\S]*?>医院地址</b>：([\s\S]*?)<.*?>联系电话</b>：(.*?)</li'
# for i in re.findall(pattern, data):
#     print(i)
