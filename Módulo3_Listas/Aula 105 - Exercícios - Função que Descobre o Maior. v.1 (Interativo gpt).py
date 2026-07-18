def linha():
    print("=-=" * 20)


def maior(*valores):
    if len(valores) == 0:
        print("Nenhum valor foi informado.")
        return

    maior_num = max(valores)
    total = len(valores)

    print(f"Analisando valores: {valores}")
    print(f"Foram informados {total} valores ao todo.")
    print(f"O maior valor informado foi {maior_num}.")


# Programa principal
linha()
print("Bem-vindo ao analisador de números!")
todos_valores = []  # lista que vai acumular todos os números de várias rodadas

continuar = True
while continuar:
    valores_usuario = []
    print("Digite números para esta rodada. Digite 0 para parar.")

    # Loop de entrada de números
    while True:
        num = int(input("Digite um número: "))
        if num == 0:
            break
        valores_usuario.append(num)
        todos_valores.append(num)  # adiciona também na lista global

    linha()
    maior(*valores_usuario)  # mostra maior da rodada
    linha()

    # Pergunta se quer continuar
    resp = input("Deseja adicionar novos números? [S/N]: ").strip().upper()
    if resp != "S":
        continuar = False

# Mostra o maior de todas as rodadas
linha()
print("Resumo final de todas as rodadas:")
maior(*todos_valores)
linha()
print("Programa finalizado. Obrigado!")
