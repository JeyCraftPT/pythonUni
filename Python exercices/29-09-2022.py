print("Exercício 1")
print("*---------------------------*")
print("|                           |")
print("*---------------------------*")

######################################

print("Exercício 2")
print("*---------------------------*")
print("|                           |")
print("*-----------|---|-----------*")
print("            |   |")
print("*-----------|---|-----------*")
print("|                           |")
print("*---------------------------*")

######################################

from math import *
print("Exercício 3")

a = 1.0 + sqrt(2) - 3
print ("O valor de a é ", a)

b = 2 / 2 + sin(1.7)
print ("O valor de b é ", b)

######################################

print("Exercício 4")
import math
#dir(math)
#print (dir()) #mostra as dirétórias da biblioteca NOT WORKING

#help(math)
#print(help()) #equivalente ao help normal NOT WORKING

######################################

print("Exercício 5")

nome = input("Qual é o seu nome? ")
print ("Olá", nome, "!  Bem vindo ao mundo criativo da programação?")

######################################

print("Exercício 6")

nome1 = input("Qual é o seu primeiro nome?")
nome2 = input("Qual é o seu último nome?")

print ("BILHETE PARA O VOO TAP45FA0174\n PASSAGEIRO: ", nome2, ", ", nome1)  

######################################

Fahrenheit = input("Quantos graus Fahrenheit estão?")

celcius = (5/9)*(int(Fahrenheit)-32)
print("Estão", celcius, "graus celcius")