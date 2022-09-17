import cv2
import matplotlib.pyplot as plt
img=cv2.imread("box.png")

# cv2.imshow("image",img)
# draw simple line
lined_img=cv2.line(img,(0,0),(200,200),(0,0,255),5)
# cv2.imshow("lined_img",lined_img)

# draw arrowed line
arrow_lined=cv2.arrowedLine(img,(0,0),(100,100),(255,0,0),10)
# cv2.imshow("arrow_lined",arrow_lined)


# draw rectangle
draw_rect=cv2.rectangle(img,(50,50),(100,100),(0,2555,0),5)
# cv2.imshow("draw_rect",draw_rect)



#draw circle

draw_circle=cv2.circle(img,(200,100),50,(0,0,0),5)
font=cv2.FONT_ITALIC
cv2.putText(draw_circle,"opencv_python",(50,50),font,1,(0,0,0),5)
# cv2.imshow("draw_circle",draw_circle)




images=[img,lined_img,draw_rect,draw_circle]
titles=["image","lined_img","draw_rect","draw_circle"]
count=4
for i in range(count):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


