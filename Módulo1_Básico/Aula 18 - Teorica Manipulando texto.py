print()
print()
print("Curso em vídeo Python")
print()

frase = str("Curso em Video Python")

print(frase[6])         # Mostra o caractere na posição 6 (começa do 0).
print(frase[6:])        # Mostra do caractere 6 até o final da string.
print(frase[:6])        # Mostra do início até o caractere 5.
print(frase[3:13])      # Mostra do caractere 3 até o 12 (o final não entra).
print(frase[6::2])      # Mostra do caractere 6 até o fim, pulando de 2 em 2.

print(len(frase))       # Conta quantos caracteres tem a string, incluindo os espaços.

print(frase.find("deo"))  # Mostra a posição onde começa a palavra "deo" (ou -1 se não encontrar).
print(frase.count("o"))   # Conta quantas vezes a letra "o" aparece na string.

print("Curso" in frase)   # Verifica se "Curso" está dentro da string. Retorna True ou False.

print(frase.replace("Video", "Tela"))  # Substitui "Video" por "Tela" (sem alterar a original).

print(frase.upper())      # Converte toda a string para letras MAIÚSCULAS.
print(frase.lower())      # Converte toda a string para letras minúsculas.

print(frase.capitalize()) # Deixa só a primeira letra da frase maiúscula, o resto em minúsculas.
print(frase.title())      # Deixa a primeira letra de cada palavra em maiúscula.

print(frase.strip())      # Remove todos os espaços extras do começo e do final da string.
print(frase.lstrip())     # Remove apenas os espaços do lado esquerdo (início).
print(frase.rstrip())     # Remove apenas os espaços do lado direito (final).

print(frase.split())      # Separa a string em palavras e coloca cada uma em uma posição de uma lista.

print("".join(frase))     # Junta a string caractere por caractere. Pode colocar algo entre aspas para separar, ex: "-".join(frase)
