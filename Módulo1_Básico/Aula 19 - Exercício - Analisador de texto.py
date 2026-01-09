#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
print()
nome = str(input("Digite seu nome: ")).strip()   #Acrescentando o .strip() no final da str, tira os epaços nas pontas.
print("Analisando seu Nome....puff")
print("Caracteres total no nome: {}".format(len(nome)))
print("Nome em letras Maiúsculas: {}".format(nome.upper()))
print("Nome com todas as letras minúsculas: {}".format(nome.lower()))
print("Caracteres total sem espaços: {}".format(len(nome.replace(" ",""))))    #metodo 01
print("Caracteres total sem espaços: {}".format(len(nome) - nome.count(" ")))  #metodo 02
print("Caracteres total no primeiro nome: {}".format(nome.find(" ")))  #metodo 01
separa = nome.split() #metodo 02
print(separa)
print("Seu primeiro nome é {}  e ele tem {} letras".format(separa[0], len(separa[0])))