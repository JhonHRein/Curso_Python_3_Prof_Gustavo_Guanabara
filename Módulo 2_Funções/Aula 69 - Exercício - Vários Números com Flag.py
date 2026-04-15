print()
#print("Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).")
cont = soma = 0
while True:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f"A contagem dos numeros Digitados: {cont} tentativas")
print(f"A somatoria dos numeros : {soma}")