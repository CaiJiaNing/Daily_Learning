# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread

# imread = image read
# 读取图片
img = imread('../dataset/lena.png')

# plt.imshow() 用于将二维数组（或图像数据）渲染为可视化图像
plt.imshow(img)

# plt.show() 启动一个GUI事件，打开一个窗口展示图片，并阻塞程序
plt.show()