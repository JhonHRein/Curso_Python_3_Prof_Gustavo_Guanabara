

#Estruturas de controle (o que são e para que servem)

#Condicionais (if, elif, else)

#Laços de repetição (for)

#Condições aninhadas (if dentro de if)

#Exemplos práticos simples e com lógica comentada

# 1. O que são Estruturas de Controle?
#São formas que o Python (ou qualquer linguagem) usa para controlar o fluxo do programa, ou seja:

#“Em que ordem as coisas vão acontecer.”

# Elas permitem-te tomar decisões ou repetir ações com base em condições.

#2. Condicionais: if, elif, else
#Sintaxe básica:
#python
#Copiar
#Editar
#if condição:
    # faz isso se a condição for verdadeira
#elif outra_condição:
    # faz isso se a primeira não for verdadeira, mas essa for
#else:
    # faz isso se nenhuma das condições anteriores for verdadeira
#Exemplo:
#python
#Copiar
#Editar
#idade = int(input("Qual sua idade? "))

#if idade >= 18:
 #   print("Você é maior de idade.")
#elif idade > 0:
 #   print("Você é menor de idade.")
#else:
 #   print("Idade inválida.")

#3. Laço for
#É usado quando você sabe quantas vezes quer repetir algo.

#Forma 1: for i in range(...)
#python
#Copiar
#Editar
#for i in range(5):  # Vai de 0 até 4 (5 vezes)
 #   print("Repetição:", i)
#Exemplo prático:
#python
#Copiar
#Editar
#for i in range(3):
 #   nome = input("Digite um nome: ")
 #  print("Você digitou:", nome)
# 4. Condições aninhadas
#Significa ter um if dentro de outro if.

#Exemplo:
#python
#Copiar
#Editar
#numero = int(input("Digite um número: "))

#if numero > 0:
    #if numero % 2 == 0:
    #    print("É um número positivo e par.")
    #else:
     #   print("É um número positivo e ímpar.")
#else:
    #print("O número não é positivo.")



print("###################################################################")
print()
print()
soma = 0
soma_pares = 0

for i in range(6):
    numero = int(input("Digite um valor: "))

    if numero % 2 == 0:
        print(f"O número {numero} é Par.")
        soma += numero  # soma os pares
        soma_pares += 1  # conta os pares
    else:
        print(f"O número {numero} é Ímpar.")

print()
print(f"A soma dos números pares é {soma}")
print(f"Você digitou {soma_pares} números pares.")

