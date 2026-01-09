print("Desenvolva um programa que leia o comprimento de três retas\ne diga ao usuário se elas podem ou não formar um triângulo.")
print("Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar\nque tipo de triângulo será formado:\n– EQUILÁTERO: todos os lados iguais\n– ISÓSCELES: dois lados iguais, um diferente\n– ESCALENO: todos os lados diferentes")
print()
print()
ang_1 = int(input("Digite um valor entre 0 e 999: "))
ang_2 = int(input("Digite um segundo valor: "))
ang_3 = int(input("Digite um terceiro valor: "))
lista = ang_1, ang_2, ang_3
print()
print(f"Os números escolhidos são: {lista}")
print()
if (ang_1 < ang_2 + ang_3)and(ang_2 < ang_1 + ang_3)and(ang_3 < ang_1 + ang_2):
    print("A soma dos valores formam um triangulo perfeito.")
else:
    print("A soma dos valores nao formam um triangulo perfeito.")
if ang_1 == ang_2 == ang_3:
    print("Equilátero: Todos os lados iguais. ")
elif ang_1 != ang_2 and ang_2 != ang_3 and ang_1 != ang_3: # linha corrigida pelo gpt, erro de logica.
    print("ESCALENO: Todos os lados diferentes. ")
else:
    print("Isósceles: Dois lados iguais, um diferente. ")


