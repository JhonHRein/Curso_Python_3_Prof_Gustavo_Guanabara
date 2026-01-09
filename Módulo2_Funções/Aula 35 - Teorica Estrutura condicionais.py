#Estrutura Condicional Composta

nome = str(input("Qual o seu nome? ")).strip()
if nome == "Jhon":
    print("Tenha um bom dia, {}".format(nome))
else:
    print("Desculpa, achei que era outra pessoa.")
print()
print()

# ESTRUTURA CONDICIONAL ANINHADA , USANDO ELIF

nome = str(input("Qual o seu nome? ")).strip()
if nome == "Jhon":
    print("Tenha um bom dia {}".format(nome))
elif nome == "João" or nome == "Pedro" or nome == "Matheus":
    print("{}, é um nome bem comum!".format(nome))
else:
    print("Desculpa, achei que era outra pessoa.")