import cv2
import numpy as np
img=cv2.resize(cv2.imread('messi.jpg',0),(512,512))
rows,columns=img.shape
# cols-1 and rows-1 are the coordinate limits
M=cv2.getRotationMatrix2D(((columns-1)/2.0,(rows-1)/2.0),90,1)
dst=cv2.warpAffine(img,M,(rows,columns))



cv2.imshow("rotated image",dst)
cv2.imshow("original image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()

