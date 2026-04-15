print()
#print("Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.")
resp = "S"
soma = 0
maior = menor = 0
quant = 0
while resp in "Ss":
    num = int(input("Digite um valor: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer Continuar [S/N]: "))
media = soma / quant
print(f"Foram Digitados {quant} números.")
print(f"O menor número é o {menor}, o maior é: {maior}, e a média é: {media}")



















