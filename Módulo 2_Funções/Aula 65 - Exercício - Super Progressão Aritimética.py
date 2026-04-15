print()
#print("Melhore o DESAFIO 61, perguntando para o utilizador se ele quer mostrar mais alguns termos.\nO programa encerrará quando ele disser que quer mostrar 0 termos.")
print()
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite o valor da razão: "))
decimo = termo + (10 - 1) * razao
atual = termo # começa no 1º termo.
c = 1         # contador de termons já exibidos.
total = 0     # total acumulado de termos exibidos.
mais = 10     # começa mostrando 10 termos.
while mais != 0:
    total += mais  # soma os novos termos ao total
    while c <= total:   # aqui os termos sao mostrados um por um
        print(f"{atual}", end= " ")
        atual += razao
        c += 1
    print("Pausa")   # pausa e uma nova pergunta a seguir
    mais = int(input("Quantos termos voce quer mostrar a mais: "))
print(f"progressão finalizada com {total} termos mostrados.")
#✅ Conclusão:
#Esse é um exemplo clássico e bem didático que mostra como o while é poderoso. Não se preocupa se parece muito de primeira — com mais 2 ou 3 exercícios assim, você vai pegar o jeito de vez.


