# This is a python program used to demonstrate the if() condition judgment process
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

"""
if account == account_user_input:
    if password == password_user_input:
        print("欢迎登陆")
    else:
        print("密码错误")
else:
    print("输入的账号不存在")
"""