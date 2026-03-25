print()
print("Faça um programa que leia o peso de cinco pessoas.\nNo final, mostre qual foi o maior e o menor peso lidos.")
print()
maior = 0
menor = 0
for i in range(5):
    peso = float(input(f"Digite o {i+1}º seu peso: "))
    if i  == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso é {maior}")
print(f"O menor peso é {menor}")
