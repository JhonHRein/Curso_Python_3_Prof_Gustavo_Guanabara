print("Desenvolva uma lógica que leia o peso e a altura de uma pessoa,\ncalcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:\nIMC abaixo de 18,5: Abaixo do Peso\nEntre 18,5 e 25: Peso Ideal\n25 até 30: Sobrepeso\n30 até 40: Obesidade\nAcima de 40: Obesidade Mórbida")
print()
altura_cm = float(input("Digite o valor da sua altura: "))
peso = float(input("Digite o valor do seu peso: "))
altura_m = altura_cm / 100
massa = peso / (altura_m * altura_m)
print(f"Seu IMC é: {massa:.2f}")
if massa <= 18.5:
    print("Abaixo do peso.")
elif massa <= 25:
    print("Peso Ideal.")
elif massa <= 30:
    print("Sobrepeso.")
elif massa <= 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida.")

