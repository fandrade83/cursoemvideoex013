'''
Desenvolva um prog. que pergunta a distancia de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens
mais longas.
'''
'''distancia = float(input('Qual é a distancia da sua viagem? '))
print('Vc esta orestes a começar uma viagem de {}km. '.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''

distancia = float(input('Qual é a distancia da sua viagem? '))
print('Vc esta orestes a começar uma viagem de {}km. '.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))




