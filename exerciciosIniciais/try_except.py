try:
    a=int(input('Digite um valor: '))
    b=int(input('Digite outro valor: '))
    r = a/b

except (ValueError, TypeError):
    print('Houve um problema com os tipos de dados digitados')

except ZeroDivisionError:
    print(f'{a} não pode ser dividido por 0')

except (KeyboardInterrupt):
    print('Houve uma parada abrupta duratne a inserção de erros')

except Exception as erro:
    print(f'O erro encontrado foi: {erro}')
# --------------- CLÁUSULAS OPCIONAIS ---------------
else:
    print(f'Resultado final: {r}')
finally:
    print('Volte sempre!')