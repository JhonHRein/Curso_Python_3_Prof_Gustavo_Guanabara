print()
print("Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.\nCaso esteja errado, peça a digitação novamente até ter um valor correto.")
print()
sexo = " "
while sexo not in ("m", "f"):
    sexo = str(input("Qual seu sexo ? (m/f): ")).lower().strip()
    if sexo not in ("m", "f"):
        print("Resposta Inválida.")
print(f"Sexo {sexo.upper()} registrado com sucesso.")
