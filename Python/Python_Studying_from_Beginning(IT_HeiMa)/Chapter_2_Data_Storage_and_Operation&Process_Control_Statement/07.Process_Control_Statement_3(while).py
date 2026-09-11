# Loop control statement(while-else loop)
i = 0
while i < 10:
    print("人生苦短，我用Python")
    i += 1
else:
    print("循环正常结束，执行else代码块")

# Case 1
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 2
print("0-100之间的偶数和为：", sum)

i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print("0-100之间的偶数和为：", sum)
