# OpenCV.py

import os
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("C:\\Users\\karmi\\OneDrive\\Desktop\\bear.jpg")
img_cvted = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_threshold = cv2.threshold(img_cvted, 80, 255, cv2.THRESH_BINARY) # the values here represent that the value of pixels in images below 80 will be taken as 0 and above 80 will be taken as 255

img_threshold = cv2.blur(img_threshold, (10,10)) # removed noise
ret, img_threshold = cv2.threshold(img_threshold, 80, 255, cv2.THRESH_BINARY)

cv2.imshow("image", img_threshold)
cv2.waitKey(0)