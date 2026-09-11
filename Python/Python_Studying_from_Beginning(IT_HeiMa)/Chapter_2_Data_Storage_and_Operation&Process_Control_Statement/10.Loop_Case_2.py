"""
    random.randint(a, b)  # Return a random integer N such that a <= N <= b. 
"""
import random
random_number = random.randint(1, 100)  # Generate a random integer between 1 and 100
user_guess = int(input("请输入你猜测的数字（1-100）："))  # Prompt the user to guess the number
while user_guess != random_number:  # Continue looping until the user guesses the correct number
    if user_guess < random_number:  # If the guess is less than the random number
        print("你猜的数字小了，请重新输入！")  # Inform the user that their guess is too low
    else:  # If the guess is greater than the random number
        print("你猜的数字大了，请重新输入！")  # Inform the user that their guess is too high
    user_guess = int(input("请输入你猜测的数字（1-100）："))  # Prompt the user to guess again
print("恭喜你，猜对了！")  # Inform the user that they have guessed correctly