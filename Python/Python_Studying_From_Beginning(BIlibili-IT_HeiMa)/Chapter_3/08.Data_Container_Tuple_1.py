"""
Tuple:
    Immutable
"""
tuple1 = ()
tuple1 = tuple()

t1 = (80, 95, 78, 50, 76, 80, 85, 20)
print(t1)
print(type(t1))

print(t1[0])
print(t1[-1])

print(t1[0:5:2])

count_t1 = t1.count(80)
print(count_t1)

idx = t1.index(80)
print(idx)

t2 = (100)
print(type(t2))

t3 = (100,)
print(type(t3))