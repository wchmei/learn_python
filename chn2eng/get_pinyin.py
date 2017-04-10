# coding:utf-8
# python2.7拼音转换

import json,re
import sys

reload(sys)
sys.setdefaultencoding('Gb18030')

# 指定字典
# 可以更换带注音的字典，格式为 “UTF-8编号”：“拼音注音”
dict_f = u'Pinyin.json'

# 去掉括号里面的内容
def th_zf(strs):
    # 将 () 英文括号 替换为 （） 中文括号
    strs = strs.replace(u'（',u'(').replace(u'）',u')').replace(u'、',u'').replace(u' ',u'')
    a1 = re.compile('\(.*?\)')
    txt = a1.sub('',strs)
    return txt
# json转字典
with open(dict_f, 'r') as flo:
    dict_js = json.loads(flo.read())

# 转换函数 将 数据组 转换为 ShuJuZu
def title(strs):
    strs = th_zf(strs)
    pinyin = []
    try:
        for i in strs:
            idx = ord(i)
            k = str(hex(idx))
            k = k.replace('0x', '').upper()
            py = dict_js[k].split(' ')[0][:-1].title()
            pinyin.append(py)
        return ''.join(pinyin)
    except Exception:
        return strs.replace(' ', '')
# 转换函数 将 数据组 转换为 sjz
def shortname(strs):
    strs = th_zf(strs)
    pinyin = []
    try:
        for i in strs:
            idx = ord(i)
            k = str(hex(idx))
            k = k.replace('0x', '').upper()
            py = dict_js[k].split(' ')[0][:1].lower()
            pinyin.append(py)
        return ''.join(pinyin)
    except Exception:
        return strs.replace(' ', '')

if __name__ == '__main__':
    test_t = u'北海市农业局(市林业局、市扶贫办)'
    print th_zf(test_t)
    print title(test_t)
    print shortname(test_t)
