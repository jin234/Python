
def line():
   print("-"*40)

W = float(input("Enter Your Weight : "))
H = float(input("Enter Your Height : "))
bmi = W/((H/100)**2)
line()
print("Your BMI is {0:,.2f}".format(bmi))
line()
