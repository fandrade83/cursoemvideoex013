'''
Daça um prog. que leia uma frase pelo teclado e mostre:
Quantas vezes aparecem a letra 'A'.
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a Ultima Vez.
'''

frase = str(input('Digite uma Frase: ')).upper().strip()
print('A letra A aparece {} vezes ma frase. '.format(frase.count('A')))
print('A primeira Letra A aparece na posição {}'.format(frase.find('A')+1))
print('A Letra A aparece pela ultima Vez na posição {}'.format(frase.rfind('A')+1))
