print()
print()
print(" Faça um programa que leia um ano qualquer e mostre se ele é bissexto.")
print()
from random import randint
ano =  randint(1900, 2025)
print(ano)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Esse ano {} é bissexto".format(ano))
else:
    print("Esse ano {} não é bissexto".format(ano))