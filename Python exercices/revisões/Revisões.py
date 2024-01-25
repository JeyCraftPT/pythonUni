compra = int(input("Qual é o valor das compras?: "))
desconto = compra + (compra*0.05)

if compra < 100 :
    print ("O preço da compra fica a", compra, "sem os portes")
elif compra >= 100 and compra < 200:
    print ("O preço da compra fica a", compra, "com os portes")
elif compra >= 200 :
    print ("O preço da compra fica a", desconto, "com os portes")

palavra = str(input("Qual é a palavra? "))
comprimento = len(palavra)-1
while comprimento >= 0 :
    print (palavra[comprimento], end=" ")
    comprimento -= 1

print()

tamanho =int(input("Qual é o tamanho do tabuleiro? "))
inicio = 0

while True :
    if 1 <= tamanho <= 9 :
        while inicio < tamanho :                                   #Para fazer o que está para baixo para cada fila
            inicio +=1 
            valor = 0
            while valor < tamanho :                                #para escrever os números para cada fila sendo "valor" o números
                valor +=1
                if valor < tamanho :                               #dar print aos núemros todos exepto o último
                    print (" " + str(valor)+ " " + "|" , end="")   
                elif valor == tamanho :                            #dar print ao último número deles todos
                    print (" " + str(valor))
            if 0 < inicio < tamanho:                               #dar print as linhas a separar
                print ((tamanho-1)*"---+"+"---")
    else:
        print ("O valor tem de estar entre 1 e 9")
        tamanho =int(input("Qual é o tamanho do tabuleiro? "))
print ()