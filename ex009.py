'''
Exercício Python 9: Faça um programa que leia um número Inteiro qualquer
e mostre na tela a sua tabuada.
'''

n = int(input('Digite um\033[1;34m numero\033[m para ver sua taboada: '))
print('_' * 12)
print('\033[0;34m{} x {:2} = {:2}\033[m'.format(n, 1, n*1))
print('\033[0;34m{} x {:2} = {:2}\033[m'.format(n, 2, n*2))
print('\033[0;34m{} x {:2} = {:2}\033[m'.format(n, 3, n*3))
print('\033[0;34m{} x {:2} = {}\033[m'.format(n, 4, n*4))
print('\033[0;34m{} x {:2} = {}\033[m'.format(n, 5, n*5))
print('\033[0;34m{} x {:2} = {}\033[m'.format(n, 6, n*6))
print('\033[0;34m{} x {:2} = {}\033[m'.format(n, 7, n*7))
print('\033[0;34m{} x {:2} = {}\033[m'.format(n, 8, n*8))
print('\033[0;34m{} x {:2} = {}\033[m'.format(n, 9, n*9))
print('\033[0;34m{} x {:2} = {}\033[m'.format(n, 10, n*10))
print('_' * 12)
