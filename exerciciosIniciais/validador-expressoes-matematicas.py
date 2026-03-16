expressao = input('Digite uma expressão a ser validada: ')
pilha = list()

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')

    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão Invalida ou Incompleta!')