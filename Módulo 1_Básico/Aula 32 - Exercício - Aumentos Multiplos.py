print()
print()
print("Escreva um programa que pergunte o salário de um funcionário\ne calcule o valor do seu aumento. Para salários superiores a R$1250,00,\ncalcule um aumento de 10%. Para os inferiores ou iguais,\no aumento é de 15%.")
print()
print()
#Aumentos Multiplos de Salarios.
salario_real = float(input("Qual o valor atual do seu salario?: "))
result_10 = salario_real + (salario_real * 10) / 100 #aumento de 10%
result_15 = salario_real + (salario_real * 15) / 100 #aumento de 15%
print()
if salario_real >= 1250:
    print("Funcionarios com salarios de {:.2f} reais, receberao\num aumento de 10% subindo para {:.2f} reais.".format(salario_real, result_10))
else:
    print("Funcionários com salarios de {:.2f} reais. receberao\num aumento de 15% subindo para {:.2f} reais.".format(salario_real, result_15))