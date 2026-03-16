import math

numeroReal = float(input('Digite um número, pode ser quebrado:'))

numeroInteiro = int(numeroReal)
numeroInteiroBiblioteca = math.trunc(numeroReal)

print(f'Forma nativa de fazer, usando (int): {numeroInteiro}')
print(f'Forma com biblioteca integrada, usando (math.trunc): {numeroInteiroBiblioteca}')