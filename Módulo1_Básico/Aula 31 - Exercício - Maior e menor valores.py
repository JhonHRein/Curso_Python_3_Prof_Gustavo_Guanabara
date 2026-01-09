print()
print()
print("Faça um programa que leia três números e mostre qual é o maior e qual é o menor.")
from random import randint
print()
n1 = randint(0, 1000)
n2 = randint(0, 1000)
n3 = randint(0, 1000)
lista = n1, n2, n3
print(f"Os Numeros para analise são os: {lista}")
print()
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print("O Menor Valor é: {}".format(menor))
print(f"O Maior valor é: {maior}")


'''# ======== Lógica para encontrar o menor número ========

#if a <= b and a <= c:     # Se A for menor ou igual a B e C, A é o menor
   # menor = a
#elif b <= a and b <= c:   # Se não, testa se B é o menor
   # menor = b
#else:                     # Se nenhum dos dois, C é o menor
 #   menor = c

# ======== Lógica para encontrar o maior número ========

#if a >= b and a >= c:     # Se A for maior ou igual a B e C, A é o maior
  #  maior = a
#elif b >= a and b >= c:   # Se não, testa se B é o maior
  #  maior = b
#else:                     # Se nenhum dos dois, C é o maior
   # maior = c

# Mostra o resultado
#print(f"O menor valor é {menor}")
#print(f"O maior valor é {maior}")'''