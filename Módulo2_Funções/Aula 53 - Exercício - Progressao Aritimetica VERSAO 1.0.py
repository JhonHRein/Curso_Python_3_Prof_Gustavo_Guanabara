print("Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,\nmostre os 10 primeiros termos dessa progressão.")
print()
primeiro_termo = int(input("Digite o valor do termo: "))
razao = int(input("Digite um valor para razão: "))
termo_atual = primeiro_termo
for i in range(10):
    print(termo_atual, end= " ")
    termo_atual = termo_atual + razao

#RESOLUÇÃO DO PROFESSOR GUANABARA

print()
primeiro = int(input("Primeiro termo: "))
raz = int(input("Razão: "))
decimo = primeiro + (10 -1) *raz
for c in range(primeiro, decimo, raz):
    print(f"{c}", end=" ")
print("ACABOU!")