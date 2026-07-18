#print("Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.")
print()
lista = []
while True:
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso")
    else:
        print("Valor duplicado, sem adição na lista")
    while True:
        resp = input("Quer continuar? (s/n)").lower().strip()
        if resp in ('s', 'n'):
            break
        print("Digite apenas S para continuar ou N para sair.")

    if resp == 'n':
        break
print("Fim do programa")
print(f"Valores únicos em ordem crescente: {sorted(lista)}")



