num = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Ana', 'Bruno', 'Carlos', 'Diana']
nasc_anos = [2004, 2025]

for n in num:
    print(n)

for nome in nomes: 
    print(nome)

for ano in nasc_anos:
    idade = 2025 - ano
    print(f'Quem nasceu em {ano} tem {idade} anos em 2025.')


for i in range(10, 0, -1):
    print(i)


print('Tabuada de Multiplicação')    
digitado = input('Digite um numero pra fazer uma tabuada:')

for i in range(1, 11):
    resultado = int(digitado) * i
    print(f'{digitado} x {i} = {resultado}')


lista_num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
soma = 0    

try:
    for n in lista_num:
        soma += n
    print(f'A soma dos números da lista é: {soma}')
except Exception as e:
    print('Erro: A lista contém um valor não numérico.')


lista_valores = [5, 10, 23, 42, 57, 68, 79, 81, 95, 100]
soma_valores = 0    

try:
    for valor in lista_valores:
        soma_valores += valor
    print(f'A soma dos valores da lista é: {soma_valores}')
except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida.')
except Exception as e:
    print('Erro: Ocorreu um erro ao processar a lista.')