usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha de 4 dígitos: ")

if senha != "1234" or usuario != "Lorena":
    print("Senha e usuario incorreto. Acesso negado.")
else:
    print("Acesso concedido. Bem-vindo,", usuario)