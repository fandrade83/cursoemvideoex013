'''
Crie um prog. que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras em maiúsculos e minusculas.
Quantas letras ao todo (sem considerar os espaços).
Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome Completo: ')).strip()
print('Analisamdo seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minpusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
