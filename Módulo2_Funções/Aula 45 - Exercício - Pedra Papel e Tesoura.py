from random import randint
from time import sleep
print()
print("Crie um programa que faça o computador jogar Jokenpô com você.")
print("-=-"*10)
print("GAME JOKENPÔ")
print("-=-"*10)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura """)
jogador = int(input("Qual a sua jogada?: "))
print("-=-"*10)
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PÔ")
sleep(0.5)
print("-=-"*10)
print(f"VOCE ESCOLHEU: {itens[jogador]}")
print(f"COMPUTADOR ESCOLHEU: {itens[computador]}")
print()
if computador == 0:
    if jogador == 0:
        print("PEDRA com PEDRA da EMPATE!")
    elif jogador == 1:
        print("PEDRA perde para PAPEL,  JOGADOR GANHOU!")
    elif jogador == 2:
        print("PEDRA ganha de TESOURA, COMPUTADOR GANHOU!")
    else:
        print("JOGADA INVALIDA!")
elif computador == 1:
    if jogador == 1:
        print("PAPEL com PAPEL da EMPATE!")
    elif jogador == 2:
        print("PAPEL perde para TESOURA, JOGADOR GANHOU!")
    elif jogador == 0:
        print(" PAPEL ganha de PEDRA, COMPUTADOR GANHOU!")
    else:
        print("JOGADA INVALIDA!")
elif computador == 2:
    if jogador == 2:
        print("TESOURA com TESOURA, da EMPATE!")
    elif jogador == 1:
        print("TESOURA ganha de PAPEL, COMPUTADOR GANHOU!")
    elif jogador == 0:
        print("TESOURA perde de PEDRA, JOGADOR GANHOU!")
    else:
        print("JOGADA INVALIDA")
else:
    print("Fim")