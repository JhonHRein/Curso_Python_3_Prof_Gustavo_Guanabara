print()
print()
print("Desenvolva um programa que leia o comprimento de três retas\ne diga ao usuário se elas podem ou não formar um triângulo.")
print()
print()
from random import randint #Metodo usando randint para simular usuario.
r11 = randint(0, 999)
r22 = randint(0, 999)
r33 = randint(0, 999)
listaa = r11, r22, r33
print(listaa)
if r11 < r22 + r33 and r22 < r11 + r33 and r33 < r11 + r22:
    print("A soma dos valores formam um triangulo perfeito")
else:
    print("A soma dos valores nao formam um triangulo perfeito")
print()
print("-="*50)
print()
print()
r1 = float(input("Primeiro segmento: ")) #Metodo " analogico"
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
lista = r1, r2, r3
print(lista)
print("Analisador de triangulos")
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar triangulos")
else:
    print("Os segmentos acima nao podem formar triangulos")