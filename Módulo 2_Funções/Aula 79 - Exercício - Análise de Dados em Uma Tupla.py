print("Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.")
print()
print()

valores = []  # lista temporária para armazenar os números
cont = 0
# Lê 4 valores válidos (entre 0 e 10)
while len(valores) < 4:
    numero = int(input("Digite um valor entre 0 e 10: "))
    if numero < 0 or numero > 10:
        print("Número inválido. Tente novamente.")
    else:
        valores.append(numero)
# Converte a lista em tupla
valores_tupla = tuple(valores)
# Contar quantas vezes apareceu o número 9
qtd_nove = valores_tupla.count(9)
# Verifica se o número 3 está presente e mostra sua primeira posição
if 3 in valores_tupla:
    posicao_tres = valores_tupla.index(3) + 1  # +1 para mostrar posição “humana”
else:
    posicao_tres = None
# Pega todos os pares
pares = tuple(num for num in valores_tupla if num % 2 == 0)
# Exibe os resultados
print(f"\nTupla com os valores digitados: {valores_tupla}")
print(f"O número 9 apareceu {qtd_nove} vez(es).")
if posicao_tres:
    print(f"O número 3 foi digitado pela primeira vez na {posicao_tres}ª posição.")
else:
    print("O número 3 não foi digitado.")

print(f"Números pares encontrados: {pares}")


