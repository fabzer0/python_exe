class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        if self.pinA == None:
            return int(input('Enter pin A input for gate ' + self.get_label() + '-->'))
        else:
            return self.pinA.get_from().get_output()
    def get_pinB(self):
        if self.pinB == None:
            return int(input('Enter pin B input for gate ' + self.get_label() + '-->'))
        else:
            return self.pinB.get_from().get_output()

class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        self.pin = None

    def get_pin(self):
        return int(input('Enter pin input for logic gate ' + self.get_label() + '-->'))

class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def performGateLogic(self):
        a = self.get_pinA()
        b = self.get_pinB()

        if a == 1 and b == 1:
            return 1
        else:
            if (a and b) > 1:
                print('Invalid Input')
            else:
                return 0

    

class OrGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def performGateLogic(self):
        a = self.get_pinA()
        b = self.get_pinB()

        if a == 0 and b == 0:
            return 0
        else:
            if (a and b) > 1:
                print('Invalid Input')
            else:
                return 1

    def set_next_pin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError('Error: NO EMPTY PINS')

    

class NotGate(UnaryGate):
    def __init__(self, label):
        super().__init__(label)

    def performGateLogic(self):
        a = self.get_pin()

        if a == 0:
            return 1
        else:
            if a > 1:
                print('Invalid Input')
            else:
                return 0

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
       
        else:
            raise RuntimeError('Error: NO EMPTY PINS')


    


class Connector:
    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.fgate

    def get_to(self):
        return self.tgate

    
g1 = AndGate('G1')
print(g1.get_output())
g2 = AndGate('G2')
print(g2.get_output())
g3 = OrGate('G3')
print(g3.get_output())
g4 = NotGate('G4')
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
print(g4.get_output())
    

