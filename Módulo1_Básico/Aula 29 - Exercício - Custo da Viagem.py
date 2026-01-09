print()
print()
print("Desenvolva um programa que pergunte a distância de uma viagem em Km.\nCalcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km\ne R$0,45 para viagens mais longas.")
print()
distancia = float(input("Digite a quilometragem a ser percorrida: "))
import math
pas_01 = distancia * 0.50
pas_02 = distancia * 0.45
if distancia <= 200:
    print("O valor da sua passagem será de R$ {:.2f} reais.\nTarifa de R$ 0,50 Centavos por quilometro.".format(pas_01))
else:
    print("O valor da sua passagem sera de R$ {:.2f} reais.\nTarifa de R$ 0,45 Centavos por quilometro.".format(pas_02))
19//2
