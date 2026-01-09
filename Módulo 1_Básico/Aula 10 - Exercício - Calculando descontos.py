#Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
print()
valor = float(input("Digite o preço do produto: "))
desconto = valor - (valor * 5 / 100)
print("Valor de produto com 5% de desconto é R$ {:.2f} Reais".format(desconto))