def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (last + first) //2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    print("Really ", found, "and mark you that number, %d you chose is found at position %d of the list " % (item, midpoint))

myList = [23, 45, 76, 77, 87, 98]
num = int(input("Input the number"))
(binarySearch(myList, num))
            
