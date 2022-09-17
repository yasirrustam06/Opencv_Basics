import cv2
img = cv2.imread("image.jpeg")
Gray_Image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
RGB_Image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
