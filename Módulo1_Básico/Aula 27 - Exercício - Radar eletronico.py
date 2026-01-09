from os.path import split
from traceback import print_tb

print()
print("Escreva um programa que leia a velocidade de um carro.\nSe ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.\nA multa vai custar R$7,00 por cada Km acima do limite.")
print()
print()
from random import randint
import math
print()
carro = randint(50, 100)
print("Seu veículo passo no Radar a {} km/h.".format(carro))
print()
if carro <=80:
    print("Velocidade permitida")
elif carro >81:
    print("VOCE FOI MULTADO POR EXCESSO DE VELOCIDADE!!")
    print("Excesso de velocidade, Multa de R$ 100,00 reais e R$ 7,00 reais por km a cima da velocidade.")
print()
print()
print()
print("*"*50)
print("METODO DE EXERCICIOS CHAT GPT")
print()
print()
from random import randint

print()
print("Escreva um programa que leia a velocidade de um carro.\nSe ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.\nA multa vai custar R$7,00 por cada Km acima do limite.")
print()

carro = randint(50, 100)
print("Seu veículo passou no radar a {} km/h.".format(carro))
print()

if carro <= 80:
    print("Velocidade permitida. Dirija com segurança! 🚗💨")
else:
    excesso = carro - 80
    multa = 100 + (excesso * 7)
    print("🚨 VOCE FOI MULTADO POR EXCESSO DE VELOCIDADE!!")
    print("Você ultrapassou o limite em {} km/h.".format(excesso))
    print("Multa de R$ 100,00 fixos + R$ 7,00 por km excedente.")
    print("Valor total da multa: R$ {:.2f}".format(multa))