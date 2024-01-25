from math import * 

print ("exercicio 1")

valor_real = 2*(5*(int(input("Cada tarte custa 5 euros, quantas tartes quer? "))))
taxa_de_iva = float (input("A taxa de Iva é:"))
taxa_de_iva = taxa_de_iva/100
valor_absoluto = valor_real + (valor_real*taxa_de_iva)
print ("O valor do iva é" , taxa_de_iva , "logo o seu preço final será", valor_absoluto)

####################################

print ("exercicio 2")

teste1 = float(input("Quanto tiveste no teu primeiro teste?"))
teste2 = float(input("Quanto tiveste no teu segundo teste?"))
teste3 = float(input("Quanto tiveste no teu terceiro teste?"))
média = (teste1 + teste2 + teste3) / 3
print ("A tua média é ", média)

####################################

print ("exercicio 3")

print ("Agora vamos tentar determinar a tua classificação por frequência")
TE1 = 0.45*(float(input("Para isso precisamos de saber quanto tiveste no teu primeiro teste ")))
TE2 = 0.45*(float(input("Para isso precisamos de saber quanto tiveste no teu segundo teste ")))
AP = 0.1*(float(input("Nas aulas práticas o teu desempenho foi avaliado, quanto tiveste? ")))
CF = TE1 + TE2 + AP
print ("Acabaste o teu semetre com uma classificação por frequência de", CF)
####################################

print ("exercicio 4")

print("O triângulo tem 3 lados e precisamos de saber a medida de todos para poder calcular a área")
lado1 = float(input("Qual é a medida do primeiro lado?"))
lado2 = float(input("Qual é a medida do segundo lado?"))
lado3 = float(input("Qual é a medida do terceiro lado?"))
p = (lado1 + lado2 + lado3) / 2
area = sqrt(p*(p-lado1) * (p-lado2) * (p-lado3))
area1 = round(area,5)
print ("A área do triângulo é", area1)

####################################

print ("exercicio 5")

N = int(input("Qual é o comprimento que quer a sua forma?"))
C = "-"
E = " "
print ("*"+ C*N +"*")
print ("|"+ E*N + "|")
print ("|"+ E*N + "|")
print ("*"+ C*N +"*")

####################################

print ("exercicio 6")

print ("este programa vai converter horas, minutos e segundos em segundos")
h = int(input("Horas:"))
m = int(input("Minutos:"))
s = int(input("Segundos:"))
s2 = ((h*3600) + (m*60) + s)
print("Isso dá um valor de", s2, "segundos")

####################################

print ("exercicio 7")

segundos = int(input("Quantos segundos:"))
horas = segundos // 3600
minutos = (segundos % 3600) //60
segundos = (segundos % 3600) % 60
print (horas, "horas,", minutos , "minutos e", segundos)
