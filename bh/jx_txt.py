# -*- coding: utf-8 -*-
#python2.7
import json,sys  
reload(sys)  
sys.setdefaultencoding('utf8')
# 实际要提取出来的字段
ziduans =['shineRange','faultCause','maintainCount','mapId','mapX','mapY','pageSize','cameraManfac', 'availgisChannelList',
 'cameraModel','sn','deviceType','unitType','state','supportViewDomain',
 'channelNum','hdFlag','type','unitSeq','sort','minMapX','targetType',
 'manufacture','location','carNum','userId','id','name','maxMapY',
 'defenseLineStr','minMapY','direction','channelClass','shineDistance',
 'presetPoint','shineAngle','maxMapX','installDate','radiateType'	,
 'deviceCode','org','channelId','orgName','currentPage']
#  输入的json格式路径
inpath = r'D:\learn_python\bh\公安视频点坐标.txt'
# 输出路径
outpath = r'D:\learn_python\bh\video.txt'
uipath = unicode(inpath,"utf-8")
with open(uipath) as txt:
    # txt_points = txt.readlines()
    # # 将txt转换为json
    data = json.load(txt)
    for each_poi in data:
        for each_ziduan in ziduans:
            if each_poi[each_ziduan] == None:
                each_poi[each_ziduan] = ''
            with open (outpath,'a') as new_txt:
                new_txt.write('%s|' %(each_poi[each_ziduan]))
        with open (outpath,'a') as new_txt:
            new_txt.write('\n')




