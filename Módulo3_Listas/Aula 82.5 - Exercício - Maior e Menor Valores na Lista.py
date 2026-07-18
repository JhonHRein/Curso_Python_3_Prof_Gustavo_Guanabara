#print("Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.")
print()
valores = []
maior = menor = 0
for cont in range(0,5):
    num = int(input("Digite um valor: "))
    valores.append(num)
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f"A lista com os valores digitados sao: {valores}")
for posi, val in enumerate(valores):
    print(f"Na posição: {posi} temos o valor {val}")
print(f"\nO maior valor digitado foi {maior} nas posições: ", end="")
for i, v in enumerate(valores):
    if v == maior:
        print(i, end=" ")
print(f"\nO menor valor digitado foi {menor} nas posições: ", end="")
for i, v in enumerate(valores):
    if v == menor:
        print(i, end=" ")
