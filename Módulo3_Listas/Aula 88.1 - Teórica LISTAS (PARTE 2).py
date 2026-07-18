"""Exemplo clássico: validar uma resposta S/N
python
Copiar
Editar
while True:
    resp = input("Quer continuar? (S/N): ").strip().lower()
    if resp in ('s', 'n'):
        break
    print("Resposta inválida. Digite apenas S ou N.")
O que está acontecendo aqui?

strip() ➜ remove espaços.

lower() ➜ deixa tudo minúsculo, aceita S, s, N, n.

while True ➜ repete até receber resposta válida.

if resp in ('s', 'n') ➜ só aceita s ou n."""
"""alidando números inteiros
Muitas vezes o usuário pode digitar uma letra por engano, e o int(input(...)) quebra o programa. Então usamos try-except:

python
Copiar
Editar
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Erro: digite um número inteiro válido.")
Assim você evita que o programa trave se o usuário digitar letras ou algo inválido.

🎯 Validar se número está dentro de um intervalo
python
Copiar
Editar
while True:
    idade = int(input("Digite sua idade: "))
    if 0 < idade < 120:
        break
    print("Idade inválida. Digite entre 1 e 119.")
🧠 Dicas para boas validações
Dica	Explicação
Use while True:	Cria um laço infinito até o dado ser válido
Combine strip() + lower()	Para evitar problemas com espaços ou letras maiúsculas
Use try-except para números	Protege contra entradas inválidas
Explique o erro ao usuário	Ajuda a entender o que deve corrigir

🔁 Validação dentro de outros laços
Você pode usar um segundo while dentro do primeiro (como você faz) para validar apenas a entrada, separando lógica do resto do código. Isso deixa o programa mais limpo e organizado.

""🧱 O que é uma lista composta?
Uma lista composta é uma lista que contém outras listas dentro dela.
Ou seja: uma estrutura de dados em camadas.

✅ Exemplo:
python
Copiar
Editar
pessoa1 = ['Maria', 22]
pessoa2 = ['João', 30]

grupo = [pessoa1, pessoa2]
Agora, grupo é uma lista composta:

lua
Copiar
Editar
grupo = [['Maria', 22], ['João', 30]]
📦 Acessando dados de uma lista composta
Você usa dois índices:

O primeiro índice acessa a lista interna.

O segundo índice acessa o elemento dentro da sublista.

🔍 Exemplo:
python
Copiar
Editar
print(grupo[0])       # ['Maria', 22]   → a primeira sublista
print(grupo[0][0])    # Maria          → nome da primeira pessoa
print(grupo[1][1])    # 30             → idade da segunda pessoa
🧠 Criando uma lista composta com input (mais prático)
Exemplo com input de várias pessoas:
python
Copiar
Editar
pessoas = []
dado = []

for _ in range(2):  # cadastrar 2 pessoas
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    dado.append(nome)
    dado.append(idade)
    pessoas.append(dado[:])  # faz uma cópia da lista `dado`
    dado.clear()             # limpa a lista para o próximo cadastro

print(pessoas)
🔑 Importante:
dado[:] cria uma cópia da lista.

dado.clear() limpa a lista original.

Isso evita que todas as posições da lista principal fiquem iguais.

🧪 Resultado desse código:
Suponha que o usuário digitou:

makefile
Copiar
Editar
Nome: Ana
Idade: 20
Nome: Pedro
Idade: 25
O conteúdo final será:

python
Copiar
Editar
[['Ana', 20], ['Pedro', 25]]
🔁 Percorrendo uma lista composta com for
python
Copiar
Editar
for pessoa in pessoas:
    print(f"{pessoa[0]} tem {pessoa[1]} anos.")
🧮 Como se fosse uma tabela (mentalmente)
Pense assim:

ini
Copiar
Editar
pessoas = [
    ['Ana', 20],
    ['Pedro', 25],
    ['Clara', 18]
]
É quase como uma tabela com linhas e colunas:

Linha = pessoa

Coluna 0 = nome

Coluna 1 = idade"""



"""teste = list()
teste.append("Jhon")
teste.append(36)
galera = list()
galera.append(teste[:])  #Sem o sinal de [:] o código faz uma ligação entre as listas deste e galera, usando o sinal, ele faz uma cópia da lista original.
teste[0] = "Maria"
teste[1] = 18
galera.append(teste[:])
print(galera)"""

galera = list()  #Lista principal
dado = list()    #Lista secundária
total_maior =  total_menor = 0
for c in range(0,4):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
# PARA SABER A MAIOR IDADE DA LISTA.
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        total_maior += 1
    else:
        print(f"{p[0]} é menor de idade")
        total_menor += 1
print(f"{total_maior} São maiores de idade.  E {total_menor} São menores de idade.")
