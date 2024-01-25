from math import sqrt, pi

print ("Exercício 1")
n = int(input("Quantas vezes quer ver a frase? "))
print ("Programar é fixe \n"*n)
###################################################
print ("Exercício 2")
m = int(input("Quer ver os números inteiros até quanto: "))
b = 0
while b < m :
    b += 1
    print (b)
###################################################
print ("Exercício 3")
q = int(input("Quer ver os números pares até quanto: "))
w = 0
while w < q :
    w += 1
    if w % 2 == 0 :
        print(w)
###################################################
print ("Exercício 4")
l = int(input("Número em que começa: "))
o = int(input("Número em que acaba: "))
if l < o :
    while l <= o :
        print(l)
        l +=1
else :
    print ("O número inicial tem de ser menor!!")
###################################################
print ("Exercício 5")
p = int(input("Número em que começa: "))
k = int(input("Número em que acaba: "))
d = 0
if p < k :
    while p <= k :
        print(p)
        d += p
        p += 1
    print (d)
else :
    print ("O número inicial tem de ser menor!!")
###################################################
print ("Exercício 6")
f = int(input("Introduza um número positivo: "))
while f < 0 :
    f = int(input("Introduza um número positivo: "))
else :
    g = sqrt(f)
    print (g)
###################################################
print ("Exercício 7")
h = int(input("Introduza um número positivo: "))
while h < 0 :
    h = int(input("Introduza um número positivo: "))
else :
    print ("Conseguiste finalmente pôr um número positivo!!!!!")
###################################################
print ("Exercício 8")
triangulo = int(input("Qual queres que seja o comprimento final do triângulo?: "))
triangulo1 = 1
while triangulo1 <= triangulo :
    print("#"*triangulo1)
    triangulo1 += 1
###################################################
print ("Exercício 9")
sair = 0
Volumeesf = 1
volumepir = 2
volumecil = 3
escolha = int(input("Cálculos Volumétricos\n 0 - Sair \n 1 - Volume da Esfera \n 2 - Volume da Pirâmide \n 3 - Volume da Cilindro \n Escolha a sua opção"))

if escolha == sair :
    print ("Feito")

elif escolha == Volumeesf :
        raioesf=int(input("Qual é o raio da esfera?: "))
        Volume1 = 4/3 * pi * raioesf**3
        if Volume1 > 0 :
            print("O volume é:"+Volume1)
        else :
            print ("Não é possível calcular")
        

elif escolha == volumepir :
    ladopir = int(input("A base é um quadrado, qual é a medida do lado?: "))
    areabasepir = ladopir**2
    alturapir = int(input("Quão alta é a piramide?: "))
    Volume2 = (areabasepir * alturapir) / 3
    if Volume2 > 0 :
            print("O volume é:"+Volume2)
    else :
            print ("Não é possível calcular")

elif escolha == volumecil : 
    alturacil = int(input("Qual é a altura do cilindro?: "))
    raiocil = int(input("Qual é o raio da base do cilindro?: "))
    areabasecil = raiocil**2 * pi
    Volume3 = areabasecil * alturacil
    if Volume3 > 0 :
            print("O volume é:"+Volume3)
    else :
            print ("Não é possível calcular")

elif escolha < 0 or escolha > 3 :
    print ("Essa opção não é válida!")
###################################################
print ("Exercício 10")
sair = 0
Volumeesf = 1
volumepir = 2
volumecil = 3
escolha = int(input("Cálculos Volumétricos\n 0 - Sair \n 1 - Volume da Esfera \n 2 - Volume da Pirâmide \n 3 - Volume da Cilindro \n Escolha a sua opção"))

while escolha <0 or escolha >3 :
    print ("Essa opção não é válida")
    escolha = int(input("Cálculos Volumétricos\n 0 - Sair \n 1 - Volume da Esfera \n 2 - Volume da Pirâmide \n 3 - Volume da Cilindro \n Escolha a sua opção"))

if escolha == sair :
    print ("Feito")

elif escolha == Volumeesf :
        raioesf=int(input("Qual é o raio da esfera?: "))
        Volume1 = 4/3 * pi * raioesf**3
        if Volume1 > 0 :
            print("O volume é:"+Volume1)
        else :
            print ("Não é possível calcular")
        

elif escolha == volumepir :
    ladopir = int(input("A base é um quadrado, qual é a medida do lado?: "))
    areabasepir = ladopir**2
    alturapir = int(input("Quão alta é a piramide?: "))
    Volume2 = (areabasepir * alturapir) / 3
    if Volume2 > 0 :
            print("O volume é:"+Volume2)
    else :
            print ("Não é possível calcular")

elif escolha == volumecil : 
    alturacil = int(input("Qual é a altura do cilindro?: "))
    raiocil = int(input("Qual é o raio da base do cilindro?: "))
    areabasecil = raiocil**2 * pi
    Volume3 = areabasecil * alturacil
    if Volume3 > 0 :
            print("O volume é:"+Volume3)
    else :
            print ("Não é possível calcular")
###################################################
print ("Exercício 11")
um = 1
numerocoisas = 0
valorcoisas = 0
while um == 1 :
    Valor = int(input("Diga um dos valores para somar para a média"))
    valorcoisas += Valor
    numerocoisas += 1
    if Valor == 0 :
        um = 2
        numerocoisas -= 1
        Valorfinal = valorcoisas / numerocoisas 
        print ("A média aritmética é: ",Valorfinal)
###################################################
print ("Exercício 12")
Valormultiplicar = int(input("Qual é o número que quer em fatorial?: "))
quantascoisas = 1
valorater = 0
yau = 1
while quantascoisas < Valormultiplicar :
    valorater = quantascoisas * (quantascoisas + 1) 
    quantascoisas += 1
print ("O Valor Final é: ",valorater)
###################################################
print ("Exercício 13")
f1 = 1
f2 = 1
yau = 0
cao = 1
quantos = int(input("Quer saber quantos termos da sequência de Fibonacci? "))
print (f1)
print (f1)
while cao < quantos :
    yau = f1 + f2
    print(yau)
    f1 = f2
    f2 = yau
    cao +=1 
###################################################
print ("Exercício 14")
baixo = 0
medio = 0
alto = 0
todos = 0
um = 1
while um == 1 :
    peso = float(input("Qual é o peso do aluno? "))
    if peso >30 and peso <= 50 :
        baixo +=1
        todos +=1
    elif peso > 50 and peso < 75 :
        medio +=1 
        todos +=1
    elif peso > 75 :
        alto += 1
        todos +=1
    elif peso <= 30 :
        baixo +=1
        todos +=1
        print ("Existem", baixo , "alunos com peso a baixo dos 50")
        print ("Existem", medio , "alunos com peso acima dos 50 e abaixo dos 75")
        print ("Existem", alto , "alunos com peso superior a 75")
        um = 0