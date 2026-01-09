print()
print("Exercício Python 040: Crie um programa que leia duas notas de um aluno\ne calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:\nMédia abaixo de 5.0: REPROVADO\nMédia entre 5.0 e 6.9: RECUPERAÇÃO\nMédia 7.0 ou superior: APROVADO. ")
print()
nota_01 = float(input("Digite a sua primeira nota: "))
nota_02 = float(input("Digite a sua segunda nota: "))
media = (nota_01 + nota_02) / 2
if media < 5.0:
    print(f"Sua média foi: {media}, REPROVADO.")
elif (media >= 5.0) and (media <= 6.9):
    print(f"Sua media foi {media}, RECUPERAÇÃO.")
elif media >= 7.0:
    print(f"Sua média foi {media}, APROVADO.")
