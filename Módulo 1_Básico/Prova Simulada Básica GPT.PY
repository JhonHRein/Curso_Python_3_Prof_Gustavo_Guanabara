# TESTE CODEX

# Exercício 01 – Nome e idade
print()
print("Exercício 01 – Nome e idade")
nome = str(input("Digite seu nome completo: "))
idade = int(input("Digite a sua idade: "))
print("Prazer {}, {} anos".format(nome, idade))
print("Total de caracteres no nome (sem espaços): {}".format(len(nome.replace(" ", ""))))


# Exercício 02 – Operadores Matemáticos e Arredondamento
print()
print("Exercício 02 – Operadores e arredondamentos")
import math
n1 = float(input("Digite um valor decimal: "))
n2 = float(input("Digite outro valor decimal: "))
soma = n1 + n2
div = n1 / n2
print("A soma entre os valores é: {:.2f}".format(soma))
print("Divisão com duas casas: {:.2f}".format(div))
print("Divisão arredondada com round(): {}".format(round(div)))
print("Divisão arredondada para cima com ceil(): {}".format(math.ceil(div)))


# Exercício 03 – Aleatoriedade com lista de filmes
print()
print("Exercício 03 – Lista de filmes e sorteio")
import random
filmes = ["Eu sou a lenda", "Corrida Fatal", "Tranças do Rei Careca", "A volta dos que não foram"]

# Sorteando um filme
sorteado = random.choice(filmes)
print("Filme sorteado: {}".format(sorteado))

# Mostrando todos os filmes em ordem embaralhada
random.shuffle(filmes)
print("Ordem embaralhada dos filmes:")
for i, filme in enumerate(filmes, 1):
    print("{}. {}".format(i, filme))


# Exercício 04 – Módulo math e trigonometria
print()
print("Exercício 04 – Trigonometria com math")
angulo = float(input("Digite o valor de um ângulo: "))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print("Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(seno, cosseno, tangente))


# Exercício 05 – Manipulação de Texto
print()
print("Exercício 05 – Manipulação de texto")
frase = str(input("Digite uma frase: "))
print("Frase em minúsculas: {}".format(frase.lower()))
print("Quantidade de letras 'a': {}".format(frase.lower().count("a")))
print("A letra 'e' aparece pela primeira vez na posição: {}".format(frase.lower().find("e") + 1))




