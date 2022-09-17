import cv2
import numpy as np

img=np.zeros((1024,1024,3),dtype='float32')

def draw(event,x,y,flags,param):
    if cv2.EVENT_RBUTTONDOWN:
        cv2.line(img,(x,y),(x+2,y+2),(255,0,0),5,None)

cv2.namedWindow('mywindow')
cv2.setMouseCallback('mywindow',draw)
while True:
    cv2.imshow("mywindow",img)


    if cv2.waitKey(9)==239:
        break


cv2.destroyAllWindows()

