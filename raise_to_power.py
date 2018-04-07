def power(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res

print(power(4,4))
print(power(25,2))
