"""
lambda parameters_list: expression
"""

lambda : print("-------------")

lambda x, y: x + y


out_line = lambda : print("-------------")
add = lambda x, y: x + y

out_line()
print(add(100, 200))


# Case 1: Using lambda for printing a line of dashes
def out_line():
    print("-------------")

lambda : print("-------------")

out_line = lambda : print("-------------")
out_line()

# Case 2: Using lambda for addition
def add(x, y):
    return x + y

lambda x, y: x + y

add = lambda x, y: x + y
print(add(100, 200))


# Case 3
data_list = ["C++", "C", "Python", "Java", "JavaScript", "Go", "Rust"]

print(data_list)

data_list.sort()
print(data_list)

data_list.sort(key=lambda x: len(x)) # Sort by length of the string
print(data_list)

data_list.sort(key=lambda x: len(x), reverse=True) # Sort by length of the string in descending order
print(data_list)

data_list.sort(key=lambda x: x[-1]) # Sort by the last character of the string
print(data_list)