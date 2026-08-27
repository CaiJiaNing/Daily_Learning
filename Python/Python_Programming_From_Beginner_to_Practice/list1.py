bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[-1])

print(bicycles[0:2])
print(bicycles[0:3:2])

print("***************************************************")

motorcycles1 = ['honda','yamaha','suzuki']
print(motorcycles1[0])
motorcycles1[0] = 'ducati'
print(motorcycles1)

print("***************************************************")

motorcycles2 = ['honda','yamaha','suzuki']
print(motorcycles2)
motorcycles2.append('ducati')
print(motorcycles2)

print("***************************************************")

motorcycles3 = ['honda','yamaha','suzuki']
print(motorcycles3)
motorcycles3.insert(0,'ducati')
print(motorcycles3)

print("***************************************************")

motorcycles4 = ['honda','yamaha','suzuki']
print(motorcycles4)
del motorcycles4[0]
print(motorcycles4)

print("***************************************************")

motorcycles5 = ['honda','yamaha','suzuki']
print(motorcycles5)
poped_motorcycles5 = motorcycles5.pop()
print(poped_motorcycles5)
print(motorcycles5)

print("***************************************************")

motorcycles6 = ['honda','yamaha','suzuki']
print(motorcycles6)
poped_motorcycles6 = motorcycles6.pop(0) # 弹出栈底元素
print(poped_motorcycles6)
print(motorcycles6)

print("***************************************************")

motorcycles7 = ['honda','yamaha','suzuki','suzuki','ducati']
print(motorcycles7)
motorcycles7.remove('suzuki') # 移除第一个值匹配元素
print(motorcycles7)

print("***************************************************")

cars1 = ['bmw','audi','toyota','subaru']
print(cars1)
cars1.sort() # 按字母升序排列，永久生效
print(cars1)

print("***************************************************")

cars2 = ['bmw','audi','toyota','subaru']
print(cars2)
cars2.sort(reverse = True) # 按字母降序排列，永久生效
print(cars2)

print("***************************************************")

cars3 = ['bmw','audi','toyota','subaru']
print(cars3)
print(sorted(cars3)) # 按字母升序排列，临时
print(cars3)
print(sorted(cars3,reverse = True)) # 按字母降序排列，临时

print("***************************************************")

cars4 = ['bmw','audi','toyota','subaru']
print(cars4)
cars4.reverse() # 反转列表，永久生效
print(cars4)

print(len(cars4)) # 列表长度