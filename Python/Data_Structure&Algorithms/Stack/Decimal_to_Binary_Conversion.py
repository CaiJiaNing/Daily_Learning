from Stack1 import Stack

def decimal_to_binary(num):
    s = Stack()
    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num = num // 2

    binary_num = ""
    while not s.is_empty():
        binary_num += str(s.pop())

    return binary_num