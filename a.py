def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    if found:
        print("The number %d is found at position %d " % (item, midpoint))
    else:
        print("The number", num , "is not found in the list")
   

myList = [12, 23, 43, 54]
num = int(input("Input the number "))
binarySearch(myList, num)
