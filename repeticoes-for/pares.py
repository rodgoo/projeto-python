pares = 0  # guarda a soma dos PARES
paresCont = 0 # mostra quantos PARES foram digitados

imp = 0  # guarda a soma dos IMPARES
impCont = 0 # mostra quantos IMPARES foram digitados

for n in range(1,7):
    numero = int(input(f'Digite o {n} valor:'))
    if numero == 0: # Valida se algum número inputado é 0, se for, quebra o código na hora!
        print('Esse número não permite operações, tente valores diferentes')
        break

    if numero % 2 == 0:
        pares += numero
        paresCont += 1

    elif numero % 2 != 0:
        imp += numero
        impCont += 1

if numero !=0:
    print(f'Números informados: {paresCont} pares, e soma {pares}')
    print(f'Números informados: {impCont} ímpares, e soma {imp}')
