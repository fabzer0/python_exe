from functools import lru_cache


@lru_cache(maxsize=1000)
def finobacci(n):
    #check that the input is a positive integer

    if type(n) != int:
        raise TypeError('n must be a positive int')
    if n < 1:
        raise ValueError('n must be a positive int')

    #Compute the nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return finobacci(n-1) + finobacci(n-2)

for n in range(1,101):
    print(n, ':', finobacci(n))
