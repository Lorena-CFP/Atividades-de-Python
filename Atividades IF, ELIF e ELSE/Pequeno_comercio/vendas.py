venda_macas=int(input('Digite o valor da venda de maçãs: '))
venda_bananas=int(input('Digite o valor da venda de bananas: '))

if venda_macas > venda_bananas:
    print('A venda de maçãs foi maior.')
elif venda_bananas > venda_macas:
    print('A venda de bananas foi maior.')
else:
    print('As vendas foram iguais.')    