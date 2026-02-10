p3 = float(input('[Pergunta 3]: Me diga duas notas de um aluno, calcularei e te falo a média. Valor 01:'))
p31 = float(input('[Pergunta 3]: Valor 02:'))

mediaCalculo = (p3+p31)/2
mediaCalculo1 = (p3+p31)//2

media = print('A média encontrada foi de:',mediaCalculo)

if mediaCalculo < 5.0:
    print('Reprovado')

if mediaCalculo >= 5.0 and mediaCalculo <= 6.9:
    print('Recuperação')

if mediaCalculo > 7.0:
    print('Aprovado')