"""print("Crie um programa  que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""
print()
print("CADASTRO DE PRODUTOS...")
print("-=-"*10)
print()
soma = caro = barato = mais_barato = 0
while True:
    produto = str(input("Qual o nome do produto?: "))
    preco = int(input("Qual o preço do produto?: "))
    soma = soma + preco
    if preco >= 1000:
        caro += 1
    if preco < 1000:
        barato = preco
        mais_barato = produto
    print("-=-"*10)
    while True:
        resp = str(input("Continuar cadastrando produtos?(S/N): ")).lower().strip()
        if resp == "s":
            print("-=-"*10)
            break
        elif resp == "n":
            print("Encerrando Cadastro...")
            sair = True
            break
        else:
            print("Resposta inválida. Digite apenas S ou N.")
    if resp == "n":
        break
print("-=-"*10)
print("FIM DO CADASTRO")
print("-=-"*10)
print(f"Total gasto na compra: {soma} Reais")
print(f"{caro} Produtos custam mais de R$1000 Reais.")
print(f"Nome do produto mais barato é: {mais_barato}")
print(f"O produto mais barato custa: {barato} Reais.")
print()
print()
#####################################################################################################################
#Versao chat gpt
print()
print("CADASTRO DE PRODUTOS...")
print("-=-" * 10)
print()

soma = caro = 0
barato = None
mais_barato = ""
primeiro = True  # flag para identificar o primeiro produto

while True:
    produto = str(input("Qual o nome do produto?: "))
    preco = int(input("Qual o preço do produto?: "))
    soma += preco

    if preco > 1000:
        caro += 1

    # Descobre o mais barato
    if primeiro or preco < barato:
        barato = preco
        mais_barato = produto
        primeiro = False

    print("-=-" * 10)

    while True:
        resp = str(input("Continuar cadastrando produtos?(S/N): ")).lower().strip()
        if resp == "s":
            print("-=-" * 10)
            break
        elif resp == "n":
            print("Encerrando Cadastro...")
            break
        else:
            print("Resposta inválida. Digite apenas S ou N.")

    if resp == "n":
        break

print("-=-" * 10)
print("FIM DO CADASTRO")
print("-=-" * 10)
print(f"Total gasto na compra: {soma} Reais")
print(f"{caro} produtos custam mais de R$1000 Reais.")
print(f"Produto mais barato: {mais_barato} custando R${barato}")

