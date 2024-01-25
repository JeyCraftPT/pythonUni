L = []
B = int(input("número1 "))
C = int(input("número2 "))
A = int(input("Diz um número: "))
while A > 0:
    if A != 0:
        L.append(A)
        A = int(input("Diz um número: "))
def valida(L:list, B:int , C:int) -> bool:
    D = False
    for a in range(len(L)-1):
        if L[a] >= B or L[a] <= C:
            D = True
            break
        else:
            D = False
            break
    return D
print ("Válida(", L, ",",B,",",C,")====>",valida(L, B, C))

#################################################################################

L = []
B = int(input("número1 "))
C = int(input("número2 "))
A = int(input("Diz um valor para a lista: "))

while A > 0:
    if A != 0:
        L.append(A)
        A = int(input("Diz um valor para a lista: "))

def valida(L:list, B:int , C:int) -> bool:
    D = False
    for a in range(len(L)-1):
        if L[a] >= 0 or L[a] <= 20:
            D = True
        else:
            D = False
            break
    return D

if valida(L):
    for o in range (len(L)):
        print (L[o], " ", L[o]*"|")

#################################################################################

A = str(input("Diz cenas: "))
A = A.split()
def contanegas (A:str) -> int:
    A = A.count ("nao")
    return A
print (contanegas(A))
