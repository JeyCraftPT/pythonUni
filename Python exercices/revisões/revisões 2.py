from random import randint
n = int(input("sim"))
m = int(input("nao"))
K = []
K = n * [0]
for I in range(len(K)):
    K[I] = m * [0]
    for J in range(len(K[I])):
        K[I][J] = randint (0,100)
        print ("%6d" % K[I][J], end="")
    print()

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

print ()
print ("ex 13")
print ()
N = int(input("ihasf"))
for I in range(N+1):
    print ("*" + N *"---*")
    if I != N :
        print ("|" + N *"   |")
print()
print("ex4")
print()
Q = int(input("diz o número de itens na matriz: "))
R = Q * [0]
for A in range(len(R)-1):
    R[A] = randint (1,100)
print(R)
print()
print("ex5")
Q = int(input("diz o número de itens na matriz: "))
R = Q * [0]
for A in range(len(R)-1):
    R[A] = randint (1,100)
maior = R[0]
for C in range(len(R)-1):
    if R[C] > maior :
        maior = R[C]
print (R)
print (maior)
print ()
print ("Teste de matriz")
print()
A = int(input("Diz o número de linhas: "))
B = int(input("diz o número de colunas: "))
G = A * [0]
for I in range (len(G)):
    G[I] = B * [0]
    for J in range (len(G[I])):
        G[I][J] = randint (1,100)
        print("%6d" % G[I][J], end="")
    print()
print()
print ("ex15")
print()
t = int(input("AIAIAI"))
for w in range(t):
    for c in range (w+1, w+t+1):
        print("%4d" % c, end="")
    print()

print ()
print ("tenta outra vez")
print ()
h = int(input("diz cena"))
for d in range(h):
    for y in range (h, d+h+1):
        print ("%4d" % y, end="")
    print()

