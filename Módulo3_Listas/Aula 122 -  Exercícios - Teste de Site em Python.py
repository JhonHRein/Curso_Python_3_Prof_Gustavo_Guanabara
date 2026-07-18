#print(Crie um código em Python que teste se o site pudim está acessível pelo computador usado.)
print()
import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site pudim nao esta acessível no momento!")
else:
    print("Conseguir acessar o site Pudim com sucesso!")
    print(site.read())

####################################################################
"""
📌 Exercício: Testar se o site Pudim está acessível

🔹 Bibliotecas usadas:
1. import urllib
   - Módulo nativo do Python para trabalhar com URLs (endereços da internet).
   - Possui submódulos como: urllib.request, urllib.error, urllib.parse etc.

2. import urllib.request
   - Responsável por abrir e ler URLs, como se fosse um navegador acessando páginas.
   - O comando urllib.request.urlopen("url") tenta abrir a página e retorna um objeto com os dados dela (conteúdo HTML, por exemplo).

------------------------------------------------------------

🔹 Estrutura do código:

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")

- O programa tenta acessar o site Pudim.
- Se a conexão for bem-sucedida, a variável 'site' recebe o objeto com o conteúdo da página.
- Se der erro (ex: sem internet, site fora do ar), o programa não quebra porque temos o try/except.

------------------------------------------------------------

except urllib.error.URLError:
    print("O site pudim nao esta acessível no momento!")

- Caso aconteça um erro de rede (URLError), o Python exibe a mensagem de que o site não está acessível.
- Sem esse tratamento, o programa pararia com erro.

------------------------------------------------------------

else:
    print("Conseguir acessar o site Pudim com sucesso!")
    print(site.read())

- O bloco else só executa se NÃO ocorrer nenhum erro no try.
- Primeiro, confirma que o acesso deu certo.
- Depois, exibe o conteúdo do site com site.read(), que mostra o HTML cru da página.

------------------------------------------------------------

🔹 Em resumo:
- urllib.request.urlopen("url") → tenta abrir a página.
- except urllib.error.URLError → trata erro de conexão (site fora do ar, sem internet, etc).
- site.read() → lê e exibe o conteúdo HTML do site.

Esse exercício é uma introdução prática a:
✅ Tratamento de exceções com try/except
✅ Testes de conexão de rede
"""

