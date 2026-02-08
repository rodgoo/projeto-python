cidade = input("Digite a cidade: ").strip().lower().split()

validaSanto = 'santo' in cidade
validadorPrioridade = validaSanto and cidade[0] == 'santo'

# Valida se houver Santo
if validaSanto == True :
    print('Sua cidade possui em algum lugar o nome Santo, OK!')
else:
    print('Sua cidade não atende aos critérios desejados, tente novamente com outra cidade!')

# Valida se for a PRIMEIRA cidade que começa com Santo
if validadorPrioridade == True :
    print('Sua cidade começa com: Santo, aprovado!')

elif validaSanto == True:
    print('Sua cidade pode até conter Santo, porém, não no começo, reprovado!')

else:
    print('Nada aqui foi atendido, tente novamente com outra cidade, desde que atenda aos critérios pedidos.')

print(cidade)