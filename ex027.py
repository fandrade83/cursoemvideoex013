'''
Faça Um Prog. que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e ultimo nome separadamente.
EX: Ana Maria de Souza
Primeiro = Ana
Ultimo = Souza
'''
n = str(input('Digite Seu nome Completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu Primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))




