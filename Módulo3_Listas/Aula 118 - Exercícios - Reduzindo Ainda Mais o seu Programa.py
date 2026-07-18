#print("Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui. ")
print()
from utilidadesCeV import moeda
#PROGRAMA PRINCIPAL
num = float(input("Digite o preço: R$"))
moeda.resumo(num, 20, 12)