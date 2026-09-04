import sys, os
# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 项目根目录（即 Deep_Learning_from_Scratch 目录）
project_root = os.path.dirname(script_dir)
sys.path.append(project_root)
# sys.path.append(os.pardir)

from dataset import mnist

# (训练图像, 训练标签), (测试图像, 测试标签)
# normalize 是否将输入图像正规化为 0.0-1.0 的值
# flattern 是否展开输入图像(变成一维数组)
# one_hot_label 是否将标签保存为 one-hot 表示
(x_train, t_train), (x_test, t_test) = mnist.load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)
