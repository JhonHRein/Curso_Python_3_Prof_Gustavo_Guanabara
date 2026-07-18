#print("Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.")
print()
matriz = []
for linha in range(3):#para cada linha até 3
    linha_temp = [] # lista temporária
    for coluna in range(3): # para cada coluna até 3
        valor = int(input(f"Digite um valor para [{linha},{coluna}]: "))
        linha_temp.append(valor) #Adiciona números de valor dentro da linha_temp.
    matriz.append(linha_temp) #Adiciona os números de linha_temp em matriz.
print(f"Matriz final")
for l in matriz:  #Para ler cada indice da lista Matriz.
    print(l)

###############################################################################
#Codigo do Professor Guanabara


"""matriz = [0,0,0], [0,0,0], [0,0,0]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}],[{c}]: "))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end="")"""
