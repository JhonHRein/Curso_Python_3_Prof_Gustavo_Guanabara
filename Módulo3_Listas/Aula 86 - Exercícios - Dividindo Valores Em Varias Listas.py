#print("Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.")
print()
tab_geral: list[int] = []
tab_par: list[int] = []
tab_impares: list[int] = []
while True:
    num = (int(input("Digite um valor numérico: ")))
    tab_geral.append(num)
    if num  % 2 == 0:
        tab_par.append(num)
    elif num % 2 == 1:
        tab_impares.append(num)
    while True:
        resp = str(input("Quer continuar ? (S/N)")).strip().lower()
        if resp in ("s","n"):
            break
        print("Resposta inválida, apenas digite: (S/N)")
    if resp == "n":
        print("Fim do programa")
        break
print()
print("-=-"*13)
print(f"Números pares digitados: {tab_par}")
print(f"Números ímpares digitados: {tab_impares}")
print(f"Todos os números digitados :{tab_geral}")






