#ENUNCIADO DO EXERCÍCIO 95
#print("Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.")
#print(Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.)
print("==== GERENCIAMENTO DE JOGADORES ==== ")
print("=-="*15)
print()
dados = list()
gol = list()
soma = porcent = 0
while True:
    jogador = dict()  #Dicionario dentro do while, para renovar os dados com novo dicionário a cada volta
    gols_por_partida = list()
    jogador['Nome'] = str(input("Atleta: "))
    num_partidas = int(input(f"Quantas partidas o {jogador['Nome']} Jogou: "))
    jogador['Partidas'] = num_partidas
    for c in range(num_partidas):
        gols = int(input(f"Gols por Partida - {c +1}º Jogo: "))
        gols_por_partida.append(gols)

    jogador['Gols'] = gols_por_partida
    jogador['Total'] = sum(gols_por_partida)
    jogador['Aproveitamento'] = (jogador['Total'] * 100) // num_partidas if num_partidas > 0 else 0 #Se o número de partidas for maior que 0, faz o cálculo
#Caso contrário, o aproveitamento será 0
    dados.append(jogador.copy())
    while True:
        resp = str(input("Quer Continuar? [S/N]: ")).lower()[0]
        if resp in "sn":
            break
        print("Resposta inválida, apenas S ou N")
    if resp == "n":
        print("Fim do Gerenciador de Atleta")
        break
print()
print("==== APROVEITAMENTO DE TODOS OS ATLETAS ====")
print("=-="*15)
for atleta in dados:
    print(f"- \nJogador: {atleta['Nome']}")
    print(f"- Total de gols: {atleta['Total']}")
    print(f"- Partidas jogadas: {atleta['Partidas']}")
    print(f"- Aproveitamento: {atleta['Aproveitamento']}%")
    print("- Gols por partida:")
    for indice, gols_feitos in enumerate(atleta['Gols']):
        print(f"  → {indice + 1}º jogo: {gols_feitos} gol(s)")
print("=-="*30)
# Sistema opcional de consulta individual
while True:
    busca = str(input("\nDeseja ver o desempenho detalhado de qual jogador? (Digite o nome ou 'sair'): ")).strip().title()
    if busca == 'Sair':
        print("Encerrando visualização individual.")
        break
    encontrado = False
    for atleta in dados:
        if atleta['Nome'] == busca:
            print(f"\nDesempenho detalhado de {atleta['Nome']}:")
            for indice, gols_feitos in enumerate(atleta['Gols']):
                print(f"  → {indice + 1}º jogo: {gols_feitos} gol(s)")
            encontrado = True
            break
    if not encontrado:
        print("⚠️ Jogador não encontrado. Tente novamente.")

