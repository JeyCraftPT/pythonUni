from dataclasses import dataclass

@dataclass
class Estudante:
    numero : int
    nome : str
    media: float

a = Estudante (58712, "John Rambsy", 16)
b = Estudante (58712, "John Rambsy2", 17)
c = Estudante (58712, "John Rambsy3", 18)
print (a.nome, a.media)
#a.media = a.media - 0.11
print (a)

def mediaturma (L:list):
    soma = 0
    for x in L:
        soma += x
    return soma/len(L)
print (mediaturma({a.media, b.media, c.media}))

##################################################

produtos = { "cerveja":75 , "nata":65 , "cafe":55}
print (produtos.keys())
print (produtos.get("cafe"))
print(produtos["cafe"]) 
produtos["cafe"] = produtos ["cafe"] + 1 #soma 1 a key cafe de valor 55 o que dá 56
print (produtos.get("cafe")) #dá "print" do cafe

##################################################

produtos = { "cerveja":75 , "nata":65 , "cafe":55}
for item in produtos.keys():
    print (item.ljust(20,"."), produtos[item]/100,"$") #print (item, justificado a esquerda , dividir o preço por 100)

##################################################

def somar (*valores):
    s = 0
    for x in valores:
        s = s + x
    return s

if __name__ == "__main__":
    c = somar (3,4)
    print (c)

    print (somar())
    print (somar(1,2,3))

###################################################

def area (**kwargs):
    a = 0
    if "base" in kwargs and "altura" in kwargs:
        a = kwargs ["base"]*kwargs["altura"]/2
    return a

print (area (base=7, altura= 3))

###################################################

def isprime (p:int) -> bool :
    for k in range (2,p):
        if p%k == 0 : # Existe um divisor logo n é primo
            return False
    return True

print ("primos")
p = int (input("p= "))
if isprime(p) :
    print ("É primo")
else :
    print ("Número vulgar")

def showprimes (a:int, b:int) -> None:
    for p in range (a,b+1):
        if isprime(p):
            i += 1
            print (i, p)

showprimes (1,1000)