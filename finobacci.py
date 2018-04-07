finobacci_cache = {}
def finobacci(n):
    if n in finobacci_cache:
        return finobacci_cache[n]

    if n == 1 or n == 2:
        value = 1
    
    elif n > 2:
        value = finobacci(n-1) + finobacci(n-2)
    finobacci_cache[n] = value
    return value
        
for n in range(1,101):
    print(n, ':', finobacci(n))
