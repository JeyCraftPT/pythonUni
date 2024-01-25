
print (" ex 1 ")
quantidade = int(input("Quantas vezes quer ver a frase?: "))
print (quantidade * "Programar é fixe\n")
print ()
print ()
print (" ex 2 ")
quantos = int(input("Quer ver os números inteiros até quanto?: "))
zero = 0
while zero <= quantos :
    print (zero)
    zero += 1
print ()
print ()
print (" ex 3 ")
quantos2 = int(input("Quer ver os números inteiros até quanto?: "))
zero2 = 0
while zero2 <= quantos2 :
    if zero2%2 != 0 :
        print (zero2)
        zero2 += 1
    else:
        zero2 += 1
print ()
print ()
print (" ex 4 ")
A = int(input("Diz um número que seja menor que o próximo: "))
B = int(input("Diz um número que seja maior que o anterior: "))
C = A
if A > B :
    print ("A tem de ser menor que B")
else :
    while A <= B :
        if A != B:
            print (A , "+ " , end="")
            A += 1
        else :
            print (A)
            A += 1
print ()
print ()
print(" ex 5 ")
A2 = int(input("Diz um número que seja menor que o próximo: "))
B2 = int(input("Diz um número que seja maior que o anterior: "))
C2 = A2
if A2 > B2 :
    print ("A tem de ser menor que B")
else :
    while A2 <= B2 :
        if A2 != B2:
            print (A2 , "+ " , end="")
            A2 += 1
            C2 += A2
        else :
            print (A2 , "= ", end="")
            print (C2)
            A2 += 1
print ()
print ()
print (" ex 8 ")
escadas = int(input("Qual é o tamanho das escadas"))
começo = 1
while começo <= escadas: 
    print (começo *"#")
    começo += 1
print ()
print ()
print (" ex 12 ")
Valormultiplicar = int(input("Qual é o número que quer em fatorial?: "))
valorater = 1
while Valormultiplicar > 0:
    valorater = valorater * Valormultiplicar
    Valormultiplicar -= 1
print ("O Valor Final é: ",valorater)
print ()
print ()
print (" ex 13 ")
quantosquer = int(input("quantos elementos quer? "))
yau = 1
yau2 = 1
cao = 1
gato = 0
if quantosquer == 0 :
    print ("0")
elif quantosquer == 1 :
    print (yau2)
elif quantosquer == 2 :
    print (yau)
    print (yau2)
else :
    print (yau)
    print (yau2)
    while cao <= quantosquer-2 :
        gato = yau + yau2
        print (gato)
        yau = yau2
        yau2 = gato
        cao += 1
