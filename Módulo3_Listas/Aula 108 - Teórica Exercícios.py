def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f

#PROGRAMA PRINCIPAL

n = int(input("Digite um número: "))
print(f"O fatorial de {n} é igual a {fatorial(n)}")

