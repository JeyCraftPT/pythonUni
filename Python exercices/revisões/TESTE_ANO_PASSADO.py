print("Exercício 1")
print()
print()

n = float(input("Indique o Valor Gasto: "))

if n >= 200:
    print("O Valor Total é de " + str((n-n*0.05)) + "€ e com Portes de Oferta.")
elif n >= 100:
    print("O Valor Total é de " + str(n) + "€ e com Portes de Oferta.")
else:
    print("O Valor Total é de " + str(n) + "€ Sem Portes Incluídos.")

print("============================")
print()
print("Exercício 2")
print()
print()

palavra = str(input("Escreva Uma Palavra: "))
tamanho_palavra = len(palavra)-1
palavra_contrario = ""

while tamanho_palavra >= 0:
    print("Índice: " + str(tamanho_palavra))
    if tamanho_palavra == 0:
        palavra_contrario += palavra[tamanho_palavra]
    else:
        palavra_contrario += palavra[tamanho_palavra] + " "
    tamanho_palavra -= 1

print(palavra_contrario)

print("============================")
print()
print("Exercício 3")
print()
print()

tamanho = int(input("Tamanho da Matriz: "))
inicio = 0

while True:
    if 1 <= tamanho <= 9:
        while inicio < tamanho:
            inicio += 1
            valor = 0
            while valor < tamanho:
                valor += 1
                if valor == tamanho:
                    print(" " + str(valor) + " ")
                else:
                    print(" " + str(valor) + " " + "|", end="")

            if 0 < inicio < tamanho:
                print((tamanho-1)*"---+" + "---")
    else:
        print("Valor Inválido. Insira um Valor Entre 1 e 9.")
        tamanho = int(input("Tamanho da Matriz: "))

