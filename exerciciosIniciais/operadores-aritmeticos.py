n1 = int(input('Digite um valor 01: '))
n2 = int(input('Digite um valor 02: '))

soma = n1 + n2
sub = n1 - n2
mult= n1 * n2
div = n1 / n2
divi = n1 // n2
exponent = n1 ** n2
sobra = n1 % n2
igual = n1 == n2

print('A soma entre {} e {} vale: {}'.format(n1, n2, soma))
print('A subtração entre {} e {} vale: {}'.format(n1, n2, sub))
print('A multiplicação entre {} e {} vale: {}'.format(n1, n2, mult))
print('A divisão entre {} e {} vale: {:.3f} (sem arrendomdamento de 3 casas decimais): {}'.format(n1, n2, div, div))
print('A divisão exata entre {} e {} vale: {}'.format(n1, n2, divi))
print('A exponencição entre {} e {} é: {}'.format(n1, n2, exponent))
print('A sobra entre {} e {} é: {}'.format(n1, n2, sobra))
print('Os valores entre {} e {} são iguais? {}'.format(n1, n2, igual))


