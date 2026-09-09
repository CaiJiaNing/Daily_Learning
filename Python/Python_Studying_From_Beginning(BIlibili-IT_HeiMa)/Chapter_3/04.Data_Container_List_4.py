# Case 1
list_user_input = []

for i in range(10):
    user_input = int(input())
    list_user_input.append(user_input)

print(list_user_input)

list_user_input.sort()
print(list_user_input)

print(min(list_user_input))

print(max(list_user_input))

print(sum(list_user_input)/len(list_user_input))



# Case 2
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

num_list1 = num_list1 + num_list2

new_list = []
for num in num_list1:
    if num in new_list:
        continue
    else:
        new_list.append(num)

print(new_list)


result = sorted(set(num_list1 + num_list2))

print(result)
print(type(result))

# Unpacking 解包
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

num_list = [*num_list1, *num_list2]
print(num_list)


# Case 3: 列表推导式
list = []
for i in range(1, 21):
    list.append(i**2)
print(list)

list = [i**2 for i in range(1,21)]
print(list)

num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
new_list = []
for num in num_list:
    if num % 2 == 0:
        new_list.append(num**2)
print(new_list)

new_list = [num**2 for num in num_list if num % 2 ==0]
print(new_list)