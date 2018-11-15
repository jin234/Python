def line(symble, lenght):
    print(symble*lenght)

def CircleCal(Radius):
    return (Radius*Radius*3.1428571)

def RectangleCal(Width,Lenght):
    return Width*Lenght

def Gradeing(Score):
    if Score >= 97:
        return "A+"
    elif Score >= 93:
        return "A"
    elif Score >= 90:
        return "A-"
    elif Score >= 87:
        return "B+"
    elif Score >= 83:
        return "B"
    elif Score >= 80:
        return "B-"
    elif Score >= 77:
        return "C+"
    elif Score >= 73:
        return "C"
    elif Score >= 70:
        return "C-"
    elif Score >= 67:
        return "D+"
    elif Score >= 63:
        return "D"
    elif Score >= 60:
        return "D-"
    else:
        return "F"
