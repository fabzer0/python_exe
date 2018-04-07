def factorial(number):
    '''this is a recursive function that can get the factorial(n!) of any
        number. factorial is the multiplication of positive integers between
        1 and the number n. i.e 3! = 1*2*3 the ans is 6'''
    
    if number == 0:
        return 1
    else:
        return number*factorial(number-1)

print(factorial(0))
