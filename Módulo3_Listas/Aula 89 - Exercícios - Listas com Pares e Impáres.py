#print("Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os numa lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.")
print()
principal = []
pares = []
impares = []
for i in range(0,7):
    num = int(input("Digite um número : "))
    principal.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"Lista dos números digitados em ordem crescente: {sorted(principal)}")  #Aqui adicionei sorted() só por questão estética, não foi pedido.
print(f"Números pares em ordem crescente: {sorted(pares)}")
print(f"Números ímpares em ordem crescente: {sorted(impares)}")

#############################################################################################
#Metodo com listas e sub - listas.PROF Guanabara

numeros = [[], []]  # índice 0 = pares, índice 1 = ímpares

for i in range(0, 7):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        numeros[0].append(num)  # adiciona nos pares
    else:
        numeros[1].append(num)  # adiciona nos ímpares

print(f"Números pares: {sorted(numeros[0])}")
print(f"Números ímpares: {sorted(numeros[1])}")
