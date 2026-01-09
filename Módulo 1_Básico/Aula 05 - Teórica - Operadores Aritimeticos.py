#Operadores aritimeticos.

n1 = int(input(" Digite um valor: "))
n2 = int(input(" Digite outro valor: "))
soma = n1 + n2
media = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
resto_divisao = n1 % n2
elevado_potencia = n1 ** n2

print(" A soma é: {}\n O produto é: {}\n Divisão é: {:.2f}".format(soma,media,divisao))   #Formatação Antiga.
print(" A divisão inteira é: {}\n O resto da divisão é: {}\n A potência é: {}".format(divisao_inteira,resto_divisao,elevado_potencia))