from pythonds.basic.stack import Stack

rem_stack = Stack()
def to_string(n, base):
    convert_string = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            rem_stack.push(convert_string[n])
        else:
            rem_stack.push(convert_string[n%base])
        n = n // base

    rem_string = ''
    while not rem_stack.isEmpty():
        rem_string = rem_string + str(rem_stack.pop())
    return rem_string

print(to_string(1, 10 ))
