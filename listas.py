num = [2,5,9,1]
num[2] = 3 # Altera o número da posição 0,1,[2] para o número 3

num.append(4) # Adiciona o número 4 à lista
num.sort() # Sorteia os números em ordem crescente
num.insert(2,0) # Inseriu o número 0 na posição 0,1,[2] do código (alterando a posição dos índices)
num.pop() # Deleta o ÚLTIMO elemento da lista
num.pop(2) # Deleta o elemento 0,1,[2] da lista
num.sort(reverse=True) # Sorteia os números em ordem crescente e REVERTE A ORDEM

if 4 in num:
    num.remove(4)
    print('Número 4 removido com sucesso!')
else:
    print('Número 4 não está na lista')

print(num)
print(f'Essa linha conta com {len(num)} elementos!')