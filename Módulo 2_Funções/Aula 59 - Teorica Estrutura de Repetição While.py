n = 1     # garante que o while rode pela primeira vez
par = impar = 0   # Modo de mostrar que ambas as variaveis é zero e deixa o codigo enxuto, na mesma linha
while n != 0:   # enquanto n for diferente de zero, continue
    n = int(input("Digite um Valor: ")) # valor digitado pelo usuario
    if n != 0: # SE n for diferente de zero
        if n % 2 == 0: # SE  n for divisivel por 2 e igual a zero
            par += 1   # contador de quantos pares  
        else:
            impar += 1
print(f"Voce digitou {par} números pares e {impar} números ímpares.")