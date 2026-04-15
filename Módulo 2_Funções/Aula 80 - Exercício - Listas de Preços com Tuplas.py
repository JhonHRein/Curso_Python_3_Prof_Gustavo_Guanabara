#print("Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.")
print()
produtos = "Banana",2.00, "Maça", 5.00, "Mamão", 3.00, "Goiaba", 5.00, "laranja", 1.00
print(f"{'Produto':<15}{'Preço':>6}")
print("==="*10)
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preço = produtos[i + 1]
    print(f"{nome:<15}R${preço:>6.2f}")

"""# Criando uma tupla com nome e preço de produtos (alternando: nome, preço)
produtos = ("Lápis", 1.75,
            "Borracha", 2.00,
            "Caderno", 15.90,
            "Estojo", 8.00)

# Imprime o cabeçalho da "tabela"
# 'Produto' alinhado à esquerda ocupando 20 espaços
# 'Preço' alinhado à direita ocupando 10 espaços
print(f"{'Produto':<20}{'Preço':>10}")

# Linha separadora com 30 traços
print("-" * 30)

# Laço que percorre os índices de 2 em 2 (0, 2, 4, 6...) porque os dados estão em pares
for i in range(0, len(produtos), 2):
    nome = produtos[i]           # Pega o nome do produto
    preco = produtos[i + 1]      # Pega o preço correspondente
    
    # Imprime o nome alinhado à esquerda (20 espaços)
    # e o preço com R$ alinhado à direita (7 espaços), com 2 casas decimais
    print(f"{nome:<20}R$ {preco:>7.2f}")
"""