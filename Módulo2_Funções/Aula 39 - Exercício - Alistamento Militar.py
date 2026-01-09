print("Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem\ne informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,\nse é a hora exata de se alistar ou se já passou do tempo do alistamento.\nSeu programa também deverá mostrar o tempo que falta ou que passou do prazo.")
print()
print("PROGRAMA MILITAR BRASILEIRO - PROCESSO DE CAPITALIZAÇÃO DE JOVENS SOLDADOS")
print("*-=-*"*13)
print()
nome_jovem = str(input("Escreva seu nome completo: ")).strip()
idade_jovem = int(input("Qual a sua data de nascimento (ex: 1900): "))
print()
apto = 2025 - idade_jovem
restante_idade  = 18 - apto
if apto == 18:
    print("Sr. {}. Está Apto a servir as forças armadas. Completa {} anos esse ano de 2025.".format(nome_jovem, apto))
elif apto < 18:
    print("O Sr. {}, Não esta em idade de alistamento de serviço militar obrigatório.\nTem {} anos.\nAinda falta {} anos para o alistamento.".format(nome_jovem,apto, restante_idade, ))
elif apto > 18:
    print("O Sr. {}. Não se encontra Apto a servir as Forças Armadas.\nSe encontra com {} anos.\nDispensa Militar.".format(nome_jovem, apto))
#########################################################################################################################################
# versao corrigida com gpt e usando f-string
print()
print()
print()
print("PROGRAMA MILITAR BRASILEIRO - PROCESSO DE CAPITALIZAÇÃO DE JOVENS SOLDADOS")
print("*-=-*" * 13)
print()

nome_jovem = input("Escreva seu nome completo: ").strip()
ano_nascimento = int(input("Qual a sua data de nascimento (ex: 2000): "))
ano_atual = 2025
idade = ano_atual - ano_nascimento
alistamento = ano_nascimento + 18

print()

if idade == 18:
    print(f"Sr. {nome_jovem}, está Apto a servir as Forças Armadas.")
    print(f"Você completa 18 anos em {ano_atual}. Compareça ao quartel mais próximo.")
elif idade < 18:
    anos_restantes = 18 - idade
    print(f"O Sr. {nome_jovem} não está em idade de alistamento.")
    print(f"Atualmente você tem {idade} anos. Ainda faltam {anos_restantes} anos para se alistar.")
    print(f"Seu alistamento será em {alistamento}.")
else:
    anos_atraso = idade - 18
    print(f"O Sr. {nome_jovem} já passou da idade do alistamento.")
    print(f"Você tem {idade} anos. Deveria ter se alistado em {alistamento}, há {anos_atraso} anos.")
    print("Procure o setor de regularização militar.")
