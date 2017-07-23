# -*- coding: utf-8 -*-
#python3.41
#解析 http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type= 网址
# http://gkcx.eol.cn/soudaxue/queryschool.html?&argschtype=HND%E9%A1%B9%E7%9B%AE&page=1
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
from bs4 import Tag
import time
province = ['北京']
# province = ['北京', '天津', '河北', '河南', '山东', '山西', '陕西', '内蒙古', '辽宁', '吉林', '黑龙江', \
#             '上海', '江苏', '安徽', '江西', '湖北', '湖南', '重庆', '四川', '贵州', '云南', '广东', '广西',\
#             '福建', '甘肃', '宁夏', '新疆', '西藏', '海南', '浙江', '青海', '香港', '澳门']
def bs4_2_str(x):
    return str(x).replace('\n','').replace("'","").replace(u'\xa0', u'').replace(' ','')\
    .replace(u'\ufeff','').replace(u'\ue001','').replace(u'\ufffd','').strip()

#获取根据网址得到hmtl
def cx(provin,page1):
    #需要查询的网址
    url = "http://data.api.gkcx.eol.cn/soudaxue/queryschool.html?"
    head = {}
    #模拟google浏览器中的信息，注：更新了浏览器后，此信息有变化，更新了，重新更新了下面所有类容后可以重新模拟翻页功能
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    data = {}
    data['messtype'] = 'json'
    data['province'] = provin
    data['page'] = page1 #页码
    data['size'] = 20
    data['_'] = 1492734878950
#得到data
    data = urllib.parse.urlencode(data).encode('utf-8')
#使用python请求模拟浏览器请求数据
    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    #等到html
    html = response.read().decode('utf-8')
    return html

def jx_json(dmp_uni):
    shools = dmp_uni['school']
    for each_shool in range(len(shools)):
        schoolcode = shools[each_shool]['schoolcode']
        schoolname= shools[each_shool]['schoolname']
        oldname = shools[each_shool]['oldname']
        schoolnature = shools[each_shool]['schoolnature']
        level = shools[each_shool]['level']
        membership  = shools[each_shool]['membership']
        print ('%s|%s|%s|%s|%s|%s'% (schoolcode,schoolname,oldname,schoolnature,level,membership))
for each_pro in province:
    htm = cx(each_pro, 1)
    dmp_uni = json.loads(htm)
    province_university_num = int((dmp_uni['totalRecord']['num']))
    max_page = (province_university_num // 20) + 2
    # jx_json(dmp_uni)
    time.sleep(1)
    for each_page in range(1,max_page):
        htm1 = cx(each_pro, each_page)
        dmp_uni1 = json.loads(htm1)
        jx_json(dmp_uni1)
        time.sleep(1)
