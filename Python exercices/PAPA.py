numeros = [23, 47, 84, 12]
i = int(input("Indique um número: "))

for x in range(len(numeros)):
    if numeros[x] == i:
        print("Arrroz")

produtos = { "cerveja":32, "massa":47, "cafe": 25}
produto = str(input("Indique um produto a procurar: "))

def verificar_produto(list, product):
    exist = False
    for x in list.keys():
        if x == product:
            exist = True

    return exist

produto_existente = verificar_produto(produtos, produto)
if produto_existente:
    print("Este produto existe na lista de produtos.")
else:
    print("Este produto não existe na lista de produtos.")
