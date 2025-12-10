dia_um=input('Digite o primeiro dia em numero:')
dia_dois=input('Digite o segundo dia em numero:')
dia_tres=input('Digite o terceiro dia em numero:')

if (dia_um >=0 and dia_dois >= 0 and dia_tres >=0):
    tempo_total = int(dia_um) + int(dia_dois) + int(dia_tres)
    print(f'O tempo total é de {tempo_total} dias.')
else:
    print('Por favor, insira valores válidos para os dias.')
  