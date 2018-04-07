class InputOutString:
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input(str())
    def printString(self):
        return self.s.upper()

one = InputOutString()
one.getString()
print(one.printString())
