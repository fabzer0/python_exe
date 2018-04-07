def checking_off(string1, string2):
    alist = list(string2)
    pos1 = 0
    stillOk = True
    while pos1 < len(string1) and stillOk:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if string1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            alist[pos2] = None
        else:
            stillOk = False
        pos1 += 1
    return stillOk

print(checking_off('pinto', 'tonpi'))
        
