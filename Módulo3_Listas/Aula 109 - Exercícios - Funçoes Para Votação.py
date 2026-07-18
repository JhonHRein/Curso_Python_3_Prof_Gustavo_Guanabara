#print("Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.")

print()
def voto(ano_nascimento):
    from datetime import datetime
    cld = datetime.now()
    ano_atual = cld.year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO."
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."


def lin():
    print("=-="* 15)

#PROGRAMA PRINCIPAL
lin()
print("PROGRAMA DE ANALISE DE VOTO!")
lin()
ano = int(input("Ano de nascimento: "))
print(voto(ano))


##########################################################################
#VERSAO GPT

'''from datetime import datetime
print()
cld = datetime.now()

def voto(ano_nascimento):
    ano_atual = cld.year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO."
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."

def lin():
    print("=-=" * 15)

# Programa principal
lin()
print("PROGRAMA DE ANÁLISE DE VOTO")
lin()
ano = int(input("Ano de nascimento: "))
print(voto(ano))'''
