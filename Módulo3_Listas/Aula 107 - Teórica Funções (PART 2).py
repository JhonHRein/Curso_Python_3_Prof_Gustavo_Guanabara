#INTERACTIVE HELPE, OU ajuda interativa, pode se chamar de help()
#formas de chamar a ajuda, usando o python console, ou dessas formas a baixo.
print()
def contador(i, f, p):
    """
    • > Faz uma contagem e mostra na tela
    :param i: inicio de contagem.
    :param f: Fim da Contagem
    :param p: Passo da contagem
    :return: Sem Retorno
    Função criada por Dev. Jhon Herbert Rein.
    """
    c = i
    while c <= f:
        print(f"{c}", end=" ")
        c += p
    print("Fim")

#Programa Principal
contador(0, 50, 4)

help(contador)


#_________________________________________________________________
# PARAMETERS OPCIONAL

def somar(a, b, c):
    s = a + b + c
    print(f" a soma vale {s}")



somar(3, 2, 5)
somar(8, 4)



##########################################################
def somar(*valores, mostrar=True):
    """
    Função que soma vários números.
    :param valores: Vários números (quantidade indefinida)
    :param mostrar: (opcional) se True, mostra o resultado na tela. Se False, só retorna o valor.
    """

    total = 0
    for numero in valores:  # percorre cada número recebido
        total += numero  # soma todos

    if mostrar:  # se o usuário não passar nada, mostrar=True por padrão
        print(f"A soma dos valores {valores} é {total}")
    return total  # devolve o resultado (sempre)


# ====== Programa Principal ======

somar(2, 4, 6)  # Mostra a soma na tela (porque mostrar=True por padrão)
resultado = somar(10, 20, 30, mostrar=False)  # Não imprime nada, mas guarda na variável
print(f"O resultado armazenado foi: {resultado}")

##########################################################################
"""
📌 RESUMO: ESCOPO DE VARIÁVEIS EM PYTHON

1. Variável Local:
   - Criada dentro de uma função.
   - Só existe dentro dessa função.
   - Some da memória quando a função termina.

2. Variável Global:
   - Criada fora de todas as funções.
   - Pode ser usada por qualquer função do programa.
   - Mas, se você tentar modificar uma variável global dentro de uma função,
     precisa usar a palavra-chave 'global'.

⚡ Regra de ouro:
- Tudo que é criado DENTRO de def é LOCAL (a não ser que use 'global').
- Tudo que é criado FORA de def é GLOBAL.
"""

# Exemplo prático:

# Variável global
mensagem = "Sou Global!"

def exemplo1():
    # Variável local (só existe aqui dentro)
    mensagem_local = "Sou Local!"
    print("Dentro da função:", mensagem_local)

def exemplo2():
    # Aqui conseguimos LER a variável global, mas não mudá-la
    print("Dentro da função:", mensagem)

def exemplo3():
    global mensagem  # avisamos ao Python que vamos mexer na global
    mensagem = "Fui alterada dentro da função!"
    print("Dentro da função:", mensagem)


# ===== Programa Principal =====
print("---- Teste 1 ----")
exemplo1()
# print(mensagem_local)  # ❌ ERRO! (não existe fora da função)

print("\n---- Teste 2 ----")
exemplo2()
print("Fora da função:", mensagem)

##################################################################################
#Retorno de valores

"""
📌 RESUMO: RETORNO DE VALORES EM FUNÇÕES (return)

1. Por padrão, funções em Python não retornam nada → retornam 'None'.
2. Usamos 'return' para devolver um valor para quem chamou a função.
3. Uma função pode:
   - Retornar um único valor.
   - Retornar vários valores (em forma de tupla).
   - Encerrar imediatamente a execução (tudo depois do 'return' é ignorado).
"""

# -------- Exemplo 1: Sem return --------
def somar_sem_retorno(a, b):
    print("A soma é:", a + b)  # apenas mostra na tela

resultado = somar_sem_retorno(5, 3)
print("Resultado guardado:", resultado)  # Resultado será None


# -------- Exemplo 2: Com return --------
def somar_com_retorno(a, b):
    return a + b  # devolve o valor da soma

resultado = somar_com_retorno(5, 3)
print("Resultado guardado:", resultado)  # Agora temos o valor em 'resultado'


# -------- Exemplo 3: Vários returns --------
def par_ou_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print("7 é:", par_ou_impar(7))
print("8 é:", par_ou_impar(8))


# -------- Exemplo 4: Vários valores --------
def operacoes(a, b):
    soma = a + b
    sub = a - b
    mult = a * b
    return soma, sub, mult  # retorna uma tupla (3 valores)

res = operacoes(10, 5)
print("Resultado completo:", res)       # (15, 5, 50)
print("Apenas soma:", res[0])           # 15





