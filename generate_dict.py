def generate_dict(n):
    adict = {}
    for i in range(1, n+1):
        adict[i] = i**2
    return adict

print(generate_dict(8))
        
