from random import *
print ("ex 1")
def entre (x:int, a:int, b:int) -> bool:
    if a<x<b or b<x<a:
        return True
    else:
        return False
a = int(input("introduz um valor:"))
b = int(input("introduz um valor:"))
x = int(input("introduz um valor:"))
#d = entre (a, b ,x)
if entre(x,a,b):
    print("Sim")
else: 
    print("Não")
print()
print("#########################")
print()
print("ex 2")
L = []
cao = 0
while cao < randint(0,10) :
    L.append(randrange (1,50))
    cao += 1
maior = L[0]
for a in range(len(L)):
    if L[a] > maior:
        maior = L[a]
print(L)
print("O maior elemento da lista é:", maior)
print()
print("#########################")
print()
print("ex 3")
def troca(L:list, a:int, b:int):
    if 0 < a <= len(L) or 0 < b <= len(L):
        c = L[a]
        L[a] = L[b]
        L[b] = c 
        return L
    else:
        return False
L = []
cao = 0
while cao < 10 :
    L.append(randrange (1,50))
    cao += 1
print (L)
a = 2
b = 4
print (troca (L, a, b))
print()
print("#########################")
print()
print("ex 4")
L = []
cao = 0
b = 0
while cao < randint(0,10) :
    L.append(randrange (1,50))
    cao += 1
def maxpos(L:list) -> int:
    b = 0
    maior = L[0]
    for a in range(len(L)):
        if L[a] > maior:
            b = a
    return b
print(L)
print (maxpos(L))
print()
print("#########################")
print()
print("ex 5")
print()
print("#########################")
print()
print("ex 6")
a = 
def sequencia (L:list):
    b = False
    for a in range (len(L)):
        if L[a] == L[a-1]+1:
            if L[a] == L[a-2]+2:
                b = True
    return 
L = []
cao = 0
while cao < randint(0,10) :
    L.append(randrange (1,10))
    cao += 1
print (L)
print (sequencia(L)
print()
print("#########################")
print()
print("ex 7")
a = 0
def sequencia (L:list):
    for a in range (len(L)):
        if L[a] == L[a-1] == 7 or L[a] == L[a-2] == 7:
            return True
        else :
            return "Não tem sequencia de 7"
L = []
cao = 0
while cao < randint(0,10) :
    L.append(randrange (1,10))
    cao += 1
print (sequencia(L))
print()
print("#########################")
print()
print("ex 8")
A = str(input("Pôe a frase que queres separada: "))
L=[]
for a in range (len(A)):
    L.append(A[a])
for b in range (len(A)):
    if A[b].isalpha() == True:
        print(A[b], end="")
    else:
        print()
print()
print("#########################")
print()
print("ex 9")
A = str(input("Pôe a frase que queres negada: "))
L=[]
g = False
o = 0
for a in range (len(A)):
    L.append(A[a])
for i in range (len(A)):
    if A[i-2]+A[i-1]+A[i] == "nao":
        g = True
if g == False:
    for b in range (len(A)):
        if A[b].isalpha() == True:
            print(A[b], end="")
            o = b
        else:
            break
    print (" não", end="")
    for j in range(o+1, len(A)):
        print(A[j], end="")
print()
print("#########################")
print()
print("ex 10")
A = str(input("Pôe a frase que queres separada: "))
L=[]
g = False
o = 0
for a in range (len(A)):
    L.append(A[a])
for i in range (len(A)):
    if A[i-2]+A[i-1]+A[i] == "nao":
        g = True
        o = i-2
if g == True:
    for b in range (len(A)):
        if b == o :
            break
        else:        
            if A[b].isalpha() == True:
                print(A[b], end="")
            else:
                print(end=" ")
    for e in range (o+4,len(A)):
        if A[e].isalpha() == True:
                print(A[e], end="")
        else:
            print(end=" ")
            print(end="")
print()
print("#########################")
print()
print("ex 11")
A = str(input("Qual é o nome (com extensão) do ficheiro que quer: "))
f = 0
def linhas (A):
    f = open(A, "r", encoding="utf8")
    return f.readlines(None)
print(len(linhas(A)))
print()
print("#########################")
print()
print("ex 12")
A = str(input("Qual é o nome (com extensão) do ficheiro que quer: "))
f = 0
def linhas (A):
    f = open(A, "r", encoding="utf8")
    return f.readlines(None)
for a in range (len(linhas(A))-1,-1,-1):               #IMPORTANTE!!!!! btw porque é que sem a linha extra n funciona?
    print(linhas(A)[a], end="")
print()
print("#########################")
print()
print("ex 13")
A = str(input("Qual é o nome (com extensão) do ficheiro que quer: "))
f = 0
l = 0
def linhas (A):
    f = open(A, "r", encoding="utf8")
    return f.readlines()
L = linhas(A)
print (L)
for b in range (len(L)):
    if L[b].strip().isalnum():
        l += 1
print (l)
print()
print("#########################")
print()
print("ex 14")
L= []
cao = 0
b = 0
c = 0
for a in range (randint(5,10)):
    L.append(randrange(0,10))
    cao += 1
print (L)
A = int(input("Escolhe uma posição: "))
d = len(L)-1
for i in range (len(L)-1):
    if L[i] > L[A]:
        b = L[c]
        L[c] = L[i]
        L[i] = b
        c += 1
    else:
        b = L[d]
        L[d] = L[i]
        L[i] = b
        d -= 1
print (L)
print()
print("#########################")
print()
print("ex 15")
A = str(input("Diz a frase: "))
L = []
for a in range (len(A)):
    L.append(A[a])
for b in range (len(L)):
    if L[b] == "c":
        L[b] = ord(L[b])+23
    print(L[b], end="")
print()
print("#########################")
print()
print("ex 16")
A = str(input("Diz a frase: "))
B = int(input("Qual é a chave: "))
L = []
for a in range (len(A)):
    L.append(A[a])
for b in range (len(L)):
    if L[b] == "c":
        L[b] = ord(L[b])+B
    print(L[b], end="")
print ()
for c in range (len(L)):
    x = str(L[c])
    if x.isnumeric():
        L[c] = chr(L[c]-B)
    print (L[c], end="")
print()
print("#########################")
print()
print("ex 17")