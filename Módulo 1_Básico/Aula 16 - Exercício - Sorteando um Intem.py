#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um progama que ajude ele, lendo os nomes dos alunos e escrevendo na tela o nome escolhido.
print()
import random

aluno_0 = str(input("Nome do 1º aluno: "))
aluno_1 = str(input("Nome do 2º aluno: "))
aluno_2 = str(input("Nome do 3º aluno: "))
aluno_3 = str(input("Nome do 4º aluno: "))
lista = [aluno_0, aluno_1, aluno_2, aluno_3]
sorteio = random.choice(lista)
print(f" O aluno sorteado é o : {sorteio}")
