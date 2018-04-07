def square_root(n):
    '''the formula is:
        newguess = 0.5*(oldguess + n/oldguess)'''
    
    root = n/2 # initial guess for n. this means for this instance the guess is half of n. it can be n divided by any number i.e n/5
    for i in range(20):
        root = 0.5*(root + (n/root))
    return root
print(square_root(9))
