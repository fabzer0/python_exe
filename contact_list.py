class Contact:
    def __init__(self, first, last, number=None, simcard=None):
        self.first = first
        self.last = last
        self.number = number
        if number is None:
            self.number = []
        else:
            self.number = number
        if simcard is None:
            self.simcard = []
        else:
            self.simcard = simcard

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
        

    def add_number(self, num):
        if num not in self.number:
            self.number.append(num)
        else:
            print('Contact already exists')

    def delete_number(self, num):
        if number in self.number:
            self.number.remove(num)
       

    def display_number(self):
        for num in self.number:
            print('-->', num)

    @classmethod
    def show_contact(cls, cntct):
        firsr, last, number = cntct
        return cls(first, last, number)
        
        
    
        
    

person_1 = Contact('dennis', 'okari')
#person_2 = Contact('michael', 'kijana')
#person_3 = Contact('bruce', 'wayne')

print(person_1.full_name())
#person_1.add_number(555666)
#person_1.display_number()
#print(Contact.show_contact())


        
            
