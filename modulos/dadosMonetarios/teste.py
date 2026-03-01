from modulos.dadosMonetarios.utilidadesRo import moeda, dado

# É AQUI que você chama a função.
# O import acima apenas "aprende" o que é a função, ele não executa o input.
p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)