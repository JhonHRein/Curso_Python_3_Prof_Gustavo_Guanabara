#print("Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.")
print()
lista = []
while True:
    for c in range(5):
        num = int(input("Digite um valor:"))
        if not lista or num > lista[-1]:
            lista.append(num)
            pos = len(lista) - 1
        else:
            pos = 0
            while pos < len(lista) and num > lista[pos]:
                pos += 1
            lista.insert(pos, num)
        print(f"O número {num} foi adicionado na posição: {pos} da lista!")
    print(f"Os valores digitados em ordem são: {lista}")
    while True:
        resp = str(input("Quer continuar: [S/N] ")).strip().lower()
        if resp in ( "s", "n"):
            break
        print("Resposta inválida! Digite apenas S ou N.")
    if resp == "n":
        print("Fim do programa!")
        break
#######################################################################################
#PROFESSOR GUANABARA!

list = []
for c in range(0,5):
    n = int(input("Digite um numero: "))
    if c == 0 or n > list[-1]:
        list.append(n)
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                break
            pos += 1
print(f"Os valores digitados em ordem foram: {list}")






