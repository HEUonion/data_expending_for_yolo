
import cv2

vc = cv2.VideoCapture('./VID_20190410_201559.mp4')#��Ƶ�ļ�·��
c = 1

if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False

timeF = 4 #��Ƶ֡���������Ƶ��

while rval:
    rval , frame = vc.read()
    if(c%timeF == 0):
        cv2.imwrite('./' + '20190410_201559-' + str(c) + '.jpg',frame)
    c += 1
    cv2.waitKey(1)
vc.release()