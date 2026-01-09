#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print()
salario = float(input("Digite o valor do seu ordenado salarial: "))
salario_aumento_15 = salario + ((salario * 15) / 100)
print(f"O valor do salario atualizado com 15% é de: R$ {salario_aumento_15:.2f} reais;")