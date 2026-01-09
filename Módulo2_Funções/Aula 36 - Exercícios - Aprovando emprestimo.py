print()
print("Exercício Python 36:\nEscreva um programa para aprovar o empréstimo bancário para a compra de uma casa.\nPergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.\nA prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.")
print()
print("Programa para analise de empréstimos bancários, digite as suas informações a seguir:")
print()
print("**"*50)
import time
valor_imovel = float(input("Qual o valor do imóvel?: "))
salario_base = float(input("Qual o valor do seu Salário atual?: "))
anos = float(input("Em Quantos anos deseja parcelar esse empréstimo?: "))
parcelas_mensais = valor_imovel / (anos * 12)
limite_credito_30 = salario_base * 0.30
numero_parcela = int(anos * 12)
print()
if limite_credito_30 > parcelas_mensais:
    print("PARABENS!!, seu empréstimo foi APROVADO.")
    print("Voce pagará {} parcelas de R${:.2f} reais mensais".format(numero_parcela, parcelas_mensais))
elif limite_credito_30 == parcelas_mensais:
    print("Seu pedido de empréstimo vai para avaliação interna.")
else:
    print("Analisando...")
    time.sleep(3)
    print("Seu pedido de empréstimo foi NEGADO!")


