#print("Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.)
print()
matriz = []
pares = []
impares = []
total = 0
#Construção da matriz 3x3
for linha in range(3):
    temp = []
    for coluna in range(3):
        num = int(input(f"Digite um valor para: "))
        temp.append(num)
#Identificadores de pares e ímpares
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    matriz.append(temp)
tot_par = sum(pares)
#estruturação da matriz 3x3
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end="")
    print()
#Soma da Terceira coluna da Matriz
for linha in matriz:
    total += linha[2]
print(f"Soma total de números pares: {tot_par}")
print(f"Soma dos valores da terceira coluna: {total}")
print(f"Valores da segunda linha: {matriz[1]} e o maior numero é o: {max(matriz[1])}")


