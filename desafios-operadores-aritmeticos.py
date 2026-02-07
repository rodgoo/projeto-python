p1 = int(input('[Pergunta 1]: Olá! Vou te mostrar o antecessor e sucesso de um número, por favor, me fale um valor: '))

suc = p1+1
ant = p1-1

print('Seu sucessor é:',suc)
print('Seu antecessor é:',ant)

p2 = int(input('[Pergunta 2]: Agora, me diga um número e te direi seu dobro, triplo e raiz quadrada, por favor:'))

dobro = p2**2
triplo = p2**3
raiz = p2**(1/2)

print('Seu dobro é:',dobro)
print('Seu triplo é:',triplo)
print(f'Sua raiz é: {raiz:.3f}')

p3 = int(input('[Pergunta 3]: Me diga duas notas de um aluno, calcularei e te falo a média. Valor 01:'))
p31 = int(input('[Pergunta 3]: Valor 02:'))

mediaCalculo = (p3+p31)//2
mediaCalculo1 = (p3+p31)/2

print('A média encontrada foi de:',mediaCalculo)
print('Média exata encontrada:',mediaCalculo1)

p4 = int(input('[Pergunta 4]: Escreva um valor em METROS, para ser convertido em CENTÍMETROS e MILÍMETROS:'))

cent = p4*100
mil = p4*1000

print('Em CENTÍMETROS,o valor:{} é {}cm'.format(p4,cent))
print('Em MILÍMETROS,o valor:{} é {}mm'.format(p4,mil))

p5 = int(input('[Pergunta 5]: Escreva um valor, em seguida, será disponibilizado sua tabuada em multiplicação:'))

numero = p5

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

p6 = int(input('[Pergunta 6]: Digite o seu valor em carteira: '))
valorReal = p6
dolar = 3.27

dolaresDisponível = valorReal/dolar

print('Com essa sua quantida, é possível comprar {:.1f} doláres, parabéns!'.format(dolaresDisponível, dolaresDisponível))

largura = float(input('[Pergunta 7]: Digite a largura de uma parede: '))
altura = float(input('Digite a altura de uma parede: '))

area = (largura * altura)
pintando= area/2

print(f'A área da parede é de: {area:.2f}m²')
print(f'Será necessário {pintando:.2f} litros de tinta para pintar essa parede de {area:.2f}m²')

valoriginal = float(input('[Pergunta 8]: Será realizada uma queima de estoque na loja, me informe um valor e te levarei ao valor do novo preço com 5% de desconto'))

desconto = valoriginal * 0.05
novalor = valoriginal - desconto

print(f'O novo valor já com desconto de 5% é de {novalor}')

salarioOriginal = float(input('[Pergunta 9 - Final]: Você ganhou um aumento de 15% em seu salário, por favor, me informe seu salário atual:'))

aumento = salarioOriginal * 0.15
salarioNovo = salarioOriginal + aumento

print(f'Parabéns! Seu novo salário é de: {salarioNovo:.2f}')
