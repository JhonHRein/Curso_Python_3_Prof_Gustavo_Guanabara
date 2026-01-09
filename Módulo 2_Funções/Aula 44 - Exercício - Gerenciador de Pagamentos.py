print("Elabore um programa que calcule o valor a ser pago por um produto\nconsiderando o seu preço normal e condição de pagamento:\nà vista dinheiro/cheque: 10% de desconto\nà vista no cartão: 5% de desconto\nem até 2x no cartão: preço formal\n3x ou mais no cartão: 20% de juros")
print()
produto = float(input("Digite o valor do produto: R$ "))
print()
print("FORMAS DE PAGAMENTO:\nDinheiro/Cheque desconto 10% Digite: 1\nCartão a vista desconto 5% Digite: 2\nParcelamento 2x no Cartão sem juros Digite: 3\nParcelamento 3x com 20% de juros Digite: 4")
avista_10 = produto - (( 10 / 100)* produto)
avista_5 = produto - (( 5 / 100 )* produto)
cartao_2x = produto / 2
cartao_3x_jurus_20 = (produto + ((20 / 100 ) * produto )) / 3
pagamento = int(input("Qual a forma de pagamento: "))
if pagamento == 1:
    print(f"Dinheiro/Cheque Desconto de 10% R$ {avista_10} ")
elif pagamento == 2:
    print(f"A vista no cartão 5% de desconto R$ {avista_5}")
elif pagamento == 3:
    print(f"Parcelado no cartão em 2x sem juros R$ {cartao_2x} reais por parcela")
else:
    print(f"Parcelado no cartão em 3x com 20% de juros R$ {cartao_3x_jurus_20} reais por parcela")

#################################################################################################################

# versao do GPT  
print("Elabore um programa que calcule o valor a ser pago por um produto\nconsiderando o seu preço normal e condição de pagamento:\nà vista dinheiro/cheque: 10% de desconto\nà vista no cartão: 5% de desconto\nem até 2x no cartão: preço formal\n3x ou mais no cartão: 20% de juros")
print()

produto = float(input("Digite o valor do produto: R$ "))
print()
print("FORMAS DE PAGAMENTO:")
print("1 - Dinheiro/Cheque (10% de desconto)")
print("2 - Cartão à vista (5% de desconto)")
print("3 - Cartão em 2x (sem juros)")
print("4 - Cartão em 3x ou mais (20% de juros)")

pagamento = int(input("Escolha a forma de pagamento (1/2/3/4): "))

if pagamento == 1:
    valor_final = produto - (produto * 0.10)
    print(f"Pagamento à vista no dinheiro/cheque. Total: R$ {valor_final:.2f}")
elif pagamento == 2:
    valor_final = produto - (produto * 0.05)
    print(f"Pagamento à vista no cartão. Total: R$ {valor_final:.2f}")
elif pagamento == 3:
    parcela = produto / 2
    print(f"Pagamento em 2x no cartão. 2 parcelas de R$ {parcela:.2f}")
    print(f"Total: R$ {produto:.2f}")
elif pagamento == 4:
    total_com_juros = produto + (produto * 0.20)
    parcela = total_com_juros / 3
    print(f"Pagamento em 3x com juros. 3 parcelas de R$ {parcela:.2f}")
    print(f"Total com juros: R$ {total_com_juros:.2f}")
else:
    print("Opção de pagamento inválida.")
