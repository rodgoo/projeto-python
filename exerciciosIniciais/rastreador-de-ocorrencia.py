comando = input('Digite uma comando:').upper().strip()
letra = input('Digite uma letra para ser trackeada: ').upper().strip()

geral = print(f'A letra {letra} aparece {comando.count(letra)} vezes na frase.')
primeiroA = print(f'A primeira letra {letra} aparece na posição {comando.find(letra)+1} da frase')
ultimoA = print(f'A última letra {letra} aparece na posição {comando.rfind(letra)+1} da frase')