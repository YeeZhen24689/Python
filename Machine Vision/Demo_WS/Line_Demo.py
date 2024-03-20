import numpy as np
import cv2

img = cv2.imread('Sleepyhead.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img,(250,450))

cv2.line(img,(0,0),(150,150),(255,255,255),15) #B G R
#        targ,start,end     ,ColorCode_BGR,l_width

cv2.rectangle(img,(100,100),(200,150),(0,255,0),2)
#             targ,topleftcor,bottomrightcor,ColorCode_BGR,l_width

cv2.circle(img,(150,300),50,(255,255,255),-1)

pts = np.array([[10,5],[23,4],[56,6],[200,300],[40,5]],np.int32)
pts = pts.reshape((-1,1,2))

cv2.polylines(img,[pts],True,(255,0,0),5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV TEXT!',(0,130),font,1,(255,255,0),1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()