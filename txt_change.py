#coding=utf-8
import glob
import os
import glob2
from glob2 import glob

for fn in glob('*.txt'):#寻找当前文件目录下所有的txt文件
    splitName=fn.split(".")
    newName=splitName[0]
    fp = open(fn,'r')
#定义两个变量，用来寻找标签文件下的具体数据
    j = 0
    k = 0
#定义两个列表，用来存储原来的和新的坐标数据
    old_list = [0,0,0,0,0]
    new_list = [0,0,0,0,0]

    for i in range(1,5):#读取每一个坐标数据
        j = k + 2
        k = j + 7

        fp.seek(j)
#    print (fp.read(7))
        old_list[i] = fp.read(8)
        new_list[i] = old_list[i]
    new_list[1] =("%.6f" %(1 - float(new_list[1]) ) )#针对翻转之后的x的坐标进行修改，此处对数据取6位小数，保持数据格式一致性
    fp = open( newName+'_flip.txt','w')#保存修改后的数据
    for i in range(0,5):
        fp.write(str(new_list[i]))
        fp.write(' ')
    fp.close
