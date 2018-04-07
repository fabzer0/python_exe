def greatest_common_divisor(num, den):
    if num > den:
        while num % den == 0:
            num = num
            den = den
        return den
    else:
        if num > den:
            while num % den != 0:
                oldnum = num
                oldden = den

                num = oldden
                den = oldnum % oldden
            return 1
        else:
             if num < den:
                 while den % num == 0:
                     den = den
                     num = nnum
                 return num
             else:
                 if num < den:
                     while den % num != 0:
                         oldden = den
                         oldnum = num

                         den = oldnum
                         num = oldden % oldnum

                     return 1


print(greatest_common_divisor(20, 10))
    
