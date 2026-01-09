#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
print()
altura = float(input("Qual a altura da parede?:"))
largura = float(input("Qual a largura da parede?:"))
#Cada Litro de tinta pinta 2m².
m2 = altura * largura
print("Essa parede tem: {}m²".format(m2))
tinta = m2 / 2
print("São necessários {:.1f} Litros de Tinta para pintar uma parede de {}m²".format(tinta,m2))