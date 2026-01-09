print("Desenvolva um programa que leia seis números inteiros e mostre a soma\napenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.")
print()
soma = 0
cont = 0
for i in range(6):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        soma += numero
        cont = cont + 1
    else:
        print()
print(f"Números Pares, apareceu {cont} vezes na sessão.")
print("Números ímpares serão desconsiderados.")
print("Fim de somatória.")
