import time

def sequentialSearch(alist, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    if found:
        print("The number %d is found at position %d" % (item, pos))

    end = time.time()
    print(end - start)

testList = [23, 32, 45,23]

sequentialSearch(testList, 45)

                     
