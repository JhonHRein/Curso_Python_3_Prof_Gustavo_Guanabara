print("Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5\ne peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.\nO programa deverá escrever na tela se o usuário venceu ou perdeu.")
#print()
#print("Vou pensar em um numero entre 0 e 10. Tente Adivinhar...")
#numero = str(input("Em qual numero eu pensei?")).strip()
#print()
#("Analisando sua resposta!....puff")
#print()
#if numero == "7":
   # print("PARABENS!, VOCÊ ACERTOU")
#else:
   # print("ERROOOOOUU!!  HAHAHAH! Tente de novo!!")
#print()
print()
print("*"*50)
print()
print("METODO DO PROFESSOR E CHATGPT")
print()
from random import randint  #metodo para escolher numero aleatorio inteiro.
from time import sleep      #metodo para fazer esperar alguns segundos ate o proximo comando.
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
numero_pensado = randint(0, 10)
numero = int(input("Em qual número eu pensei? ").strip())

print("\nAnalisando sua resposta... puff 💭\n")
sleep(2)
if numero == numero_pensado:
    print("PARABÉNS! VOCÊ ACERTOU!")
else:
    print("ERROOOOU!! HAHAHA! Eu pensei no número {}.".format(numero_pensado))