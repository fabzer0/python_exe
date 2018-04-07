class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        '''This method is a constructor method. it automatically
            takes self as the first argument and the rest of the
            arguments which are attributes follows'''
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        '''This method returns the full name of each empolyee if
            called upon when printing'''
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        '''class methods are simply alternatives methods for constructors
            This method takes cls as the first arg always. Since its a
            class method, the raise_amount will be applied to the whole
            class and not each instances'''
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        '''The method splits the hyphen in the case where a user inputs creds
            hyphen delimited values and returns creds without hyphens'''
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: #in python mon is seen as 0 while sun is seen as 6
            return False
        return True
    
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        '''Before instantiating new instances, Employee class should be instantiated. It
            can be done using two ways, using super().__init__ or Employee.__init__
            Note that using super().__init__ we omit the self arg'''
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name()) 
  

dev_1 = Developer('fabisch', 'apeli', 254065, 'Python') #the arguments should be positional
dev_2 = Developer('corey', 'schafer', 290345, 'Java')   #with respect to how they were instantiated
                                                      #in the constructor method
mngr_1 = Manager('Sue', 'Smith', 90000, [])

print(mngr_1.email)
mngr_1.add_emp(dev_2)
mngr_1.add_emp(dev_1)
mngr_1.remove_emp(dev_2)
mngr_1.print_emps()


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


new_emp_2 = Employee.from_string(emp_str_2)

import datetime
my_date = datetime.date(2018, 2, 10)

#print(Employee.is_workday(my_date))
#print(new_emp_2.full_name())
#print(new_emp_2.email)
#print(new_emp_2.pay)


#Employee.set_raise_amt(1.05)                                               
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#print(emp_1.full_name())
#print(emp_1.prog_lang)
#emp_1.apply_raise()
#print(emp_1.pay)
#print(emp_2.full_name())
#print(emp_2.pay)
#emp_2.apply_raise()
#print(emp_2.pay)
#print(Employee.num_of_emps)


print(dev_1)

