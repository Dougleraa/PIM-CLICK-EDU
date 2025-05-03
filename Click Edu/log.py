import banco

def login():
    global usuario_logado
    print('\033[36mVocê escolheu a opção de login\033[0m')
    email = input('\033[36mDigite seu email: \033[0m')
    senha = input('\033[36mDigite sua senha: \033[0m')
    usuarios = banco.carregar_dados()
    ### laço para verificar se usuario já foi cadastrado e se a senha está correta ###
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print('Login efetuado com sucesso !! seja bem vindo(a), {}!'.format(usuario['nome_user']))
            usuario_logado = usuario # login com sucesso
            if "frequencia" not in usuario_logado:
                usuario_logado["frequencia"] = {"Pensamento": 0, "Segurança": 0, "Python": 0}

            return True
    print('email ou senha incorretos, tente novamente !')
    return False

def logout():
    global usuario_logado
    if usuario_logado:
        print(f'\033[36mUsuário {usuario_logado["nome"]} fez logoff.\033[0m')
        usuario_logado = None
    else:
        print('\033[33mNenhum usuário está logado.\033[0m')
usuario_logado = None
