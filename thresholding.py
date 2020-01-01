import cv2
import matplotlib.pyplot as plt
# 阈值化

img = cv2.imread(r'./pic/1.jpg')

'''
# (1)
# 二进制阈值化
_, thresh_0 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 反二进制阈值化
_, thresh_1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# 阈值化到零
_, thresh_2 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# 反阈值化到零
_, thresh_3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# 和阈值截断
_, thresh_4 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

images = [img, thresh_0, thresh_1, thresh_2, thresh_3, thresh_4]
fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (13, 13))
for ind, p in enumerate(images):
    ax = axs[ind//3, ind%3]
    ax.imshow(p)
    ax.axis('off')
plt.show()
'''




# (2)
# 自适应阈值化
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Adaptive Thresholding
_, thresh_binary = cv2.threshold(img, thresh = 127, maxval = 255, type = cv2.THRESH_BINARY)
adap_mean_2 = cv2.adaptiveThreshold(img, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 7, 2)
adap_mean_2_inv = cv2.adaptiveThreshold(img, 255,
                                        cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY_INV, 7, 2)
adap_mean_8 = cv2.adaptiveThreshold(img, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 7, 8)
adap_gaussian_8 = cv2.adaptiveThreshold(img, 255,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 7, 8)

images = [img, thresh_binary, adap_mean_2, adap_mean_2_inv,
          adap_mean_8, adap_gaussian_8]
fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (15, 15))
for ind, p in enumerate(images):
    ax = axs[ind%2, ind//2]
    ax.imshow(p, cmap = 'gray')
    ax.axis('off')
plt.show()

