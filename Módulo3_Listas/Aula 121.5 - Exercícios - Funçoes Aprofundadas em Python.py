#print(" Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.")
#exercicio 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n:)
print()


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print("Erro: Digite um valor inteiro válido!")
            continue
        except KeyboardInterrupt :
            print("Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print("Error: Tivemos um problema com os dados digitados! ")
            continue
        except KeyboardInterrupt:
            print("Usuário preferiu nao informar os dados!")
            return 0
        else:
            return n


#PROGRAMA PRINCIPAL
try:
    num = leia_int("- Digite um numero inteiro: ")
    print(f"- Você digitou o numero: {num}")
    valor = leia_float("- Digite um numero real: ")
    print(f"- Você digitou o numero: {valor}")
finally:
    print("Programa finalizado. Obrigado por usar!")

