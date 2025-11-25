#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diaria = 60.00
valor_por_km = 0.15

veiculo = float(input("Qual a Permanecia de uso do veículo em dias?: "))
rodagem = float(input("Digite a kilometragem percorrida?: "))

custo_dia = veiculo * diaria
custo_km = rodagem * valor_por_km
custo_total = custo_dia + custo_km

print(f"Valor total a pagar é: R${custo_total}\n- Valor por km rodados: R${custo_km}\n- Valor da diária: R${custo_dia}")