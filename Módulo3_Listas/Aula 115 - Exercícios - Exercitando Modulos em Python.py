#print("Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.")
# programa principal

from utilidadesCeV import moeda

valor = float(input("Digite um preço R$: "))
taxa = int(input("Digite a porcentage: "))
aum = moeda.aumentar(valor, taxa)
dim = moeda.diminuir(valor, taxa)
dob = moeda.dobro(valor)
met = moeda.metade(valor)

print(f"O valor {valor} aumentando em {taxa}% é R$: {aum}")
print(f"Com diminuição de {taxa}% é R$: {dim}")
print(f"O Dobro é R$: {dob}")
print(f"E a metade é R$: {met}")


############################################################################

""""# ===== MÓDULO MOEDA =====
def aumentar(num, taxa):
    return num + (num * taxa / 100)

def diminuir(num, taxa):
    return num - (num * taxa / 100)

def dobro(num):
    return num * 2

def metade(num):
    return num / 2


# ===== PROGRAMA PRINCIPAL =====
valor = float(input("Digite um preço R$: "))
taxa = float(input("Digite a porcentagem (%): "))

aum = aumentar(valor, taxa)
dim = diminuir(valor, taxa)
dob = dobro(valor)
met = metade(valor)

print(f"\nO valor {valor} aumentando em {taxa}% é R$: {aum}")
print(f"Com diminuição de {taxa}% é R$: {dim}")
print(f"O Dobro é R$: {dob}")
print(f"E a metade é R$: {met}")"""

