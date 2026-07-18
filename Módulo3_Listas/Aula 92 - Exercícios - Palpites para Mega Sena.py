"""""#print(" Faça um programa que ajude um jogador da mega-sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.")
print()
from random import randint
from time import sleep
print("*"*5,"Programa Gerador de Palpites para Mega-Sena","*"*5)
print("-=-"*19)
print()
while True:
    lista_principal = [] #Add pelo chat GPT boa prática
    valor = int(input("Digite o valor de quantos jogos deseja gerar?: "))
    lista_principal.clear()
    for n in range(valor):
        lista_temp = []
        while len(lista_temp) < 6:
            gerador = randint(1, 61)
            if gerador not in lista_temp:
                lista_temp.append(gerador)
        lista_principal.append(lista_temp)
    print("Palpites de Dezenas por jogo:")
    for i, jogo in enumerate(lista_principal, 1):
        print(f"Jogo {i}: {sorted(jogo)}")
    print(f"Palpites de Dezenas por jogo:\n{lista_principal}")
    while True:
        resp = str(input("Deseja Gerar mais palpites? (S/N)")).strip().lower()
        if resp in ("n", "s"):
            break
        else:
            print("Resposta inválida, apenas (S/N)")
    if resp == "n":
        print("Fim do Gerador de palpites.")
        break"""

########################################################################
# RESOLUÇÃO PROFESSOR GUANABARA.
from random import randint
print()
lista = list()
jogos = list()
quant = int(input("Quantos jogos voce quer que eu sorteie?: "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")








