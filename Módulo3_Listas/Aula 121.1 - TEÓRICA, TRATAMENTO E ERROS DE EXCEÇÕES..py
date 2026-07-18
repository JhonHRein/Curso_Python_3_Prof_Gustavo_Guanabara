#Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.
print()
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que voce digitou!")
except Exception as erro:
    print(f"Infelizmente tivemos um problema {erro.__class__}")
except ZeroDivisionError:
    print("Não é possível dividir um numero por zero!")
except KeyboardInterrupt:
    print("O usuário preferiu nao informar os dados!")
else:
    print(f"O resultado é {r:.2f}")
finally:
    print("Volte sempre! Muito Obrigado!")




#####################################################################################
"""
📌 Aula: Tratamento de Erros e Exceções em Python

➡ O que são erros?
Erros são problemas que acontecem durante a execução do programa e que podem fazer com que ele pare de funcionar.

Exemplo comum:
    print(10/0)   # Erro de divisão por zero

➡ Diferença entre Erro e Exceção:
- Erro de sintaxe: acontece quando o código foi escrito errado (o programa nem executa).
- Exceção: acontece durante a execução, mesmo com o código escrito corretamente.

➡ Como tratar exceções?
Usamos o bloco try / except:

    try:
        # Código que pode gerar erro
    except:
        # Código que será executado se houver erro

➡ Exemplo básico:
    try:
        num = int(input("Digite um número: "))
        print(f"Você digitou {num}")
    except:
        print("ERRO! Você não digitou um número válido.")

➡ Usando exceções específicas:
    try:
        a = int(input("Número: "))
        b = int(input("Divisor: "))
        print(a / b)
    except ValueError:
        print("Você não digitou um número inteiro!")
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")

➡ Usando else e finally:
- else → executa apenas se NÃO ocorrer erro.
- finally → sempre executa, independente de erro ou não.

Exemplo:
    try:
        n = int(input("Digite um número: "))
    except:
        print("Erro!")
    else:
        print("Tudo certo, sem erros!")
    finally:
        print("Fim do programa.")   # Sempre será exibido

➡ Boas práticas:
1. Sempre trate exceções específicas (ValueError, ZeroDivisionError, etc.).
2. Use mensagens amigáveis para o usuário.
3. Evite deixar o programa quebrar — trate os erros e continue a execução.

"""