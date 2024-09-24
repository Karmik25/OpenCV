# OpenCV.py

import os
import cv2
import matplotlib.pyplot as plt

# Use a valid file path
# image_path = os.path.join(r"C:\Users\karmi\OneDrive\Desktop\bear.jpg")
# 
# Read the image using OpenCV
img = cv2.imread("C:\\Users\\karmi\\OneDrive\\Desktop\\bear.jpg")

cv2.imshow("Image", img)
cv2.waitKey(0)