print()
print("Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo\ndesconsiderando os espaços. Exemplos de palíndromos:")
print("- A sacada da casa")
print("- A torre da derrota")
print("- O lobo ama o bolo")
print()
frase = str(input("Escreva uma frase com no maximo 6 palavras: ",)).strip().lower()
frase_editada = frase.replace(" ","")
frase_invertida = frase_editada[::-1]
print(frase_invertida)
if frase_editada == frase_invertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo!")