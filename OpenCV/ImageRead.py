# OpenCV.py

import os
import cv2
import matplotlib.pyplot as plt

# Use a valid file path
# image_path = os.path.join(r"C:\Users\karmi\OneDrive\Desktop\bear.jpg")
# 
# Read the image using OpenCV
img = cv2.imread("C:\\Users\\karmi\\OneDrive\\Desktop\\bear.jpg")

# Convert the image from BGR (OpenCV format) to RGB (Matplotlib format)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off')
plt.show()