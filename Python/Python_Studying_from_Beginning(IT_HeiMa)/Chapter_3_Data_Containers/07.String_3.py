# Case 1: Palindrome string
user_input= input()
flag = False

if user_input == user_input[::-1]:
    flag = True

print(flag)

# Case 2
user_input = input()

user_input_reversed = user_input[::-1]

user_input_reversed_upper = user_input_reversed.upper()

l = list(user_input_reversed_upper)
print(l)