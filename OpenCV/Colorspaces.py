import cv2
import os

img = cv2.imread("C:\\Users\\karmi\\OneDrive\\Desktop\\bear.jpg")

img_cvted = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img',img_cvted)
cv2.waitKey(0)