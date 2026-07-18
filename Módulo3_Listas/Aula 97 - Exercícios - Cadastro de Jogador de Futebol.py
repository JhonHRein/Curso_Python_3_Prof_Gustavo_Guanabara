#print("Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.")
print()
print("==== GERENCIAMENTO DE JOGADORES ==== ")
print("=-="*20)
rendimento = dict()
gols = list()
total_gols = 0
rendimento['Nome do jogador'] = str(input("Nome do Atleta: "))
num_partidas = int(input(f"Quantas partidas o {rendimento['Nome do jogador']} jogou?: "))
for c in range(num_partidas):
    gol = int(input(f"Quantos gols na partida {c +1}: "))
    gols.append(gol)

rendimento['Gols'] = gols  # Armazena a lista no dicionário
rendimento['Total de gols'] = sum(gols)  # Soma total de gols

print("=-="*20)
print(f"==== RENDIMENTO DO ATLETA:    {rendimento['Nome do jogador'].upper():>7}  ====")
print()
for chave, valor in rendimento.items():
        print(f"- {chave:<20}: {valor}")
print()
print("Gols por partida:")
for i, g in enumerate(rendimento['Gols']):
    print(f"  → Partida {i+1}: {g} gol(s)")



