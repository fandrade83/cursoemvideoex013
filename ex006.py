'''
Exercício Python 006: Crie um algoritmo que leia um número
e mostre o seu dobro, triplo e raiz quadrada.
'''
'''
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vle {}. \nA Raiz quadrada de {} é igual a {:.2f}.'.format(n, d, t, r))
'''

n = int(input('Digite um numero: '))
print('O dobro de {} vale {},'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrade de {} é igual a `{:.2f}'.format(n, (n*3), n, pow(n, (1/2))))



