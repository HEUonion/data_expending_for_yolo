
import cv2

vc = cv2.VideoCapture('./VID_20190410_201559.mp4')#视频文件路径
c = 1

if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False

timeF = 4 #视频帧数计数间隔频率

while rval:
    rval , frame = vc.read()
    if(c%timeF == 0):
        cv2.imwrite('./' + '20190410_201559-' + str(c) + '.jpg',frame)
    c += 1
    cv2.waitKey(1)
vc.release()