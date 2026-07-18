#print("Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.")
print()
from utilidadesCeV import moeda


# PROGRAMA PRINCIPAL
valor = float(input("Digite um preço R$: "))
taxa = float(input("Digite a porcentagem: "))

print(f"-Aumentando em {taxa}% é    {moeda.aumentar(valor, taxa, True)}")
print(f"-Com diminuição de {taxa}% é    {moeda.diminuir(valor, taxa, True)}")
print(f"-O Dobro é      {moeda.dobro(valor, True)}")
print(f"-E a metade é   {moeda.metade(valor, True)}")



