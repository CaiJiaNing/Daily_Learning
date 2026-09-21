"""
位置参数：调用函数时根据函数定义时的位置传递参数

调用函数时参数顺序与定义函数时参数顺序完全一致

"""
def reg_stu(name, age, gender, city):
    print(f"姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city":city}

stu1 = reg_stu("张三", 18, "男", "北京")
print(stu1)

"""
关键字参数：调用函数时以函数定义时形参名称作为关键字，以“键 = 值”的形式传递参数（不要求顺序）
"""
stu2 = reg_stu(name="张三", age=18, gender="男", city="北京")
print(stu2)

stu3 = reg_stu(gender="男", name="王武", city="上海", age=22)
print(stu3)

"""
!!! 位置参数和关键字参数混用，关键字参数必须在位置参数之后 !!!
"""
stu4 = reg_stu("赵四", 28, gender="男", city="上海")
print(stu4)


"""
默认参数（缺省参数），为参数提供默认值
调用函数时，可以不传递有默认值的参数

默认参数必须放在没有默认值的参数列表之后
"""
def reg_stu2(name, age, gender, city="北京"):
    print(f"姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city":city}

stu5 = reg_stu2("张三", 18, "男")
print(stu5)

stu6 = reg_stu2("李四", 22, "男", "深圳")
print(stu6)
