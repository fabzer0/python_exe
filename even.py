def evenNumbers(numbers):
    for i in numbers:
        if i%2==0:
            yield i

numbers = [3,4,5,6,7,8,9,10]
evens = evenNumbers(numbers)
for n in evens:
    print(n)
