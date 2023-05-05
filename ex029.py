'''
Escreva um prog. que leia a velocidade de um carro.
Se ela ultrapassar 80km/h. Mostrar msg dizendo que ele foi multado.
A multa vai custar R$7.00 por cada km acima do limite
'''
velocidade = float(input('Digite a Velocidade: '))
if velocidade > 80:
    print('MULTADO!  Voce excedeu o limite permitido que é de 80km/h ')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
