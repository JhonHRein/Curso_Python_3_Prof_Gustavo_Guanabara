print()
"""print("Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.")"""
print()
homem = 0
maioridade_18 = 0
mulheres_menos_18 = 0
while True:
    sexo = str(input("Qual o seu sexo? (Homem/Mulher): ")).lower().strip()
    idade = int(input("Qual a sua idade?: "))
    if sexo in ["homem", "h", "H"]:
        homem += 1
    if idade >= 18:
        maioridade_18 += 1
    if sexo in ["mulher", "m", "M"] and idade < 18:
        mulheres_menos_18 += 1
    prox = str(input("Quer continuar? Sim para continuar, Não para encerrar: ")).lower().strip()
    if prox in ["sim", "s"]:
        continue
    elif prox in ["nao", "n"]:
        break
print(f"Numero de pessoas com maioridade {maioridade_18}")
print(f"Numero de homens cadastrados {homem}")
print(f"Numero de mulheres com menoridade {mulheres_menos_18}")

