soluçao = list(input("Qual é a palavra a adivinhar? "))
letras = []
rabos =[]
while True :
    jogada = list(input("Qual é a tua jogada? "))
    letras = []
    founded = False
    hasIn = False
    if jogada != soluçao:
        for i in range (len(jogada)):
            if (jogada [i] == soluçao [i]):
                if not hasIn:
                    rabos.append(jogada[i])
                    print (str(jogada [i]).upper(), end="") 
                    hasIn = True
                else:
                    rabos.append(jogada[i])
                    print (str(jogada [i]).lower(), end="") 

            founded = False
            hasIn = False
            print(" | ", end="")
        print(" ") 
        rabos =[]
    else:
        for i in range (len(jogada)):
            print (str(jogada [i]).upper()," | ", end="") 
        print(" ") 
        break
