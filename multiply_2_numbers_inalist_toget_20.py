def sequential_search1(alist):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == 2:
            found = True
        else:
            pos += 1
    return alist[pos]

alist = [2,4,1,6,5,40,-1, 10]


def sequential_search2(alist):
    last = len(alist) - 1
    first_number = sequential_search1(alist)
    first = alist.index(first_number)
    found = False
    while first < alist[first] <= last and not found:
        if alist[first] == 40:
            found = True
        else:
            first += 1
    return found

print(sequential_search2(alist))

