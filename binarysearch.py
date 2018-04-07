import time

def binarySearch(alist, item):
    start = time.time()
    first = 0
    last = len(alist)-1
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

    end = time.time()
    print(end - start)
testList = [23, 32, 45,23]
binarySearch(testList, 45)
