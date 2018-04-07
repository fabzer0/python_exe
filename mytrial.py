def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    if found:
        print("The number %d is found at position %d " % (item, pos))

myList = [12, 32, 23, 98]
sequentialSearch(myList, 23)
