#Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente.
from math import radians
import math
angulo = float(input("Digite o valor do ângulo: "))
rad = math.radians(angulo)
cos = math.cos(rad)
sen = math.sin(rad)
tgn = math.tan(rad)
print(f"- O angulo de: {angulo:.2f}º\n- Angulo de seno: {sen:.2f}º\n- Angulo de cosseno: {cos:.2f}º\n- Angulo da tangente: {tgn:.2f}º ")
print()
print("__"*80)
print("Segundo Método Curso em video")
#Formataçao antiga no exemplo .format
import math
ang = float(input("Digite um novo angulo:"))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tgn = math.tan(math.radians(ang))
print("O Angulo de {}º\n tem o seno de {:.2f}º\nO cosseno de {:.2f}º\ntangente de {:.2f}".format(ang,seno,coss,tgn))