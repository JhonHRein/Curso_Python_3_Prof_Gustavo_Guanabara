#115a: Vamos criar um menu em Python, usando modularização.
#115b: Vamos ver como fazer acesso a arquivos usando o Python.

from utilidadesCeV.menumod import *
from utilidadesCeV.arquivo import *
from utilidadesCeV.arquivo import cadastrar


arq = "Curso em video.txt"
if not arquivo_existe(arq):
    criar_arquivo(arq)

# PROGRAMA PRINCIPAL
while True:
    resp1 = menu(["Ver pessoas cadastradas.",
                  "Cadastrar nova Pessoa.",
                  "Sair do Sistema."])
    if resp1 == 1:
        # Opções de listas e conteúdo de um arquivo
        ler_arquivo(arq)
    elif resp1 == 2:
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        cadastrar(arq, nome, idade)
    elif resp1 == 3:
        print("Finalizando Sistema...")
        break