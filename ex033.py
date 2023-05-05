'''
Fça um prog. que leia tres numeros e mostre qual é o maior e qual é o menor
'''

a = int(input('Primeiro Valor: '))
b = int(input('Segunto Valor: '))
c = int(input('Terceiro Valor: '))
# Verificando quem é Menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é Maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O Menor valor digitado foi {menor}')
print(f'O Maior valor digitado foi {maior}')

