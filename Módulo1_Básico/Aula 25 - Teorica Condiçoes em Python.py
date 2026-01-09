print()
nome = input("Qual seu nome:").strip()
if nome == "Jhon":                                        #Condição Simples
    print("Que nome lindo voce tem!")
elif nome == "Maria":
    print("é um nome normal para mim")
else:
    print("Nao é um nome lindo como Jhon, mais ta valendo!") #Condição composta
print("Bom dia Sr(a). {}".format(nome))
print()
print()
n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
m = (n1 + n2/2)
print("Sua média é: {:.1f}".format(m))
print("PARABENS!"if m >= 8 else "ESTUDE MAIS") #Condição simplificada
