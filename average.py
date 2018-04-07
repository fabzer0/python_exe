def addition(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

mylist = list(range(1,21))
def get_average(mylist):
    total = addition(mylist)
    list_size = len(mylist)
    return total/list_size
print(get_average(mylist))

    
