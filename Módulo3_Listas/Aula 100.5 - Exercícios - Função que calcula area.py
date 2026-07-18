#print(" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.")
print()
def area(largura, comprimento):
    total = largura * comprimento
    print(f"A área de um terreno com {largura}m² de largura e {comprimento}m² de comprimento\nmede um total de {total}m²")


def edi():
    print("CONTROLE DE TERRENO")
    print("=-="*12)

#Programa Principal
edi()
larg  = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
area(largura=larg, comprimento=comp)


