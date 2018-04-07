def find_power(base, exponent):
    res = 1
    if exponent == 0:
        return 1
    else:
        for i in range(exponent):
            res *= base

        return res

ans = find_power(10,2)
print(ans)
