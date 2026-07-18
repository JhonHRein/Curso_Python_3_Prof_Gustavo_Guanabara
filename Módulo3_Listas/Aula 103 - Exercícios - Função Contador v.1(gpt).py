print()
def contador(inicio, fim, passo):
    # 1. Tratar passo inválido
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo

    # 2. Lógica da contagem
    if inicio <= fim:
        for numero in range(inicio, fim+1, passo):
            print(numero, end=" ")
    else:
        for numero in range(inicio, fim-1, -passo):
            print(numero, end=" ")

    # 3. Finalização
    print("FIM")


# Testes
contador(1, 5, 1)
contador(10, 0, 2)
contador(3, 10, 0)

'''Valor original do passo	Ajuste feito	Resultado usado no range
2	nenhum	2
-2	passo = -passo → 2	2
0	passo = 1	1
5	nenhum	5
-7	passo = -passo → 7	7

✅ Explicação visual:

O sinal do passo negativo é invertido (-passo) porque a contagem crescente ou decrescente já é decidida pelo if inicio <= fim / else.

Passo positivo não precisa de alteração.

Passo zero é ajustado para 1 para evitar erro no range().'''
