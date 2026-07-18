#print("Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.")
from random import randint
print()

def sorteia():
    numeros = []
    for i in range(0, 5):
        dezenas = randint(0,99)
        numeros.append(dezenas)
    print(f"Os Numeros sorteados são: {numeros}")
    return numeros


def somapar(lista):
    total = 0
    for n in lista:
        if n % 2 == 0:
            total += n
    print(f"Total da soma dos números pares sorteados: {total}")


#Programa principal
numeros_sorteados = sorteia()
somapar(numeros_sorteados)

'''[Programa Principal] 
         |
         v
   chama sorteia()
         |
         v
   sorteia pega a lista global "numeros"
   adiciona 5 números dentro dela
         |
         v
   imprime a lista global

[Programa Principal]
         |
         v
   chama somarpar()
         |
         v
   somarpar olha a mesma lista global "numeros"
   soma só os pares
   imprime o total
[Programa Principal] 
         |
         v
   chama sorteia()
         |
         v
   sorteia cria uma lista "numeros"
   adiciona 5 números
   DEVOLVE a lista com return
         |
         v
[Programa Principal] recebe a lista
guarda em "numeros_sorteados"

[Programa Principal]
         |
         v
   chama somarpar(numeros_sorteados)
         |
         v
   somarpar recebe a lista
   soma só os pares
   imprime o total
'''



