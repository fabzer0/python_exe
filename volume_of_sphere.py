import math
def volume_of_sphere(r):
    v = (4/3) * math.pi * r**3
    
    return v
print(volume_of_sphere(int(input('Enter radius --> '))))
