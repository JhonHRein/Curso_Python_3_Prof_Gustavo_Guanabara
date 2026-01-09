print("Exercício Python 041: A Confederação Nacional de Natação precisa de um programa\nque leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:\nAté 9 anos: MIRIM\nAté 14 anos: INFANTIL\nAté 19 anos: JÚNIOR\n Até 25 anos: SÊNIOR\nAcima de 25 anos: MASTER")
print()
print()
print("-=-=-"*10)
print("PROGRAMA DE CLASSIFICAÇÃO POR IDADE - ATLETAS DE NATAÇÃO")
print("-=-=-"*10)
print()
from datetime import date
atleta = int(input("Digite o ano de nascimento do atleta: "))
ano = date.today().year
idade = ano - atleta
if idade <= 9:
    print(f"Atletas com {idade} anos, - CATEGORIA MIRIM. ")
elif idade <= 14:
    print(f"Atletas com {idade} anos, - CATEGORIA INFANTIL.")
elif idade <= 19:
    print(f"Atletas com  {idade} anos, - CATEGORIA JÚNIOR. ")
elif idade <= 25:
    print(f"Atletas com {idade} anos, - CATEGORIA SÊNIOR. ")
else:
    print(f"Atletas com {idade} anos, - CATEGORIA MASTER. ")



