def factorial(number):
    product = 1
    for i in range(number):
        product = product * (i+1)
    return product

user_input = int(input('Enter any integer that is not negative: '))
response = factorial(user_input)
print(response)
