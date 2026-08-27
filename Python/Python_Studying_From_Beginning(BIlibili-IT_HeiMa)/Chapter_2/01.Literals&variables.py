# This is a simple Python program that demonstrates literals and variables.
print(100)  # int
print(3.14)  # float
print(True)  # bool
print(False)  # bool
print("Hello, World!")  # str
print("-------------")  # str
print(None)  # NoneType

# Demonstrate arithmetic operations with boolean values
print(True + 1)  # True is treated as 1
print(False - 1)  # False is treated as 0

# Demonstrate variable assignment and usage
# Python is a dynamically typed language, so variables can change types.
num = 1114.1 # Assigning a float value to the variable 'num'
print(num) # Printing the value of 'num'

num = num + 1 # Incrementing the value of 'num' by 1
print(num) # Printing the updated value of 'num'

num = 'OK' # Assigning a string value to the variable 'num'
print(num) # Printing the value of 'num'

num = True # Assigning a boolean value to the variable 'num'
print(num) # Printing the value of 'num'

# Case 1
amount_of_play = 20.7
increment = 50
for i in range(2):
    amount_of_play += increment
    print(f"Amount of play after {i+1}-month: {amount_of_play}")  # Printing the updated value of 'amount_of_play' after each increment    

# Case 1-update
amount_of_play, increment = 20.7, 50 # Assigning values to 'amount_of_play' and 'increment' in a single line
for i in range(2):
    amount_of_play += increment
    print(f"Amount of play after {i+1}-month: {amount_of_play}")  # Printing the updated value of 'amount_of_play' after each increment    


# Swapping values of two variables
a, b = 10, 20 # Assigning values to 'a' and 'b' in a single line
print(a, b) # Printing the values of 'a' and 'b'
c = a
a = b
b = c
print(a, b) # Printing the values of 'a' and 'b' after swapping