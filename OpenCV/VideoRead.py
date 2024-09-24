import cv2
import os
import matplotlib.pyplot as plt

video_path = cv2.imread("C:\\Users\\karmi\\OneDrive\\Desktop\\earth.mp4")
video = cv2.VideoCapture(video_path)

ret = True
while ret:
    ret, frame = video.read()
    if ret: 
        cv2.imshow('frame', frame)
        cv2.waitKey(40)