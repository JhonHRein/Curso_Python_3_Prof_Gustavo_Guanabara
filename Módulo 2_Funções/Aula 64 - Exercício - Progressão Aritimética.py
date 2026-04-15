print()
print("Refaça o DESAFIO 53, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.")
print()
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite o valor da razão: "))
decimo = termo + (10 - 1) * razao
c = 1
atual = termo
while c <= 10:
    print(f"{atual}", end= " ")
    atual += razao
    c += 1
print("Fim")

