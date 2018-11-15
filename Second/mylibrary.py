import math as M
import datetime as D
import os




def showCurThaiYear():
    TY = D.datetime.now().year + 543
    return TY
def calMBI(w,h):
   #bmi = w/((h/100)**2)
   bmi = w/M.pow(h/100,2)
   return bmi
def bmitype(bmi):
   if(bmi<=18.50):
       return 'underweight'
   elif(bmi<=22.99):
       return 'normalweight'
   elif(bmi<=30):
       return 'overweight'
   elif(bmi>30):
       return 'obecity'
def line1():
   print("-"*40)
#limit ให้คำสั่งที่อยูช้างล่างรันแค่ใน main ของตัวเอง
if __name__ == '__main__':
    print('this is message from my lib')
