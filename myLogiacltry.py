class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        pinA = None
        pinB = None

    def getPinA(self):
        return int(input('Enter pin A input for gate ' + self.getLabel() + '-->'))

    def getPinB(self):
        return int(input('Enter pin B for input gate ' + self.getLabel() + '-->'))


class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        pin = None

    def getPin(self):
        return int(input('Enter pin for input gate ' + self.getLabel() + '-->'))


class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self, label):
        super().__init__(label)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
             return 0
        else:
            return 1


gate = AndGate('or')
print(gate.getOutput())
