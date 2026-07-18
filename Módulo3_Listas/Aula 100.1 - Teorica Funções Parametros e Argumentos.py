def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)


#############################################################
def dobrar_valores(lista_numeros):
    indice = 0
    while indice < len(lista_numeros):
        lista_numeros[indice] *= 2
        indice += 1

valores_originais = [6, 3, 9, 1, 0, 2]
dobrar_valores(valores_originais)
print(valores_originais)

"""EXPLICAÇÃO EM PORTUGUÊS LÓGICO:
Linha por linha:
def dobrar_valores(lista_numeros):
→ Estou criando uma função chamada dobrar_valores.
Ela recebe uma lista de números como parâmetro.

indice = 0
→ Crio a variável indice, que começa em zero, para percorrer a lista.

while indice < len(lista_numeros):
→ Enquanto o índice for menor que o tamanho da lista, continue o laço.

lista_numeros[indice] *= 2
→ Multiplico o valor que está na posição atual da lista por 2.

indice += 1
→ Avanço para o próximo item da lista.

valores_originais = [6, 3, 9, 1, 0, 2]
→ Crio uma lista chamada valores_originais com os valores iniciais.

dobrar_valores(valores_originais)
→ Chamo a função, enviando essa lista.
A função dobra cada número dentro dela.

print(valores_originais)
→ Imprimo a lista já modificada: [12, 6, 18, 2, 0, 4]"""