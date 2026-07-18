#print("Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista. No final, mostre:\nA) Quantas pessoas foram cadastradas.\nB) Uma listagem com as pessoas mais pesadas.\nC) Uma listagem com as pessoas mais leves.)
print()
cadastro = []
pessoas = []
maior = menor = 0
while True:
    pessoas.append(str(input("Qual seu nome? ")))
    pessoas.append(int(input("Qual seu peso em kg? ")))
    cadastro.append(pessoas[:])
    if len(cadastro) == 1:          # bloco if para menor e maior peso!
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    pessoas.clear()
    while True:                    # Bloco WHILE para validação se quer continuar!
        resp = str(input("Quer continuar (S/N)")).strip().lower()[0]
        if resp in ("s", "n"):
            break
        else:
            print("Resposta Inválida, apenas S ou N")
    if resp == "n":
        print("Fim do programa")
        break
print(f"\nTotal de pessoas cadastradas: {len(cadastro)}")
print(f"O maior peso foi de {maior}kg. Peso de:", end=' ')
for p in cadastro:
    if p[1] == maior:
        print(f"[{p[0]}]", end=' ')
print()
print(f"O menor peso foi de {menor}kg. Peso de:", end=' ')
for p in cadastro: # bloco FOR para selecionar a pessoa que corresponde ao menor peso!
    if p[1] == menor:
        print(f"[{p[0]}]", end=' ')
