#print("Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)")
print()
def leiaInt(mensagem):
    valor = input(mensagem)
    return valor


# PROGRAMA PRINCIPAL
n = leiaInt("Digite um numero: ")
if n.isnumeric():
    print(f"Voce Acabou de digitar o numero {n}")
else:
    print("Valor inválido!")


######################################################################
#Versao corrigida do GPT

def leiaInt(mensagem):
    while True:  # laço para repetir até receber um valor válido
        valor = input(mensagem)
        if valor.isnumeric():
            return int(valor)  # retorna como número inteiro
        else:
            print("ERRO! Digite um número inteiro válido.")

# PROGRAMA PRINCIPAL
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")

###############################################################################
#VERSAO DO PROF. GUANABARA

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\33[0;31mERRO! digite um numero inteiro válido.\33[m")
        if ok :
            break
    return valor


#PROGRAMA PRINCIPAL
n = leiaInt("Digite um valor: ")
print(f"Você acabou de digitar o numero {n}")




