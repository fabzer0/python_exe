def sorting_and_compare(string1, string2):
    '''Even though string1 and string2 are differrent they are anagrams only
        if they consist of exactly the same characters. So if we begin by sorting
        each string alphabetically from A to Z, we will end up with the same string
         if the two original strings are anagrams'''
    
    alist1 = list(string1)
    alist2 = list(string2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(string1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False
    return matches

print(sorting_and_compare('python', 'typhon'))
