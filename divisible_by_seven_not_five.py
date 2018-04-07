def divisibility_test():
    alist = []
    for i in range(2000, 3200+1):
        if i % 7 == 0 and i % 5 != 0:
            alist.append(str(i))
    return ','.join(alist)

print(divisibility_test())
