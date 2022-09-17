import cv2
import numpy as np

img=cv2.resize(cv2.imread("messi.jpg",0),(512,512))
rows,colm=img.shape
 # creat the matrix and specify the new coordinates
M=np.float32([[1,0,100],[0,1,50]])
dst=cv2.warpAffine(img,M,(rows,colm))
cv2.imshow("transformed image",dst)
cv2.imshow("original image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


























