
#print("Crie um programa que leia um numero de 0 a 9999 e mostre na tela\nCada um dos Digitos separados")
print()
#Resoluçao do professor
n1 = int(input("Digite um numero de 0 a 9999:"))
n = str(n1)
print("Analisando o numero {}".format(n1))
print("Unidade:{}".format(n[3]))
print("Dezena:{}".format(n[2]))
print("Centena:{}".format(n[1]))
print("Milhar:{}".format(n[0]))

#print("obs: 01 : Nesse caso o (int) numero primitivo que so serve para numeros inteiros nao podendo fatiar\nou seja colocando n = str(n1), transforma o int em string, podendo fatiar por caracteres usando o .format(n[])")

#print("Resolvendo exercicios de forma matematica para cada unidade de medida")
print()
n2 = int(input("Digite um valor de 0 a 9999:"))
u = n2 // 1 % 10
d = n2 // 10 % 10
c = n2 // 100 % 10
m = n2 // 1000 % 10
print("Analisando o numero {}".format(n2))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))