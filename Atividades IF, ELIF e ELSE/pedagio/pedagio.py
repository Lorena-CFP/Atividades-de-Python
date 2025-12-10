distancia=int(input('Digite a distância percorrida em km: '))

if distancia <= 100:
    print('Pedagio: R$ 10,00') 
elif distancia > 100 and distancia <= 200:
    print('Pedagio: R$ 20,00')
else:
    print('Pedagio: R$ 30,00')