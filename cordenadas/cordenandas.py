cordenadas_x = input('Digite as coordenada x: ')
cordenadas_y = input('Digite as coordenada y: ')

if cordenadas_x>'0' and cordenadas_y>'0':
    print("As coordenadas estão no primeiro quadrante.")
elif cordenadas_x < '0' and cordenadas_y > '0':
    print("As coordenadas estão no segundo quadrante.")
elif cordenadas_x < '0' and cordenadas_y < '0':
    print("As coordenadas estão no terceiro quadrante.") 
elif cordenadas_x > '0' and cordenadas_y < '0':
    print("As coordenadas estão no quarto quadrante.")
else:
    print("As coordenadas estão na origem.")    