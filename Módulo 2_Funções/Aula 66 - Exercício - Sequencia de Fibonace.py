print()
#print("Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.")
print()
print("SEQUENCIA DE FIBONACCI")
print()
n = int(input("Quantos termos voce quer mostrar?: "))
t1 = 0
t2 = 1
cont = 2
i = 0
print(f"{t1} {t2}",end=" ")
while cont < n:
        t3 = t1 + t2
        print(f"{t3}",end=" ")
        t1 = t2
        t2 = t3
        cont += 1
while True:
    novo = int(input("\nDeseja mostrar mais quantos termos?: "))
    if novo == 0:
        print("Fim do Programa")
        break
    for _ in range(novo):
        t3 = t1 + t2
        print(f"{t3}", end=" ")
        t1 = t2
        t2 = t3
        cont += 1



