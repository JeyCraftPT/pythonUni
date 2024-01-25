from random import *
from math import * 
print("Exercício 1")
L = [2,0,1,2,1,9,9,0]
for i in range(len(L)-1,0,-1) : #range(início,fim,step)
    print (L[i], end= " => ")
print (L[0]) 
#########################################
print("Exercício 2")
L = [2,0,1,2,1,9,9,0]
yau = len(L)-1              #este é o indíce do último 0
while yau != 0 :            # enquanto yau n for 0
    print (L[yau], end=":") #dá print ao número daquele índice
    yau -= 1                #retira 1 ao índice
print(L[0])                 #dá print ao último
#########################################
print("Exercício 3")
L = [2,0,1,2,1,9,9,0]
yau = 0
um=0
while yau != len(L) :
    um = L[yau] + um
    yau += 1
print(um)
#########################################
print("Exercício 4")
quantos = int(input("Quantos queres? "))
P = []
cao = 0
while cao < quantos :
    P.append(randrange (1,50))
    cao += 1
print (P)
#########################################
print("Exercício 5")
quantos = int(input("Quantos queres? "))
P = []
cao = 0
while cao < quantos :
    P.append(randrange (1,50))
    cao += 1
maior = P[0]
for i in range(len(P)):
    if P[i] > maior:
        maior = P[i]

print (P)
print("O maior número da lista é: " + str(maior))
#########################################
print("Exercício 6")
quantos = int(input("Quantos queres? "))
P = []
cao = 0
while cao < quantos :
    P.append(randrange (1,50))
    cao += 1
menor = P[0]
for i in range(len(P)):
    if P[i] < menor:
        menor = P[i]

print (P)
print("O menor número da lista é: " + str(menor))
#########################################
print("Exercício 7")
quantos = int(input("Quantos queres? "))
P = []
cao = 0
posicao = 0
while cao < quantos :
    P.append(randrange (1,50))
    cao += 1
menor = P[0]
for i in range(len(P)):
    if P[i] < menor:
        posicao = i

print (P)
print("O menor número da lista é: " + str(posicao)) 
#########################################
print("Exercício 8")
K = []
dogo = 0
quantos = int(input("Quantos queres? "))
while dogo < quantos :
    K.append(randrange(-10,10))
    dogo += 1
piqueno = 0
for i in range (len(K)) :
    if K[i] < piqueno :
        K[i] = 0

print (K) 
#########################################
print("Exercício 9")
m = int (input("yau"))
n = int (input("yau2"))
A = m*[0]
for i in range(len(A)) :
    A[i] = n*[0]
    print( A[i]) 
#########################################
print("Exercício 10")
m = int (input("yau"))
n = int (input("yau2"))
A = m*[0]
for i in range(len(A)) :
    A[i] = n*[0]
    for l in range(len(A[i])):
        A[i][l] = randint(0,100)
    print (A[i])
#########################################
print("Exercício 11")
m = int (input("yau"))
n = int (input("yau2"))
A = m*[0]
for i in range(len(A)) :
    A[i] = n*[0]
    for l in range(len(A[i])):
        A[i][l] = randint(0,100)
        print ("%6d" % A[i][l], end="")
    print ("") 
#########################################
print("Exercício 12")
m = randint (1,5)
n = randint (1,5)
hau = 0
A = m*[0]
for i in range(len(A)) :
    A[i] = n*[0]
    for l in range(len(A[i])):
        A[i][l] = randint(0,100)
        hau += A[i][l]
hau = hau / (m + n)
hau = round(hau,3)
print (hau) 
#########################################
print("Exercício 13")
for o in range (0,7) :
    if o%2 == 0 :
        print ("*---*---*---*")
    else :
        print ("|   |   |   |") 
#########################################
print("Exercício 14")
n = int(input("Quantos quer de 1 a 20: "))
for o in range (0, n) :
    print ("*---*"+"---*" * (n-1))
    print ("|   |"+"   |" * (n-1))
print ("*---*"+"---*" * (n-1))
#########################################
print("Exercício 15")
