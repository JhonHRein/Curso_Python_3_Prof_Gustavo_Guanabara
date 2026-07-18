#print("Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.")
print()
boletin = list()
dados = {}
for _ in range(1):
    dados["Nome:"] = str(input("Nome do aluno: "))
    dados["Média:"] = float(input(f"Qual a média de {dados['Nome:']}: "))
    boletin.append(dados.copy())
print()
print("-=-"*12)
for dados in boletin:
    for n, m in dados.items():
        print(f"- {n} {m}")
if dados["Média:"] >= 6.5:
    print("Situação Aprovado")
else:
    print("Situação Reprovado")

##############################################################################
    #BOLETIN FEITO PAR MAIS ALUNOS CHATGPT

# Lista para armazenar os boletins de vários alunos
"""boletim = list()

# Início de um laço infinito (ele só para se o usuário quiser)
while True:
    # Cria um dicionário vazio para cada novo aluno
    dados = {}

    # Coleta o nome do aluno
    dados["Nome"] = str(input("Nome do aluno: "))

    # Coleta a média do aluno
    dados["Média"] = float(input(f"Qual a média de {dados['Nome']}: "))

    # Define a situação com base na média e armazena no dicionário
    if dados["Média"] >= 6.5:
        dados["Situação"] = "Aprovado"
    else:
        dados["Situação"] = "Reprovado"

    # Adiciona uma cópia do dicionário à lista principal
    boletim.append(dados.copy())

    # Pergunta se o usuário deseja continuar ou não
    continuar = str(input("Deseja adicionar outro aluno? [S/N]: ")).strip().upper()
    if continuar != "S":
        break  # Sai do laço se a resposta não for S

# Linha de separação
print()
print("-=-" * 12)

# Exibe todos os boletins cadastrados
print("BOLETIM GERAL:")
for aluno in boletim:
    for chave, valor in aluno.items():
        print(f"- {chave}: {valor}")
    print("-" * 30)  # Linha separadora entre alunos"""


