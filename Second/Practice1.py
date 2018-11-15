import PracLib as PL

def line():
    PL.line("*", 40)

print("             Menu")
line()
print(" C or c : Area of Circle")
print(" S or s : Area of Rectangle")
line()
Choice = input("Enter Your Choice : ")
line()

if Choice.lower() == 'c':
    Radius = float(input("Please input Radius : "))
    line()
    print("AREA = {0:.2f}".format(PL.CircleCal(Radius)))
elif Choice.lower() == 's':
    Width = float(input("Please input Width : "))
    Length = float(input("Please input Length : "))
    line()
    print("AREA = {0:.2f}".format(PL.RectangleCal(Width,Length)))
line()
