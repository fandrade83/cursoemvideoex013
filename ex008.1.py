'''
Exercício Python 8: Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
'''

'''
dm(Decímetro) é igual a: valor*10
cm(Centrímetro) é igual a: valor*100
mm(Milímetro) é igual a: valor*1000
dam(Decâmetro) é igual a: valor/10
hm(Hectômetro) é igual a: valor/100
km(Quilômetro) é igual a: valor/1000
vamos a resolução:
'''

medida = float(input('Digite uma distancia: '))
dam = medida / 10
hm = medida / 100
km = medida / 1000
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A distancia de {} é igual a {}dam \n {}hm \n {}km \n {}dm \n {}cm \n {}mm'.format(medida, dam, hm, km, dm, cm, mm))

