import cv2
import numpy as np
import matplotlib.pyplot as plt
# 边缘检测

img = cv2.imread(r'./pic/1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

'''
# (1)边缘检测
edges = cv2.Canny(image=img, threshold1=127, threshold2=127)
plt.figure(figsize=(20, 20))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(edges)
plt.axis('off')
plt.show()
'''



'''
med_val = np.median(img)
lower = int(max(0, .7*med_val))
upper = int(min(255, 1.3*med_val))

img_k5 = cv2.blur(img, ksize = (5, 5))
# 阈值不同的边缘检测
edges_k5 = cv2.Canny(img_k5, threshold1 = lower, threshold2 = upper)
edges_k5_2 = cv2.Canny(img_k5, lower, upper+100)
# 模糊化 ksize = 9
img_k9 = cv2.blur(img, ksize = (9, 9))
# 阈值不同的边缘检测
edges_k9 = cv2.Canny(img_k9, lower, upper)
edges_k9_2 = cv2.Canny(img_k9, lower, upper+100)

images = [edges_k5, edges_k5_2, edges_k9, edges_k9_2]
plt.figure(figsize = (20, 15))
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])
    plt.axis('off')
plt.show()
'''
