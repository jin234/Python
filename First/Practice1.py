
def line():
    print("-"*30)



Price = float(input("Enter Price  of Product : "))
Amount = float(input("Enter Amount of Product : "))
Total = Price*Amount
Vat = Total*7/100
GTotal = Total+Vat
line()
print("PRICE       : {0:10,.2f} Baht".format(Price))
print("AMONUT      : {0:10,.2f}".format(Amount))
print("SUBTOTAL    : {0:10,.2f} Baht".format(Total))
line()
print("VAT (7%)    : {0:10,.2f} Baht".format(Vat))
print("GRAND TOTAL : {0:10,.2f} Baht".format(GTotal))
line()
