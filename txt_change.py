#coding=utf-8
import glob
import os
import glob2
from glob2 import glob

for fn in glob('*.txt'):#Ѱ�ҵ�ǰ�ļ�Ŀ¼�����е�txt�ļ�
    splitName=fn.split(".")
    newName=splitName[0]
    fp = open(fn,'r')
#������������������Ѱ�ұ�ǩ�ļ��µľ�������
    j = 0
    k = 0
#���������б������洢ԭ���ĺ��µ���������
    old_list = [0,0,0,0,0]
    new_list = [0,0,0,0,0]

    for i in range(1,5):#��ȡÿһ����������
        j = k + 2
        k = j + 7

        fp.seek(j)
#    print (fp.read(7))
        old_list[i] = fp.read(8)
        new_list[i] = old_list[i]
    new_list[1] =("%.6f" %(1 - float(new_list[1]) ) )#��Է�ת֮���x����������޸ģ��˴�������ȡ6λС�����������ݸ�ʽһ����
    fp = open( newName+'_flip.txt','w')#�����޸ĺ������
    for i in range(0,5):
        fp.write(str(new_list[i]))
        fp.write(' ')
    fp.close
