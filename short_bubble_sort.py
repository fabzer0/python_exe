def short_bubble_sort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

        passnum -= 1

alist = [20, 30, 40 ,90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(alist)
print(alist)
