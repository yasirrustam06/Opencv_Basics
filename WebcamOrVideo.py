import cv2

cap = cv2.VideoCapture(0)  # For 0 means It will open webcam  Also video.mp4 It will opencv the video

while True:
    ret,img = cap.read()
    cv2.imshow("Image",img)
    cv2.waitKey(1)
