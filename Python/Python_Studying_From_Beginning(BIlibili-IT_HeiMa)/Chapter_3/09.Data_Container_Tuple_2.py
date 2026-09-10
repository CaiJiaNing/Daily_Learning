"""
Tuple:
    Packing: 将多个值合并到一个容器中
    Unpacking: 将容器解开成独立的元素，分别赋值给多个变量
"""
t = (5, 7, 9, 11)

a, b, c, d = t
x, *y, z = t
s, *o = t
*o, e = t