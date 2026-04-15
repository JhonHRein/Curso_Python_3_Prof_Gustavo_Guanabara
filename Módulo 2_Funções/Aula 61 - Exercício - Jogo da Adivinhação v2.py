print()
#print("Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.\nSó que agora o jogador vai tentar adivinhar até acertar, mostrando no final\nquantos palpites foram necessários para vencer.")
print()
from random import randint
print("Vou escolher um numero de 0 a 10 e voce tente adivinhar!")
maquina = randint(0, 10)
palpites = 0
jogador = 0
print()
while jogador != maquina:
    jogador = int(input("Adivinhe qual numero estou pensando entre 0 e 10: "))
    palpites += 1
    if maquina == jogador:
        print(f"Voce Acertou, o numero escolhido foi {maquina}")
    else:
        print("PEEEE, Você ERROUUUUU,\nTente de novo!")
        if jogador < maquina:
            print("Dica: Tente um número MAIOR.\n")
        elif jogador > maquina:
            print("Dica: Tente um número MENOR.\n")
print()
print(f"Foram necessários {palpites} tentativas para acertar!")


