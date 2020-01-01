import os
import cv2
import numpy as np

'''
img = cv2.imread(r'D:\GraA&Q\OpenCVtest\pic\0.jpg', 0)  # 灰度图
img = cv2.imread(r'D:\GraA&Q\OpenCVtest\pic\0.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)
'''

img1 = np.empty((500, 500, 3), np.int8)
img1[..., 0] = 255
img1[..., 1] = 0
img1[..., 2] = 0

# img1 = img1[:, :, ::-1]
cv2.imshow('img1', img1)
cv2.waitKey(0)
