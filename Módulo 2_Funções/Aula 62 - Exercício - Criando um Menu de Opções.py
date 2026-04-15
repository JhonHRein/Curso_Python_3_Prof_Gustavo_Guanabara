from time import sleep
from random import randint

print("\n.....MENU DE OPÇÕES.....\n")

opcao = 0  # inicialização da variável para entrar no while
valor = 0
novo_valor = 0

while opcao != 5:
    print("Escolha uma das opções abaixo:")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do Programa")

    opcao = int(input("Digite o número da opção escolhida: "))
    print()

    # Somar, multiplicar e comparar requerem valores
    if opcao in [1, 2, 3]:
        valor = int(input("Digite um valor: "))
        novo_valor = int(input("Digite um novo valor: "))

        if opcao == 1:
            soma = valor + novo_valor
            print(f"A soma entre {valor} e {novo_valor} é {soma}")
        elif opcao == 2:
            multi = valor * novo_valor
            print(f"A multiplicação entre {valor} e {novo_valor} é {multi}")
        elif opcao == 3:
            maior = valor if valor > novo_valor else novo_valor
            print(f"O maior valor entre {valor} e {novo_valor} é {maior}")

    elif opcao == 4:
        valor = randint(0, 999)
        novo_valor = randint(0, 999)
        print(f"Novos números gerados:\n[1] {valor}\n[2] {novo_valor}")

    elif opcao == 5:
        print("Finalizando menu de opções...")
        sleep(1.5)
        print("Programa encerrado com sucesso!")

    else:
        print("Opção inválida! Tente novamente.")

    print()  # Espaço entre as execuções do menu
