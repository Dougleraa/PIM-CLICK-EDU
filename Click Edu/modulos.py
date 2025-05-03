from time import sleep

def modpens01():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 01 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mFUNDAMENTOS DO PENSAMENTO COMPUTACIONAL\033[0m')
        print('''\033[36m
Objetivo Geral: Apresentar o que é o pensamento computacional, desenvolver suas habilidades-chave e 
mostrar como ele pode ser usado para resolver problemas de forma lógica, organizada e eficiente — 
dentro e fora da programação.

1. O que é Pensar Computacionalmente?
Definição: Pensar computacionalmente é aplicar princípios da ciência da computação para resolver problemas
de maneira sistemática. Isso não significa necessariamente programar, mas estruturar o pensamento de forma
lógica, eficiente e estratégica.

Exemplo cotidiano:
Organizar sua rotina semanal pode ser feito de forma computacional:
Que tarefas são fixas?
Quais são prioridades?
O que pode ser feito em paralelo?

2. As Quatro Habilidades-Chave do Pensamento Computacional
a) Abstração
Focar no que é essencial e ignorar o que é desnecessário.
Exemplo: Ao pedir comida por um aplicativo, você abstrai todo o processo da cozinha, focando apenas no 
cardápio e no pedido.
b) Decomposição
Dividir um problema grande em partes menores e mais simples.
Exemplo: Planejar uma viagem envolve separar passagens, hospedagem, passeios, orçamento etc.
c) Reconhecimento de Padrões
Identificar semelhanças ou repetições para prever comportamentos ou otimizar tarefas.
Exemplo: Se toda segunda-feira você gasta mais tempo no trânsito, pode antecipar essa tendência.
d) Algoritmos
Sequência de passos claros para resolver um problema.
Exemplo: Receita de bolo — siga um passo a passo para alcançar um resultado.

3. Aplicações Fora da Programação
Essas habilidades são úteis em diversas áreas:
Educação: organizar conteúdo e métodos de ensino.
Negócios: otimizar processos, tomada de decisão baseada em dados
Saúde: protocolos de atendimento ou triagem.
Vida pessoal: organização financeira, planejamento de estudos, hábitos saudáveis.
\033[0m''')
        escolha_pen01 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pen01 == '0':
            break
        else:
            escolha_pen01 = input('\033[36mEscolha inválida \033[m')

def modpens02():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 02 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mRACIOCÍNIO LÓGICO E PROPOSIÇÕES\033[0m')
        print('''\033[36m
Objetivo Geral: Desenvolver a capacidade de pensar logicamente, entender o que são proposições e como 
elas se combinam por meio da lógica binária (Verdadeiro/Falso), preparando a base para decisões algorítmicas
 e codificação futura.

1. O que são Proposições?
Definição: Uma proposição é uma afirmação que pode ser verdadeira (V) ou falsa (F), mas nunca as duas ao 
mesmo tempo.
Exemplos de proposições:
"O céu é azul." Certo (Pode ser avaliada como verdadeira.)
"2 + 2 = 5." Errada  (Pode ser avaliada como falsa.)
Exemplos de frases que não são proposições:
"Feche a janela." (É um comando, não pode ser julgada como V ou F.)
"Será que vai chover?" (É uma pergunta, sem valor lógico.)

2. Lógica Binária: Verdadeiro (V) ou Falso (F)
A base do raciocínio computacional está na lógica binária, onde só existem dois valores possíveis:
(Verdadeiro) ou 0 (Falso).
Importância: É o mesmo princípio usado em circuitos eletrônicos e programação — tudo se resume a decisões 
lógicas com base nesses dois valores.

3. Lógica Verbal e Numérica
a) Exercícios de Lógica Verbal:
Problemas de dedução.
Ex: "Se todo gato mia, e se Bichano mia, então Bichano é gato?"
b) Exercícios de Lógica Numérica:
Sequências lógicas: 2, 4, 6, _, _
Quebra-cabeças: “Maria tem o dobro da idade de João, que tem 10. Quantos anos Maria tem?”
\033[0m''')
        escolha_pen02 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pen02 == '0':
            break
        else:
            escolha_pen02 = input('\033[36mEscolha inválida \033[m')

def modpens03():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 03 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mESTRUTURA DE PROBLEMAS E ALGORISTMOS\033[0m')
        print('''\033[36m
Objetivo Geral: Ensinar o aluno a identificar, entender e organizar problemas de forma lógica, estruturando
soluções através de algoritmos simples. Isso estabelece as bases para qualquer atividade de programação ou 
automação de tarefas.

1. O que é um Algoritmo?
Definição: Um algoritmo é uma sequência finita de passos organizados e lógicos para resolver um problema ou 
realizar uma tarefa.

Exemplos simples de algoritmos do dia a dia:
Receita de bolo
Rotina matinal (acordar, escovar os dentes, tomar café...)
Instruções para montar um móvel
Palavra-chave: Clareza. Um bom algoritmo deve ser claro, objetivo e executável.

2. Componentes Básicos de um Algoritmo
Entrada
Dados ou informações necessárias para começar.
Exemplo: Para fazer um suco, você precisa de frutas, água e açúcar.

Processamento
O que será feito com os dados.
Exemplo: Bater os ingredientes no liquidificador.

Saída
O resultado final.
Exemplo: O suco pronto.

3. Representando Problemas como Sequência Lógica
Passo a Passo para Estruturar um Problema:
Compreender o problema
O que está sendo pedido?
Quais dados são fornecidos?
Identificar as partes (entrada, processamento e saída)
Criar a sequência de etapas
Organizar cada ação necessária para alcançar o objetivo.
Testar mentalmente ou com exemplos
Isso ajuda a ver se o algoritmo resolve de fato o problema.

Exemplos Práticos
Exemplo 1: Fazer um sanduíche
Entrada: pão, queijo, presunto
Processamento: colocar o queijo e o presunto entre os pães
Saída: sanduíche pronto

Exemplo 2: Verificar se um número é par
Entrada: número
Processamento: dividir o número por 2 e verificar o resto
Saída: se o resto for zero, é par; senão, é ímpar
\033[0m''')
        escolha_pen03 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pen03 == '0':
            break
        else:
            escolha_pen03 = input('\033[36mEscolha inválida \033[m')

def modpens04():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 04 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mREPRESENTAÇÃO DE ALGORISTMOS\033[0m')
        print('''\033[36m
Objetivo Geral: Ensinar o aluno a traduzir um algoritmo mental ou escrito em diferentes formas de 
representação, como narrativa, fluxograma e pseudocódigo, preparando para transições futuras à programação 
real.

1. Por que Representar um Algoritmo?
Representar um algoritmo de forma estruturada permite:
Melhor visualização do processo
Facilidade na identificação de erros
Clareza ao comunicar soluções com outras pessoas
Base para codificação em linguagens de programação

2. Tipos de Representações: 
a) Narrativa (Descrição Informal)
Definição: Representação do algoritmo como uma sequência de instruções em linguagem natural, de forma 
simples e direta.
Exemplo:
Algoritmo para preparar um café:
1. Ferva a água
2. Coloque o pó de café no filtro
3. Despeje a água sobre o pó
4. Deixe o café coar
5. Sirva na xícara

Vantagem: Fácil de escrever e entender
Limitação: Pode ser ambíguo ou impreciso

b) Fluxograma (Representação Gráfica)
Definição: Representa o algoritmo com símbolos gráficos padronizados, facilitando a visualização do 
fluxo de decisões e processos.

Principais símbolos:
Símbolo	           Nome	               Função
Elipse	        Início/Fim	      Indica onde começa/termina
Retângulo	     Processo	      Ações ou cálculos
Losango	         Decisão	      Condições (sim/não)
Seta	         Setas	          Indicam o fluxo do algoritmo

 Vantagem: Visual, ótimo para iniciantes
Limitação: Exige familiaridade com os símbolos

c) Pseudocódigo (Linguagem Estruturada)
Definição: Forma textual parecida com um código de programação, mas escrita em linguagem natural 
estruturada, com comandos claros e organizados.

Exemplo:
Início
  Ler número
  Se número % 2 = 0 então
    Escrever "Número é par"
  Senão
    Escrever "Número é ímpar"
Fim

Vantagem: Aproxima o aluno da lógica de programação
Limitação: Requer organização e padronização

Comparando as Representações:
Representação	       Linguagem	     Complexidade	     Quando usar?
Narrativa	           Natural	          Baixa	             Início do aprendizado
Fluxograma	           Visual	          Média	             Visualização de lógica e decisões
Pseudocódigo	       Estruturada	      Média/Alta	     Transição para programação
\033[0m''')
        escolha_pen04 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pen04 == '0':
            break
        else:
            escolha_pen04 = input('\033[36mEscolha inválida \033[m')

def modseg01():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 01 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mO QUE É SEGURANCA DIGITAL ?\033[0m')
        print('''\033[36m
Segurança digital é o conjunto de práticas, ferramentas e tecnologias usadas para proteger informações
e sistemas digitais contra acessos não autorizados, ataques, danos ou roubo. Ela tem três objetivos 
principais:
1. Confidencialidade: garantir que só pessoas autorizadas tenham acesso às informações.
2. Integridade: assegurar que os dados não sejam alterados de forma indevida ou corrompidos.
3. Disponibilidade: manter os sistemas e dados acessíveis sempre que forem necessários.

Esses princípios são conhecidos como CIA (Confidentiality, Integrity, Availability) e formam a base da 
segurança digital.
Ameaças mais comuns à segurança digital:
Hackers = pessoas que exploram vulnerabilidades nos sistemas para obter acesso não autorizado.
Nem todo hacker é mal-intencionado (alguns ajudam a encontrar falhas), mas aqui estamos falando dos que 
causam danos, roubos ou invasões.
Malware = É a abreviação de “software malicioso”. Pode incluir:
Vírus – programas que se espalham e prejudicam os dispositivos.
Spyware – espionam suas atividades para roubar dados.
Ransomware – sequestram seus dados e exigem pagamento para liberar.
Phishing = Tentativas de enganar você para obter informações confidenciais, como senhas ou dados bancários.
Vêm disfarçados de e-mails ou mensagens legítimas, mas são fraudes digitais.

Outros exemplos de riscos:
Ataques de negação de serviço (DDoS): sobrecarregam um sistema para tirá-lo do ar.
Roubo de identidade: uso indevido de informações pessoais para cometer fraudes.
Engenharia social: quando alguém manipula você para revelar informações, sem usar 
tecnologia diretamente.

Para refletir: Você já pensou quantas informações suas estão online? Fotos, conversas, documentos, 
dados bancários... A segurança digital é o que nos ajuda a proteger esse mundo invisível, mas tão valioso.
\033[0m''')
        escolha_seg01 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_seg01 == '0':
            break
        else:
            escolha_seg01 = input('\033[36mEscolha inválida \033[m')

def modseg02():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 02 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mPOR QUE A SEGURANÇA DIGITAL É IMPORTANTE ?\033[0m')
        print('''\033[36m
Vivemos cada vez mais conectados. Compramos online, usamos aplicativos de banco, estudamos, trabalhamos
e até nos relacionamos através de plataformas digitais. Com tudo isso, nossos dados estão constantemente
circulando pela internet — e é aí que a segurança digital se torna essencial.
A segurança digital protege a vida digital das pessoas e das organizações, evitando prejuízos financeiros, 
emocionais e sociais.
Principais razões pelas quais ela é tão importante:

1. Proteção de dados
A segurança digital impede que seus dados sejam acessados, alterados ou roubados por pessoas não autorizadas. 
Imagine se alguém conseguisse acesso ao seu e-mail, às suas redes sociais ou à sua conta bancária.
Com uma boa segurança, essas informações ficam seguras contra invasões, vazamentos ou usos indevidos.

2. Preservação da privacidade
Privacidade significa ter controle sobre suas próprias informações. A segurança digital ajuda a garantir 
que seus dados:
Não sejam compartilhados sem sua permissão.
Não sejam usados por empresas ou criminosos para fins desconhecidos.
Não sejam expostos publicamente por falhas ou ataques.

Exemplo: Um aplicativo que coleta seus dados sem consentimento está violando sua privacidade. A segurança 
digital ajuda a evitar isso com boas práticas e regulamentações, como a LGPD (Lei Geral de Proteção de Dados).

3. Garantia de confiabilidade
Um sistema digital seguro é um sistema confiável:
Funciona corretamente.
Responde de forma estável.
Está livre de falhas causadas por vírus, ataques ou sabotagens.
Isso é essencial para serviços como:
Hospitais (onde falhas podem colocar vidas em risco),
Escolas (que guardam históricos escolares e dados de alunos),
Empresas (que dependem de sistemas para funcionar diariamente).

4. Prevenção de prejuízos financeiros e reputacionais
Ataques cibernéticos podem causar:
Roubo de dinheiro
Fraude em compras online
Clonagem de cartões
Queda na confiança do público (em empresas ou instituições)
Um simples descuido com a segurança pode gerar consequências sérias — tanto para pessoas quanto para organizações.

5. Responsabilidade social e coletiva
A segurança digital não é só um problema individual. Quando um computador é infectado, ele pode se tornar uma 
porta de entrada para atacar outros sistemas.
Manter a segurança dos seus dispositivos e dados ajuda a proteger também:
Sua família,
Seus colegas de trabalho,
E até a rede de toda uma empresa ou escola.

Para refletir:
"Privacidade e segurança não são luxos digitais – são direitos básicos."
Entender a importância da segurança digital é o primeiro passo para agir de forma mais consciente e responsável 
no mundo online.
\033[0m''')
        escolha_mod02 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_mod02 == '0':
            break
        else:
            escolha_mod02 = input('\033[36mEscolha inválida \033[m')

def modseg03():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 03 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mQUAIS SÃO OS PROBLEMAS QUE AMEAÇAM NOSSA SEGURANÇA DIGITAL?\033[0m')
        print('''\033[36m
A internet oferece inúmeras facilidades, mas também é um ambiente onde diversos riscos podem comprometer
nossa segurança e privacidade. Conhecer essas ameaças é essencial para saber como se proteger.
Vamos explorar as principais formas como a segurança digital pode ser comprometida e como essas ameaças 
afetam pessoas, empresas e instituições.

1. Hackers mal-intencionados
São pessoas ou grupos que tentam acessar sistemas ou dados sem autorização, muitas vezes com objetivos 
criminosos. Eles exploram falhas de segurança ou tentam enganar os usuários para obter acesso. Podem 
roubar dados, espalhar vírus, derrubar sites ou até sequestrar sistemas inteiros (como no caso de ataques
com ransomware). Nem todo hacker é criminoso! Existem os chamados "hackers éticos" que trabalham para 
descobrir falhas e ajudar a corrigir vulnerabilidades.

2. Malware (software malicioso)
Malware é um tipo de programa criado para causar dano, roubo de informações ou controle de sistemas. 
Os principais tipos incluem:
Vírus: se anexam a arquivos e se espalham entre dispositivos.
Spyware: espiam o que o usuário faz e enviam essas informações para terceiros.
Adware: enchem a tela de anúncios e podem coletar dados sem permissão.
Ransomware: sequestram os dados e exigem pagamento para liberar o acesso.
Muitas vezes, o malware entra no sistema através de downloads suspeitos, anexos de e-mail ou sites inseguros.

3. Phishing
Phishing é uma técnica de engenharia social usada para enganar pessoas e fazer com que elas entreguem dados 
confidenciais, como senhas e números de cartão. Acontece geralmente por e-mails falsos, SMS, redes sociais 
ou até sites que imitam páginas oficiais. Essas mensagens usam urgência, ameaças ou recompensas falsas para 
persuadir o usuário.
Exemplo: um e-mail dizendo que seu banco bloqueou sua conta e pedindo para você clicar em um link e 
"verificar seus dados".

4. Ataques DDoS (Negação de Serviço Distribuída)
Nesses ataques, criminosos sobrecarregam um site ou sistema com acessos falsos, fazendo com que ele saia do ar.
São comuns contra sites de empresas, instituições públicas ou bancos. Não visam roubo de dados diretamente, mas
 sim causar prejuízos financeiros e de reputação.

5. Engenharia social
Ao invés de atacar o sistema, esses golpes exploram comportamentos humanos. São tentativas de manipular ou enganar
 as pessoas para conseguir informações ou acesso.
Podem envolver telefonemas falsos, conversas manipuladoras ou criação de laços de confiança falsos (como perfis 
falsos em redes sociais).
Exigem atenção, senso crítico e cuidado ao compartilhar informações.

6. Vazamentos de dados
Ocorrem quando informações pessoais, financeiras ou confidenciais são expostas na internet, geralmente após:
Invasões de sistemas,
Falhas de segurança, Ou falta de cuidados com o armazenamento e o compartilhamento de dados. Uma vez vazados,
esses dados podem ser usados em fraudes, extorsões ou clonagens de identidade.

Para refletir:
"A maior parte dos ataques cibernéticos não acontece por causa da tecnologia, mas por falhas humanas." 
Entender as ameaças é o primeiro passo para se proteger. No próximo módulo, você vai aprender como evitar 
esses problemas com boas práticas simples, mas eficazes.
\033[0m''')
        escolha_mod03 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_mod03 == '0':
            break
        else:
            escolha_mod03 = input('\033[36mEscolha inválida \033[m')

def modseg04():
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

def modpython01():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 01 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mINTRODUÇÃO AO PYTHON\033[0m')
        print('\033[36mBreve resumo da história e uso da Linguagem Python\033[0m')
        print('''\033[36m
Python foi criado por Guido van Rossum em 1989, na Holanda, como um sucessor da linguagem ABC,
com o objetivo de ser fácil de ler, escrever e manter. A primeira versão oficial, Python 0.9.0,
foi lançada em 1991, já com funcionalidades como tratamento de exceções, tipos de dados básicos
(strings, listas, dicionários), e módulos. Desde então, o Python evoluiu com a ajuda de uma
comunidade ativa de desenvolvedores. Ele se tornou uma linguagem de código aberto, mantida pela
Python Software Foundation (PSF). Atualmente, o Python está em sua versão 3.x, com atualizações
frequentes que melhoram o desempenho, a segurança e a clareza da linguagem.
Python é conhecido por sua simplicidade e versatilidade. Por isso, é utilizado em diversas áreas:

- Desenvolvimento Web com frameworks como Django e Flask, é possível criar sites e aplicações 
web completos;
- Ciência de Dados e Análise Estatística: bibliotecas como Pandas, NumPy, Matplotlib e Scikit-learn
 fazem do Python uma das linguagens mais usadas por cientistas de dados;
 - Inteligência Artificial e Machine Learning: com bibliotecas como TensorFlow, PyTorch e Keras, 
 Python é a principal linguagem para criar modelos inteligentes;
- Automação de Tarefas: muitas pessoas usam Python para automatizar tarefas repetitivas no computador, 
como organização de arquivos, envio de e-mails ou raspagem de dados da internet;
- Desenvolvimento de Jogos: com bibliotecas como Pygame, é possível criar jogos 2D simples para fins 
educativos ou de entretenimento;
- Educação: por ser fácil de aprender, Python é amplamente usado em cursos introdutórios de programação 
ao redor do mundo.

Por que aprender Python?
Sintaxe clara e fácil de entender;
Comunidade grande e ativa;
Documentação rica;
Usado por empresas como Google, NASA, Netflix e Spotify; Ótimo para iniciantes e poderoso para profissionais.
 \033[0m''')
        sleep(2.0)
        print('')
        print('\033[36mCOMO INSTALAR O PYTHON (PASSO A PASSO)\033[0m')
        print('''\033[36m
Passo 1: Acesse o site oficial
Vá até o site: https://www.python.org

Passo 2: Vá até a seção de downloads
Clique na aba “Downloads”
O site detecta automaticamente seu sistema (Windows, macOS ou Linux)
Clique em “Download Python [download the latest version/download da versão mais recente]”

Passo 3: Execute o instalador
Após o download, abra o arquivo baixado
Antes de clicar em “Install Now”, marque a opção:
“Add Python to PATH” (muito importante!)

Passo 4: Instalação
Clique em “Install Now”
Aguarde o processo terminar
Ao final, clique em “Close”

Passo 5: Verificar se foi instalado
Abra o Prompt de Comando (Windows) ou Terminal (macOS/Linux)
Digite: python 
Se aparecer algo como Python 3.x.x, está instalado corretamente!
Caso não apareça, reinstale o programa.

\033[0m''')
        sleep(2.0)
        print('')
        print('\033[36mCOMO USAR O TERMINAL E EDITORES COM PYTHON\033[0m')
        print('''\033[36m
1 . Usando o Terminal
O terminal (ou prompt de comando) é a forma mais direta de rodar Python.
Passo a passo:
Abra o terminal:
Windows: Pesquise por cmd ou Prompt de Comando
macOS/Linux: Use o app "Terminal"
Digite: Python
Isso abre o modo interativo (REPL), onde você pode digitar comandos Python direto na tela.
Para rodar um arquivo .py salvo, vá até a pasta do arquivo e digite:
python nome_do_arquivo.py

2. Usando o VSCode (Visual Studio Code)
O VSCode é um editor leve e muito usado para Python.
Passo a passo:
Baixe e instale: https://code.visualstudio.com
Abra o VSCode e instale a extensão “Python” (ícone de quadrado no menu lateral > buscar "Python" > instalar).
Abra uma pasta onde ficará seu projeto.
Crie um novo arquivo com final .py, por exemplo: teste.py
Escreva o código Python, como:
print("Hello, World!")
Clique no botão de “Play” no topo direito ou pressione Ctrl + F5 para executar o programa.

3. Usando o PyCharm
O PyCharm é um IDE completo, ideal para projetos maiores.
Passo a passo:
Baixe e instale: https://www.jetbrains.com/pycharm/
Use a versão Community (gratuita)
Crie um novo projeto
Escolha a versão do Python instalada (geralmente o PyCharm detecta automaticamente)
Crie um novo arquivo .py
Escreva o código e clique com o botão direito > “Run 'nome_do_arquivo'”

\033[0m''')
        escolha_pymod01 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod01 == '0':
            break
        else:
            escolha_pymod01 = input('\033[36mEscolha inválida \033[m')

def modpython02():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 02 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mVARIAVEIS E TIPOS DE DADOS\033[0m')
        print('''\033[36m
Neste módulo, vamos aprender a declarar variáveis e a trabalhar com os tipos de dados mais comuns em 
Python: números, strings e booleanos, além de converter tipos (casting).

1. O que são variáveis?
Variáveis são espaços na memória onde podemos guardar valores para usar depois.
Exemplo:
| nome = "Ana" |
| idade = 25 |
Aqui, nome guarda uma string e idade guarda um número inteiro.

2. Tipos de dados

a) Números
int → Números inteiros (sem vírgula)
float → Números decimais (com vírgula, mas em Python usa-se o ponto .)
Exemplo:
| idade = 30          # int |
| altura = 1.75       # float |

b) Strings
Usadas para armazenar textos
Sempre entre aspas simples ou aspas duplas
Exemplo:
| nome = "Carlos" |
| frase = 'Python é fácil!' |

c) Booleanos
Representam valores verdadeiros ou falsos
Em Python, usamos True e False (com letra maiúscula)
 Exemplo:
| maior_de_idade = True |
| tem_carteira = False |

3. Conversão de Tipos (Casting)
Às vezes, precisamos converter um tipo de dado para outro, como transformar texto em número ou número em texto.
 Exemplos:
| # int para string |
| idade = 20 |

| idade_str = str(idade) |
| # string para int |

| numero = int("10") |
| # float para int (perde a parte decimal) |
| altura = int(1.75) |

| # int para float |
| peso = float(64) |

| # string para float |
| valor = float("3.14") |
Importante: ao converter string para número, o texto deve conter apenas dígitos, ou o Python dará erro.
“#” é utilizada para fazer comentários, válidos apenas para quem está programando, a máquina não os entende.
\033[0m''')

        escolha_pymod02 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod02 == '0':
            break
        else:
            escolha_pymod02 = input('\033[36mEscolha inválida \033[m')

def modpython03():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 03 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mOPERADORES EM PYTHON\033[0m')
        print('''\033[36m
Neste módulo, vamos aprender como fazer operações matemáticas, comparações e como usar operadores lógicos 
para criar condições mais inteligentes nos seus programas.

1. Operadores Aritméticos
Usados para fazer contas matemáticas com números (int ou float).
Operador	Nome
+	        Adição	
-	        Subtração	
*	        Multiplicação	
/	        Divisão (float)	
//	        Divisão inteira	
%	        Módulo (resto)	
**	        Potência	
Exemplos:
| soma = 10 + 5 |
| divisao_inteira = 9 // 2 |
| potencia = 3 ** 2 |

2. Operadores de Comparação
Usados para comparar valores. Sempre retornam True ou False.
Operador	Significado	
==	        Igual  a	Ex.: 5 == 5	 True
!=	        Diferente de	Ex.: 5 != 3	True
> 	        Maiorque	Ex.: 5 > 3	True
<	        Menor que	Ex.: 5 < 3	False
>=	        Maior ou igual    Ex.: 5 >= 5	 True
<=	        Menor ou igual	Ex.: 6 <= 4	 False
 Exemplo:
| idade = 18 |
| maior_de_idade = idade >= 18  # True |

3. Operadores Lógicos
Usados para combinar condições (muito usados em if e while).
Operador	Significado	
and	         E (ambas verdadeiras)   Ex.: True and False = False
or	         OU (uma ou ambas)       Ex.: True or False = True
not	         NÃO (inverte valor)	 Ex.: not True = False
Exemplo:
idade = 20
| tem_carteira = True |
| pode_dirigir = idade >= 18 and tem_carteira  # True |

DICA: O operador ‘AND’ terá como resultado verdadeiro apenas se ambas as condições forem verdadeiras.
Caso contrário, o resultado será falso.
O operador ‘OR’ terá como resultado falso apenas se ambas as condições forem falsas. Em todos os outros 
casos, o resultado será verdadeiro.
\033[0m''')

        escolha_pymod03 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod03 == '0':
            break
        else:
            escolha_pymod03 = input('\033[36mEscolha inválida \033[m')

def modpython04():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 04 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mENTRADA E SAÍDA DE DADOS\033[0m')
        print('''\033[36m
Neste módulo, você aprenderá como:
Pedir informações do usuário com input();
Mostrar resultados na tela com print();
Deixar sua saída mais bonita com formatação de strings.

1. Entrada de dados – input()
A função input() serve para ler dados do usuário via teclado.
O valor retornado sempre é uma string (texto), mesmo que o usuário digite números.
Exemplo:
| nome = input("Qual seu nome? ") |
| print("Olá,", nome) |
Conversão após o input:
| idade = int(input("Digite sua idade: ")) |
| altura = float(input("Digite sua altura: ")) |

 2. Saída de dados – print()
A função print() mostra mensagens ou valores na tela.
Exemplo:
| print("Seja bem-vindo!") |
| print("A soma de 2 + 2 é", 2 + 2) |

3. Formatação de Strings
Usamos a formatação para exibir variáveis dentro de frases com mais clareza.
 a) f-strings (forma moderna e prática — Python 3.6+)
| nome = "Luna" |
| idade = 22 |
| print(f"{nome} tem {idade} anos.") |
b) .format() (forma tradicional, compatível com versões antigas)
| print("{} tem {} anos.".format(nome, idade)) | 

 c) Formatação com casas decimais:
| preco = 5.6789 |
| print(f"Preço: R$ {preco:.2f}")  # R$ 5.68 |
\033[0m''')
        escolha_pymod04 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod04 == '0':
            break
        else:
            escolha_pymod04 = input('\033[36mEscolha inválida \033[m')

def modpython05():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 05 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mESTRUTURAS DE DECISÃO – IF, ELIF, ELSE\033[0m')
        print('''\033[36m
Estruturas de decisão permitem que o programa tome decisões diferentes com base em condições.
1. A estrutura 'if'
Executa um bloco de código somente se a condição for verdadeira (True).
Exemplo:
| idade = 20 |
| if idade >= 18: |
|    print("Você é maior de idade.") |
Dica: O bloco dentro do if precisa estar identado (recuado com tab ou 4 espaços).

2. A estrutura 'if + else'
Usada para escolher entre dois caminhos: se a condição for falsa, executa o else.
Exemplo:
| idade = 16 |
| if idade >= 18: |
|    print("Maior de idade.") |
| else: |
|    print("Menor de idade.") |

3. A estrutura 'if + elif + else'
Usada quando há várias condições diferentes. O elif significa “senão, se...”.
Exemplo:
| nota = 7 |
| if nota >= 9: |
|    print("Ótimo!") |
| elif nota >= 7: |
|    print("Bom!") |
| elif nota >= 5: |
|    print("Regular") |
| else: |
|    print("Reprovado.") |

4. Operadores que ajudam nas decisões
Você pode usar operadores de comparação e lógicos nas condições do if.
 Exemplo:
| idade = 18 |
| tem_carteira = True |
| if idade >= 18 and tem_carteira: |
|    print("Pode dirigir.") |
| else: |
|    print("Não pode dirigir.") |
\033[0m''')
        escolha_pymod05 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod05 == '0':
            break
        else:
            escolha_pymod05 = input('\033[36mEscolha inválida \033[m')

def modpython06():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 06 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mESTRUTURAS DE REPETIÇÃO\033[0m')
        print('''\033[36m
Este módulo ensina como repetir comandos automaticamente, sem ter que escrever várias vezes a mesma linha
de código. Isso é feito com as estruturas while e for.

1. while: repete enquanto a condição for verdadeira
A estrutura while é usada quando não sabemos quantas vezes o código será repetido. Ela repete um bloco de 
código enquanto a condição for verdadeira.
Exemplo:
| contador = 1 |
| while contador <= 5: |
|    print(f"Número: {contador}") |
|    contador += 1  # aumenta 1 a cada repetição |

O que acontece aqui:
Começa com contador = 1
Enquanto contador for menor ou igual a 5, o programa imprime o número
Depois, ele soma +1 em contador
Quando contador chega em 6, a condição fica falsa e o laço para
Cuidado com loops infinitos!
Se você esquecer de atualizar a variável dentro do while, o código pode nunca parar.
| # ERRADO - loop infinito! |
| x = 0
| while x < 5:
|    print(x)
|   # x não muda, então repete pra sempre!

2. for: ideal para repetições com quantidade conhecida
O for é ótimo quando você já sabe quantas vezes deseja repetir algo. Ele funciona com listas,
strings ou com a função range() (que cria uma sequência de números).
Exemplo com range():
| for i in range(1, 6): |
|    print(f"Passo: {i}") |
Aqui o que acontece:
•	range(1, 6) gera os números: 1, 2, 3, 4, 5 
•	O for roda uma vez para cada número
3. A função range()
A função range() gera uma sequência de números. É muito usada com for.
Formato:
| range(início, fim, passo) |
início: número inicial (opcional, padrão é 0) 
fim: onde para (não inclui esse número!) 
passo: de quantos em quantos (opcional) 
Exemplos:
| range(5)         # 0, 1, 2, 3, 4 |
| range(1, 6)      # 1, 2, 3, 4, 5 |
| range(10, 0, -2) # 10, 8, 6, 4, 2 |

4. A função enumerate()
O enumerate() é usado em conjunto com o for para pegar o índice e o valor de uma lista ao mesmo 
tempo.
Exemplo:
| nomes = ["Ana", "Bruno", "Carlos"] |
| for i, nome in enumerate(nomes): |
|    print(f"{i} - {nome}") |
Saída:
| 0 – Ana |
| 1 – Bruno |
| 2 – Carlos |
Isso é útil para numerar itens, criar menus, etc.
\033[0m''')
        escolha_pymod06 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod06 == '0':
            break
        else:
            escolha_pymod06 = input('\033[36mEscolha inválida \033[m')

def modpython07():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 07 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mFUNÇÕES\033[0m')
        print('''\033[36m
Funções são blocos de código reutilizáveis. Elas ajudam a organizar o programa e evitar repetições.
1. Definindo funções com def
Para criar uma função em Python, usamos a palavra-chave def, seguida do nome da função e parênteses ().
Exemplo simples:
| def saudacao(): |
|    print("Olá! Seja bem-vindo ao curso de Python!") |
Para executar a função, basta chamá-la pelo nome:
| saudacao() |

2. Parâmetros e retorno
Funções podem receber dados (parâmetros) e devolver resultados (com return).
Exemplo com parâmetros:
| def apresentar(nome): |
|    print(f"Olá, {nome}!") |
apresentar("Ana")  # Olá, Ana! 

Exemplo com retorno:
| def somar(a, b): |
|    return a + b |
| resultado = somar(3, 5) |
| print(f"Resultado: {resultado}")  # Resultado: 8 |
return envia o resultado da função de volta para quem a chamou.

3. Funções integradas (built-in)
O Python já vem com várias funções prontas que você pode usar a qualquer momento. Vamos ver algumas das mais usadas:

Função	O que faz	
print()	Exibe algo na tela	Ex.: print("Oi")
len()	Conta quantos itens tem uma lista ou string	Ex.: len("Python") → 6
sum()	Soma todos os números de uma lista	Ex.: sum([1, 2, 3]) → 6
max()	Retorna o maior valor	Ex.: max(10, 20, 5) → 20
min()	Retorna o menor valor	Ex.: min(3, 1, 9) → 1
type()	Mostra o tipo de dado	Ex.: type(5) → <class 'int'>
input()	Lê uma entrada do usuário	Ex.: nome = input("Seu nome: ")
\033[0m''')
        escolha_pymod07 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod07 == '0':
            break

        else:
            escolha_pymod07 = input('\033[36mEscolha inválida \033[m')

def modpython08():
    while True:
        print('\033[35m ==========\033[0m' ' \033[1;36m MODULO 08 \033[0m' '\033[35m ==========\033[0m')
        sleep(2.0)
        print('\033[36mMANIPULAÇÃO DE ARQUIVOS (BÁSICO)\033[0m')
        print('''\033[36m
Neste módulo, vamos aprender a abrir, ler e escrever arquivos de texto (.txt) usando Python.
1. Abrindo arquivos com open()
A função open() é usada para acessar arquivos. Ela pode abrir arquivos para leitura, escrita 
ou adição de conteúdo.
Sintaxe:
| open("nome_do_arquivo.txt", "modo") |
        Modo	               Ação
"r"	leitura (read)     –      padrão
"w"	escrita (write)    –   sobrescreve o conteúdo
"a"	acrescenta (append) – adiciona no final
"x"	cria um novo arquivo (erro se já existir)

2. Lendo arquivos
Exemplo:
| arquivo = open("exemplo.txt", "r") |
| conteudo = arquivo.read() |
| print(conteudo) |
| arquivo.close() |
| read() lê todo o conteúdo do arquivo. |

Ler linha por linha:
| arquivo = open("exemplo.txt", "r") |
| for linha in arquivo: |
|    print(linha.strip())  # .strip() remove o \n – quebra de linha |
| arquivo.close() |

3. Escrevendo arquivos com .write()
Exemplo:
arquivo = open("novo.txt", "w")
arquivo.write("Primeira linha do arquivo.\n")
arquivo.write("Segunda linha.")
arquivo.close()
OBS: Com o modo "w", o conteúdo anterior é apagado!

4. Adicionando conteúdo com "a" (append)
Exemplo:
| arquivo = open("novo.txt", "a") |
| arquivo.write("\nNova linha adicionada.") | 
| arquivo.close() |

5. Usando with open() (forma recomendada)
Usar with garante que o arquivo será fechado automaticamente.
|with open("exemplo.txt", "r") as arquivo: |
|    print(arquivo.read()) |
Boa prática para evitar erros de arquivos abertos por muito tempo.

6. Fechando arquivos com .close()
Sempre que você usa open() para abrir um arquivo, é importante fechá-lo depois de terminar 
a leitura ou escrita. Isso é feito com o método .close().
Exemplo:
| arquivo = open("dados.txt", "r") |
| conteudo = arquivo.read() |
| arquivo.close() |

Por que usar .close()?
Libera recursos do sistema;
Garante que todas as alterações feitas no arquivo sejam salvas corretamente;
Evita erros, como tentar abrir o mesmo arquivo duas vezes ao mesmo tempo.

Dica:
Usar with open() já cuida disso automaticamente, sem precisar escrever .close():
| with open("dados.txt", "r") as arquivo: |
|    print(arquivo.read())  # O arquivo será fechado automaticamente aqui |
\033[0m''')
        escolha_pymod08 = input('\033[36mDigite 0 para voltar:  \033[m')
        if escolha_pymod08 == '0':
            break
        else:
            escolha_pymod08 = input('\033[36mEscolha inválida \033[m')

