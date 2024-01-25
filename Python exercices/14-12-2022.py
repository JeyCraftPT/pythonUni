from dataclasses import dataclass
from math import *

@dataclass
class item:
    nome : str
    preco : float

a = item ("arroz", 7.99)
b = item ("massa", 10.99)
d = item ("molho", 8.99)
print (a)

c = int(a.preco) / int(b.preco)
print (c)

def mediapreco (L:list): # L:list é o "input" que é dado ao usar a função
    soma = 0
    for x in L: # vai acrescentando os valores dados
        soma += x
    return soma/len(L) # o output é a soma dos valores todos a dividir pelo comprimento da lista

print (mediapreco ({a.preco , b.preco , d.preco})) # o que está entre parenteses são os valores que são usados na função "mediapreco"

class Ponto: 
  x: int
  y: int

  def __init__(self, x, y): 
    self.x = x
    self.y = y

  def distance(self):
    return sqrt(self.x**2+self.y**2)

  def __str__(self):
    return f'({self.x},{self.y})'
p = Ponto(-7,3)
print(p)

@dataclass
class Rectangulo:
  origem: Ponto 
  compri: int 
  largur: int

@dataclass 
class Circulo:
  centro: Ponto 
  raio: int

a = Ponto(2,1)
print(a.y)

retA = Rectangulo(Ponto(2,2),3,7)
cirA = Circulo(Ponto(150,200), 70)

print(retA)
print(cirA)

def areaRect(r:Rectangulo) -> int:
  area = r.compri * r.largur
  return area

def areaCirc(c:Circulo) -> int:
  area = 3.1415 * c.raio**2
  return area

print("Area do rectangulo:", areaRect(retA))

print("Area do circulo:", areaCirc(cirA))

print(a.distance())
b = Ponto(73,151)
print(b.distance())

class Circulo: 
  centro: Ponto 
  raio: int

  def __init__(self, c:Ponto, r:int): 
    self.centro = c
    self.raio = r

  def area(self):
    return pi*self.raio**2

  def perimetro(self):
    return 2*self.raio*pi


class Retangulo: 
  origem: Ponto 
  compri: int 
  largur: int

  def __init__(self, p:Ponto, comprimento:int, largura:int): 
    self.origem = p
    self.compri = comprimento
    self.largur = largura

  def area(self):
    return self.compri*self.largur

  def perimetro(self):
    return 2*self.compri + 2*self.largur

C1 = Circulo(Ponto(1,1), 3)
C2 = Circulo(Ponto(20,10),4)
R1 = Retangulo(Ponto(1,1), 10, 11)
print(C1.area(), C2.area(), R1.area())
print(C1.perimetro(), C2.perimetro(), R1.perimetro())