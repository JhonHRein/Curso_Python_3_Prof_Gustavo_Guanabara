#print("Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.")
print()
print("-=-"*12)
print(f"{"PROGRAMA PARA MÉDIA E NOTAS DE ALUNOS"}")
print("-=-"*12)
print()
ficha = list()
while True:
    nome = str(input("Nome do aluno: "))
    nota1 = float(input("1° Nota: "))
    nota2 = float(input("2° Nota: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    while True:
        resp = str(input("Quer Continuar? (S/N): ")).lower().strip()
        if resp in ("s","n"):
            break
        else:
                    print("Respostas inválida, apenas 'S' ou 'N'.")
    if resp == "n":
        print("Fim do programa!")
        break
print("-=-"*12)
#print(f"{ficha}")
print(f"{"No.":<5}{"Nome.":<10}{"Média.":>8}")
print("__"*12)
for i, a in enumerate(ficha):
    print(f"{i:<5}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("__"*12)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe):"))
    if opc == 999:
        print("Finalizando...")
        break
    if opc <= len(ficha) -1:
        print(f"Notas de  {ficha[opc] [0]} são {ficha[opc] [1]}")
    else:
        print("Número Inválido. Tente novamente.")



