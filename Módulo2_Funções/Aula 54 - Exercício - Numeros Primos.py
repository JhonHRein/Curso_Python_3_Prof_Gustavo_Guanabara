print("Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.")
print()
numero = int(input("Digite um numero qualquer: "))
if numero <= 1:
    print(f"O numero: {numero} NÃO É PRIMO.")
elif numero == 2:
    print(f"O numero: {numero} É PRIMO")
else:
    eh_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            eh_primo = False
            break
        if eh_primo:
            print(f"O numero: {numero} É PRIMO")
        else:
            print(f"O numero: {numero} É COMPOSTO.")

