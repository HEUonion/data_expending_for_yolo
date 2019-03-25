import cv2
from glob2 import glob

for fn in glob('*.jpg'): #确认文件格式
    img=cv2.imread(fn)
    horizontal_img=cv2.flip(img,1)
    splitName=fn.split(".")
    newName=splitName[0]
    cv2.imwrite(newName+'_flip.jpg',horizontal_img)
