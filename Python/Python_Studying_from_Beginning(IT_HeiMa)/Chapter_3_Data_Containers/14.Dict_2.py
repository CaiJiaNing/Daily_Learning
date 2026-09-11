dict1 = {"小智":675, "李思":608, "李琦":478, "小黑":545, "文韬":429}
print(dict1)

dict1["涛哥"] = 688
print(dict1)

dict1["涛哥"] = 700
print(dict1)

score = dict1.pop("涛哥")
print(score)
print(dict1)

dict1["涛哥"] = 700
print(dict1)

del dict1["涛哥"]
print(dict1)

score = dict1["李思"]
print(score)

score = dict1.get("小智")
print(score)


print(dict1.keys())

print(dict1.values())

print(dict1.items())


for k in dict1.keys():
    print(f"{k}: {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]}: {item[1]}")

for k, v in dict1.items():
    print(f"{k}: {v}")