print()
print("Crie um programa que leia o ano de nascimento de sete pessoas.\nNo final, mostre quantas pessoas ainda não atingiram a maioridade\ne quantas já são maiores.")
print()
from datetime import date
data_atual = date.today().year
soma_maior = 0
soma_menor = 0
for i in range(7):
    idade_real = int(input(f"{i + 1}ª pessoa - Digite o ano do seu nascimento: "))
    idade_somada = data_atual - idade_real
    if idade_somada <= 17:
        soma_menor += 1
    else:
        soma_maior += 1
print(f"{soma_menor} pessoas nao atingiram a maioridade.")
print(f"{soma_maior} pessoas ja atingiram a maioridade.")