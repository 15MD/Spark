import cv2
import numpy as np 


cap1 = cv2.VideoCapture('C:/Users/10694387/Downloads/index.m3u8')
#cap1 = cv2.VideoCapture('C:/Users/10694387/Downloads/sample_960x540.mp4')
cap2 = cv2.VideoCapture('C:/Users/10694387/Downloads/stream.m3u8')
#cap2 = cv2.VideoCapture('C:/Users/10694387/Downloads/SampleVideo_1280x720_1mb.mp4')
while cap1.isOpened() or cap2.isOpened():

    okay1  , frame1 = cap1.read()
    okay2 , frame2 = cap2.read()

    if okay1:
        hsv1 = cv2.cvtColor(frame1 , cv2.COLOR_BGR2HSV)
        cv2.imshow('fake' , hsv1)

    if okay2:
        hsv2 = cv2.cvtColor(frame2 , cv2.COLOR_BGR2HSV)
        cv2.imshow('real' , hsv2)

    if not okay1 or not okay2:
        print('Cant read the video , Exit!')
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.waitKey(1)

cap1.release()
cap2.release()
cv2.destroyAllWindows()