# BMI calculator
person1 = "Fabisch"
height_m1 = 2.5
weight_kg1 = 67

person2 = "Fabisch's sister"
height_m2 = 2
weight_kg2 = 70

person3 = "Fabisch's brother"
height_m3 = 2.3
weight_kg3 = 63

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 13:
        return name + ' is not overweight'
    else:
        return name + ' is overweight'

print(bmi_calculator(person1, height_m1, weight_kg1))
print(bmi_calculator(person2, height_m2, weight_kg2))
print(bmi_calculator(person3, height_m3, weight_kg3))
