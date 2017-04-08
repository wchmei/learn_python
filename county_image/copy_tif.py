# -*- coding: utf-8 -*-
'''
拷贝tif文件到硬盘
'''
import shutil,glob,os,time
# 要查找tif文件的目录
old_dir = r'E:\image\20170324_image\山东省\*\*\*.tif'
old_path = r'E:\image\20170324_image'
# 要拷贝文件的新目录
new_path = r'F:\image\city_image0329'
# 查找每个需要拷贝的文件
for filename in glob.glob(old_dir):
    # print(filename)
    begintime = time.perf_counter()
    # 替换得到新的文件
    new_file = filename.replace(old_path,new_path)
    # 替换得到新的文件目录
    new_dir = os.path.dirname(new_file)
    # 文件不存在就生成新目录
    if os.path.isdir(new_dir) == False:
        print(new_dir)
        # 递归创建多层目录
        os.makedirs(new_dir)
        # 拷贝文件
    shutil.copyfile(filename,new_file)
    endtime = time.perf_counter()
    costtime = endtime - begintime
    print(new_file,costtime)

