import cv2
import numpy as np
from math import floor

infile = r'.\pic\picyq.jpg'
outfile = r'.\pic\picyq1.jpg'

orimg = cv2.imread(infile)
rows, cols, channels = orimg.shape
cv2.imshow('original img', orimg)

# # 剪裁缩放
# cutX = int(0.5 * (cols - 1074))  # 1074=358*3
# cutY = floor(0.5 * (rows - 1323))  # 不支持小数
# img_cropped = orimg[cutY:rows - cutY, cutX:cols - cutX]  # 裁剪坐标为[y0:y1, x0:x1]
# y1, x1 = img_cropped.shape[0:2]  # 剪裁后的尺寸
#
# img = cv2.resize(img_cropped, (int(x1 / 3), int(y1 / 3)))  # 缩放
# cv2.imshow('resize:', img)
# cv2.waitKey()  # 程序显示出图片后将暂停，等待接收一个键盘输入
# cv2.destroyAllWindows()  # 关闭特定窗口

img = cv2.imread(infile)

# 转换hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 色调（H），饱和度（S），明度（V）
lower_blue = np.array([90, 70, 70])
upper_blue = np.array([110, 255, 255])

# 将hsv值位于区间[lower_blue,upper_blue]的部分置为255（白），位于区间外的部分置为0（黑）
mask = cv2.inRange(hsv, lower_blue, upper_blue)  # 黑白图像
cv2.imshow('Mask', mask)

# 腐蚀膨胀，去掉目标外的孤立点
erode = cv2.erode(mask, None, iterations=2)
# cv2.imshow('erode', erode)
dilate = cv2.dilate(erode, None, iterations=2)
dilate = cv2.medianBlur(dilate, 1)
dilate = cv2.GaussianBlur(dilate, (3, 3), 1)


cv2.imshow('dilate', dilate)

# 遍历替换
x2, y2 = dilate.shape[0:2]
for i in range(x2):
    for j in range(y2):
        if dilate[i, j] == 255:  # 背景部分为255（白）
            img[i, j] = (0, 0, 255)#此处替换颜色，为BGR通道
            img[i, j] = (255, 255, 255)
cv2.imshow('res', img)
cv2.imwrite(outfile, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
