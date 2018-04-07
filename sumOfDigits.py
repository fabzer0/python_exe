def sumOfDigits(alist):
    sum = 0
    for i in alist:
        i = str(i)
        i.split()
        for j in i:
            sum += int(j)
    return sum

alist = [12,3,6,4]
res = sumOfDigits(alist)
print(res)
