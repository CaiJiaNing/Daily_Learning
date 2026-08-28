# This are some Python programs used to demonstrate the if / if-else / if-elif-else condition judgment process
score = 700
if score >= 680:
    print("欢迎你来清华读书")
    print("也恭喜你即将开始精彩的大学生活")
print("---------------------------------")

# Case 1
account = "CJN1999"
password = "990608"

account_user_input = input("请输入账号：")
password_user_input = input("请输入密码：")

if account == account_user_input and password == password_user_input:
    print("欢迎登陆")
if account != account_user_input or password != password_user_input:
    print("账号或密码输入错误")


if account == account_user_input and password == password_user_input:
    print("欢迎登陆")
else:
    print("账号或密码输入错误")

"""
if account == account_user_input:
    if password == password_user_input:
        print("欢迎登陆")
    else:
        print("密码错误")
else:
    print("输入的账号不存在")
"""

# Case 2
year_user_input = int(input("请输入需要判定的年份："))

if (year_user_input % 100 != 0 and year_user_input % 4 == 0) or (year_user_input % 400 == 0):
    print(f"{year_user_input}是闰年")
else:
    print(f"{year_user_input}是平年")




num_user_input = int(input("请输入数字："))
if num_user_input > 0:
    print(f"{num_user_input}是正数")
elif num_user_input < 0:
    print(f"{num_user_input}是负数")
else:
    print(f"{num_user_input}是0")

# Case 3
username = input("请输入用户名：")
password = input("请输入密码：")

if username == "admin" and password == "666888":
    print("登陆成功")
elif username == "root" and password == "547527":
    print("登陆成功")
elif username == "张三" and password == "123456":
    print("登陆成功")
else:
    print("登陆失败，用户名或密码错误")




# Pattern matching
day = input("请输入星期几(1-7):")
match day:
    case "1":
        print("周一")
    case "2":
        print("周二")
    case "3":
        print("周三")
    case "4":
        print("周四")
    case "5":
        print("周五")
    case "6" | "7": # | means or
        print("周末")

    case _:     # If none of the previous cases match, the default case _ will be executed
        print("输入错误")

# Case 3
num1 = float(input("请输入第一个数:"))
num2 = float(input("请输入第二个数:"))
oper = input("请输入运算符(+ - * /):")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作不支持")