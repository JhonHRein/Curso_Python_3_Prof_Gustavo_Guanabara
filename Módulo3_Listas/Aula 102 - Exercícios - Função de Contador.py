#print("Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. O programa tem que realizar três contagens através da função criada:\na) de 1 até 10, de 1 em 1\nb) de 10 até 0, de 2 em 2\nc) uma contagem personalizada")
from time import sleep

def linha():
    print("--" * 15)

def contador(inicio, fim, passo):
    #--------Tratamento do passo ----
    if passo == 0:
        passo = 1 # passo 0 travaria a contagem; ajustamos para 1

    passo = abs(passo) #garante que o passo seja positivo; o sinal a gente define o range

    # ----Cabeçalho da contagem-----
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")
    sleep(0.5) #pequena pausa para leitura

    #----Contagem crescente -----
    if inicio <= fim:
        #Range vai até o fim +1 porque o limite final do range é exclusivo
        for numero in range(inicio, fim + 1, passo):
            print(numero, end=" ", flush=True) #imprime na mesma linha, sem quebrar
            sleep(0.5)
    else:
        for numero in range(inicio, fim - 1, -passo):
            print(numero, end=" ", flush=True)
            sleep(0.5)
    print("FIM")
    print()

#==========================
# PROGRAMA PRINCIPAL
# ==========================

linha()
print("a) Contagem de 1 até 10, de 1 em 1:")
contador(1, 10, 1)

linha()
print("b) Contagem de 10 até 0, de 2 em 2:")
contador(10, 0, 2)

linha()
print("c) Agora é sua vez de personalizar a contagem! ")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)
linha()


