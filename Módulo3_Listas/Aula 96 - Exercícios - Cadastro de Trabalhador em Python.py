#print("Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.")
from datetime import datetime
print("==== PROGRAMA DE CADASTRO DE NOVOS FUNCIONÁRIOS ====")
print()
cadastro = dict()
while True:
    cadastro['Nome do Funcionário'] = str(input("Nome do funcionário: "))
    cadastro['Ano de Nascimento'] = int(input("Ano de nascimento: "))
    ano_tual = datetime.now().year
    cadastro['Idade'] = ano_tual - cadastro['Ano de Nascimento']
    cadastro['Carteira De Trabalho'] = int(input("Número da carteira de trabalho (0 não tem): "))
    if cadastro['Carteira De Trabalho'] == 0:
        cadastro['Aposentadoria com'] = "Não aplicável"
        break
    else: 
        cadastro['Contratação'] = int(input("Ano de contratação: "))
        cadastro['Salário'] = int(input("Salário: "))
        anos_contribuicao = 35
        idade_contratacao = cadastro['Contratação'] - cadastro['Ano de Nascimento']
        cadastro['Aposentadoria com'] = idade_contratacao + anos_contribuicao
    while True:
        valid = str(input("Continuar cadastro de funcionários? (S/N): ")).lower().strip()
        if valid in "s" "n":
            break
        print("Resposta Inválida. Apenas S ou N.")
    if valid == "n":
        print("Fim do Cadastro!")
        break
print("=-="*15)
for chave, valor in cadastro.items():
    print(f"- {chave:<20}: {valor}")