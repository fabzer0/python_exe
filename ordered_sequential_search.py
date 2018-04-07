def ordered_sequential_search(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found

alist = [23, 45, 54, 66, 100, 107, 190, 205, 300]
print(ordered_sequential_search(alist, 205))
print(ordered_sequential_search(alist, 200))
