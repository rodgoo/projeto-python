def notas(*n, sit=False):
    """
    Função que analisa notas e situações de alunos
    :param n: notas dos alunos disponibilizadas
    :param sit: valor opcional sobre verificação de situação do aluno
    :return: dicionário com várias informações sobre a turma
    """
    d = dict()
    d['TOTAL'] = len(n)
    d['MAIOR'] = max(n)
    d['MENOR'] = min(n)
    d['MÉDIA'] = sum(n)/len(n)

    if sit:
        if d['MÉDIA'] >= 7:
            d['SITUAÇÃO'] = 'Boa'
        elif d['MÉDIA'] >= 5:
            d['SITUAÇÃO'] = 'Razoável'
        else:
            d['SITUAÇÃO'] = 'Ruim'


    return d


#Programa Principal
resultado = notas(5, 6.4, 2, 8.6, sit=True)
print(resultado)