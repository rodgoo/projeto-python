# Define a função para dobra de valores
def dobra(valores):
    pos=0
    while pos < len(valores):
        valores[pos] *= 2
        pos +=1

#Define os valores
valores = [6,3,9,1,0,2]

#Chama a dobra dos valores
dobra(valores)
print(valores)


