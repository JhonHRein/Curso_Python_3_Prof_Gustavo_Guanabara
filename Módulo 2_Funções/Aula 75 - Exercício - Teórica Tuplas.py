"""Tuplas são imutáveis"""

lanche = "Hamburger", "Cafe", "Cigarro", "Suco", "Pudim"
#tecnica da posição usando o f ‘string’!
for cont in range(0, len(lanche)):     # primeira forma com len()
    print(f"eu vou comer {lanche[cont]} na posição {cont}")
for comida in lanche:                  # segunda forma normal simples
    print(f"Eu vou comer {comida}")

print("Comi pra caramba!")
#print(",".join(lanche))              # Imprime todos os itens da tupla separados por ", "
                                     #print(", ".join(lanche))
print(",".join(sorted(lanche)))
#COMANDO SORTED()
"""numeros = (3, 1, 4, 1, 5, 9, 2)
nomes = ["banana", "maçã", "laranja"]

# Ordenação crescente (padrão)
lista_ordenada = sorted(numeros)
# Retorna: [1, 1, 2, 3, 4, 5, 9]

# Ordenação decrescente
lista_decrescente = sorted(nomes, reverse=True)
# Retorna: ['maçã', 'laranja', 'banana']

# A sequência original não é alterada!
# print(numeros) ainda seria (3, 1, 4, 1, 5, 9, 2)
# print(nomes) ainda seria ["banana", "maçã", "laranja"]"""