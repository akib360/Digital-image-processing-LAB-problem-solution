import cv2 as cv
import numpy as np


img1 = cv.imread('python_logo.jpg')
img2 = cv.imread('opencv_logo.png')

#Image Blending
dst = cv.addWeighted(img1,0.7,img2,0.3,0)

#sub, add, mul
img_add = cv.add(img1,img2)
img_sub = cv.subtract(img1, img2)
img_mul = cv.multiply(img1, img2)

cv.imshow('dst',dst)

cv.imshow('addition',img_add)
cv.imshow('subtraction',img_sub)
cv.imshow('multiplication',img_mul)

cv.waitKey(0)
cv.destroyAllWindows()