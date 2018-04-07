class Fraction:
    def __init__(self, top, bottom):
            self.num = top
            self.den = bottom

    def show(self):
        print(self.num, "/" , self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def gcd(m, n):
        while m % n != 0:
            old_m = m
            old_n = n

            m = old_n
            n = old_m % old_n

        return n

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = Fraction.gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num*other.den
        secondnum = other.num*self.den

        return firstnum == secondnum
    
f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
print(f1+f2)
print(f1==f2)
