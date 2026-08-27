# Using input() to collect data from keyboard
name = input("请输入您的姓名：")  # Prompting the user to input their name
age = input("请输入您的年龄：") # Prompting the user to input their age
print(f"您的姓名是{name}，年龄为：{age}")  # Greeting the user with their name

# Case 1
total = 10000

password = input("请输入您的银行卡密码：")
print(f"密码正确，{password}")

num = input("请输入您的取款金额：")
print(f"取款后银行卡余额为：{total - int(num)}")