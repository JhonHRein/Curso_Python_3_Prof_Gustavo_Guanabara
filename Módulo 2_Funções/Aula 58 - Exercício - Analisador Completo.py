print()
print("Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.\nNo final do programa, mostre: a média de idade do grupo\nqual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.")
print()
total_de_idades = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menores_20 = 0
for i in range(4):
    print(f"Pessoa {i+1}:")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite o sexo (M/F)").strip().lower()
    total_de_idades += idade

    if sexo == "m" and idade > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = idade
    if sexo == "f" and idade < 20:
        mulheres_menores_20 += 1

media_idade = total_de_idades / 4

print(f"Média de idade do grupo:  {media_idade:.2f}")
print(f"O homem mais velho é: {homem_mais_velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menores_20}")