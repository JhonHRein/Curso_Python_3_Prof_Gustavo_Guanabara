"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""
print()
tabela_br_25 = "Flamengo", "Palmeiras", "Atlético-MG", "Grêmio", "São Paulo", "Internacional", "Fluminense", "Corinthians", "Red Bull Bragantino", "Athletico-PR","Cuiabá", "Fortaleza", "Botafogo", "Vasco da Gama", "Bahia", "Vitória", "Criciúma", "Juventude", "Atlético-GO", "Sport Recife"
tabela_alpha = sorted(tabela_br_25)
for t in tabela_br_25:
    print(t)
print(f"Os 5 primeiros colocados da tabela: {tabela_br_25[0:5]}")
print(f"Os 4 ultimos times da tabela {tabela_br_25[-4:]}")
print(f"Tabela em ordem alfabética: {tabela_alpha}")
print(f"O Vitória esta na: {tabela_br_25.index("Vitória")+1}ª posição")

