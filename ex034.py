'''
Escreva um prog. que pergunte o salario de um funcionario e
calcule o valor do seu aumento.

Para Salarios superiores a R$1.200,00. calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Qual é o salario do funcionario? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem Ganhava R$ {:.2f} passa a ganhar {:.2f} agora'.format(salario, novo))
