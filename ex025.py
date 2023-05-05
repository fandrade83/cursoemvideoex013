'''
Droe um prog. que leia o nome de uma pessoa e diga se tem 'SILVA' no nome.
'''

nome = str(input('Digite Seu Nome Completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))


