import cv2
import os
import numpy as np

img = cv2.imread("C:\\Users\\karmi\\OneDrive\\Desktop\\bear.jpg")

img_edge = cv2.Canny(img, 100, 200)
img_edge_dilate = cv2.dilate(img_edge, np.ones((3,3), dtype = np.int8))
img_edge_erode = cv2.erode(img_edge_dilate, np.ones((3,3), dtype = np.int8))

cv2.imshow("img", img_edge)
cv2.imshow("img_dilate", img_edge_dilate)
cv2.imshow("img_erode", img_edge_erode)

cv2.waitKey(0)