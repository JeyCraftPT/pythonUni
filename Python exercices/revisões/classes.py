from dataclasses import *
from random import *
class item():
    nome = str
    preco = int

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def total_valor(self, quantidade):
        return self.preco * quantidade


a = item("arroz", 7.98)

print(a.total_valor(4))

class loja():
    nome = str
    preco = int

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def precostock(self, quantidade):
        return self.preco * quantidade

A = loja ("arroz", 9.99)
B = loja ("massa", 5.99)

print (A.precostock(10))
quantos = int(input("Quantos queres? "))
R = []
cao = 0

while cao < quantos :
    R.append(randrange (1,50))
    cao += 1
print (R)
def maior(R:list):
    maior = R[0]
    i = 0
    for C in range(len(R)):
        if R[C] > maior :
            maior = R[C]
            i = C
    return i
print (maior(R))
