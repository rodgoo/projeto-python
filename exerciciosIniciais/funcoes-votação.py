def voto(ano):
    import datetime
    atual = datetime.date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Idade: {idade} anos. Idade não elegível para votação'
    elif idade >= 16 and idade < 18 or idade >= 65:
        return f'Idade: {idade} anos. Voto opcional'
    else:
        return f'Idade: {idade} anos. Voto obrigatório!'

print(voto(int(input('Digite seu ano de nascimento: '))))