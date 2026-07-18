#print("Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.")
print()

def ficha(jog='<Desconhecido>', gol=0):
    print(f"O Jogador {jog} fez {gol} gol(s) no Campeonato.")


#PROGRAMA PRINCIPAL
n = str(input("Nome do Jogador: "))
g = str(input("Números de gols: "))
if g.isnumeric():
    g = int(g)
else:
    gol = 0
if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n, g)
