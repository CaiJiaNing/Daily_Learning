def greet_user():
    """Function to greet the user."""
    print("Hello! Welcome to our program.")

greet_user()

print("************************************************************")

def greet_user(username):
    # username 是形参
    """显示简单的问候语"""
    print(f"Hello, {username}!")

greet_user("jesse") # jesse 是实参

print("************************************************************")

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')  # 位置实参

describe_pet(animal_type='hamster', pet_name='harry')  # 关键字实参

print("************************************************************")

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie') # 使用默认值
describe_pet(pet_name='willie') # 使用默认值
describe_pet('harry', 'hamster') # 覆盖默认值
describe_pet(pet_name='harry', animal_type='hamster') # 覆盖默认值
describe_pet(animal_type='hamster', pet_name='harry') # 覆盖默认值