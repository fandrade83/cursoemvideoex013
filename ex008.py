'''
Exercício Python 8: Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
'''

medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m correnponde a {:.0f} e {:.0f}mm'.format(medida, cm, mm))
