#########################################################################
# DEFINIÇÕES DE PERSONAGEM E IMAGENS
#########################################################################
define config.rollback_enabled = True # DESABILITAR DEPOIS DE TERMINAR O JOGO
default lumicompleto = False
default solimarcompleto = False

define n = Character("")                                         # narrador
define pov = Character("{b}[povname]{/b}", color = "#ffffff")                              #Nome de usuário

#Intro
define a = Character("{b}Diretor Almeida{/b}",color="#ffffff")
define b = Character("{b}Diretor Bastos{/b}",color="#ffffff")
define r = Character("{b}Silvia{/b}",  color="#ffffff")
define d = Character("{b}Delegado Silva{/b}", image="delegado", color="#ffffff")
define v = Character("{b}Agente Vieira{/b}",  color="#ffffff")

#Time da BRComorg
define l = Character("{b}Laura{/b}", color="#ffffff") #Gestão de relacionamento
define gi = Character("{b}Gi{/b}",color ="ffffff") #Criação de conteúdo
define m = Character("{b}Max{/b}",color ="ffffff") #Planejamento Estratégico
define doug = Character("{b}Doug{/b}",color ="ffffff") #Análise de Comunicação

# Ong Patinhas
define p = Character("{b}Paulo{/b}", color="#ffffff")     # Voluntário
define li = Character("{b}Lise{/b}", color="#ffffff")         # Diretora da ONG

# Empresa Lumi

# Universidade Solemar


# BACKGROUNDS -------------------------------------------------
image bg logo              = "images/Misc/DesenrolaLogoDigital.png"                 # sua imagem de título
image bg ceu_azul          = "images/Fundos/ceuazul.png"
image bg brcomorg_externo  = "images/Fundos/BRComorgExterno.png"
image bg brcomorg_externo_noite = "Fundos/BRComorgExternonoite.png"
image bg recepcao_2andar   = "images/Fundos/recepcaosegundoandar.png"
image bg elevador_interno  = "images/Fundos/elevadorinterno.png"
image bg elevador_externo  = "images/Fundos/elevadorexterno.png"
image bg office_interditado = "Fundos/officeinterditado.png"
image bg sala_reuniao    = "images/Fundos/saladodiretor.png"
image bg almeida_tranquilo  = "images/Fundos/diretorceriocena3tranquilo.png"
image bg almeida_serio      = "images/Fundos/diretorceriocena3.png"
image bg refeitoriobrcomorg = "Fundos/BRComorgrefeitorio.png"
image bg cabovermelhopc = "Fundos/BRComorgroffice cabo.png"
image bg cabosalo = "Fundos/cabosalo.png"
image bg diretoriabastos = "Fundos/diretoriabastos.png"
image bg saladiretor2 = "Fundos/saladiretor2.png"
image bg canilnomear = "Fundos/canilnomear.png"
image bg montarinterface = "montar interface/montarinterface.png"

image bg patinhasexterno    = "Fundos/ongpatinhas_externo.png"
image bg patinhas_recepção  = "Fundos/ongpatinhas_recepcao.png"
image bg patinhas_corredor  = "Fundos/ongpatinhas_corredor.png"
image bg patinhas_reuniao   = "Fundos/ongpatinhas_saladereuniao.png"
image bg patinhas_reuniao2  = "Fundos/ongpatinhas_saladereuniao2.png"
image bg patinhas_reuniao3  = "Fundos/ongpatinhas_saladereuniao3.png"
image bg patinhas_reuniao4  = "Fundos/ongpatinhas_saladereuniao4.png"
image bg patinhas_reuniao5  = "Fundos/ongpatinhas_saladereuniao5.png"
image bg patinhas l = "Fundos/ongpatinhas_saladereuniao com laura.png"
image bg patinhas lm = "Fundos/ongpatinhas_saladereuniao com laura e max.png"
image bg patinhas lmg = "Fundos/ongpatinhas_saladereuniao com laura e max e gi.png"
image bg patinhas lmgd = "Fundos/ongpatinhas_saladereuniao com laura e max e gi e doug.png"
image bg patinhas principal = "Fundos/ongpatinhas_saladereuniao zoom bg.png"
image bg reuniao_gi = "Fundos/ongpatinhas_saladereuniao com gi.png"
image bg patinhasmesatalkback = "Fundos/ongpatinhas_saladereuniao mesa habla.png"
image bg cardgametable1 = "cards/zoom mesa game.png"
image bg cardgametable1tutorial = "cards/zoom mesa game tutorial.png"
image bg interfacecompleta = "montar interface//interface.png"
image bg canilcompleto = "Fundos/canilnomeado.png"
image bg patinhasgi = "Fundos/patinhasgi.png"
image bg voluntarios = "Fundos/voluntarios.png"
image bg tutorial = "Fundos/pdfgitutorial.png"
image bg solucaomax = "Fundos/solucaomax.png"
image bg pcmx = "Fundos/computadormexendo.png"


# SPRITES -----------------------------------------------------
#Laura
image laura default        = "images/Personagens/lauraparadacentro.png"
image laura cafe           = "images/Personagens/lauracomcafe.png"
image laura semcafe        = "images/Personagens/laurasemcafeelevador.png"
image laura dois_cafes     = "images/Personagens/laurasegurandocafebebendocafe.png"
image laura_cochichando = "Personagens/laura cochichando.png"
image laura meiga = "Personagens/lauracontraposto.png"
image laura feliz = "Personagens/laura feliz.png"
image laura brava = "Personagens/laura brava.png"

#Delegado
image delegado serio       = "images/Personagens/delegadoserio.png"

#Silvia Recepcionista
image recepcionista espantada = "images/Personagens/recepcionista espantada.png"
image recepcionista        = "images/Personagens/recepcionistacontraposto.png"
image recepcionista feliz  = "images/Personagens/recepcionista feliz.png"

#Itens
image mesarecepcao         = "iMisc/recepcaosegundoandarmesa.png"
image recepcao_patinhas = "Misc/ongpatinhas_recepcao_mesa.png"
image mesareuniaopt = "Misc/ongpatinhas_saladereuniao zoom transparente.png"
image patinhastalkbackmesa = "Misc/ongpatinhas_saladereuniao mesa habla2.png"

#Perito
image perito pc            = "Personagens/perito pc.png"
image perito serio         = "Personagens/perito serio.png"

#Diretor Almeida
image almeida_sorriso    = "images/Personagens/diretorsorrindo.png"

#Bastos
image bastos = "Personagens/bastoss.png"

#Paulo
image paulo_1 = "Personagens/patinhas voluntario.png"
image paulo_2 = "Personagens/patinhas voluntario puto.png"
image paulo_3 = "Personagens/patinhas voluntario eh.png"
image p default = "Personagens/Paulo default.png"
image p habla = "Personagens/Paulo default hablando.png"

#Lise
image lise = "Personagens/lise.png"
image lise feliz = "Personagens/Lise Feliz.png"
image lise brava = "Personagens/Lise Brava.png"
image lise triste = "Personagens/Lize triste.png"

#Max
image maxx = "Personagens/ORG2.png"
image maxx triste = "Personagens/max triste.png"
image maxx feliz = "Personagens/max feliz.png"
image maxx raiva = "Personagens/max raiva.png"

#Gi
image gio = "Personagens/ORG3.png"
image gio raiva = "Personagens/ORG3 brava.png"
image gio feliz = "Personagens/ORG3 felix.png"

#Duog
image douglas = "Personagens/ORG4.png"
image douglas feliz = "Personagens/doug sorrindo.png"
image douglas raiva = "Personagens/doug raiva.png"
image douglas triste = "Personagens/doug triste.png"



label gameover:
    scene black with fade
    n "{b}Fim de Jogo{/b}.\nVocê recusou a missão."
    return

label continua:
    scene black with fade
    "Continua..."
    return


# ─── Sanitizador ──────────────────────────────────────────────────────────────
init python:
    import re
    def clean_name(raw: str):
        # remove espaços
        nome = re.sub(r"\s+", "", raw)
        # capitaliza
        nome = nome.capitalize()

        # lista de palavrões (variações simples, acentos, leetspeak)
        bad = [
            r"f[oó0]d[a@]s?", r"c[uú]", r"p[uú]t[a@]s?",
            r"caralh?o?s?", r"porr?a?s?", r"coc[oô0]",
            r"bost[a@]s?", r"merd[a@]s?"
        ]
        for p in bad:
            if re.fullmatch(p, nome.lower()):
                return None
        return nome

default povname = ""        # recomendado para rollback e saves
default kpi = 0


# ─── Função secreta de pontuação ───────────────────────────────────────────────
init python:
    def alterar_kpi(valor: int):
        """
        Atualiza a variável global KPI silenciosamente (sem feedback).
        """
        global kpi
        kpi += valor
# ───────────────────────────────────────────────────────────────────────────────



################################################################################
# LABEL DA CENA INICIAL
################################################################################

default pegou_cafe = False      # assume que o jogador NÃO pegou café até escolher

label cena1:

    # --- TELA PRETA + LOGO ----------------------------------------------------
    scene black with fade
    show bg logo at truecenter                    # logo centralizado na tela
    with fade
    pause 3
    hide bg logo with fade

    # --- INTRODUÇÃO DO JOGO ---------------------------------------------------
    scene bg ceu_azul with dissolve
    n "Bem-vindo a {i}Desenrola Digital{/i}, um jogo para aprender Design Thinking aplicado à Comunicação Organizacional."

    # loop até obter nome válido
    python:
        while True:
            raw = renpy.input("Qual é o seu nome?", length=32)
            nome_ok = clean_name(raw)
            if nome_ok:
                break
            renpy.say(n, "Por favor, escolha um nome apropriado (sem espaços ou palavrões).")

    $ povname = nome_ok      # armazenamento oficial com “$”

    n "Prazer em conhecê-lo, [povname]!"
    # --- EXTERIOR DA BRComorg -------------------------------------------------
    scene bg brcomorg_externo with fade:
        zoom 0.8
    n "{b}[povname]{/b}, Você é um profissional de comunicação que trabalha na agência terceirizada do Estado, a {b}BRComorg{/b}."
    n "Parece um dia comum de expediente..."
    n "{b}Horário:{/b} 08h00\nEntrada principal da {b}BRComorg{/b}\nAsa Norte, {b}Brasília.{/b}"

    # --- RECEPÇÃO / LAURA COM DOIS COPOS -------------------------------------
    scene bg elevador_interno with dissolve
    show laura dois_cafes at right:
        zoom 0.3
    n "{b}Laura{/b} Sua colega de trabalho, perto dos elevadores, equilibrando dois copos térmicos fumegantes."
    l "Bom dia {b}[povname]{/b}! Sobreviveu ao fim de semana?"
    l "Aliás, quer um café para acordar?"

    # --- MENU DE ESCOLHA ------------------------------------------------------
    menu:
        n "{b}Dica - Escolha com cuidado:{/b} suas decisões mudam o futuro da história."

        "Aceitar o café":
            $ pegou_cafe = True
            hide laura                       # apaga o sprite antigo
            show laura semcafe at right:
                zoom 0.3
            l "Aqui está, recém-passado. Vai precisar."

        "Recusar educadamente":
            $ pegou_cafe = False
            hide laura
            show laura cafe at right:
                zoom 0.34 xzoom -1.0          # continua com dois copos
            l "Tudo bem, mais cafeína pra mim então."

    # --- TRANSIÇÃO PARA ELEVADOR ---------------------------------------------
    scene bg elevador_interno with fade

    if pegou_cafe:
        show laura semcafe at right:
            zoom 0.3
    else:
        show laura cafe at right:
            zoom 0.34 xzoom -1.0

    l "O que será que nos espera hoje? Espero que o chefe esteja tranquilo."
    n "Vocês sobem em silêncio por alguns andares..."
    n "{b}Decisões de diálogo afetam sua Pontuação Geral{/b}."
    return

label cena2:

    # Portas do elevador se abrem para o open-space
    scene bg recepcao_2andar with fade
    show mesarecepcao zorder 10

    # Recepcionista Silvia ao fundo
    show recepcionista feliz at left:
        zoom 0.34
    # Laura mantém a pose coerente com a escolha do café
    if pegou_cafe:
        show laura semcafe at right:
            zoom 0.3
    else:
        show laura cafe at right:
            zoom 0.34 xzoom -1.0

    r "Olá, bom dia, Laura e [povname]."

    hide recepcionista feliz
    show recepcionista espantada at center with fade:
        zoom 0.35
    r "Os policiais chegaram hoje de manhã, disseram que…"
    hide recepcionista
    show laura default
    l "O que está acontecendo aqui? Policiais?"
    hide laura
    n "Você decide avançar para a sua mesa, hoje o clima está tenso."

    scene bg office_interditado with dissolve

    show perito pc at left:
        zoom 0.35
    show delegado serio at center:
        zoom 0.35

    n "Agentes da Polícia Federal revistam cabos, lixeiras e desconectam desktops.\
       Cadeiras foram afastadas às pressas, gavetas estão abertas, cabos pendem no ar.\
       Seus colegas observam em silêncio enquanto equipamentos são recolhidos."

    # Delegado Silva entra em cena
    
    d "{b}[povname]{/b}, de Comunicação? Sou delegado Tito Silva, Polícia Federal. Precisamos conversar — agora."

    n "Seu estômago afunda. O que, exatamente, está acontecendo?"

    d "A inteligência identificou vazamento de documentos sigilosos do governo enviados da sua máquina. Quero entender como isso aconteceu."

    n "Você não sabe exatamente a resposta..."
    d "Alguém mais tem acesso físico ou sabe a senha do seu computador?"

    n "O Agente Vieira registra cada detalhe da sua reação num bloco de notas eletrônico."

    d "Por ora, você é investigado, não réu. Sua cooperação pode mudar isso."
    hide delegado serio
    show perito serio at center:
        zoom 0.35
    v "Vamos levar este equipamento para perícia. Se estiver limpo, ótimo. Se não estiver…"
    hide perito serio
    show delegado serio at center:
        zoom 0.35
    d "O tráfego partiu com o seu token de dois fatores. Isso sugere sua conivência com o vazamento."

    d "Fique em Brasília e não acesse nenhum sistema da empresa. A perícia leva alguns dias.\
         Se descobrirmos ajuda interna, você terá chance de provar inocência; caso contrário, a acusação por crime digital será pesada."

    return

###############################################################################
# LABEL CENA 3 – SALA DE REUNIÕES, 08h37
###############################################################################

label cena3:

    # fundo da sala de reuniões
    scene bg almeida_serio with fade
    n "{b}Horário:{/b} 08h37   {b}Local:{/b} Sala de Reuniões"

    # Diretoria entra
    a "Relatórios confidenciais sobre campanhas e informações governamentais foram extraídos do nosso servidor.\
       Isso logo acionou a inteligência brasileira."

    a "Se não provarmos controle do nosso departamento antes de {b}90 dias{/b}, perdemos o contrato de {b}R$ 30 milhões/ano{/b}."

    # Bastos
    scene bg diretoriabastos:
        zoom 1.7
    show bastos at center:
        zoom 0.6
    b "E, claro, sem contrato não existirá verba para advogados que limpem seu nome."

    # Almeida faz proposta
    scene bg almeida_tranquilo

    a "Aqui está o combinado: Podemos te demitir por vazamento de dados ou você pode nos ajudar."
    a "Esta agência deve provar ao Estado que precisa de nós — \
        estamos há vinte anos à frente de inúmeros projetos."
    a "Nem eu nem Bastos acreditamos que você venderia dados desse nível."

    # Bastos
    scene bg diretoriabastos:
        zoom 1.7
    show bastos at center:
        zoom 0.6
    b "Você tem muita sorte, na verdade."

    scene bg almeida_tranquilo
    b "*inclina-se, voz fria* Falhar significa cadeia por crime digital e multa de até {b}R$ 500 mil{/b}.\
       Tem certeza de que quer recusar?"

    # Almeida entrega relatório (troca sprite)
    scene bg almeida_serio
    a "Estas três empresas respondem por mais de 80 porcento da nossa receita com o governo"
    a "Todas enfrentam crises de comunicação. Se você resolver o problema delas, podemos dar amparo jurídico.\
       Uma mão lava a outra."

    scene bg almeida_tranquilo
    a "*baixando o tom* Oferecemos um adiantamento salarial e advogado — se você topar."

    menu:
        "Aceitar":
            a "Mostre ao governo — e a nós — que ainda somos indispensáveis."
            $ alterar_kpi(10)  # boa escolha
            call screen missoes    # Continua o jogo normalmente

        "Recusar":
            a "Você perdeu o jogo."
            jump gameover

    return


# The game starts here.

label start:
    call cena1
    call cena2
    call cena3
    call continua

    return