'''
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.
'''


real = float(input('Quanto dinheiro vc tem na carteira?: R$ '))
dollar = float(input('Digite a cotação do dollar hoje em reais: R$ '))
euro = float(input('Digite a cotação do euro hoje em reais: '))
dollar = real / 5.25
euro = real / 5.64
dollar = euro / 5.64
euro = dollar / 5.25
print('Com R${:.2f} vc pode comprar US$ {:.2f}'.format(real, dollar))
print('Com R${:.2f} vc pode comprar EU$ {:.2f}'.format(real, euro))
print('Com US${:.2f} vc pode comprar EU$ {:.2f}'.format(dollar, euro))
print('Com EU${:.2f} vc pode comprar US$ {:.2f}'.format(euro, dollar))



