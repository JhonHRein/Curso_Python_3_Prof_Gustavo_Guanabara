from random import randint
from time import sleep

print("\nJOGO: JOKENPÔ")
print("-=-" * 10)
print("""Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura""")

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

try:
    jogador = int(input("Qual a sua jogada?: "))
    if jogador not in [0, 1, 2]:
        raise ValueError  # força o erro para o except abaixo

    print("-=-" * 10)
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PÔ!")
    sleep(0.5)
    print("-=-" * 10)

    print("Computador jogou: {}".format(itens[computador]))
    print("Jogador jogou: {}".format(itens[jogador]))

    if computador == jogador:
        print("EMPATE!")
    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print("VOCÊ VENCEU!")
    else:
        print("COMPUTADOR VENCEU!")

except ValueError:
    print("Jogada inválida! Digite apenas 0, 1 ou 2.")
