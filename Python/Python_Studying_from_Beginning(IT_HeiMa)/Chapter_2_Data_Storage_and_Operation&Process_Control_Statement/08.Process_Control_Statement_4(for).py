# # Loop control statement(for-else loop)
"""
for循环语句的格式：
    for 变量 in 可迭代对象(待处理的数据集):
        循环体
    else:
        循环结束时，执行的代码
"""
msg = "Hello-Python"
for i in msg:
    print(i)
else:
    print("遍历结束后执行的代码块")

msg = input("请输入一个需要遍历的字符串：")
for s in msg:
    print(f"元素：{s}")
else:
    print("遍历结束后执行的代码块")

# Case 1
total = 0
for i in range(101):
    if i % 2 == 1:
        total += i
else:
    print(f"0-100之间的奇数和为：{total}")

# Case 2
total = 0
for i in range(100, 501):
    if i % 3 == 0:
        total += i
else:
    print(f"100-500之间3的倍数的数字之和为：{total}")

"""
range()函数的使用：
    range()函数可以生成一个整数序列，常用于for循环中。
    语法：
        range(stop)  # 生成从0到stop-1的整数序列
        range(start, stop)  # 生成从start到stop-1的整数序列
        range(start, stop, step)  # 生成从start到stop-1，步长为step的整数序列
"""



# Nested loop
"""
嵌套循环：
    在一个循环体中嵌套另一个循环体，称为嵌套循环。

    for 元素 in 可迭代对象1:
        循环体的代码1
        循环体的代码2

        for 元素 in 可迭代对象2:
            循环体的代码1
            循环体的代码2
"""
m = int(input("请输入长方形的长度："))
n = int(input("请输入长方形的宽度："))
for i in range(m):
    for j in range(n):
        print("*", end="")
    print()  # end-of-line

# Case 3
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}", end="\t")
    print()  # end-of-line