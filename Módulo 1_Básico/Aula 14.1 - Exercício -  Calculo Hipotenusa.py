#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, e mostre o comprimento da hipotenusa.
print()
import math
cto = float(input("Digite o valor do Cateto Oposto: "))
cta = float(input("Digite o valor do Cateto adjacente: "))
hip = math.hypot(cto, cta)
print(f"O valor da soma entre os catetos CO: {cto} e CA: {cta} mede {hip:.2f45} da Hipotenusa")