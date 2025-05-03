from time import sleep
from datetime import datetime
import banco
import questionarios
import log
import seguranca
import modulos
arquivo = 'alunos.json'
espace = '\033[1;35m=\033[0m' * 89
titulo = '\033[1;36m CLICKEDU  \033[0m'
print(espace)
print(titulo.center(100, ' '))
print(espace)

def menu():
    print('\033[35m ====\033[0m' ' \033[1;36m MENU DE OPÇÕES \033[0m' '\033[35m ====\033[0m')
    print('')

    if log.usuario_logado:
        print('\033[35m1.\033[0m''\033[36m Cursos \033[0m')
        print('\033[35m2.\033[0m''\033[36m Informações de Segurança \033[0m')
        print('\033[35m3.\033[0m''\033[36m Fazer Logoff \033[0m') 
        print('\033[35m4.\033[0m''\033[36m Minhas Informações \033[0m')
        print('\033[35m0.\033[0m''\033[36m Sair \033[0m')
        escolha = input('\033[36mESCOLHA UMA OPÇÃO DE\033[0m \033[1;35m0-4: \033[m')
    else:
        print('\033[35m1.\033[0m''\033[;36m Fazer Cadastro \033[0m')
        print('\033[35m2.\033[0m ''\033[36mFazer Login \033[0m')
        print('\033[35m3.\033[0m ''\033[36mCursos \033[0m')
        print('\033[35m4.\033[0m ''\033[36mInformações de Segurança \033[0m')
        print('\033[35m0.\033[0m ''\033[36mSair \033[0m')
        escolha = input('\033[36mESCOLHA UMA OPÇÃO DE\033[0m \033[1;35m0-4: \033[m')

    return escolha

def excluir_usuario():
    while True:
        confirmacao = input(f"\033[33mTem certeza que deseja excluir sua conta, {log.usuario_logado['nome']}? (s/n): \033[0m").lower()
        if confirmacao == 's':
            dados = banco.carregar_dados()
            dados = [u for u in dados if u['email'] != log.usuario_logado['email']]
            banco.salvar_dados(dados)
            print("\033[31mSua conta foi excluída com sucesso.\033[0m")
            log.usuario_logado = None
            return
        elif confirmacao == 'n':
            print("\033[32mA exclusão da conta foi cancelada.\033[0m")
            return 
        else:
            print("\033[32mOpção inválida, tente novamente.\033[0m")
            True

def registrar_frequencia(modulo):
    if log.usuario_logado:
        if "frequencia" not in log.usuario_logado:
            log.usuario_logado["frequencia"] = {"Pensamento": 0, "Segurança": 0, "Python": 0}
        log.usuario_logado["frequencia"][modulo] += 1

        # Salvar no arquivo
        dados = banco.carregar_dados()
        for u in dados:
            if u["email"] == log.usuario_logado["email"]:
                u["frequencia"] = log.usuario_logado["frequencia"]
        banco.salvar_dados(dados)

def ver_notas():
    if not log.usuario_logado:
        print("\033[31mVocê precisa estar logado para ver as notas.\033[0m")
        return

    while True:
        print("\033[34m==== HISTÓRICO DE NOTAS ====\033[0m")
        notas = log.usuario_logado.get("notas", [])
        if not notas:
            print("\033[33mNenhuma nota registrada ainda.\033[0m")
        else:
            for nota in notas:
                print(f"\033[36mMódulo:\033[0m {nota['modulo']} - \033[36mNota:\033[0m {nota['nota']}/{nota['total']}")

        print("\033[35m1.\033[0m \033[36mVer média final de cada módulo\033[0m")
        print("\033[35m0.\033[0m \033[36mVoltar\033[0m")
        escolha = input("\033[36mEscolha uma opção: \033[0m")
        
        if escolha == '0':
            break
        elif escolha == '1':
            medias = {"Pensamento": [], "Segurança": [], "Python": []}
            for nota in notas:
                if "Pensamento" in nota["modulo"]:
                    medias["Pensamento"].append(nota["nota"] / nota["total"])
                elif "Segurança" in nota["modulo"]:
                    medias["Segurança"].append(nota["nota"] / nota["total"])
                elif "Python" in nota["modulo"]:
                    medias["Python"].append(nota["nota"] / nota["total"])
            
            print("\033[34m==== MÉDIAS FINAIS POR MÓDULO ====\033[0m")
            for modulo, lista in medias.items():
                if lista:
                    media = sum(lista) / len(lista)
                    print(f"\033[36m{modulo}:\033[0m média de {media*10:.1f}/10")
                else:
                    print(f"\033[33m{modulo}: Sem notas registradas.\033[0m")
                sleep(3.0)
        else:
            print("\033[33mOpção inválida.\033[0m")

def minhas_informacoes():
    import datetime
    if not log.usuario_logado:
        print("\033[31mVocê precisa estar logado para acessar essa opção.\033[0m")
        return

    print("\n\033[34m==== MINHAS INFORMAÇÕES ====\033[0m")
    print(f"\033[36mNome:\033[0m {log.usuario_logado['nome']}")
    print(f"\033[36mEmail:\033[0m {log.usuario_logado['email']}")
    print(f"\033[36mIdade:\033[0m {log.usuario_logado['idade']}")

    # Curso mais acessado
    frequencia = log.usuario_logado.get("frequencia", {"Pensamento": 0, "Segurança": 0, "Python": 0})
    curso_mais = max(frequencia, key=frequencia.get)
    print(f"\033[36mCurso mais acessado:\033[0m {curso_mais} ({frequencia[curso_mais]} vez(es))")
    print("\033[36mAcessos por curso:\033[0m")
    for curso, acessos in frequencia.items():
        print(f" - {curso}: {acessos} vez(es)")

    # Tempo na plataforma
    if 'registro' not in log.usuario_logado:
        log.usuario_logado['registro'] = str(datetime.date.today())
        dados = banco.carregar_dados()
        for u in dados:
            if u['email'] == log.usuario_logado['email']:
                u['registro'] = log.usuario_logado['registro']
        banco.salvar_dados(dados)

    data_registro = datetime.datetime.strptime(log.usuario_logado['registro'], "%Y-%m-%d").date()
    dias_na_plataforma = (datetime.date.today() - data_registro).days
    print(f"\033[36mTempo na plataforma:\033[0m {dias_na_plataforma} dia(s)")
     #Conlusão de Cursos

    conclusao = log.usuario_logado.get("conclusao", {})
    print(f"\033[36mStatus dos cursos:\033[0m")
    for curso in ["Pensamento", "Segurança", "Python"]:
        status = conclusao.get(curso, "em andamento")
        print(f" - {curso}: {status}")
    
    print("\n\033[35m1.\033[0m \033[36mExcluir minha conta\033[0m")
    print('\033[35m6.\033[0m \033[36mRecuperação de cursos\033[0m')
    print("\033[35m0.\033[0m \033[36mVoltar\033[0m")
    escolha = input("\033[36mEscolha uma opção: \033[0m")
    while True:
        if escolha == '1':
            excluir_usuario()
            break
        elif escolha  == '6':
            recuperacao()
            break
        elif escolha == '0':
            break
        else:
            print('\033[31mOpção inválida!\033[0m')

def recuperacao():
    if not log.usuario_logado:
        print("\033[31mVocê precisa estar logado para fazer a recuperação.\033[0m")
        return

    if "conclusao" not in log.usuario_logado:
        print("\033[33mVocê não finalizou nenhum curso.\033[0m")
        return

    reprovados = [curso for curso, status in log.usuario_logado["conclusao"].items() if status == "reprovado"]

    if not reprovados:
        print("\033[32mParabéns! Você não tem cursos reprovados.\033[0m")
        return

    print("\033[34m==== RECUPERAÇÃO ====\033[0m")
    for i, curso in enumerate(reprovados, 1):
        print(f"\033[35m{i}.\033[0m \033[36m{curso}\033[0m")
    print("\033[35m0.\033[0m \033[36mCancelar\033[0m")

    escolha = input("\033[36mDigite o número do curso que deseja refazer: \033[0m")
    if not escolha.isdigit() or int(escolha) < 0 or int(escolha) > len(reprovados):
        print("\033[31mOpção inválida.\033[0m")
        return
    if escolha == "0":
        return

    curso = reprovados[int(escolha) - 1]

    # Executar apenas os questionários, sem entrar no menu dos cursos
    if curso == "Pensamento":
        aplicar_questionario(questionarios.quest_pens_12, "Pensamento 1")
        aplicar_questionario(questionarios.quest_pens_34, "Pensamento 2")
    elif curso == "Segurança":
        aplicar_questionario(questionarios.quest_seg12, "Segurança 1")
        aplicar_questionario(questionarios.quest_seg_34, "Segurança 2")
    elif curso == "Python":
        aplicar_questionario(questionarios.quest_python_1234, "Python 1")
        aplicar_questionario(questionarios.quest_python_5678, "Python 2")

    print("\033[32mRecuperação finalizada. Verifique suas informações para ver se foi aprovado.\033[0m")

def aplicar_questionario(perguntas, nome_modulo="Questionário"):
    respostas_erradas = []
    pontuacao = 0

    for i, pergunta in enumerate(perguntas, start=1):
        print(f"\n\033[35mQuestão {i}:\033[0m \033[36m{pergunta['pergunta']}\033[0m")

        for letra, opcao in pergunta["opcoes"].items():
            print(f"{letra} {opcao}")

        resposta = input("\n\033[36mDigite a resposta entre a, b, c ou d: \033[0m").lower()

        if resposta == pergunta["resposta_correta"]:
            print("\033[32mCorreto!\033[0m")
            pontuacao += 1
        else:
            print("\033[31mIncorreto!\033[0m")
            respostas_erradas.append({
                "numero": i,
                "pergunta": pergunta["pergunta"],
                "resposta_correta": pergunta["resposta_correta"],
                "sua_resposta": resposta
            })

        sleep(1.2)

    # Resultado final
    print("\n\033[34m==== RESULTADO FINAL ====\033[0m")
    print(f"\033[1;36mSua nota: {pontuacao}/{len(perguntas)}\033[0m")

    if respostas_erradas:
        print("\n\033[33mVocê errou as seguintes questões:\033[0m")
        for erro in respostas_erradas:
            print(f"\033[31mQuestão {erro['numero']}:\033[0m {erro['pergunta']}")
            print(f" - \033[36mSua resposta:\033[0m {erro['sua_resposta']}")
            print(f" - \033[32mResposta correta:\033[0m {erro['resposta_correta']}\n")
    else:
        print("\033[32mParabéns! Você acertou tudo!\033[0m")

    # Salvar nota no perfil do usuário
    if log.usuario_logado:
        if "notas" not in log.usuario_logado:
            log.usuario_logado["notas"] = []
        log.usuario_logado["notas"].append({
            "modulo": nome_modulo,
            "nota": pontuacao,
            "total": len(perguntas)
        })
        dados = banco.carregar_dados()
        for u in dados:
            if u['email'] == log.usuario_logado['email']:
                u['notas'] = log.usuario_logado['notas']
        banco.salvar_dados(dados)
        # Verificar conclusão do curso
    if log.usuario_logado:
        modulos = [n for n in log.usuario_logado["notas"] if nome_modulo.split()[0] in n["modulo"]]
        if len(modulos) >= 2:
            media = sum(n["nota"] / n["total"] * 10 for n in modulos) / len(modulos)
            curso = nome_modulo.split()[0]
            if media >= 6:
                status = "aprovado"
            else:
                status = "reprovado"

            if "conclusao" not in log.usuario_logado:
                log.usuario_logado["conclusao"] = {}
            log.usuario_logado["conclusao"][curso] = status

            dados = banco.carregar_dados()
            for u in dados:
                if u["email"] == log.usuario_logado["email"]:
                    u["conclusao"] = log.usuario_logado["conclusao"]
            banco.salvar_dados(dados)

def cursos_menu():
    if not log.usuario_logado:
        print('\033[31mVocê precisa estar logado para acessar os cursos!\033[0m')
        return
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MENU DE CURSOS \033[0m' '\033[35m ==========\033[0m')
        print('')
        print('\033[35m1.\033[0m \033[36mPensamento Lógico computacional\033[0m')
        print('\033[35m2.\033[0m \033[36mSegurança Digital\033[0m')
        print('\033[35m3.\033[0m \033[36mprogramação em python\033[0m')
        print('\033[35m4.\033[0m \033[36mVer Notas dos Questionários\033[0m')
        print('\033[35m0.\033[0m \033[36mVoltar\033[0m')
        escolha_2 = input('\033[36mEscolha uma opção de\033[0m \033[35m0-4: \033[0m')
        if escolha_2 == '1':
            pensamento()
        elif escolha_2 == '2':
            seguranca_digital()
        elif escolha_2 == '3':
            python()
        elif escolha_2 == '4':
            ver_notas()
        elif escolha_2 == '0':
            break

def pensamento():
    registrar_frequencia("Pensamento")
    while True:
        sleep(2)
        print('\033[35m ==========\033[0m' ' \033[1;36m PENSAMENTO LOGICO COMPUTACIONAL \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMODULO 1\033[0m')
        print('\033[35m2.\033[0m \033[36mMODULO 2\033[0m')
        print('\033[35m3.\033[0m \033[36mMODULO 3\033[0m')
        print('\033[35m4.\033[0m \033[36mMODULO 4\033[0m')
        print('\033[35m5.\033[0m \033[36mQUESTIONARIOS\033[0m')
        print('\033[35m0.\033[0m \033[36mVoltar\033[0m')
        escolha_pensamento = input('\033[36mEscolha uma opção de\033[0m \033[35m0-5: \033[0m')
        if escolha_pensamento == '1':
            modulos.modpens01()
        elif escolha_pensamento == '2':
            modulos.modpens02()
        elif escolha_pensamento == '3':
            modulos.modpens03()
        elif escolha_pensamento == '4':
            modulos.modpens04()
        elif escolha_pensamento == '5':
            quest_pens_modulos()
        elif escolha_pensamento == '0':
            break
        else:
            pensamento()

def quest_pens_modulos():
    from time import sleep
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m QUESTIONÁRIOS - PENSAMENTO COMPUTACIONAL \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMódulo 1 e 2\033[0m')
        print('\033[35m2.\033[0m \033[36mMódulo 3 e 4\033[0m')
        print('\033[35m3.\033[0m \033[36mVoltar\033[0m')
        escolha_quest_pens = input('\033[36mEscolha uma opção entre\033[0m \033[35m1-3: \033[0m')

        if escolha_quest_pens == '1':
            print('\033[35m ==========\033[0m' ' \033[1;36mPENSAMENTO COMPUTACIONAL\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(questionarios.quest_pens_12, "Pensamento Computacional - Módulo 1 e 2")
        elif escolha_quest_pens == '2':
            print('\033[35m ==========\033[0m' ' \033[1;36mESTRUTURA E REPRESENTAÇÃO DE ALGORITMOS\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(questionarios.quest_pens_34, "Pensamento Computacional - Módulo 3 e 4")
        elif escolha_quest_pens == '3':
            break
        else:
            print('\033[31mOpção inválida!\033[0m')
        sleep(1.5)

def quest_seg_modulos():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m QUESTIONÁRIOS - SEGURANÇA DIGITAL \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMódulo 1 e 2\033[0m')
        print('\033[35m2.\033[0m \033[36mMódulo 3 e 4\033[0m')
        print('\033[35m3.\033[0m \033[36mVoltar\033[0m')
        escolha_quest_seg = input('\033[36mEscolha uma opção entre\033[0m \033[35m1-3: \033[0m')

        if escolha_quest_seg == '1':
            print('\033[35m ==========\033[0m' ' \033[1;36mSEGURANÇA DIGITAL\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(questionarios.quest_seg12, "Segurança Digital - Módulo 1 e 2")
        elif escolha_quest_seg == '2':
            print('\033[35m ==========\033[0m' ' \033[1;36mAMEAÇAS E BOAS PRÁTICAS EM SEGURANÇA DIGITAL\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(questionarios.quest_seg_34)
        elif escolha_quest_seg == '3':
            break
        else:
            print('\033[31mOpção inválida!\033[0m')
        sleep(1.5)

def quest_python_modulos():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m QUESTIONÁRIOS - PROGRAMAÇÃO EM PYHON \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMódulo 1, 2, 4 E 4\033[0m')
        print('\033[35m2.\033[0m \033[36mMódulo 5, 6, 7 e 8\033[0m')
        print('\033[35m3.\033[0m \033[36mVoltar\033[0m')
        escolha_quest_python = input('\033[36mEscolha uma opção entre\033[0m \033[35m1-3: \033[0m')

        if escolha_quest_python == '1':
            print('\033[35m ==========\033[0m' ' \033[1;36mSEGURANÇA DIGITAL\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(questionarios.quest_python_1234, "Python - Módulo 1 ao 4")
        elif escolha_quest_python == '2':
            print('\033[35m ==========\033[0m' ' \033[1;36mAMEAÇAS E BOAS PRÁTICAS EM SEGURANÇA DIGITAL\033[0m' '\033[35m ==========\033[0m')
            aplicar_questionario(questionarios.quest_python_5678, "Python - Módulo 5 ao 8")
        elif escolha_quest_python == '3':
            break
        else:
            print('\033[31mOpção inválida!\033[0m')
        sleep(1.5)

def seguranca_digital():
    registrar_frequencia("Segurança")
    while True:
        sleep(2)
        print('\033[35m ==========\033[0m' ' \033[1;36m SEGURANÇA DIGITAL \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMODULO 1\033[0m')
        print('\033[35m2.\033[0m \033[36mMODULO 2\033[0m')
        print('\033[35m3.\033[0m \033[36mMODULO 3\033[0m')
        print('\033[35m4.\033[0m \033[36mMODULO 4\033[0m')
        print('\033[35m5.\033[0m \033[36mQUESTIONARIOS\033[0m')
        print('\033[35m0.\033[0m \033[36mVoltar\033[0m')
        escolha_seguranca = input('\033[36mEscolha uma opção de\033[0m \033[35m0-5: \033[0m')
        if escolha_seguranca == '1':
            modulos.modseg01()
        elif escolha_seguranca == '2':
            modulos.modseg02()
        elif escolha_seguranca == '3':
            modulos.modseg03()
        elif escolha_seguranca == '4':
            modulos.modseg04()
        elif escolha_seguranca == '5':
            quest_seg_modulos()
        elif escolha_seguranca == '0':
            break
        else:
            seguranca_digital()


    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 04 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mBOAS PRATICAS PARA GARANTIR A SEGURANÇA DIGITAL\033[0m')
        print('''\033[36m
Agora que você já sabe o que é segurança digital, por que ela é importante e quais ameaças estão por aí,
 é hora de descobrir como se proteger na prática. Pequenas atitudes no dia a dia fazem uma grande diferença 
 para manter seus dados seguros.
Estas boas práticas valem tanto para uso pessoal quanto profissional, e devem fazer parte da sua rotina digital.

1. Use senhas fortes e únicas
Senhas são a primeira linha de defesa contra invasores. Uma boa senha deve:
Ter mais de 8 caracteres.
Incluir letras maiúsculas e minúsculas, números e símbolos.
Ser diferente para cada conta ou serviço.
Evite senhas óbvias como "123456", "senha" ou datas de aniversário.
Dica: Use um gerenciador de senhas para armazenar com segurança e lembrar todas as suas senhas diferentes.

2. Ative a autenticação multifator (MFA ou 2FA)
Essa medida adiciona uma camada extra de segurança além da senha.
Funciona assim: mesmo que alguém descubra sua senha, ainda será preciso uma segunda verificação, como:
Um código enviado por SMS ou e-mail,
Um aplicativo autenticador (como o Google Authenticator),
Biometria (impressão digital, reconhecimento facial).

3. Mantenha seus sistemas e programas atualizados
Atualizações não servem só para adicionar novos recursos — elas corrigem falhas de segurança que podem ser 
exploradas por hackers.
Atualize sempre seu sistema operacional, navegador, antivírus e aplicativos.
Ative as atualizações automáticas sempre que possível.

4. Cuidado com e-mails e mensagens suspeitas
Muitos ataques começam com phishing: mensagens falsas que tentam enganar você.
Fique atento a:
Links encurtados ou estranhos,
Erros de português,
Pressa ou ameaças para você agir rápido,
Solicitações de informações pessoais ou bancárias.
Nunca clique em links ou baixe arquivos de remetentes que você não conhece ou não confia.

5. Evite usar redes Wi-Fi públicas para tarefas sensíveis
Redes públicas (de cafés, aeroportos, shoppings) são práticas, mas podem ser inseguras. Evite acessar 
contas bancárias, e-mails ou redes sociais importantes em Wi-Fi público. Use VPNs (redes privadas virtuais) 
para proteger sua conexão quando for inevitável usar esse tipo de rede. 

6. Desconfie antes de compartilhar dados
Antes de preencher formulários online, dar seu CPF ou clicar em "aceito", pergunte-se:
"Esse site é confiável?"
"Essa informação é realmente necessária aqui?"
"Estou ciente do que estão fazendo com meus dados?"
Sempre prefira sites com “https://” e cadeado de segurança na barra de endereço.

7. Use antivírus e firewall
Essas ferramentas ajudam a detectar e bloquear ameaças automaticamente.
Um antivírus confiável pode impedir que malwares se instalem no seu dispositivo.
O firewall ajuda a controlar o tráfego de dados e proteger sua rede.

8. Faça backups regulares dos seus dados
Guardar cópias dos seus arquivos importantes é essencial para evitar perdas causadas por falhas, 
vírus ou ataques.
Use HDs externos, pen drives ou serviços de armazenamento em nuvem.
Faça backups com regularidade e mantenha pelo menos uma cópia offline.

9. Eduque-se e fique sempre atento
A melhor ferramenta de segurança é o conhecimento. Esteja sempre atualizado sobre novas ameaças, 
golpes e práticas de proteção.
Siga fontes confiáveis de tecnologia.
Compartilhe esse conhecimento com amigos, familiares e colegas de trabalho.

Para refletir:
"A segurança digital não é feita só de tecnologia. Ela começa com o seu comportamento."
Cada escolha que você faz online pode aproximar ou afastar um risco. Criar uma rotina de cuidados é o melhor 
caminho para navegar na internet com mais liberdade e menos preocupação.
\033[0m''')
        escolha_mod04 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_mod04 == '0':
            break
        else:
            escolha_mod04 = input('\033[36mEscolha inválida \033[m')

def python():
    registrar_frequencia("Python")
    while True:
        sleep(2)
        print('\033[35m ==========\033[0m' ' \033[1;36m PROGRAMAÇÃO EM PYTHON \033[0m' '\033[35m ==========\033[0m')
        print('\033[35m1.\033[0m \033[36mMODULO 1\033[0m')
        print('\033[35m2.\033[0m \033[36mMODULO 2\033[0m')
        print('\033[35m3.\033[0m \033[36mMODULO 3\033[0m')
        print('\033[35m4.\033[0m \033[36mMODULO 4\033[0m')
        print('\033[35m5.\033[0m \033[36mMODULO 5\033[0m')
        print('\033[35m6.\033[0m \033[36mMODULO 6\033[0m')
        print('\033[35m7.\033[0m \033[36mMODULO 7\033[0m')
        print('\033[35m8.\033[0m \033[36mMODULO 8\033[0m')
        print('\033[35m9.\033[0m \033[36mQUESTIONARIOS\033[0m')
        print('\033[35m0.\033[0m \033[36mVoltar\033[0m')

        escolha_python = input('\033[36mEscolha uma opção de\033[0m \033[35m1-9: \033[0m')
        if escolha_python == '1':
            modulos.modpython01()
        elif escolha_python == '2':
            modulos.modpython02()
        elif escolha_python == '3':
            modulos.modpython03()
        elif escolha_python == '4':
            modulos.modpython04()
        elif escolha_python == '5':
            modulos.modpython05()
        elif escolha_python == '6':
            modulos.modpython06()
        elif escolha_python == '7':
            modulos.modpython07()
        elif escolha_python == '8':
            modulos.modpython08()
        elif escolha_python == '9':
            modulos.quest_python_modulos()
        elif escolha_python == '0':
            break
        else:
            python()

def admin():
    dados = banco.carregar_dados()
    print("\n\033[34m==== ÁREA ADMINISTRATIVA ====\033[0m")

    # Contador de acessos por curso
    total_frequencias = {"Pensamento": 0, "Segurança": 0, "Python": 0}
    todas_idades = []
    notas_por_curso = {"Pensamento": [], "Segurança": [], "Python": []}
    conclusoes = {"Pensamento": 0, "Segurança": 0, "Python": 0}
    total_usuarios = len(dados)

    for aluno in dados:
        idade = int(aluno.get("idade", 0))
        todas_idades.append(idade)

        # Frequência por curso
        freq = aluno.get("frequencia", {})
        for curso in total_frequencias:
            total_frequencias[curso] += freq.get(curso, 0)

        # Notas
        for nota in aluno.get("notas", []):
            modulo = nota["modulo"]
            if "Pensamento" in modulo:
                notas_por_curso["Pensamento"].append(nota["nota"] / nota["total"] * 10)
            elif "Segurança" in modulo:
                notas_por_curso["Segurança"].append(nota["nota"] / nota["total"] * 10)
            elif "Python" in modulo:
                notas_por_curso["Python"].append(nota["nota"] / nota["total"] * 10)

        # Sistema de conclusão
        if "notas" in aluno:
            for curso in ["Pensamento", "Segurança", "Python"]:
                questoes = [n for n in aluno["notas"] if curso in n["modulo"]]
                if len(questoes) >= 2:
                    media = sum(n["nota"]/n["total"]*10 for n in questoes) / len(questoes)
                    if media >= 6:
                        conclusoes[curso] += 1

    # Mostrar curso mais acessado
    mais_acessado = max(total_frequencias, key=total_frequencias.get)
    print(f"\033[36mCurso mais visitado:\033[0m {mais_acessado} ({total_frequencias[mais_acessado]} acessos)")

    # Idades
    print(f"\033[36mIdades cadastradas:\033[0m {todas_idades}")

    # Notas por curso
    for curso, lista in notas_por_curso.items():
        if lista:
            media = sum(lista) / len(lista)
            print(f"\033[36mMédia de notas em {curso}:\033[0m {media:.2f}")
        else:
            print(f"\033[33mSem notas registradas para {curso}\033[0m")

    # Espera comando do admin
    comando = input("\n\033[36mDigite 'resumo' para ver estatísticas gerais ou 'sair' para voltar:\033[0m ").strip().lower()

    if comando == "resumo":
        from statistics import mean, mode

        try:
            media_idade = mean(todas_idades)
            moda_idade = mode(todas_idades)
        except:
            media_idade = moda_idade = "N/A"

        print("\n\033[34m==== ESTATÍSTICAS GERAIS ====\033[0m")
        print(f"\033[36mMédia de idades:\033[0m {media_idade}")
        print(f"\033[36mModa de idades:\033[0m {moda_idade}")

        for curso, lista in notas_por_curso.items():
            if lista:
                media = sum(lista) / len(lista)
                taxa = (conclusoes[curso] / total_usuarios) * 100 if total_usuarios > 0 else 0
                print(f"\033[36m{curso}:\033[0m média de {media:.2f} | taxa de conclusão: {taxa:.1f}%")
            else:
                print(f"\033[33m{curso}: Sem dados.\033[0m")

if __name__ == "__main__":
    while True:
        escolha = menu()
        if log.usuario_logado:
            if escolha == '1':
                cursos_menu()
            elif escolha == '2':
                seguranca.seguranca_menu()
            elif escolha == '3':
                log.logout()
            elif escolha == '4':
                minhas_informacoes()
            elif escolha == '0':
                print("\033[31mSaindo do sistema...\033[0m")
                break
            else:
                print("\033[31mOpção inválida.\033[0m")
        else:
            if escolha == '1':
                banco.cadastro()
            elif escolha == '2':
                log.login()
            elif escolha == '3':
                cursos_menu()
            elif escolha == '4':
                seguranca.seguranca_menu()
            elif escolha == '0':
                print("\033[31mSaindo do sistema...\033[0m")
                break
            else:
                print("\033[31mOpção inválida.\033[0m")

        sleep(1.5)
