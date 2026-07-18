#print("Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. O programa tem que analisar todos os valores e dizer qual deles é o maior.")
print()
def maior(*valores):
    total = len(valores)
    if total == 0:
        print("Nenhum valor foi informado")
        return
    maior_num = valores[0]
    for numero in valores:
        if numero > maior_num:
            maior_num = numero
    print(f"Analisando valores: {valores}")
    print(f"Foram informados {total} valores ao todo.")
    print(f"O maior valor informado foi {maior_num}.")


def linha():
    print("=-="*20)


#Programa principal
linha()
maior(10,11,85,96)
linha()
maior(5,8,6,)
linha()
maior(4,85)
linha()










