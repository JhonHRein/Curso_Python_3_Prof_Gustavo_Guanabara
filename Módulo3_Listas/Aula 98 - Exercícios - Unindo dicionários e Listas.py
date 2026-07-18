#print("Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média ")
from time import sleep
print("==== SISTEMA DE CADASTRAMENTO DE PESSOAS ====")
print("=-="*15)
print()
cadastro_principal = list()
cad_geral = dict()
soma = media = 0
while True:
    cad_geral['Nome:'] = str(input("Nome completo: "))
    while True:
        cad_geral['Sexo:'] = str(input("Sexo [F/M]: ")).lower()[0]
        if cad_geral['Sexo:'] in "fm":
            break
        print("ERRO:Digite apenas F ou M")
    cad_geral['Idade:'] = int(input("Idade atual: "))
    soma += cad_geral['Idade:'] #         ---->   soma das idades
    cadastro_principal.append(cad_geral.copy())
    while True:
        resp = str(input("Quer continuar com o cadastro (S/N): ")).lower()[0]
        if resp in "sn":
            break
        print("Resposta inválida, apenas S ou N")
    if resp == "n":
        print("Finalizando sistema de cadastro.")
        break
print()
print("==== FORMULÁRIO DE CADASTRO ====")
print("=-="*15)
print(f"- Ao todo temos {len(cadastro_principal)} pessoas cadastradas.")  #Quantidade de pessoas cadastradas.
media = soma // len(cadastro_principal) #Media de idade das pessoas cadastradas
print(f"- A media de idade é: {media} anos")
print(f"- As mulheres cadastradas foram: ", end="")
for p in cadastro_principal:    # código para separar mulheres dentro do dicionário.
    if p['Sexo:'] == "f":
        print(f"- {p['Nome:']} ", end="")
    print()
print(f"- Pessoas com a idade acima da média: ")
for p in cadastro_principal:     # Código para mostrar as pessoas com a idade acima da média.
    if p['Idade:'] >= media:
        for k, v in p.items():
            print(f"{k} = {v} ", end="")
        print()
print("--"*12)
for pessoa in cadastro_principal:  # lista geram de todas as pessoas cadastradas na lista em forma de lista.
    for chave, valor in pessoa.items():
        print(f"- {chave:<10} {valor}")
    print("--" * 12)
