# Match statement is a new feature in Python 3.10, which is similar to switch-case statements in other languages. It allows for more readable and maintainable code when dealing with multiple conditions.
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

# Case 1
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