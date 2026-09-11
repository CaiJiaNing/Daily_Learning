from Stack import Stack

def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "({[<":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            
            match symbol:
                case ")":
                    if s.peek() == "(":
                        s.pop()
                    else:
                        return False
                    
                case "]":
                    if s.peek() == "[":
                        s.pop()
                    else:
                        return False  

                case "}":
                    if s.peek() == "{":
                        s.pop()
                    else:
                        return False 

                case ">":
                    if s.peek() == "<":
                        s.pop()
                    else:
                        return False

                case _:
                    return False
   
    return s.is_empty()                              




def balance_checker(symbol_string):
    s = Stack()

    for symbol in symbol_string:
        if symbol in "({[<":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False
    return s.is_empty()

def matches(sym_top,symbol):
    all_lefts = "({[<"
    all_rights = ")}]>"

    return all_lefts.index(sym_top) == all_rights.index(symbol)