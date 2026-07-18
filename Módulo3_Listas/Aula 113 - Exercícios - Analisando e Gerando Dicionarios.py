#print("Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: ")
#print("Quantidade de nota.\nA maior nota.\nA menor nota.\nA média da turma.\nA situação (opcional)
print()
def notas(*nota, sit=False):
    """
    Função para analisar notas e situações de vários alunos
    :param nota: Uma ou mais notas dos alunos.
    :param sit: Valor opcional, indicando se deve ou nãp adicionar situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(nota)
    r['Maior Nota'] = max(nota)
    r['Menor Nota'] = min(nota)
    r['Média Geral'] = sum(nota)/len(nota)
    if sit:
        if r['Média Geral'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média Geral'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


#PROGRAMA PRINCIPAL
resp = notas(2.5, 5.5, 7.0, 10.0, 5.75, sit=True)
print(resp)








