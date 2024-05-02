import cv2
import numpy as np
# def read_m3(path):
cap = cv2.VideoCapture('https://void.greenhosting.ru/Multimania_Mpeg4/index.m3u8')
cap1= cv2.VideoCapture('https://magicstream.ddns.net/magicstream/stream.m3u8')
if not cap.isOpened() or not cap1.isOpened():
    print('Unable to open file')

while True:
    ret,frame1 = cap.read()
    ret1,frame2 = cap1.read()
    # height, width, _ = frame.shape
    # print('first frame size',height, width, _ )
    # height, width, _ = frame1.shape
    # print('second frame size',height, width, _ )
    # print('frame shape [0]',frame.shape[0])
    # print('frame shape [0]',frame.shape[1])
    
    if not ret or not ret1:
        break
    frame2Resized = cv2.resize(frame2,(frame1.shape[1],frame1.shape[0]))
    print('frame2Resized is ',frame2Resized.shape)
    print('frame2 is ',frame2.shape)
    print('frame1 is ',frame1.shape)
    #numpy_vertical = np.vstack((frame1, frame2))
    numpy_horizontal = np.hstack((frame1, frame2Resized))
    #final = cv2.vconcat([frame1, frame2])    
    cv2.imshow("I", numpy_horizontal)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




