renda=int(input('Digite sua renda mensal: '))
parcela=int(input('Digite o valor da parcela do empréstimo: '))

if parcela > (renda * 0.3) and renda > 2000:
    print('Empréstimo negado. A parcela excede 30% da sua renda.')
else:
    print('Empréstimo aprovado.')