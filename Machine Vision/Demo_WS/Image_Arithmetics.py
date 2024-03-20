import numpy as np
import cv2

img1 = cv2.imread('Sleepyhead.jpg')
img1 = cv2.resize(img1,(62,125))
img2 = cv2.imread('Water_Bottle.jpg')
img2 = cv2.resize(img2,(250,500))

#add = img1 + img2
#add = cv2.add(img1,img2)

#weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)
#(target1,weight,target2,weight)

rows,cols,channels = img1.shape
roi = img2[0:rows,0:cols]

img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,150,255,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask) # Bitwise is 

img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img1_fg = cv2.bitwise_and(img1,img1, mask=mask)

dst = cv2.add(img2_bg, img1_fg)
img2[0:rows,0:cols] = dst

cv2.imshow("res",img2)
cv2.imshow("mask_inv",mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

#CHALLENGE TAKE AN IMAGE WITH A BLACK BACKGROUND AND SUPERIMPOSE IT WITH ANOTHER BIGGER IMAGE SO IT HAS NO BACKGROUND#