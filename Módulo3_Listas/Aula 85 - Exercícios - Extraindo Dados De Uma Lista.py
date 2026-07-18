print()
#print"Crie um programa que vai ler vários números e colocar em uma lista.
# \nDepois disso, mostre:
# \nA) Quantos números foram digitados.
# \nB) A lista de valores, ordenada de forma decrescente.
# \nC) Se o valor 5 foi digitado e está ou não na lista. "
print()
pedido = []
while True:
    pedido.append(int(input("Digte um número: ")))
    pedido.sort(reverse=True)
    while True:
        resp = str(input("Quer continuar ? (S/N)")).strip().lower()
        if resp in ("s","n"):
            break
        print("Resposta inválida, apenas digite: (S/N)")
    if resp == "n":
        print("Fim do programa")
        break
print("-=-"* 13)
print(f"Números digitados: {len(pedido)}")
print(f"Valores em ordem decrescente: {pedido}")
if 5 in pedido:
    print("O valor 5 foi digitado e esta na lista.")
else:
    print("O valor 5 não foi digitado na lista.")



