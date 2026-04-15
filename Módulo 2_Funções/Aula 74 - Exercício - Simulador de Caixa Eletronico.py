"""print("Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.\nconsidere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.")"""
from time import sleep

print(".............BANCO CODEX..................")
print("........Seu Dinheiro Sempre Inseguro....")
print()
print("      CÉDULAS DISPONÍVEIS: R$50 - R$20 - R$10 - R$1")
print()

# Pergunta quanto o usuário quer sacar
saque = int(input("DIGITE O VALOR DO SAQUE R$: "))
print("Processando....")
sleep(2)
print("Contando notas....")
sleep(2)
print("=" * 30)

# Variável que representa o valor total que ainda falta sacar
total = saque

# Começamos pelas maiores cédulas
ced = 50

# Contador de cédulas de cada valor
totalced = 0

# Loop que vai rodar até que o total a sacar chegue a 0
while True:
    # Enquanto o valor da cédula atual ainda cabe no total do saque
    if total >= ced:
        total -= ced  # Subtrai o valor da cédula do total
        totalced += 1  # Conta uma cédula usada
    else:
        # Se usou alguma cédula dessa, mostra o total usado
        if totalced > 0:
            print(f"Total de {totalced} cédulas de R${ced}")

        # Troca para a próxima cédula menor
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        # Reinicia o contador para a nova cédula
        totalced = 0

        # Se já deu todo o dinheiro, termina o loop
        if total == 0:
            break

