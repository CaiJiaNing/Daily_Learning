# Checking the type of a variable using type()
print("Hello")
print(type("Hello"))  # <class 'str'>

print(type(100))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type(True))  # <class 'bool'>
print(type(False))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>

num = -100
print(type(num))  # <class 'int'>




# Checking the type of a variable using isinstance()
num = 3.14
print(num)
print(isinstance(num,int))  # False
print(isinstance(num,float))  # True


str1 = "Hello" # String literal using double quotes
str2 = 'Python' # String literal using single quotes
str3 = """
Hello.
    欢迎大家进入到Python课程的学习，
    我们将一起学习Python的基础知识。
"""    # Multiline string literal using triple double quotes

print(str1)
print(str2)
print(str3)

print(type(str1))  # <class 'str'>
print(type(str2))  # <class 'str'>
print(type(str3))  # <class 'str'>




# Demonstrating escape characters in strings
msg1 = 'It\'s a beautiful day!'  # Using backslash to escape the single quote
print(msg1)  # Output: It's a beautiful day!

msg2 = "It's a beautiful day!"  # Using double quotes to avoid escaping the single quote
print(msg2)  # Output: It's a beautiful day!

"""
\' -> Represents a single quote character (')
\" -> Represents a double quote character (")
\n -> Represents a newline character
\t -> Represents a tab character
"""

msg3 = "Hello 的意思是\"您好\"" # Using escape characters for double quotes
print(msg3)  # Output: Hello 的意思是"您好"

msg4 = 'hello 的意思是\"您好\"' # Using escape characters for double quotes
print(msg4)  # Output: hello 的意思是"您好"

print("\t欢迎大家进入到Python课程的学习，\n\t我们将一起学习Python的基础知识。")  # Using \n for newline and \t for tab




# Demonstrating string concatenation
slogan = "黑马程序员""成就IT黑马" # Concatenating two string literals without any operator
print(slogan)  # Output: 黑马程序员成就IT黑马

slogan2 = "黑马程序员" + "成就IT黑马" # Concatenating two string literals using the + operator
print(slogan2)  # Output: 黑马程序员成就IT黑马

s1 = "人生苦短"
s2 = "我用Python"

print("吉多·范罗苏姆：" + s1 + s2) # Concatenating string literals with a variable using the + operator

s3 = s1 + s2 # Concatenating two string variables using the + operator
print(s3)  # Output: 人生苦短我用Python

# Case1
name = "C_J_N-"
age = 27
major = "Software Engineering"
hobby = "Badminton, Cycling, Reading, Traveling, and Music"
print("Hello everyone, my name is " + name + ", I am " + str(age) + " years old, my major is " + major + ", and my hobbies include " + hobby + ".") 
# Concatenating string literals with variables of different types using the + operator
# str() is used to convert the integer variable 'age' to a string for concatenation.




# Formatting strings using the % operator
s1 = "C_J_N-"
print("Hello everyone, my name is %s, welcome to the Python course!" % s1) # Using %s as a placeholder for the string variable 's1'

s1 = "人生苦短"
s2 = "我用Python"
print("吉多·范罗苏姆：%s%s" % (s1, s2)) # Using %s as placeholders for the string variables 's1' and 's2'

name = "C_J_N-"
age = 27
major = "Software Engineering"
hobby = "Badminton, Cycling, Reading, Traveling, and Music"
print("Hello everyone, my name is %s, I am %d years old, my major is %s, and my hobbies include %s." % (name, age, major, hobby)) # Using %s as placeholders for string variables and %d as a placeholder for the integer variable 'age'




# Formatting strings using the format() method
name = "C_J_N-"
print(f"Hello everyone, my name is {name}, welcome to the Python course!") # Using f-string for string formatting

s1 = "人生苦短"
s2 = "我用Python"
print(f"吉多·范罗苏姆：{s1}{s2}") # Using f-string for string formatting with variables

name = "C_J_N-"
age = 27
major = "Software Engineering"
hobby = "Badminton, Cycling, Reading, Traveling, and Music"
print(f"Hello everyone, my name is {name}, I am {age} years old, my major is {major}, and my hobbies include {hobby}.") # Using f-string for string formatting with variables of different types    

