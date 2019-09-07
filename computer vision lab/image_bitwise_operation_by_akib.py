#Image bitwise operation
import cv2
import numpy as np

# Load two images
img1 = cv2.imread('python_logo.jpg')
img2 = cv2.imread('opencv_logo.png')

And=cv2.bitwise_and(img1,img2)
cv2.imshow('AND',And)
cv2.waitKey(0)
Or=cv2.bitwise_or(img1,img2)
cv2.imshow('OR',Or)
cv2.waitKey(0)
Xor=cv2.bitwise_xor(img1,img2)
cv2.imshow('XOR',Xor)
cv2.waitKey(0)
Not=cv2.bitwise_not(img1)
cv2.imshow('NOT',Not)

cv2.waitKey(0)
cv2.destroyAllWindows()