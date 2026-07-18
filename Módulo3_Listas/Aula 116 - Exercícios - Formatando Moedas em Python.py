#: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
print()
from utilidadesCeV import moeda


#PROGRAMA PRINCIPAL
valor = float(input("Digite um preço R$: "))
taxa = float(input("Digite a porcentage: "))

aum = moeda.aumentar(valor, taxa)
dim = moeda.diminuir(valor, taxa)
dob = moeda.dobro(valor)
met = moeda.metade(valor)

print(f"O valor {moeda.real_br(valor)}, aumentando em {taxa}% é {moeda.real_br(aum)}")
print(f"Com diminuição de {taxa}% é {moeda.real_br(dim)}")
print(f"O Dobro é {moeda.real_br(dob)}")
print(f"E a metade é {moeda.real_br(met)}")


