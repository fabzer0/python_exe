def is_isogram(astring):
    if type(astring) != str:
        raise TypeError('A string value needed')
    elif astring == '':
        return astring, False
    else:
        astring = astring.lower()
        for i in astring:
            if astring.count(i) > 1:
                return astring, False
            else:
                return astring, True


astring = input('Enter a string > ')
res = is_isogram(astring)
print(res)
