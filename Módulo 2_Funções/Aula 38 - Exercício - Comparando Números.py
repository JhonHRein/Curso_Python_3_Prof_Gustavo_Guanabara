print()
print("Exercício Python 038: Escreva um programa que leia dois números inteiros\ne compare-os. mostrando na tela uma mensagem:")
print("– O primeiro valor é maior\n- O segundo valor é maior\n- Não existe valor maior, os dois são iguais")
print()
print()
numero1 = int(input("Digite um numero inteiro que represente a letra A: "))
numero2 = int(input("Digite um segundo numero inteiro que represente a letra B: "))
print()
if numero1 > numero2:
    print("O valor de A-{} é maior que o valor de B-{}".format(numero1, numero2))
elif numero2 > numero1:
    print("O valor de B-{} é maior que o valor de A-{}".format(numero2, numero1))
else:
    print("Os valores de 'A' e 'B' são iguais, nao tem comparação.")