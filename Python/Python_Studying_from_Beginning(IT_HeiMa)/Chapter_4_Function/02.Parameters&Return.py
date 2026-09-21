def circle_area(r):
    area = 3.14 * r ** 2
    return area

area = circle_area(10)
print(area)

def rectangle_area(l, w):
    area = l * w
    return area

area = rectangle_area(100, 20)
print(area)

def circle_area_len(r):
    area = 3.14 * r ** 2
    length = round(2 * 3.14 * r, 3)
    return area, length

circle = circle_area_len(10)
area, len = circle_area_len(20)

print(circle)
print(type(circle))

print(area, len)