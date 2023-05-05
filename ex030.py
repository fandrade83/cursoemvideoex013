'''
Crie um prog. que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.
'''

n = int(input('Digite um numero: '))
resultado = n % 2
if resultado == 0:
    print(f'O Numero {n} é PAR!')
else:
    print(f'O Numero {n} é IMPAR! ')

