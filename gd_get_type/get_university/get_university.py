# -*- coding: utf-8 -*-
#python3.41
#解析 http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type= 网址
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from bs4 import Tag

def bs4_2_str(x):
    return str(x).replace('\n','').replace("'","").replace(u'\xa0', u'').replace(' ','')\
    .replace(u'\ufeff','').replace(u'\ue001','').replace(u'\ufffd','').strip()

#获取根据网址得到hmtl
def cx(provin):
    #需要查询的网址
    url = "http://gkcx.eol.cn/soudaxue/queryschool.html?&province=%E6%B9%96%E5%8C%97"
    head = {}
    #模拟google浏览器中的信息，注：更新了浏览器后，此信息有变化，更新了，重新更新了下面所有类容后可以重新模拟翻页功能
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    data = {}
    data['province'] = provin
#得到data
    data = urllib.parse.urlencode(data).encode('utf-8')
#使用python请求模拟浏览器请求数据
    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    #等到html
    html = response.read().decode('utf-8')
    return html

# print(cx())
# with open(r'D:\learn_python\gd_get_type\get_university\uni.txt') as txt:
#     print(txt.read())
htm = r'D:\learn_python\gd_get_type\get_university\uni.htm'
soup = BeautifulSoup(htm,"html5lib")
print(soup)
# print (soup.find_all('em'))

# for link in soup.find_all('em'):
#     print(link)
