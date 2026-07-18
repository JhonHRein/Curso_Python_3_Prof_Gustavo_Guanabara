# ---------------------------------------------
# Aula Teórica: Dicionários em Python 🧠
# ---------------------------------------------

# Um dicionário em Python é uma estrutura que armazena pares de:
# chave -> valor
# Ele funciona como um cadastro, onde acessamos os dados pelas chaves, não por índice.

# Exemplo básico:
cadastro = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}
print(cadastro["nome"])  # Saída: Ana

# Chaves são únicas e os valores podem ser de qualquer tipo.
# Dicionários são mutáveis: você pode mudar, adicionar ou remover elementos.

# ---------------------------------------------
# Dicionário vs Lista de listas (comparação)
# ---------------------------------------------

# Lista de listas (mais difícil de entender):
alunos_lista = [
    ["Ana", 8.5, 9.0],
    ["Bruno", 7.0, 6.5]
]
print(alunos_lista[0][0])  # "Ana"
print(alunos_lista[0][1])  # 8.5

# Dicionário dentro de lista (mais claro):
alunos_dicio = [
    {"nome": "Ana", "nota1": 8.5, "nota2": 9.0},
    {"nome": "Bruno", "nota1": 7.0, "nota2": 6.5}
]
print(alunos_dicio[0]["nome"])   # "Ana"
print(alunos_dicio[0]["nota1"])  # 8.5

# ---------------------------------------------
# Função dict() — Outra forma de criar dicionários
# ---------------------------------------------

# Forma tradicional:
pessoa1 = {
    "nome": "Lucas",
    "idade": 30
}

# Usando dict():
pessoa2 = dict(nome="Lucas", idade=30)
print(pessoa2["idade"])  # Saída: 30

# Atenção:
# A função dict() só aceita nomes simples nas chaves (sem acento, espaço, etc)
# Exemplo inválido:
# contato = dict(número de telefone="99999-9999")  # ERRO: não pode espaço

# Forma correta com chaves:
contato = {
    "número de telefone": "99999-9999"
}

# dict() permite uso de underline (_), que simula espaço:
contato_valido = dict(numero_de_telefone="99999-9999")

# ---------------------------------------------
# Sobre espaços e o sinal de igual (=)
# ---------------------------------------------

# É permitido colocar espaços ao redor do sinal de igual:
d1 = dict(nome = "Lucas", idade = 30)  # Funciona

# Estilo mais comum (PEP8):
d2 = dict(nome="Lucas", idade=30)

# ---------------------------------------------
# Sobre uso de variáveis como chaves
# ---------------------------------------------

# Você pode usar variáveis como chaves, sem aspas:
chave = "profissão"
valor = "Programador"
dados = {chave: valor}
print(dados)  # {'profissão': 'Programador'}

# Mas se tentar usar sem definir as variáveis, dá erro:
# dados = {nome: Pedro}  # ERRO: 'nome' e 'Pedro' não existem como variáveis

# ---------------------------------------------
# Comparando dict() vs {}
# ---------------------------------------------

# dict() é bom para treinar, mas {} com : é mais versátil
# Por exemplo, isso não funciona com dict():
d = {
    "número de telefone": "99999-9999",
    10: "dez",
    (1, 2): "coordenada"
}

# Tudo acima funciona com {} + :, mas não com dict()

# ---------------------------------------------
# Aspas nas chaves: quando usar?
# ---------------------------------------------

# ✅ Use aspas se a chave for string literal:
d1 = {"nome": "Ana"}

# ❌ Não use aspas se for número, tupla, bool, ou variável:
d2 = {1: "um", 3.14: "pi", True: "sim", False: "não", (1, 2): "tupla"}

# ✅ Variáveis como chave (sem aspas):
nome = "chave"
valor = "conteúdo"
d3 = {nome: valor}

# ---------------------------------------------
# RESUMO FINAL 🧠
# ---------------------------------------------

# ✓ {} com dois-pontos é mais versátil que dict()
# ✓ dict() é bom para praticar, mas tem limitações
# ✓ Sempre use aspas nas chaves se for string literal
# ✓ Pode usar underline (_) para simular espaço em dict()
# ✓ {} aceita qualquer tipo de chave: string, número, tupla, bool, etc

# ---------------------------------------------
# Fim da Aula Teórica
# ---------------------------------------------
# Criando uma lista chamada 'locadora' com 3 dicionários (cada um representa um filme)
locadora = [
    {"nome": "Interestelar", "ano": 2014, "diretor": "Christopher Nolan"},
    {"nome": "O Poderoso Chefão", "ano": 1972, "diretor": "Francis Ford Coppola"},
    {"nome": "Parasita", "ano": 2019, "diretor": "Bong Joon-ho"}
]

# Percorrendo cada dicionário (filme) dentro da lista 'locadora'
for filme in locadora:
    # Exibe o nome do filme (acessa a chave "nome" dentro do dicionário atual)
    print("Filme:", filme["nome"])

    # Exibe o ano do filme (acessa a chave "ano")
    print("Ano:", filme["ano"])

    # Exibe o nome do diretor (acessa a chave "diretor")
    print("Diretor:", filme["diretor"])

    # Imprime uma linha separadora
    print("-" * 30)
#########################################################

brasil = []
estado1 = {"UF": "São Paulo", "sigla":"SP"}
estado2 = {"UF": "Rio de Janeiro", "sigla":"RJ"}
brasil.append(estado1)
brasil.append(estado2)
for linha in brasil:
    print(f"{linha}")
######################################################################
estado = dict()
brasil = list()
for c in range(0, 3):
    estado["UF"] = str(input("Unidade Federativa: "))
    estado["Sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for est in brasil:    #laço para uma lista
    for k, v in est.items():  #Laço para um Dicionário
        print(f"O campo: {k} tem o valor: {v}")