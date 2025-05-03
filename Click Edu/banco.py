import json
import os
import re

arquivo = 'alunos.json'

def cadastro():
    import datetime

    print('\033[36mVocê escolheu a opção de cadastro\033[0m')
    nome = input('\033[36mDigite seu nome completo: \033[0m').strip()
    nome_user = input('\033[36mDigite seu nome de usuário: \033[0m').strip()
    idade = input('\033[36mDigite sua idade: \033[0m')
    email = input('\033[36mDigite seu email: \033[0m')
    while True:
        senha = input('\033[36mDigite sua senha (mínimo 8 caracteres, 1 letra maiúscula, número e caractere especial): \033[0m')
        if len(senha) < 8:
            print('\033[31mA senha deve ter pelo menos 8 caracteres.\033[0m')
        elif not re.search(r'[A-Z]', senha):
            print('\033[31mA senha deve conter pelo menos uma letra MAIÚSCULA.\033[0m')
        elif not re.search(r'[a-z]', senha):
            print('\033[31mA senha deve conter pelo menos uma letra minúscula.\033[0m')
        elif not re.search(r'\d', senha):
            print('\033[31mA senha deve conter pelo menos um número.\033[0m')
        elif not re.search(r'[\W_]', senha):  # \W = qualquer caractere que não é letra ou número
            print('\033[31mA senha deve conter pelo menos um caractere especial (!@#$%^&*...).\033[0m')
        else:
            break

    novo_aluno = {
        'nome': nome,
        'nome_user': nome_user,
        'idade': idade,
        'email': email,
        'senha': senha,
        'registro': str(datetime.date.today())

    }
    dados = carregar_dados()
    dados.append(novo_aluno)
    salvar_dados(dados)
    print('\033[36mUsuario {}, Cadastrado com sucesso !\033[0m'.format(nome))

def carregar_dados():
    if os.path.exists(arquivo):
        with open(arquivo,'r') as f:
            return json.load(f)
    return []

def salvar_dados(lista_alunos):
    with open(arquivo, 'w') as f:
        json.dump(lista_alunos, f, indent=4)

