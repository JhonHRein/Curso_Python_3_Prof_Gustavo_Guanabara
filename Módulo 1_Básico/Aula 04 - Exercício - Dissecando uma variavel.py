#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

frase = input("Digite uma frase ou sequência de palavras: ")
print(type(frase))         # Mostra o tipo da variável (sempre será <class 'str'> aqui)

print("Só tem espaços? ", frase.isspace())     # Verifica se a string só contém caracteres de espaço
print("É um número? ", frase.isnumeric())      # Verifica se a string só contém dígitos (0-9)
print("É alfabético? ", frase.isalpha())      # Verifica se a string só contém letras (a-z, A-Z)
print("É alfanumérico? ", frase.isalnum())    # Verifica se a string contém letras e/ou números (alfabéticos + numéricos)
print("Está em maiúsculas? ", frase.isupper()) # Verifica se todas as letras na string estão em maiúsculas
print("Está em minúsculas? ", frase.islower()) # Verifica se todas as letras na string estão em minúsculas
print("Está capitalizada? ", frase.istitle())  # Verifica se a string está no formato de título (primeira letra de cada palavra maiúscula e o resto minúscula)