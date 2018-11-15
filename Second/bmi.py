import mylibrary as ml
from mylibrary import bmitype,showCurThaiYear
if __name__ == '__main__':
    weight = float(input("Enter Weight : "))
    Height = float(input("Enter Height : "))

    bmi = ml.calMBI(weight,Height)
    ml.line1()
    print("BMI is {0:,.2f}".format(bmi))
    print("You are {0}".format(ml.bmitype(bmi)))
    ml.line1()
