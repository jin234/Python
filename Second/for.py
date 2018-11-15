'''




def sumTO(N1,N2):
    total = 0
    for i in range(N1,N2+1,1):
        total += i
    return total

print("ANS : ",sumTO(1,1000))


car = ('toyota', 'Honda' , 'Susuki', 'Gm', 'Gm')
carl = set(car)
for i in car:
    print('{0}'.format(i))

print('carl = {0}'.format(type(carl)))
'''

N = int(input("input N : "))
M = int(input("input M : "))
for N
    for i in range(1,13,1):
        print('{0} x {1:2} = {2:2} '.format(N,i,i*N))
