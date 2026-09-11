from Stack1 import Stack

"""
中序表达式转后序表达式
    (1)创建一个栈用于存储运算符；创建一个空的列表用于存储后序表达式;创建一个字典用于存储运算符的优先级

    (2)使用split()方法将中序表达式分割为一个个的token

    (3)遍历每一个token:
        (a)如果token是操作数
           -->则直接将其添加到后序表达式列表中

        (b)如果token是左括号
           -->则将其压入栈中

        (c)如果token是右括号
           -->则从栈中弹出运算符并添加到后序表达式列表中,直到遇到左括号为止

        (d)如果token是运算符,则将其与栈顶的运算符进行比较:

            (i)如果"栈为空"或"栈顶运算符的优先级小于当前运算符的优先级"
               -->则将当前运算符压入栈中

            (ii)如果"栈顶运算符的优先级大于或等于当前运算符的优先级"
                -->则将栈顶运算符弹出并添加到后序表达式列表中,
                -->然后循环至(ii)
                -->直到(i)
                -->然后将当前运算符压入栈中

    (4)遍历完所有token后,将栈中剩余的运算符依次弹出并添加到后序表达式列表中

    (5)将后序表达式列表转换为字符串并返回
"""
def infix_to_postfix(expression):
    precedence = {} # Define operator precedence

    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    precedence["("] = 1

    op_stack = Stack()  # Operator stack
    postfix_list = []   # Postfix output list
    token_list = expression.split() # Split the expression into tokens

    for token in token_list:
        # Handle operands
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)

        # Handle operators
        elif token == '(':
            op_stack.push(token)

        # Handle closing parenthesis
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()

        # Handle other operators
        else:
            while (not op_stack.is_empty()) and (precedence[op_stack.peek()] >= precedence[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    # Pop any remaining operators from the stack
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)
    # Convert the postfix list to a string and return it
     # join() method is used to concatenate the elements of the list into a single string, with a space as the separator.