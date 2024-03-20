import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Water_Bottle.jpg',cv2.IMREAD_GRAYSCALE) # -> 0
#IMREAD_COLOR -> 1
#IMREAD_UNCHANGED -> -1

imgplus = cv2.resize(img,(500,1000)) 

cv2.imshow('Image',imgplus)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img,cmap='gray',interpolation='bicubic')
#plt.plot([50,100],[80,3000],'c',linewidth = 5)
#plt.show()

cv2.imwrite('BottleRed.jpg',img)