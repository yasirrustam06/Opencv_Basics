import cv2
img = cv2.imread("image.jpeg")
cv2.imwrite("Save_Image.png", img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
