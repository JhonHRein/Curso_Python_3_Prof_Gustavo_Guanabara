#print("Faça um mini sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.")
print()
print()



def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)


#PROGRAMA PRINCIPAL
comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELPE")
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')