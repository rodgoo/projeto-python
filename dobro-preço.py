valoriginal = float(input('Será realizada uma queima de estoque na loja, me informe um valor e te levarei ao valor do novo preço com 5% de desconto'))

desconto = valoriginal * 0.05
novalor = valoriginal - desconto

print(f'O novo valor já com desconto de 5% é de {novalor}')