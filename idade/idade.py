idade = int(input('Digite sua idade:'))

if idade >= 0 and idade < 12:
    print('Você é uma Criança.') 
elif idade >= 12 and idade <= 18:
    print('Você é um Adolescente.')
else:
    print('Você é um Adulto.')