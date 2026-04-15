#print("Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.")
print()
cont = 0
print("Digite um numero para calcular a sua tabuada\nou digite (-1) para sair do programa.")
while True:
    num = int(input("Digite um numero: "))
    if num < 0:
        break
    for cont in range(1, 11):
        print(f" {num} x {cont} = {num*cont}")
print("Fim de Calculo")



