"""
Set:
    Automatic deduplication
    Disordered, non-repeatable and modifiable
"""
s1 = {"C", "D", "X", "T", "O", "U"}
s2 = set()
# s3 = {}  s3 是字典

s3 = {5, 3, 2, 0, 9, 12, 43, 64, 22, 5, 0}
print(s3)
print(type(s3))


s1 = {100, 200, 300, 400, 500, 600, 700, 800}
print(s1)

s1.add(1200)
print(s1)

s1.remove(200)
print(s1)

e = s1.pop()
print(e)
print(s1)

s1.clear


s2 = {"A", "B", "C", "D", "E", "X", "Y"}
s3 = {"C", "E", "Y", "Z"}

print(s2.difference(s3))
print(s3.difference(s2))

print(s2.union(s3))
print(s3.union(s2))

print(s2.intersection(s3))
print(s3.intersection(s2))