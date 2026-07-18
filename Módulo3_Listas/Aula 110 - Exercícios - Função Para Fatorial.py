#print(" Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.")
print()

def fatorial(num=1, show=False):
    """

    Calcula o fatorial de um numero.

    :param num: O numero a ser calculado
    :param show:(opcional) Mostrar ou nao a conta.
    :return: O valor fatorial de um numero n.
    """
    from time import sleep
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            print("x" if c > 1 else "=", end=" ")
            sleep(0.3)
        f *= c
        if show:
            print(f)
    return f


#Programa principal
numero = int(input("Digite um fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero, show=True)}")

