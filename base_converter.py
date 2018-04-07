from pythonds.basic.stack import Stack

def base_converter(dec_number, base):
    '''This is a function that takes any decimal number and converts it according to the
        specified base'''
    digits = '0123456789ABCDEF'
    rem_stack = Stack()
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ''
    while not rem_stack.isEmpty():
        new_string = new_string + digits[rem_stack.pop()]
    return new_string

print(base_converter(233, 16))
print(base_converter(233, 8))
print(base_converter(233, 5))
print(base_converter(233, 2))
