"""#tuplas = () # Tuplas recebem parenteses, são imutaveis, nao pode ser modificadas.
#listas = [] # Listas recebem cochetes, são modificadas,

# ------------------------ LISTAS - RESUMO DE MÉTODOS DE ADIÇÃO E REMOÇÃO ------------------------

# append() ➜ Adiciona um item no final da lista
lista = [1, 2, 3]
lista.append(4)  # Resultado: [1, 2, 3, 4]

# insert(posição, valor) ➜ Insere um item em uma posição específica (empurra os outros)
lista = [1, 2, 3]
lista.insert(1, 99)  # Resultado: [1, 99, 2, 3]

# Substituição direta ➜ Altera o valor de uma posição específica
lista = [1, 2, 3]
lista[1] = 99  # Resultado: [1, 99, 3]

# del lista[posição] ➜ Remove um item de uma posição (não retorna nada)
lista = [10, 20, 30]
del lista[1]  # Resultado: [10, 30]

# pop() ➜ Remove o último item e retorna ele
lista = [1, 2, 3]
valor = lista.pop()  # valor = 3, lista = [1, 2]

# pop(posição) ➜ Remove item da posição escolhida e retorna ele
lista = [1, 2, 3]
valor = lista.pop(0)  # valor = 1, lista = [2, 3]

# remove(valor) ➜ Remove o PRIMEIRO item com o valor indicado (não usa posição)
lista = [10, 20, 30, 20]
lista.remove(20)  # Resultado: [10, 30, 20]

# Obs: remove() dá erro se o valor não estiver na lista
# Use: if valor in lista: lista.remove(valor)

# ------------------------ FIM DO RESUMO ------------------------

# ------------------------ RESUMO DO COMANDO list() ------------------------

# 1. Criar uma lista vazia
lista_vazia = list()
print(lista_vazia)  # Resultado: []

# 2. Converter uma string em lista de caracteres
palavra = "python"
lista_letras = list(palavra)
print(lista_letras)  # Resultado: ['p', 'y', 't', 'h', 'o', 'n']

# 3. Converter uma tupla em lista
tupla = (1, 2, 3)
lista_de_tupla = list(tupla)
print(lista_de_tupla)  # Resultado: [1, 2, 3]

# 4. Converter um range em lista
intervalo = range(5)  # de 0 até 4
lista_range = list(intervalo)
print(lista_range)  # Resultado: [0, 1, 2, 3, 4]

# 5. Converter um conjunto (set) em lista
conjunto = {10, 20, 30}
lista_conjunto = list(conjunto)
print(lista_conjunto)  # Resultado: [10, 20, 30] (a ordem pode variar)

# 6. Converter dicionário em lista (pega apenas as chaves por padrão)
dicionario = {"a": 1, "b": 2}
lista_chaves = list(dicionario)
print(lista_chaves)  # Resultado: ['a', 'b']

# ------------------------ FIM DO RESUMO ------------------------"""
num = []
for cont in range(0,5):
    num.append(int(input("Digite um valor: ")))
for c, v, in enumerate(num):
    print(f"Na posição {c} encontrei o valor {v}")

