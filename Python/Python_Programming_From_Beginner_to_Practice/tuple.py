dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250
# tuple 元组 定义后不可修改

print("************************************************************")

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

print("************************************************************")

dimensions = (400,100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)

print("************************************************************")