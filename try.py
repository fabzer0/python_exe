def sequentialSearch(alist, number):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == number:
            found = True
        else:
            pos += 1
    return found

myList = [23, 43, 65, 54]
print(sequentialSearch(myList, 43))
