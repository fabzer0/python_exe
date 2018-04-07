def arr_tuple(value):
    a = value.split(',')
    t = tuple(a)

    return a, t
    

value = input()
print(arr_tuple(value))
