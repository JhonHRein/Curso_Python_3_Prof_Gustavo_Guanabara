#Somando dois numeros!

print()
num1 = int(input("Digite um valor : "))
num2 = int(input("Digite um novo numero: "))
soma = num1 + num2
print(f"A soma entre o numero {num1} e {num2} é: {soma}")
print()

n1 = float(input("Digite um numero:"))
n2 = float(input("Digite outro numero:"))
s = n1 + n2
print('a soma entre',n1, 'e',n2, 'vale:',s)              #Ex. com Formatação antiga
print("A soma entre {} e {} vale: {}".format(n1, n2, s)) #Exemplo com formataçao usando .format
print(f"a soma entre {n1} e {n2} vale: {s}")             #Exemplo com formataçao atual, usando f-string.
print()


#Usando (str) com numeros nao acontece a soma, apenas uniao dos valores das variáveis! identifica como texto!
n1 = str(input("Digite um numero:"))
n2 = str(input("Digite outro numero:"))
s = n1 + n2
print('a soma entre',n1, 'e',n2, 'vale:',s)                   #Ex. com Formatação antiga
print("A soma entre {} e {} vale: {}".format(n1, n2, s))      #Exemplo com formataçao usando .format
print(f"a soma entre {n1} e {n2} vale: {s}")                  #Exemplo com formataçao atual, usando f-string.