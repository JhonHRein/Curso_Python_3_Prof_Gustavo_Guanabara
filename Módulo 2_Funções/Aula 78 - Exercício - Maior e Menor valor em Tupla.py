#print("Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla")
import random
print()
from random import randint
aleotorios = [random.randint(0, 99) for _ in range(5)]
sorteio = tuple(aleotorios)
print(f"Os numeros sorteados é: {sorteio}")
print(f"O maior numero sorteado é: {max(sorteio)}")
print(f"O menor numero sorteado é: {min(sorteio)}")


