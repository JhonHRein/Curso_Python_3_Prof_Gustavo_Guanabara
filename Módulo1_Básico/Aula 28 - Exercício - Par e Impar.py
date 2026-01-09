print()
print()
print("Crie um programa que leia um número inteiro\ne mostre na tela se ele é PAR ou ÍMPAR.")
print()
from random import randint
numero = randint(1, 999)   #Uso o randint para simular um usuário, assim só dou Run no programa!
print("O numero sorteado é: {}".format(numero))
if numero % 2 == 0:
    print("Este numero é Par")
else:
    print("Este numero é ímpar")