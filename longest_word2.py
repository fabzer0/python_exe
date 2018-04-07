def longest_word(astring):
    astr = astring.split()
    max = 0
    for i in astr:
        if max < len(i):
            max = len(i)

    for j in astr:
        if len(j) == max:
            return j


astring = input(str('Type a sentence => '))
result = longest_word(astring)
print(result)
