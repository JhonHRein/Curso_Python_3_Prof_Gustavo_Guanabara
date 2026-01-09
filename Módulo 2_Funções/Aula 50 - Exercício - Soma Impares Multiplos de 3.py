print("Faça um programa que calcule a soma entre todos os números que são múltiplos de três\ne que se encontram no intervalo de 1 até 500.")
print("Soma ímpares múltiplos de três")
print()
soma = 0
cont = 0
for impares in range(0, 501):
    if impares % 3 == 0 and impares % 2 != 0: # conta para pares e impares
        print(impares,end=',')
        soma = soma + impares  #Acomulador soma +  variavel
        cont = cont + 1        #Contador  cont = 0 +1
print()
print(f"A soma de todos os valores é {soma} ")
print(f"Todos os valores solicitados é {cont}")
print("Fim da Contagem")


