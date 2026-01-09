#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
print()
print()
cidade = str(input("Digite o nome de uma cidade brasileira qualquer:")).strip()
print("Analisando se essa Cidade: {}, possui o nome SANTO em sua composição....".format(cidade))
print(cidade[:5].upper() == "Santo")



