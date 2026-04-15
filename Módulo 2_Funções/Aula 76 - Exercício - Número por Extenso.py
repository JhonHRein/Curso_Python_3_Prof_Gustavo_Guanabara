#print("Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. O seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.")
print()
cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    numero_desejado = int(input("Escolha um número entre 0 e 20: "))
    if 0 <= numero_desejado <= 20:  # Identificador, identifica se o numero desejado esta dentro do cont.
        print(f"Voce digitou o número: {cont[numero_desejado]}")
    else:
        print("Número Inválido, tente novamente!")
    novo_num = str(input("Quer continuar ? (S/N) ")).strip().lower()
    if novo_num == "s":
        continue
    elif novo_num == "n":
        print("Fim do programa")
        break
    else:
        print("Comando inválido")
