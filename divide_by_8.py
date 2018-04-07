from pythonds.basic.stack import Stack

def divide_by8(dec_number):
    rem_stack = Stack()
    while dec_number > 0:
        rem = dec_number % 8
        rem_stack.push(rem)
        dec_number = dec_number // 8

    octal_string = ''
    while not rem_stack.isEmpty():
        octal_string = octal_string + str(rem_stack.pop())
    return octal_string

print(divide_by8(233))
