def remove_duplicates(astring):
    result = []
    for i in astring:
        if i not in result:
            result.append(i)
    result = ''.join(result)
    diff = len(astring) - len(result)
    return result, diff

the_string = input(str('Insert a string => '))
print(remove_duplicates(the_string))
