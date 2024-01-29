import cv2
import numpy as np

image = cv2.imread('Day8/image.jpeg')
print(image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

edges = cv2.filter2D(gray_image, -1, kernel)

cv2.imshow('original image', gray_image)
cv2.imshow('edge detection', edges)
cv2.waitKey(0)
