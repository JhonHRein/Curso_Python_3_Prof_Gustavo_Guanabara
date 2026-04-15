#print("Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.")
print()
from random import randint

print("JOGO DO PAR OU ÍMPAR!")
print("=*=" * 10)
vitorias = 0  # Contador de vitórias do jogador
while True:
    jogador = input("Escolha PAR ou ÍMPAR: ").strip().lower()
    # Verifica se o jogador digitou corretamente
    if jogador not in ['par', 'impar']:
        print("Opção inválida! Digite apenas 'par' ou 'impar'.")
        continue
    numero_jogador = int(input("Digite um número: "))
    numero_comp = randint(0, 10)
    total = numero_jogador + numero_comp

    print(f"Você jogou {numero_jogador} e o computador {numero_comp}. Total = {total}")

    # Verifica se o total é par ou ímpar
    resultado = 'par' if total % 2 == 0 else 'impar'

    if jogador == resultado:
        print("Você VENCEU!")
        vitorias += 1  # Conta uma vitória
    else:
        print("Você PERDEU!")
        break  # Encerra o jogo

print(f"Fim de jogo! Você venceu {vitorias} vez(es) consecutivas.")
print()
print()
from random import randint

print("JOGO DO PAR OU ÍMPAR — MELHOR DE 3!")
print("=*=" * 10)

acertos = 0
rodadas = 0

while rodadas < 3:
    comp = randint(0, 100)
    jogador = input("Par ou Ímpar? ").strip().lower()

    if jogador not in ['par', 'impar']:
        print("Opção inválida. Digite apenas 'par' ou 'impar'.")
        continue  # repete a mesma rodada

    print(f"Número gerado: {comp}")
    resultado = "par" if comp % 2 == 0 else "impar"

    if jogador == resultado:
        print("Você acertou!")
        acertos += 1
    else:
        print("Você errou!")

    rodadas += 1
    print("-" * 30)

# Resultado final
print("\nFIM DO JOGO")
print(f"Você acertou {acertos} de 3 rodadas.")

if acertos >= 2:
    print("🎉 Parabéns, você venceu!")
else:
    print("😢 Que pena, você perdeu. Tente novamente!")


###########################################################################

print()
print("Minha versao ")
print()
from random import randint
print("JOGO DO PAR OU ÍMPAR MELHOR DE 3!!")
print("=*="*10)
cont = 0
while cont != 3:
    comp = int(randint(0, 100))
    jogador = str(input("Escolhar PAR ou Ímpar: ")).lower().strip()
    print(f"Numero gerado é: {comp}")
    if comp % 2 == 0 and jogador == "par" or comp % 2 == 1 and jogador == "impar":
        print("Vitoria do Jogador")
    else:
        if jogador != "par" and jogador != "impar":
            print("Caracteres inválidos")
        print("Vitoria do Computador")
    cont += 1
print("Fim de Jogo")





