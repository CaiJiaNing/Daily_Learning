magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}\n")
print("Thank you, everyone. That was a great magic show!")

print("************************************************************")

for value in range(1,5): # range(a,b,c) 从a到b-1 步长c
    print(value)

numbers = list(range(1,6))
print(numbers)

print("************************************************************")

even_numbers = list(range(2,11,2))
print(even_numbers)

print("************************************************************")

squares = [] # [] 创建空列表
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
print(min(squares),max(squares),sum(squares))

print("************************************************************")

squares = [value**2 for value in range(1,21)]  # 列表推导式
print(squares)

print("************************************************************")

players = ['charles','martina','michael','florence','eli']
print(players[:])
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[0::2])

print("************************************************************")

for player in players[:3]:
    print(player)

print("************************************************************")