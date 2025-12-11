while True:
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")

    if len(senha) < 5:
        print("Onome de usuario deve ter pelo menos 5 caracteres. Tente novamente.")
        continue
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 dígitos. Tente novamente.")
        continue    

    print("Cadastro realizado com sucesso!")
    break