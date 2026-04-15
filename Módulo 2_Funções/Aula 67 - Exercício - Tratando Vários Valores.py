print()
#print("Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o utilizador digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)")
print()
cont = 0
soma = 0
while cont != 999:
    num = int(input("Digite um valor de 0 a 999: "))
    if num > 1000:
        print("Valor Invalido")
    elif num == 999:
        break
    else:
        cont += 1
        soma += num
print(f"Foram digitados {cont} tentativas, ate o fim")
print(f"A soma dos números é: {soma}")
##########################################################################
print()
print()
contador = 0
somatoria = 0
numero = 0
while numero != 999:
    numero = int(input("Digite um valor até 999: "))
    contador += 1
    soma += numero
    if numero == 999:
        break
print(f"foram digitados {numero} numeros")
print(f"A soma entre os números digitados é {soma}")