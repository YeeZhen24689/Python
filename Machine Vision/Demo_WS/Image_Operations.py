import numpy as np
import cv2

img = cv2.imread('Water_Bottle.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img,(500,1000))

img[55,55] = [255,255,255]
px = img[55,55] # The target values
#print(px)

#ROI = Region of image
img[100:150, 100:150] = [255,255,255]
#print(roi)

#Regions of images
bottle = img[300:700,200:400] # The range for y comes first
img[0:400,0:200] = bottle

cv2.imshow('Bottle',img)
cv2.waitKey(0)
cv2.destroyAllWindows

