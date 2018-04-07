def recur(alist):
    non_duplicate = []
    duplicate = []
    for i in alist:
        if i not in non_duplicate:
            non_duplicate.append(i)
        elif i in non_duplicate:
            if i not in duplicate:
                duplicate.append(i)
    return duplicate

alist = [76, 43, 34, 98, 45, 43, 23, 76]
print(recur(alist))
