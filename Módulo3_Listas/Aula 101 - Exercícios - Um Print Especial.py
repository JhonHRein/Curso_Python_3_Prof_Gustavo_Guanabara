#print("Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.\nEx:\nEscreva(‘Olá, Mundo!’)Saída:\nOlá, Mundo!")
print()
def escreva(txt):
    print("~" * (len(txt) + 4))
    print(f"  {txt}")
    print("~" * (len(txt) + 4))


#programa principal
frase = str(input("Escreva uma frase: "))
escreva(txt=frase)


