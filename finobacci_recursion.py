def finobacci(n):
    '''without memoization the program will be slow given a range of bigger
        numbers'''
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return finobacci(n-1) + finobacci(n-2)
for n in range(1,101):
    print(n, ':', finobacci(n))
