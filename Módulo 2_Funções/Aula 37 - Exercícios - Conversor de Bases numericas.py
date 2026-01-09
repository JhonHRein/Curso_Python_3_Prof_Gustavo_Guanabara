print()
print("Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer\ne peça para o usuário escolher qual será a base de conversão:\n1 para binário, 2 para octal e 3 para hexadecimal.")
print()
print()
numero = int(input("Digite um número aleatório:"))
print("=-="*20)
print("Escolha a base de conversão:\n[ 1 ] BINARIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL")
resu = int(input("Qual a sua opção:"))
if resu == 1:
    print("O numero {} convertido para binario é: {}".format(numero, bin(numero)[2:]))
elif resu == 2:
    print("O numero {} convertido para octal é : {}".format(numero, oct(numero)[2:]))
elif resu == 3:
    print("O numero {} convertido para hexadecimal é : {}".format(numero, hex(numero)[2:]))
else:
    print("Escolha uma das alternativas.")

