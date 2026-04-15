#print("Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.")
print()
times = "Corinthians", "Palmeiras", "Santos", "Sao Palo"
vogais = "aeiouAEIOU"
contador_vogais = 0
for nome_time in times:
    vogais_encontradas = ""
    for letra in nome_time:
        if letra in vogais:
            contador_vogais += 1
            vogais_encontradas += letra
    print(f"Na palavra: {nome_time}, temos as vogais: {vogais_encontradas}")
print(f"O numero de vogais em todos os times é {contador_vogais}")


