# Faça um programa que leia pelo teclado
# e mostre na tela o seu tipo primivito
# e todas as ingormaçoes prossiveis sobre ela.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem Espaços? ', a.isspace())
print('É um Numero? ', a.isnumeric())
print('É Alfabétito? ', a.isalpha())
print('É Alfanumérico? ', a.isalnum())
print('Ésta em Maiusculo? ', a.isupper())
print('É Minusculo? ', a.islower())
print('Ésta Capitalizada? ', a.istitle())


