from pythonds.basic.stack import Stack

def general_parchecker(symbol_string):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '[{(':
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    return balanced

def matches(open, close):
    opens = '[{('
    closes = ']})'
    return opens.index(open) == closes.index(close)

print(general_parchecker('{{[()()]}()}'))
print(general_parchecker('{[]}[)'))


