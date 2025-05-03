from time import sleep

def seguranca_menu():
    sleep(1.5)
    print('')
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m SEGURANÇA \033[0m' '\033[35m ==========\033[0m')
        print('')
        print('\033[35m1\033[0m. \033[36mPOLITICA DE PRIVACIDADE\033[0m')
        print('\033[35m2.\033[0m \033[36mTermos da LGPD\033[0m')
        print('\033[35m0.\033[0m \033[36mVoltar\033[0m')

        escolha_3 = input('\033[36mEscolha uma opção entre\033[0m \033[35m0-2: \033[0m')
        if escolha_3 == '0':
            break
        elif escolha_3 == '1':
            politica_privacidade()
        elif escolha_3 == '2':
            lgpd_termos()
        else:
            print('\033[31mOpção inválida!\033[0m')

def lgpd_termos():
    while True:
        sleep(1.5)
        print('\033[35m ==================\033[0m' ' \033[1;36m LGPD \033[0m' '\033[35m ==================\033[0m')
        print('''\033[36m
A Lei Geral de Proteção de Dados (LGPD) (Lei nº 13.709/2018) 
regulamenta o tratamento de dados pessoais no Brasil
\033[0m''')
        print('')
        sleep(1.5)
        print('\033[35m1.\033[0m \033[36mO QUE É LGPD? \033[0m')
        print('''\033[36m
A LGPD (Lei Geral de Proteção de Dados) estabelece regras sobre a coleta,
armazenamento, tratamento e compartilhamento de dados pessoais, 
garantindo mais segurança e transparência aos usuários.\033[0m''')
        print('')
        sleep(1.5)
        print('\033[35m2.\033[0m \033[36mPRINCIPIOS DA LGPD \033[0m')
        print('''\033[36m
A lei se baseia em princípios fundamentais, como:
Finalidade: Os dados são coletados para um propósito específico e legítimo.
Necessidade: Apenas os dados estritamente necessários são coletados.
Transparência: O usuário será informado sobre o uso dos dados.
Segurança: Medidas serão adotadas para proteger os dados contra acessos não autorizados.
Consentimento: O usuário deve autorizar o uso de seus dados de forma clara e livre.\033[0m''')
        print('')
        sleep(1.5)
        print('\033[35m3.\033[0m \033[36mDIREITOS DO USUARIO\033[0m')
        print('''\033[36m
Saber quais dados estão sendo coletados.
Solicitar a correção de informações incorretas.
Pedir a exclusão dos seus dados.
Revogar o consentimento para o uso dos dados.\033[0m''')
        print('')
        sleep(1.5)
        print('\033[35m4.\033[0m \033[36mCOMO PROTEGEMOS SEUS DADOS\033[0m')
        print('''\033[36m
Utilizamos medidas de segurança para proteger seus dados contra acessos indevidos.
Seus dados são usados apenas para os fins necessários e permitidos por você.
Não compartilhamos seus dados com terceiros sem sua autorização.\033[0m''')
        print('')
        escolha_5 = input('\033[36mDigite 0 para voltar: \033[0m')
        if escolha_5 == '0':
            break
        else:
            print('\033[36mopção inválida, digite 0 para voltar:\033[0m')

def politica_privacidade():
    while True:
        sleep(1.5)
        print(
            '\033[35m ==================\033[0m' ' \033[1;36m POLITICA DE PRIVACIDADE \033[0m' '\033[35m ==================\033[0m')
        print('''
        \033[36m
Esta politica de privacidade explica como a ClickEdu 
coleta, usa, armazena, e protege os dados pessoais de 
seus usuários, em conformidade com a lei geral de 
proteção de dados pessoais (lei nº13.709/2018-LGPD 
o marco civil da internet (lei nº13.965/2014) 
e outras normas aplicáveis.\033[0m
        ''')
        sleep(1.5)
        print('\033[35m2.\033[0m \033[36mDADOS COLETADOS\033[0m')
        print('''\033[36m
2.1. Dados fornecidos pelo usuário:
Nome completo;
Endereço de e-mail;

2.2. Dados coletados automaticamente:
Endereço IP;
Informações sobre o dispositivo;
Histórico de acesso e interação com a plataforma.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m3.\033[0m \033[36mFINALIDADE DO TRATAMENTO DOS DADOS\033[0m')
        print('''\033[36m
Os dados coletados são utilizados para:
Criar e gerenciar contas dos usuários;
Disponibilizar cursos e conteúdo educacional;
Melhorar a experiência do usuário na plataforma;
Cumprir obrigações legais e regulatórias;
Realizar comunicação com o usuário sobre atualizações e serviços.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m4.\033[0m \033[36mCOMPARTILHAMENTO DE DADOS\033[0m')
        print('''\033[36m
Não compartilhamos informações de identificação pessoal publicamente 
ou com terceiros, exceto quando exigido por lei.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m5.\033[0m \033[36mSEGURANÇA DOS DADOS\033[0m')
        print('''\033[36m
A ClickEdu adota medidas técnicas e administrativas para proteger
os dados pessoais contra acessos não autorizados, vazamentos e 
outros incidentes.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m6.\033[0m \033[36mDIREITO DO TITULAR DOS DADOS\033[0m')
        print('''\033[36m
O usuário pode exercer seus direitos previstos na LGPD, incluindo:
Confirmação da existência de tratamento de dados;
Acesso aos dados pessoais;
correção de dados incompletos, inexatos ou desatulizados;
Solicitação de exclusão de dados desnecessários;
revogação do consentimento para uso de dados.

O uso continuado de nossso site será considerado como aceitação
de nossas práticas acerca da privacidade e informações pessoais.
Se você tiver alguma duvida sobre como lidamos com dados do 
usuário e informações pessoais, entre em contato pelo
e-mail: suport@clickedu.com.br\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m7.\033[0m \033[36mRETENÇÃO E EXCLUSÃO DOS DADOS\033[0m')
        print('''\033[36m
Os dados serão armazenados pelo tempo necessário para cumprir as 
finalidades mencionadas, respeitando prazos legais e regulatórios.
Após esse período, os dados serão anonimizados ou excluídos de forma segura.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m8.\033[0m \033[36mALTERAÇÕES NA POLITICA DE PRIVACIDADE\033[0m')
        print('''\033[36m
A ClickEdu pode atualizar esta Política de Privacidade periodicamente. 
Os usuários serão notificados sobre alterações relevantes.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m9.\033[0m \033[36mRESPONSABILIDADE DO USUÁRIO\033[0m')
        print('''\033[36m
O usuário se compromete a fazer uso adequado dos conteúdos e da informação 
que a ClickEdu oferece no site e, com caráter enunciativo, mas não limitativo:
A) Não se envolver em atividades que sejam ilegais ou contrárias à boa-fé e 
à ordem pública; B) Não difundir propaganda ou conteúdo de natureza racista, 
xenofóbica, jogos de azar, qualquer tipo de pornografia, de apologia ao 
terrorismo ou contra os direitos humanos; C) Não causar danos aos sistemas 
físicos (hardwares) e lógicos (softwares) da ClickEdu, de seus fornecedores
ou terceiros, nem introduzir ou disseminar vírus informáticos ou quaisquer 
outros sistemas de hardware ou software que possam causar danos anteriormente 
mencionados.\033[0m''')
        sleep(1.5)
        print('')
        print('\033[35m10.\033[0m \033[36mCONTATO\033[0m')
        print('''\033[36m
Em caso de dúvidas sobre esta Política de Privacidade, 
entre em contato pelo e-mail: suport@clickedu.com.br.\033[0m''')
        print('')
        escolha_4 = input('\033[36mDigite 0 para voltar: \033[0m')
        if escolha_4 == '0':
            break
        else:
            print('\033[36mopção inválida, digite 0 para voltar:\033[0m')