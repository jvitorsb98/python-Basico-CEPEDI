import random
import os
erros = 0
sorteado = random.randrange(0,100)
jogador=int(input("Digite seu numero: "))
while(sorteado!=jogador):
    if sorteado < jogador:
        print("Chutou alto demais")
    else:
        print("Chutou baixo demais")
    erros +=1
    jogador=int(input("Digite seu numero: "))
print("Parabens!!")
print("Acertou com " + str(erros) + "erros")