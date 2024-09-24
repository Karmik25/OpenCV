#using a handwritten img to clearly understand-  this is an image which has no global value for threshold

import cv2
import os

img = cv2.imread("C:\\Users\\karmi\\OneDrive\\Desktop\\handwritten.png")
img_cvted = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_thresh = cv2.adaptiveThreshold(img_cvted, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
ret, simple_thresh = cv2.threshold(img_cvted, 80, 255, cv2.THRESH_BINARY)
 
cv2.imshow('img', adaptive_thresh)
cv2.imshow('simple_thresh', simple_thresh)

cv2.waitKey(0)

