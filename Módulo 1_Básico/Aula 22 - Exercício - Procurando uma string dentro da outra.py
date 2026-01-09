# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
print()
nome = str(input("Digite seu nome: ")).strip()
print("Seu nome tem Silva? {}".format("SILVA" in nome.upper())) #Deixando a variavel original e colocando Upper apenas no print, onde precisa
