print()
#print("Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:5! = 5 x 4 x 3 x 2 x 1 = 120")
import math
print("CALCULADORA DE FATORIAL")
print()
numero = int(input("Digite um numero :"))
factor = math.factorial(numero)
print(f"O fatorial do numero: {numero} é {factor}")

##############################################################
print()
print("CALCULADORA DE FATORIAL")
print("versao GPT")
print()
numero = int(input("Digite um número: "))
contador = numero
fatorial = 1
print(f"{numero}! = ", end="")
while contador > 0:
    print(f"{contador}", end=" x " if contador > 1 else " = ")
    fatorial *= contador
    contador -= 1
print(f"{fatorial}")

########################################################################
print()
print("VERSAO FOR")
print("Calculadora de fatorial")
n = int(input("Digite um valor para descobrir o seu fatorial: "))
fatoria = 1
for i in range(n, 0, -1):
    print(f"{i}", end=" x " if i > 1 else " = ")
    fatoria = fatoria * i
print(f"{fatoria}")




