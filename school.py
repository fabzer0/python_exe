class School:
    population = 0
    
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

        School.population += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

class Teachers(School):
    def __init__(self, first, last, age, subj):
        super().__init__(first, last, age)

        self.subj = subj

class Students(School):
    def __init__(self, first, last, age, subj_s=None):
        super().__init__(first, last, age)
        if subj_s is None:
            self.subj_s = []
        else:
            self.subj_s = subj_s

    def add_subj(self, sbj):
        if sbj not in self.subj_s:
            self.subj_s.append(sbj)

    def remove_subj(self, sbj):
        if sbj in self.subj_s:
            self.subj_s.remove(sbj)

    def print_subj(self):
        for sbj in self.subj_s:
            print('-->', sbj)
        
        
sbjcts = ['Mathematics', 'English', 'Kiswahili', 'Chemistry', 'Biology', 'Physics', 'C.R.E']



#TEACHERS
fst_tchr = Teachers('faith', 'njagi', 55, sbjcts[2])
scd_tchr = Teachers('michael', 'wamuyu', 35, sbjcts[0])
thrd_tchr = Teachers('jamal', 'gadaffi', 40, sbjcts[1])
frth_tchr = Teachers('ruth', 'were', 27, sbjcts[6])
ffth_tchr = Teachers('elizabeth', 'njoki', 33, sbjcts[5])
sxth_tchr = Teachers('jacob', 'mzee', 49, sbjcts[4])
#STUDENTS
fst_sdnt = Students('bravin', 'keith', 17)
scd_sdnt = Students('jenifer', 'hudson', 19, [])

#print(sxth_tchr.subj)
print(fst_sdnt.full_name())
fst_sdnt.add_subj(sbjcts[0])
#scd_sdnt.add_subj(sbjcts[1])
#scd_sdnt.add_subj(sbjcts[2])
#scd_sdnt.add_subj(sbjcts[3])
#scd_sdnt.remove_subj(sbjcts[1])
fst_sdnt.print_subj()
#print(scd_sdnt.age)
#print(School.population)

        

