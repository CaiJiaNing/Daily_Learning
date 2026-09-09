"""
    list_name = [element1, element2, element3, ...]
    Different types of data can be stored in a list, and the elements can be of different types.
    Elements in a list are ordered and can be accessed by their index, starting from 0.
    Lists are mutable, meaning you can change their content without changing their identity.
"""
s = [56, 90, 88, 65, 90, "A", "Hello", True]

print(type(s))  # type() 


print(s[0])
print(s[-(len(s))])
print(s[-8])

s[5] = "B"
print(s[5])

print(s)
del s[6]
print(s)

peak = s.pop()
print(peak)
print(s)

s.append("CJN")
print(s)

for item in s:
    print(item)