from Stack1 import Stack

def decimal_convert(num, base):
    s = Stack()
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while num > 0:
        remainder = num % base
        s.push(remainder)
        num = num // base

    converted_num = ""
    while not s.is_empty():
        converted_num += digits[s.pop()]

    return converted_num