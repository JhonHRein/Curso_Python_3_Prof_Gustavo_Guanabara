import math

numm = float(input("Digite um valor:"))
pot = pow(numm, 2)
print("O quadrado de {} é {}".format(numm,pot))


from math import sqrt,floor
print()
num = float(input("Digite um novo valor:"))
raiz = sqrt(num)
print("A potencia de {} é igual a {}".format(num,floor(raiz)))
print("Exercicio 1 : Codex")
print()

import math
num1 = float(input("Digite um numero qualquer:"))
inteiro = math.trunc(num1)
print("o numero {} tem sua parte inteira {}".format(num1,inteiro))
print("_"*50)
print()
print("Exercicio 2 : codex")
print()

import math
n1 = float(input("digite um numero:"))
n2 = math.trunc(n1)
n3 = int(n1)
n4 = math.ceil(n1)
print(" formato trunc {}, formato ceil {}, formato int {}".format(n2,n4,n3))
print("_"*50)
print()
print("Exercicio 3 : Codex")
print()

import math
valor_compra = float(input("Digite o valor da sua compra :"))
valor_pago = float(input("Digite o valor de pagamento:"))
troco_correto = valor_pago - valor_compra
troco = math.trunc(troco_correto)
trocor = math.ceil(troco_correto)
troco_real = float(troco_correto)
print("Valor do produto R$:{}\nValor do pagamento R$ {}\nTroco Inteiro R$ {}\nValor arredondado R$ {}\nTroco com centavos R$ {:.2f}".format(valor_compra,valor_pago,troco,trocor,troco_real))
