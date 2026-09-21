num = 100
num2 = 400
def circle_area(r):
    pi = 3.14
    area = pi * r ** 2

    num = 100000
    print(num)

    global num2
    num2 = 500000
    print(num2)

    return area

count = 0
print("num =", num)
c_area = circle_area(10)
print(c_area)

print(num)
print(num2)
