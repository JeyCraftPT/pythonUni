from math import *
print (" ex 1")
a = int(input("Diga um número: "))
b = int(input("Diga outro número: "))

if a > b :
    print("O número maior é" , a)
else :
    print ("O número maior é" , b)
print ()
print ()
print ()
print (" ex 2 ")
v = int(input("número"))
b = int(input("número"))
n = int(input("número"))

if v > b and v > n :
    print (v , "é o maior")
elif b > v and b > n :
    print(b , "é o maior")
else :
    print (n , "é o maior")
print ()
print ()
print ()
print (" ex 12 ")
carro = int(input(" 1- ligueiro 2- pesado 3-motocilco"))

passe = int(input("quantos passageiros"))

if carro == 1 :
    if passe == 1 :
        print ("3,25")
    elif passe == 2 :
        print ("1,5")
    elif passe >= 3 :
        print ("0,75")
if carro == 2 :
    if passe == 1 or passe == 2 :
        print ("5,65")
    elif passe >=3 :
        print ("4")
if carro == 3 :
        print ("0,75")

print ()
print ()
print ()
print (" ex 3 ")
numero = int(input("diga um número: "))
if numero%2 == 0 :
    print ("é par")
else :
    print ("é ímpar")

print ()
print ()
print ()
print (" ex 4 ")
dividir = int(input("número: "))
if dividir == 0 :
    print ("nulo")
elif dividir % 3 == 0 :
    print ("é divisível por 3")
else :
    print ("não é divisível por 3")
print ()
print ()
print ()
print (" ex 6 ")
poi = int(input("numero :"))
poi2 = int(input("numero :"))
poi3 = int(input("numero :"))
if poi > poi2 and poi > poi3 :
    if poi2 > poi3 :
        print (poi)
        print(poi2)
        print (poi3)
    else :
        print(poi)
        print(poi3)
        print(poi2)
elif poi2 > poi and poi2 > poi3 :
    if poi > poi3 :
        print (poi2)
        print (poi)
        print (poi3)
    else:
        print (poi2)
        print (poi3)
        print (poi)
else :
    if poi > poi2 :
        print (poi3)
        print (poi)
        print (poi2)
    else :
        print (poi3)
        print(poi2)
        print (poi)
print ()
print ()
print ()
print (" ex 7 ")
prim = int(input("número"))
sec = int(input("número"))
trec = int(input("número"))
if sec**2-(4*prim*trec) > 0:
    raiz = sqrt(sec**2-(4*prim*trec))
    cima1 = (sec - raiz) / 2 * prim
    cima2 = (sec + raiz) / 2 * prim
    print ("as raizes são", cima1, "e", cima2)
else :
    print ("Não pode ser pois a raiz é negativa")
print ()
print ()
print ()
print (" ex 8 ")
inta = float(input("Diz um dos números do intervalo: "))
intb = float(input("Diz um dos números do intervalo: "))
if inta > intb :
    print ("I= [",inta,",",intb,"]")
else:
        print ("I= [",intb,",",inta,"]")
print ()
print ()
print ()
print (" ex 9 ")
mul = "x"
div = "/"
som = "+"
sub = "-"
N = str(input("Diz qual a operação que queres fazer para A o primeiro valor e B o segundo: "))
A = int(input("A= "))
B = int(input("B= "))
C = 0
if N == mul :
    C = A * B
    print(C)
elif N == div :
    C = A / B
    print (C)
elif N == som:
    C = A + B
    print (C)
elif N == sub:
    C = A - B
    print(C)
print ()
print ()
print ()
print (" ex 11 ")
ano = int(input("ano= "))
if ano%4 == 0 and ano%100 != 0 :
    print ("O ano é bissexto")
elif ano%400 == 0:
    print ("O ano é bissexto")
else :
    print ("O ano não é bissexto")
