def remove_duplicates(astring):
    result = []
    for i in astring:
        if i not in result:
            result.append(i)
    result.sort()
    result = ''.join(result)
    diff = len(astring) - len(result)
    return result, diff

user_prompt = input(str('Enter a string => '))
print(remove_duplicates(user_prompt))
