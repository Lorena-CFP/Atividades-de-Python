n1=int(input('Digite a primeira nota: '))
n2=int(input('Digite a segunda nota: '))
n3=int(input('Digite a terceira nota: '))
media=(n1+n2+n3)/2

if media >= 7:
    print('Aprovado!') 
elif media >=5 and media <7:
    print('Recuperação.')
else:
    print('Reprovado.')