"""
    break：Break out of the current loop
    continue：Skip the rest of the code inside the loop for the current iteration only
    pass：Do nothing, acts as a placeholder
"""
user1 = {"username": "admin", "password": "666888"}
user2 = {"username": "zhangsan", "password": "123456"}
user3 = {"username": "taoge", "password": "888666"}
list_users = [user1, user2, user3]

while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    for user in list_users:
        if username == user["username"] and password == user["password"]:
            print("登录成功！")
            break
    else:
        print("用户名或密码错误，请重新输入！")
        continue
    break