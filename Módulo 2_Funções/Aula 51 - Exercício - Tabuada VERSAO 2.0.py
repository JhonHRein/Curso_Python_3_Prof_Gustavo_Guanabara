print("Refaça o DESAFIO  da primeira tabuada e mostrando a tabuada de um número que o usuário escolher,\nsó que agora utilizando um laço for.")
print()
numero = int(input("Digite um valor para ver a sua tabuada: "))
print(f"Tabuada do: {numero} ") # Lembrando que o 'C' é o contador. Cont.
for c in range (1, 11):
    print(f"{numero} x {c} = {numero*c}")