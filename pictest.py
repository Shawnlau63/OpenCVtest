import numpy as np
import matplotlib.pyplot as plt
import cv2
# 基本操作

# 读取图片
img = cv2.imread(r'./pic/0.jpg')

# 绘制矩形
cv2.rectangle(img, pt1=(100, 100), pt2=(400, 400), color=(255, 255, 0),thickness=3)

# 绘制圆形
cv2.circle(img, center=(250, 250), radius=150, color=(0, 255, 255), thickness=3)

# 添加文字
cv2.putText(img, text='dogge', org=(250, 250), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.5, color=(0, 255, 0), thickness=3, lineType=cv2.LINE_AA)

# 展示图片
cv2.imshow('img', img)

# 窗口等待
cv2.waitKey(5000)
# 关闭窗口
cv2.destroyAllWindows()

# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img', img_rgb)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()
