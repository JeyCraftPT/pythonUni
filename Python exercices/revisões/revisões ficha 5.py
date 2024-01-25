from math import *
from random import *

print ("ex 1")
print ()
L = [2,0,1,2,1,9,9,0]
for i in range (len(L)-1 , 0 , -1):
    print(L[i] , "=> " , end="")
print (L[0])
print ()
print("ex 2")
print()
L = [2,0,1,2,1,9,9,0]
cao = len(L)-1
while cao > 0 :
    print(L[cao],": ", end="")
    cao -= 1
print (L[0])
print ()
print ("ex 3")
print ()
L = [2,0,1,2,1,9,9,0]
gato = 0
peixe = 0
foca = 1
while gato < len(L)-1 :
    peixe = peixe + L[foca]
    foca += 1
    gato += 1
print(peixe)
print ()
print("ex 4")
print ()
R = []
N = int(input("Diga quantos números quer na lista "))
kao = 0
while kao < N :
    R.append(randint(1,100))
    kao += 1
print (R)
print ()
print ("ex 5")
print()
R = []
N = int(input("Diga quantos números quer na lista "))
kao = 0
while kao < N :
    R.append(randint(1,100))
    kao += 1
print (R)
maior = R[0]
kao = 0
for K in range(len(R)-1):
    if R[K] > maior:
        maior = R[K]
print (maior)
print ()
print ("ex 6")
print ()
R = []
N = int(input("Diga quantos números quer na lista "))
kao = 0
while kao < N :
    R.append(randint(1,100))
    kao += 1
print (R)
menor = R[0]
kao = 0
for K in range(len(R)-1):
    if R[K] < menor:
        menor = R[K]
print (menor)
print ()
print ("ex 7")
print ()
R = []
N = int(input("Diga quantos números quer na lista "))
kao = 0
cato = 0
while kao < N :
    R.append(randint(1,100))
    kao += 1
print (R)
menor = R[0]
kao = 0
for K in range(len(R)-1):
    if R[K] < menor:
        menor = R[K]
        cato = K
print (menor)
print (cato)
print ()
print ("ex 8")
print ()
R = []
N = int(input("Diga quantos números quer na lista "))
kao = 0
cato = 0
while kao < N :
    R.append(randint(-10,10))
    kao += 1
menor = 0
kao = 0
for K in range(len(R)):
    if R[K] <= menor:
        R[K] = 0
print (R)
print ()
print ("ex 9")
print ()
m = int(input("colunas: "))
n = int(input("comprimento: "))
R = []
R = m * [0]
for I in range (len(R)):
    R[I] = n * [0]
    for f in range (len(R[I])):
        R[I][f] = randint(0,100)
    print (R[I])
print ()
