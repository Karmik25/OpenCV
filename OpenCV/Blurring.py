import cv2
img = cv2.imread("C:\\Users\\karmi\\OneDrive\\Desktop\\bear.jpg")

k_size = 7  # blurring capacity,  more the value, more the image will be blur

img_blur1 = cv2.blur(img, (k_size,k_size))
img_GaussianBlur = cv2.GaussianBlur(img, (k_size, k_size), 3)
img_medianBlur = cv2.medianBlur(img, k_size)

cv2.imshow('img',img_medianBlur)
cv2.waitKey(0)