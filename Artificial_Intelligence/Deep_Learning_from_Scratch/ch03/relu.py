# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)

# ylim() 设置或获取Y轴显示范围
plt.ylim(-1.0, 5.5)
plt.show()
