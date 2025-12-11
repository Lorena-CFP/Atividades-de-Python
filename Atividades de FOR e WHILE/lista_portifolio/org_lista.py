projetos =["website", "app móvel", "sistema de gestão", "e-commerce", None]

for projeto in projetos:
   if projeto is not None:
       print(f'{projeto}') 
else:
    print('Projeto não definido.')