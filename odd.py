def oddNumbers(numbers):
    for i in numbers:
        if i%2!=0:
            yield i

numbers = [2,3,4,5,6,7,8,9,10]
odds = oddNumbers(numbers)
for n in odds:
    print(n)




