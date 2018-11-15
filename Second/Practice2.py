import PracLib as PL

def line():
    PL.line("-", 40)

print("             INPUT YOUR SCORE")
line()
Mid = float(input("Enter Your Midterm Point  : "))
Fin = float(input("Enter Your Final Point    : "))
Hw = float(input("Enter Your HomeWork Point : "))
line()
print("Your Grade is {0}".format(PL.Gradeing(Mid+Fin+Hw)))
