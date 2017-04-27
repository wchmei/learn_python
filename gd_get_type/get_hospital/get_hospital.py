# -*- coding: utf-8 -*-
#python3.41
#解析 http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type= 网址
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
from bs4 import Tag
import time
# province1 = ['21508']  #新疆生产建设兵团
# province2 = range(7180,7241,2)
# province = province1 + province2

provinces = {7180	:	'北京市',7182	:	'天津市',
7184	:	'河北省',7186	:	'山西省',
7188	:	'内蒙古自治区',7190	:	'辽宁省',
7192	:	'吉林省',7194	:	'黑龙江省',
7196	:	'上海市',7198	:	'江苏省',7200	:	'浙江省',
7202	:	'安徽省',7204	:	'福建省',
7206	:	'江西省',7208	:	'山东省',
7210	:	'河南省',7212	:	'湖北省',
7214	:	'湖南省',7216	:	'广东省',7218	:	'广西壮族自治区',
7220	:	'海南省',7222	:	'重庆市',
7224	:	'四川省',7226	:	'贵州省',
7228	:	'云南省',7230	:	'西藏自治区',
7232	:	'陕西省',7234	:	'甘肃省',
7236	:	'青海省',7238	:	'宁夏回族自治区',
7240	:	'新疆维吾尔族自治区',
21508	:	'新疆生产建设兵团'
}

def bs4_2_str(x):
    return str(x).replace('\n','').replace("'","").replace(u'\xa0', u'').replace(' ','')\
    .replace(u'\ufeff','').replace(u'\ue001','').replace(u'\ufffd','').strip()

#获取根据网址得到hmtl
def cx(provin):
    #需要查询的网址
    url = "https://www.hqms.org.cn/usp/roster/rosterInfo.jsp?"
    head = {}
    #模拟google浏览器中的信息，注：更新了浏览器后，此信息有变化，更新了，重新更新了下面所有类容后可以重新模拟翻页功能
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    data = {}
##    data['messtype'] = 'json'
    data['provinceId'] = provin
    # & htype = & hgrade = & hclass = & hname = &
    data['htype'] =''
    data['hgrade'] = ''
    data['hclass'] =''
    data['hname'] = ''
    # data['page'] = page1 #页码
    # data['size'] = 20
    data['_'] = 1493113481101
#得到data
    data = urllib.parse.urlencode(data).encode('utf-8')
#使用python请求模拟浏览器请求数据
    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    #等到html
    html = response.read().decode('utf-8')
    return html

def jx_json(hospitals):
    # hospitals = dmp_uni['school']
    for hospital in range(len(hospitals)):
        provinceIds = provinces[hospitals[hospital]['provinceId']]
        hName= hospitals[hospital]['hName']
        hGrade = hospitals[hospital]['hGrade']
        hType = hospitals[hospital]['hType']
        # level = shools[each_shool]['level']
        # membership  = shools[each_shool]['membership']
        print ('%s|%s|%s|%s'% (provinceIds,hName,hGrade,hType))
for each_pro in provinces:
    htm = cx(each_pro)
    dmp_uni = json.loads(htm)
    jx_json(dmp_uni)
    time.sleep(1)
    # province_university_num = int((dmp_uni['totalRecord']['num']))
    # max_page = (province_university_num // 20) + 2
    # jx_json(dmp_uni)
    # time.sleep(1)
    # for each_page in range(1,max_page):
        # htm1 = cx(each_pro, each_page)
        # dmp_uni1 = json.loads(htm1)
        
        # time.sleep(1)
