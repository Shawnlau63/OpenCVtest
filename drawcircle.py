import cv2
# 绘制圆形操作


def draw_circle(event, x, y, flags, param):
    # 若事件为鼠标左键点击，则画实心圆,flags, param这两个参数必不可少
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=5, color=(87, 184, 237), thickness=-1)
    # 若事件为鼠标右键点击，则画空心圆
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=10, color = (87, 184, 237), thickness=1)

img = cv2.imread(r'./pic/0.jpg')

# 使用cv2.setMouseCallback()函数，在窗口和我们在步骤1中创建的函数draw_circle之间建立一个连接。
cv2.namedWindow(winname='my drawing')# 交互必要步骤
cv2.setMouseCallback('my drawing', draw_circle)

while True:
    cv2.imshow('my drawing', img)
    # 若按esc键，则退出，cv2.waitKey(10)为必须，不然会无法加载图片
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()