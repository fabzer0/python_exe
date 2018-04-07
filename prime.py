def prime_numbers(number, last):
    for num in range(number, last+1):
        j = 2
        for j in range(j, num):
            if not num%j:
                break
        if j > (num/j) and num != 1:
                print(num)

if __name__ == '__main__':
    prime_numbers(1, 20)
