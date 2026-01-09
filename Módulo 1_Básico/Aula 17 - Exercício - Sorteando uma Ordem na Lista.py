#O mesmo professor do desafio anterior, quer sortear a ordem de apresentação de trabalhos dos aluns, Faça um programa nque leia o nome dos quatros alunos e mostre a ordem sorteada!")
print()
import random
aluno_0 = input("Nome do 1º aluno: ")
aluno_1 = input("Nome do 2º aluno: ")
aluno_2 = input("Nome do 3º aluno: ")
aluno_3 = input("nome do 4º aluno: ")
lista = [aluno_0, aluno_1, aluno_2, aluno_3]
sorteio = random.shuffle(lista)
print("=-="*10)
print("A ordem de apresentação sera:")
print(lista)
