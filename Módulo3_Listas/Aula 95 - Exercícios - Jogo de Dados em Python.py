#print("Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.")
from random import randint
print("==JOGO DADOS DA SORTE==")
print("=-="*12)
jogo = {}
for i in range(1, 5):
    jogo[f'Jogador {i}'] = randint(1, 6)
for jogador, valor in jogo.items():
    print(f'- {jogador} tirou {valor} no dado')
print("=-="*12)
print("== RANKING DOS JOGADORES==")
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)
for pos, (jogador, valor) in enumerate(ranking, start=1):
    print(f'{pos}º lugar: {jogador} com {valor}')



