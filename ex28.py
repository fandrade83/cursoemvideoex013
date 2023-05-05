'''Escreva um prog. que faça o computadpr "pensar" em um numero inteiro entre 0 e 5
e peça para o usuario tentar descobror qual foi o numero escolhido pelo compytador.

O prog. deverá escrever na tela se o usuario vencou ou perdeu
'''
'''n = float(input('Digite um numero: '))
if n <= 5:
    print('ACERTOU'.format(n))
else:
    print('ERROU! ')'''

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o pc "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Vc conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}'.format(computador, jogador))
