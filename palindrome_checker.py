from pythonds.basic.deque import Deque

def pal_checker(astring):
    char_deque = Deque()
    for ch in astring:
        char_deque.addRear(ch)

    still_equal = True
    while char_deque.size() > 1 and still_equal:
        first = char_deque.removeFront()
        last = char_deque.removeRear()
        if first != last:
            still_equal = False
    return still_equal

print(pal_checker('madam'))
print(pal_checker('dennis'))
