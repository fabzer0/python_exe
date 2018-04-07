from pythonds.basic.stack import Stack

def divide_by2(dec_number):
    '''This function takes in a decimal number and converts it to a binary number'''
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number//2

    bin_string = ''
    while not rem_stack.isEmpty():
        bin_string = bin_string + str(rem_stack.pop())
    return bin_string

print(divide_by2(42))
print(divide_by2(233))
print(divide_by2(487))
