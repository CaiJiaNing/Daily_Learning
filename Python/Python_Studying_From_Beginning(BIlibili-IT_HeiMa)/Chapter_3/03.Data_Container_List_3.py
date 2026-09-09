s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

s.append(10000)
print(s)

s.insert(3,500)
print(s)

s.remove(1)
print(s)

s.sort()
print(s)

s.sort(reverse=True)
print(s)

sorted(s)

s.reverse()
print(s)