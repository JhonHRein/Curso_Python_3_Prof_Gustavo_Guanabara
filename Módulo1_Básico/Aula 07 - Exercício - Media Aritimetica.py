# Desenvolva um programa que leia as duas notas de um aluno e calcule e mostre sua média.
print()

nota_01 = float(input("Digite o valor da sua nota, prova n.1º: "))
nota_02 = float(input("Digite o valor da sua nota, prova n.2º: "))

media = (nota_01 + nota_02) / 2  #Aplicação de ordem de procedencia no calculo.
print()
print("=-="*12)
print(f"A média entre as duas notas é: {media}")
print("=-="*12)