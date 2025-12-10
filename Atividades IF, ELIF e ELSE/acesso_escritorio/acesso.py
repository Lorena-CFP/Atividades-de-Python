hora_acesso=int(input('Digite a hora de acesso ao escritório (0-23): '))

if hora_acesso < 8 or hora_acesso > 18:
    print('Acesso negado. Fora do horário de expediente.')
else:   
    print('Acesso permitido. Bem-vindo ao escritório.')