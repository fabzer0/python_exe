def selection_sort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1): #excluding index 0 because it has posOfMax
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp



    
alist = [54,34,64,23,76,98,36,12,88]
selection_sort(alist)
print(alist)
