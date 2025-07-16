#Missão3

default origem_cabo       = False   # laudo reconhecido
default suspeita_guava    = False   # jogador percebe implicação maior
default denunciar_pf      = False   # decidiu avisar a PF imediatamente

###Characters
define prof = Character("{b}Prof. Raquel{/b}",color = "#ffffff")
define rep = Character("{b}Repórter Julia{/b}",color = "#ffffff")
image r1 = "solemar/rep1.png"
image r2 = "solemar/rep2.png"
image reporter = "solemar/reporter.png"
image caio = "solemar/caio 1.png"
image caio bravo = "solemar/caio 2bravo.png"
image bastos sorri = "solemar/levesorrizo.png"
image pr = "solemar/prof1.png"
image pr2 = "solemar/prof1.1.png"
image ti = "solemar/ti.png"

### BACKGROUNDS
image bg bastoscelular = "solemar/bastoscelular.png"
image bg vidrado = "solemar/vidrado.png"
image bg aud3 = "solemar/aud3.png"
image bg delegacia = "solemar/delegacia.png"
image bg solemar externo = "solemar/Universidade Solemar Externo.png"
image bg solemar externo_manifestacao = "solemar/manifestacao.png"
image bg solemar externo_noite = "solemar/campusnoite.png"
image bg solemar sala = "solemar/salaaula.png"
image bg salaquadro = "solemar/salaquadro.png"
image bg salaquadro2 = "solemar/salaquadro2.png"
image bg salaquadro3 = "solemar/salaquadro3.png"
image bg informatica = "solemar/informatica.png"
image bg auditorioescola = "solemar/auditorio.png"
image bg auditorioescola2 = "solemar/aud2.png"
image bg advcelular = "solemar/adv celular.png"
image bg bastospego = "solemar/bastospego.png" 
image bg bastosaterrorizado = "solemar/bastosaterrorizado.png"
image bg bastospreso = "solemar/bastospreso.png" 
image bg jornal = "solemar/jornal.png" 
image bg aeroporto = "solemar/aeroporto.png"
image bg prisao1 = "solemar/prisao1.png"
image bg prisao2 = "solemar/prisao2.png"
image bg quadro = "solemar/quadro.png"
image bg postits = "solemar/postits.png"
image bg pcmade = "solemar/minigame/pc made.png"
image bg briefing = "solemar/reuniaoadv.png"
image bg policias = "solemar/policias.png"
image bg policias2 = "solemar/policias2.png"
image bg policias3 = "solemar/policias3.png"
image bg pendrive = "solemar/pendrive.png"
image bg clap = "solemar/clap.png"
image bg novosistema = "solemar/novosistema.png"
image bg balao = "solemar/balao.ong"
image bg instavel = "solemar/instavel.png"
image bg indicadores = "solemar/indicadores.png"
image bg simnao = "solemar/simnao.png"
image bg entrance = "solemar/entrance.png"


###############################################
# LABEL – BRIEFING COM DIRETORIA E ADVOGADO   #
###############################################
###############################################
# LABEL – BRIEFING ENTRE PROTAGONISTA & ADV.  #
###############################################
label missao3:
    if cabo_entregue:
        jump briefing_cabo_guava
    else:
        jump solemar_externo

label briefing_cabo_guava:

    scene black with fade
    play music "sus.ogg"
    n "{b}Sala de reuniões{/b}\n{b}07h45{/b}"
    play sound "ui.ogg"
    scene bg briefing with dissolve

    # --- AMBIENTE -----------------------------------------------------------

    show adv at center:
        zoom 0.6
        ypos 1500
    adv "{b}Bom dia, [povname].{/b} Tenho algo que muda o tabuleiro."
    play sound "ui.ogg"
    adv "O laboratório concluiu a análise do {i}cabo SALO{/i} que você encontrou."
    play sound "ui.ogg"

    # --- REVELAÇÃO ----------------------------------------------------------
    adv "Esse cabo é fabricado {b}exclusivamente{/b} pela {b}Guava{/b}."
    play sound "ui.ogg"
    adv "— sim, {i}a{/i} Guava que todo mundo usa."
    play sound "ui.ogg"

    $ origem_cabo = True               # flag global

    pov "Guava faz cabos de rede também? Achei que eles só vendessem eletrônicos de consumo..."
    play sound "ui.ogg"
    
    adv "Justamente. Cabos com esse sistema são raríssimos fora de laboratórios de segurança."
    play sound "ui.ogg"

    # --- DECISÃO DO PROTAGONISTA ------------------------------------------
    menu:
        n "{b}Próximo passo?{/b}"

        "Protocolar o laudo hoje mesmo na Polícia Federal":
            play sound "menu.ogg"
            $ choices_log.append(("menu10", "Clicou Protocolar o laudo hoje mesmo na Polícia Federal", renpy.get_game_runtime()))
            $ denunciar_pf = True
            pov "Quero isso registrado na cadeia de custódia oficial antes que alguém sumam com a prova."
            play sound "ui.ogg"
            show adv at center:
                zoom 0.6
                ypos 1500
            adv "Perfeito. Faço o ofício para o Delegado Silva agora de manhã."
            play sound "ui.ogg"
            $ kpi += 5
            jump solemar_externo

        "Checar antes se existe nota fiscal ou ordem de compra interna":
            play sound "menu.ogg"
            $ choices_log.append(("menu10", "Clicou Checar antes se existe nota fiscal ou ordem de compra interna", renpy.get_game_runtime()))
            $ suspeita_guava = True
            pov "Melhor ver se esse lote aparece em algum pedido legítimo da BRComorg."
            play sound "ui.ogg"
            show adv at center:
                zoom 0.6
                ypos 1500
            adv "Solicitarei acesso ao ERP e às declarações de importação. Se não houver registro, o buraco é mais fundo."
            play sound "ui.ogg"
            $ kpi += 3
            jump solemar_externo

        "Guardar o laudo e capturar mais tráfego de rede Guava primeiro":
            play sound "menu.ogg"
            $ choices_log.append(("menu10", "Clicou Guardar o laudo e capturar mais tráfego de rede Guava primeiro", renpy.get_game_runtime()))
            pov "Quero mais pacotes que provem a assinatura da Guava antes de expor isso."
            play sound "ui.ogg"
            show adv at center:
                zoom 0.6
                ypos 1500
            adv "Concordo. Posso instalar um sniffer nos switches durante a madrugada para rastrear MAC-prefixos da Guava."
            play sound "ui.ogg"
            jump solemar_externo
            # KPI neutro
################################################################################
# SEÇÃO 1 — CHEGADA À UNIVERSIDADE SOLEMAR (caos da matrícula)
# Arquivo: missoes.rpy        label: solemar_externo
################################################################################

# ─── Variáveis novas ──────────────────────────────────────────────────────────
default solemar_abordagem   = ""      # "{b}Aluno Caio{/b}" | "imprensa" | "contornar"
default mapa_ok             = False   # (será usado na etapa de Empatia)
# -----------------------------------------------------------------------------

label solemar_externo:
    stop music fadeout 1
    scene black with fade
    pause 1
    scene bg solemar externo with dissolve
    n "{b}Universidade Solemar – Portão Principal{/b}\n{b}08h52{/b}"
    play sound "ui.ogg"
    scene bg solemar externo_manifestacao with dissolve

    play music "protest.ogg" fadein 1
    n "O campus fervilha. Centenas de estudantes entoam gritos de protesto:\n ‘Portal fora do ar, queremos estudar!’"
    play sound "ui.ogg"
    scene bg solemar externo_manifestacao:
        matrixcolor SaturationMatrix(0)
    show reporter zorder 10
    # Repórter da TV local
    show caio at center:
        zoom 0.6
    # Líder estudantil

    "{b}Caio Mendes – DCE{/b}" "Sem transparência, sem aula! Portal bugado e boato de corte de vagas!"
    play sound "ui.ogg"
    # equipe chega
    show laura_cochichando at left:
        xzoom -1
    play sound "lauracochicho.ogg"
    l "{i}(sussurra){/i} Situação sensível… Precisamos decidir como avançar."
    play sound "ui.ogg"
    hide laura_cochichando
    hide reporter
    # --- MENU DE ABORDAGEM ---------------------------------------------------
    menu:
        n "{b}Seu primeiro movimento?{/b}"

        "Dialogar com o aluno Caio para entender a dor":
            play sound "menu.ogg"
            $ choices_log.append(("menu11", "Clicou Dialogar com o aluno Caio para entender a dor", renpy.get_game_runtime()))
            $ solemar_abordagem = "dce_"
            $ alterar_kpi(8)
            pov "O que está acontecendo aqui?"
            play sound "ui.ogg"
            show caio at center:
                zoom 0.6

            "{b}Aluno Caio{/b}" "A galera não consegue confirmar disciplinas, e a reitoria não posta um único aviso claro."
            play sound "ui.ogg"
            show lauracontraposto at left:
                zoom 0.6
                ypos 1400
            l "Prometo que traremos respostas hoje. Mas precisamos de detalhes."
            play sound "ui.ogg"
            hide lauracontraposto
            
        "Dar entrevista imediata à imprensa para acalmar o público":
            play sound "menu.ogg"
            $ choices_log.append(("menu11", "Clicou Dar entrevista imediata à imprensa para acalmar o público", renpy.get_game_runtime()))
            $ solemar_abordagem = "imprensa"
            $ alterar_kpi(3)
            pov "Se não controlarmos a narrativa, a crise explode."
            play sound "ui.ogg"
            hide caio
            show r1 at center:
                zoom 0.6
                ypos 1200
            rep "Qual a falha real do portal? A universidade fala em ‘picos de acesso’."
            play sound "ui.ogg"
            pov "Estamos levantando informação técnica agora, mas garantimos canal único de atualizações\
                a cada 2 horas — transparência total."
            play sound "ui.ogg"
            n "O repórter agradece, mas alunos atrás de você continuam gritando."
            play sound "ui.ogg"
            hide r1

        "Contornar o protesto pelos fundos do campus":
            play sound "menu.ogg"
            $ choices_log.append(("menu11", "Clicou Contornar o protesto pelos fundos do campus", renpy.get_game_runtime()))
            $ solemar_abordagem = "contornar"
            $ alterar_kpi(-5)
            pov "Melhor evitar confusão. Entramos pela garagem e falamos direto com a TI."
            play sound "ui.ogg"
            n "Vocês dão a volta. A mídia registra a manobra em live: ‘BRComorg fugindo do diálogo!’"
            play sound "ui.ogg"

    # --- CONSEQUÊNCIA VISUAL -------------------------------------------------
    if solemar_abordagem == "dce_":
        hide lauracontraposto
        scene bg solemar externo with dissolve
        stop music fadeout 1
        n "A tensão baixa levemente; algumas faixas de protesto são recolhidas."
        play sound "ui.ogg"
    elif solemar_abordagem == "imprensa":
        scene bg solemar externo_manifestacao
        n "A imprensa se afasta satisfeita, mas o coro estudantil aumenta:\
        ‘{b}Queremos falar! Sem discurso pra TV!’"
        play sound "ui.ogg"
    else:
        # contornar
        scene bg solemar externo with dissolve
        n "Vocês entram por uma porta lateral sem serem notados... por enquanto."
        play sound "ui.ogg"

    # --- TRANSIÇÃO PARA FASE DE EMPATIA --------------------------------------
    n "Próximo passo: mapear as dores de alunos, TI e Pró-reitoria."
    play sound "ui.ogg"
    scene black with fade
    pause 0.8
    jump audit_map          # → Seção de Empatia / Mapa de Dores

###############################################################################
# SEÇÃO 2 — AUDIT_MAP  (Empatia: levantamento de dores)                       #
# Continuação direta após “jump audit_map” da Seção 1                         #
###############################################################################

label audit_map:

    scene black with fade
    stop music fadeout 1
    show text "{b}Fase:{/b} Empatia" with fade
    pause 1
    scene bg solemar sala with dissolve
    n "Uma sala de aula vazia foi improvisada para ouvir os envolvidos no colapso da matrícula."
    play sound "ui.ogg"

    # ── Roda-rápida de entrevistas ─────────────────────────────────────────
    show caio at center:
        zoom 0.6
    "{b}Aluno Caio{/b}" "Sistema cai toda madrugada. Quem tenta logar depois das 6h perde vaga."
    play sound "ui.ogg"
    hide caio
    show laura default at center:
        zoom 0.4
    l "Quantos avisos oficiais vocês receberam nesses dois dias?"
    play sound "ui.ogg"
    hide laura
    show caio bravo at center:
        zoom 0.6
    "{b}Aluno Caio{/b}" "Nenhum, claro! Só prints no grupo do WhatsApp."
    play sound "ui.ogg"
    hide caio
    show pr at center:
        zoom 0.6
        ypos 1200
    prof "O sistema antigo não suportava o novo módulo de bolsa. O pessoal da TI alertou, mas o contrato já estava assinado."
    play sound "ui.ogg"
    pov "Existe cronograma público dessas etapas?"
    play sound "ui.ogg"
    prof "Ficou num PDF interno que nunca subiu ao site."
    play sound "ui.ogg"
    hide pr
    show ti at center:
        zoom 0.6
    "{b}Profissional de TI{/b}" "A origem do proeblema, na verdade, é o relatório em PDF que é gerado a cada confirmação. Trava o servidor por 4 segundos a cada aluno."
    play sound "ui.ogg"
    hide ti
    show maxx at center:
        zoom 0.4
    m "Se tirarmos esse gerador de PDF do fluxo, o portal funciona?"
    play sound "ui.ogg"
    hide maxx
    show ti at center:
        zoom 0.6
    "{b}Profissional de TI{/b}" "Respira, mas fica sem informações."
    play sound "ui.ogg"
    hide ti
    show pr at center:
        zoom 0.6
        ypos 1200
    prof "A reitoria manda e-mails de contas diferentes, mas alunos não reconhecem que são oficiais. Comunicação cruzada, ninguém entende nada."
    play sound "ui.ogg"

    # ── Mapeamento visual (narrado) ────────────────────────────────────────
    scene bg salaquadro
    n "Anotações preenchem o quadro: ‘Falha de performance’, ‘Canal disperso’, ‘Falta de cronograma público’."
    play sound "ui.ogg"
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Os três maiores probelmas são: PERFORMANCE do portal, CANAIS divergentes e FALTA de TRANSPARÊNCIA de prazos."
    play sound "ui.ogg"
    hide douglas
    show bg salaquadro2 with dissolve
    show gio at center:
        zoom 0.34
    gi "Boa. Vamos transformar em pergunta ‘How Might We’ depois."
    play sound "ui.ogg"

    # ── Encerramento da fase de Empatia ────────────────────────────────────
    n "Com as dores mapeadas, a equipe se prepara para convergir num problema-chave."
    play sound "ui.ogg"

    jump solemar_problem

###############################################################################
# SEÇÃO 3 — SOLEMAR_PROBLEM  (Definição: escolher o 'How Might We')                       #
# Continua logo após “jump solemar_problem” da Seção 2                         #
###############################################################################

label solemar_problem:

    scene black with fade
    play music "guitar.ogg"
    show text "{b}Fase:{/b} Problematização" with fade
    pause 1
    show bg salaquadro3 with dissolve
    n "Cartões de dores e ganhos agora formam três grandes colunas no quadro."
    play sound "ui.ogg"
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Problema 1: portal sobrecarregado por processo de PDF de cada matrícula."
    play sound "ui.ogg"
    hide douglas
    show maxx at center:
        zoom 0.4
    m "Problema 2: mensagens dispersas — e-mail oficial, X, Instagram, grupo de Telegram."
    play sound "ui.ogg"
    hide maxx
    show gio at center:
        zoom 0.34
    gi "Problema 3: nenhum cronograma público; boatos preenchem o vácuo."
    play sound "ui.ogg"
    hide gio
    show lauracontraposto at left:
                zoom 0.6
                ypos 1400
    l "Precisamos de uma pergunta ‘How Might We’ que una as três dores."
    play sound "ui.ogg"
    hide lauracontraposto

    menu:
        n "Qual enunciado representa melhor o problema?"

        "Como aumentar o limite do sistema do servidor?":
            play sound "menu.ogg"
            $ choices_log.append(("menu12", "Clicou Como aumentar o limite do sistema do servidor?", renpy.get_game_runtime()))
            show maxx at center:
                zoom 0.4
            n "Max balança a cabeça."
            play sound "ui.ogg"
            m "Escalar hardware sem repensar processo repete o erro do SISU: \
                em 48 h a quantidade de pessoas na fila derruba o sistema."
            play sound "ui.ogg"
            stop music fadeout 1
            hide maxx

        "Como garantir um único fluxo de informações claras e em tempo real sobre matrícula?":
            play sound "correct.ogg"
            $ choices_log.append(("menu12", "Clicou Como garantir um único fluxo de informações claras e em tempo real sobre matrícula?", renpy.get_game_runtime()))
            n "A equipe concorda em uníssono."
            play sound "ui.ogg"
            show douglas at center:
                zoom 0.5
                ypos 1300
            doug "Amarra performance (status ao vivo) + canal único + cronograma público."
            play sound "ui.ogg"
            hide douglas
            show gio at center:
                zoom 0.34
            gi "Perfeito — esse 'How Might We' resolve causa, não sintoma."
            play sound "ui.ogg"
            hide gio
            stop music fadeout 1
            jump brainstorm_solemar

        "Como lançar uma campanha divertida para distrair os alunos até o portal voltar?":
            play sound "menu.ogg"
            $ choices_log.append(("menu12", "Clicou Como lançar uma campanha divertida para distrair os alunos até o portal voltar?", renpy.get_game_runtime()))
            show gio at center:
                zoom 0.34
            gi "Isso só atraza a bomba. Precisamos transparência, não fumaça de marketing."
            play sound "ui.ogg"
            stop music fadeout 1
            hide gio

        "Como terceirizar todo o sistema para uma big tech estrangeira?":
            play sound "menu.ogg"
            $ choices_log.append(("menu12", "Clicou Como terceirizar todo o sistema para uma big tech estrangeira?", renpy.get_game_runtime()))
            show lauracontraposto at left:
                zoom 0.6
                ypos 1400
            l "Além de caríssimo, não resolve comunicação interna."
            play sound "ui.ogg"
            pov "Sem falar que os dados podem ser... roubados (crise)"
            play sound "ui.ogg"
            stop music fadeout 1
            hide lauracontraposto

    n "Tentem de novo: a pergunta precisa englobar performance, canal e cronograma."
    play sound "ui.ogg"
    jump solemar_problem

###############################################################################
# SEÇÃO 4 — BRAINSTORM_SOLEMAR  (Ideação)                                      #
# Chega aqui após “jump brainstorm_solemar”                                     #
###############################################################################

label brainstorm_solemar:

    scene black with fade
    show text "{b}Fase:{/b} Ideação" with fade
    pause 1
    scene bg quadro with fade
    play music "memorygame.ogg"
    n "Agora o time fará um Brainstorm para decidir as melhores soluções."
    play sound "ui.ogg"
    n "Nesse jogo da memória"
    play sound "ui.ogg"
    
    $ reset_memory_game_solemar() 
    call screen memory_game_solemar
    scene bg postits with dissolve
    stop music fadeout 1
    n "As ideias se acumulam nos post-its: lista de espera que não trava, \
    banner fixo no Instagram, cronograma em PDF só de leitura."
    play sound "ui.ogg"
    scene bg salaquadro
    show caio at center:
        zoom 0.6
    "{b}Aluno Caio{/b}" "Se vocês colocarem tudo num só lugar, a galera já agradece."
    play sound "ui.ogg"
    hide caio
    show r2 at center:
        zoom 0.6
        ypos 1200
    rep "E para a imprensa, um painel público com número de matrículas feitas em tempo real."
    play sound "ui.ogg"
    hide r2
    show maxx at center:
        zoom 0.4
    m "Essas ideias cobrem tudo."
    play sound "ui.ogg"
    hide maxx
    show gio at center:
        zoom 0.34
    gi "Perfeito. Bora transformar isso em algo que as pessoas possam usar."
    play sound "ui.ogg"
    n "Com as ideias escolhidas, o grupo se divide para criar rascunhos rápidos."
    play sound "ui.ogg"
    hide gio

    jump proto_solemar

###############################################################################
# SEÇÃO 5 — PROTO_SOLEMAR  (Prototipação)                                      #
# Continua direto após “jump proto_solemar”                                     #
###############################################################################

label proto_solemar:

    scene black with fade
    play music "blackscreen.ogg"
    show text "{b}Fase:{/b} Prototipagem" with fade
    pause 1
    scene bg informatica with dissolve
    n "A equipe se reúne numa pequena sala de informática, laptops abertos e café esfriando ao lado."
    play sound "ui.ogg"
    show lauracontraposto at left:
                zoom 0.6
                ypos 1400

    l "Meta do dia: rascunho funcional de cada solução digital."
    play sound "ui.ogg"
    hide lauracontraposto
    show maxx at center:
        zoom 0.4
    m "Eu fico com os textos. O painel precisa dizer tudo em vinte palavras."
    play sound "ui.ogg"
    hide maxx
    show gio at center:
        zoom 0.34

    gi "Eu crio um conjunto de ícones simples para o painel público: verde sorrindo, vermelho preocupado."
    play sound "ui.ogg"
    hide gio
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Vou substituir do sistema deles o gerador de PDF por algo mais simples."
    play sound "ui.ogg"
    hide douglas

    pov "E eu encaixo tudo num layout que qualquer pessoa entenda sem rolar a tela."
    play sound "ui.ogg"

    call screen minigame_solemar
    scene bg pcmade with dissolve
    n "Parabéns, você criou o cronograma dos alunos"
    play sound "ui.ogg"
    n "Agora eles podem acessar suas matrículas rapidamente"
    play sound "ui.ogg"

    scene bg informatica
    
    show maxx at center:
        zoom 0.4

    m "Eu escrevi os textos do painel e criei os canais oficiais, email oficial e redes sociais oficiais ."
    play sound "ui.ogg"
    hide maxx
    show gio at center:
        zoom 0.34

    gi "Montei um sistema que indica se o sistema foi atualizado ou não e que horas atualizará"
    play sound "ui.ogg"
    hide gio
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "removi o gerador de PDF e troquei por um registro leve no banco de dados"
    play sound "ui.ogg"
    hide douglas

    pov "Criei um cronograma dos alunos, avisando se estão matriculados e uma agenda pública"
    play sound "ui.ogg"
    show lauracontraposto at left:
                zoom 0.6
                ypos 1400
    l "Perfeito. Amanhã testamos com alunos, técnicos e imprensa."
    play sound "ui.ogg"
    hide lauracontraposto

    n "Eles respiram aliviados."
    play sound "ui.ogg"

    jump teste_solemar

###############################################################################
# SEÇÃO 6 — TESTE_SOLEMAR  (Validação)                                         #
# Chega aqui após “jump teste_solemar”                                         #
###############################################################################

label teste_solemar:

    scene black with fade
    stop music fadeout 1
    show text "{b}Fase:{/b} Testagem" with fade
    pause 1
    scene bg auditorioescola with dissolve
    pause 1
    scene bg auditorioescola2 with dissolve
    n "Dia seguinte, 10h00. Auditório da universidade, cadeiras ocupadas por alunos, técnicos e dois repórteres."
    play sound "ui.ogg"
    show lauracontraposto at left:
                zoom 0.6
                ypos 1400
    l "Obrigado por virem. Vamos mostrar três telas e ouvir a opinião de vocês."
    play sound "ui.ogg"
    hide lauracontraposto
    # — Teste do Painel de Status —
    scene bg novosistema at pan_left_slow:
        zoom 1.3
    n "A imagem projeta a nova cara do sistema."
    play sound "ui.ogg"
    show balao at right:
        zoom 0.7
        ypos 700
    "{b}Aluno 1{/b}" "Gostei, dá pra ver que tá funcionando agora, né?"
    hide balao
    play sound "ui.ogg"
    show balao at left:
        zoom 0.4
        ypos 700
        xzoom -1
    scene bg instavel

    "{b}Profissional de TI{/b}" "Quando ficar vermelho é porque caiu?"
    
    hide balao
    play sound "ui.ogg"
    scene bg  novosistema with dissolve
    pov "Isso mesmo. Amarelo = até cinco minutos de espera para entrar. Vermelho = sistema caiu e está desatualizado."
    play sound "ui.ogg"
    scene bg novosistema with dissolve:
        matrixcolor SaturationMatrix(0)
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Exato. Mas lembrando: nós já trocamos o gerador de PDF; o indicador serve só pra mostrar a saúde do sistema em tempo real."
    play sound "ui.ogg"
    hide douglas

    # — Teste do Aviso Único —
    scene bg indicadores
    n "A segunda tela mostra o mesmo aviso repostado nas redes sociais, email oficial e no site."
    play sound "ui.ogg"
    show r2 at center:
        zoom 0.6
        ypos 1200
    rep "Ótimo. Agora não tem uma informação diferente em cada plataforma. A informação vem de um canal oficial"
    play sound "ui.ogg"
    hide r2
    show balao at left:
        zoom 0.4
        ypos 800
        xpos 300
    "{b}Aluno 2{/b}" "Só publiquem rápido. Ontem demorou horas pra gente saber de algo."
    play sound "ui.ogg"

    # — Teste do Calendário Público —
    scene bg aud3
    n "Na terceira tela aparece um calendário colorido com as datas importantes."
    play sound "ui.ogg"
    show pr at center:
        zoom 0.6
        ypos 1200
    prof "Ajustes no dia 18, confirmação final no dia 22. Bem claro."
    play sound "ui.ogg"
    hide pr
    show balao at right:
        zoom 0.7
        ypos 700
    "{b}Aluno 3{/b}" "Coloquem um lembrete que sincronize com o celular. A gente vive de notificação."
    play sound "ui.ogg"
    hide balao
    # — Coleta de feedback —
    show lauracontraposto at left:
        zoom 0.6
        ypos 1400
    l "Respondam rápido: deu pra entender tudo? ‘Sim’ ou ‘Não’."
    play sound "ui.ogg"
    hide lauracontraposto
    scene bg simnao with dissolve
    n "Dois minutos depois, Laura lê o resultado."
    play sound "ui.ogg"

    show lauracontraposto at left:
        zoom 0.6
        ypos 1400
    l "54 de 66 marcaram ‘Sim’. Nota média: 8."
    play sound "ui.ogg"
    hide lauracontraposto
    show r1 at center:
        zoom 0.6
        ypos 1200
    rep "Com esse índice, a matéria de amanhã vai ser bem mais positiva."
    play sound "ui.ogg"
    hide r1
    show ti at center:
        zoom 0.6
    "{b}Profissional de TI{/b}" "Se colocarmos no ar ainda hoje, o portal já deve receber metade das ligações de reclamação."
    play sound "ui.ogg"
    hide ti

    # — Encerramento —
    show maxx at center:
        zoom 0.4
    m "Missão quase cumprida. Falta só colocar no ar e divulgar o link."
    play sound "ui.ogg"
    hide maxx
    show gio at center:
        zoom 0.34

    gi "E um lembrete automático para o celular, como o aluno pediu."
    play sound "ui.ogg"

    n "A equipe troca olhares de satisfação. Problema de matrícula encaminhado, mas ainda existe um problema a ser resolvido."
    play sound "ui.ogg"
    hide gio
    if origem_cabo:
        jump hack_servidor        # próxima cena onde surge o tráfego suspeito
    else:
        jump ending






###############################################################################
# SEÇÃO 7 — HACK_SERVIDOR  (Descoberta do tráfego suspeito)                    #
# Chega aqui após “jump hack_servidor” da seção de Teste                       #
###############################################################################

label hack_servidor:
    scene bg informatica with dissolve
    play music "sus.ogg"
    n "No fim da tarde, a maioria já foi embora. Mas o Doug? Doug ainda está lá, com os olhos vidrados na tela daquele servidor antigo de matrícula."
    play sound "ui.ogg"
    scene bg vidrado with dissolve
    doug "Que esquisito… o sistema nem carregou, e já tem um monte de arquivos saindo daqui para um lugar que não deveria."
    play sound "ui.ogg"

    pov "Que lugar?"
    play sound "ui.ogg"
    doug "Para um site chamado {i}‘guava-relay.com’{/i}. Isso não faz o menor sentido, esse endereço nunca deveria se comunicar com a universidade."
    play sound "ui.ogg"
    n "Você se lembra na hora do {b}cabo SALO, que também tinha conexão com a Guava{/b}."
    play sound "ui.ogg"
    doug "Olha só isso! A pasta de destino se chama {b}‘/bastos_docs’{/b}."
    play sound "ui.ogg"
    hide douglas

    pov "Não é coincidência. Consegue salvar uma cópia desse log em um pendrive?"
    play sound "ui.ogg"
    doug "Já estou baixando. Dois minutos."
    play sound "ui.ogg"
    pov "Vou ligar para o advogado, isso é um achado interessante!"
    # ─── NOTIFICAÇÃO DO ADVOGADO ──────────────────────────────────────────
    scene bg advcelular
    #show adv at center:
    #        zoom 0.6
    #        ypos 1500
    adv "(na chamada de voz) Estou na delegacia. Alguma novidade?"
    play sound "ui.ogg"
    scene black
    pause 0.1
    scene bg vidrado
    pov "Acabamos de descobrir que tem dados saindo do portal antigo de alunos para um tal de Guava"
    pov "A pasta se chama {b}‘bastos_docs’{/b}."
    play sound "ui.ogg"
    scene black
    pause 0.1
    scene bg advcelular
    adv "Isso liga o diretor diretamente ao vazamento!"
    adv "Se você tiver esses registros, salve agora mesmo e me mande só por pen drive, nada de e-mail."
    play sound "ui.ogg"

    # ─── ESCOLHA CRUCIAL ─────────────────────────────────────────────────
    menu:
        n "{b}O que você faz?{/b}"

        "Gravar o registro e entregar ao advogado pessoalmente":
            play sound "correct.ogg"
            $ choices_log.append(("menu13", "Clicou Gravar o registro e entregar ao advogado pessoalmente", renpy.get_game_runtime()))
            $ prova_bastos = True
            scene bg vidrado
            pov "Doug, copia pro pen-drive e me encontra na portaria em cinco minutos."
            play sound "ui.ogg"
            doug "Feito. Arquivo seguro."
            play sound "ui.ogg"
            scene bg advcelular 
            adv "Perfeito."
            stop music fadeout 1
            play sound "ui.ogg"

        "Avisar Bastos antes, pedindo explicação":
            play sound "menu.ogg"
            $ choices_log.append(("menu13", "Clicou Avisar Bastos antes, pedindo explicação", renpy.get_game_runtime()))
            $ prova_bastos = False
            $ denunciar_pf = True
            scene bg informatica
            pov "Vou ligar para o diretor e ver o que ele diz."
            play sound "ui.ogg"
            show douglas at center:
                zoom 0.5
                ypos 1300
            doug "Você tem certeza?"
            play sound "ui.ogg"
            hide douglas
            scene bg bastoscelular
            n "Bastos atende em viva-voz. Ao saber do log, pede que tudo seja ‘tratado internamente’ até amanhã."
            play sound "ui.ogg"

            n "Na manhã seguinte, você é convocado à sede da Polícia Federal para esclarecer o acesso ao servidor."
            play sound "ui.ogg"
            stop music fadeout 1

            jump confronto_final


        "Apagar o registro; é melhor não se meter":
            play sound "menu.ogg"
            $ choices_log.append(("menu13", "Clicou Apagar o registro; é melhor não se meter", renpy.get_game_runtime()))
            $ prova_bastos = False
            scene bg advcelular
            pov "Não quero virar alvo. Delete tudo e finge que não viu."
            play sound "ui.ogg"
            scene bg vidrado
            doug "Seu call…"
            play sound "ui.ogg"
            hide douglas
            n "O arquivo some da tela. Mas a sensação de perigo permanece."
            play sound "ui.ogg"
            stop music fadeout 1
    scene bg solemar externo_noite
    n "{b}Universidade Solemar{/b}\n{b}19h10.{/b}"
    n"Lá fora, o campus escurece. Dentro da sala, a história tomou um rumo que não dá para desfazer."
    play sound "ui.ogg"

    jump confronto_final

label ending:
    scene bg saladiretor2:
            zoom 1.4
    show bastos at center:
        zoom 0.6
    b "Bom trabalho em Solemar, equipe. A crise acabou sem manchetes negativas."
    play sound "ui.ogg"
    pov "Foi um prazer senhor Bastos"
    n "Você sente o celular vibrando no seu bolso e atende"
    scene bg advcelular
    adv "Alô [povname], tudo bem? Depois de muita busca, não encontramos mais dados sobre o caso..."
    play sound "ui.ogg"
    adv "Você terá que participar do julgamento mês que vem, darei meu melhor para te representar."
    jump epilogo_cinza



###############################################################################
# SEÇÃO 8 — CONFRONTO_FINAL                                                    #
# Continua a partir de “jump confronto_final” da seção Hack_Servidor           #
###############################################################################

label confronto_final:

    # 1 — CHEGADA À SEDE DA BRComorg NA MANHÃ SEGUINTE
    scene bg bastospego
    n "Manhã seguinte, 07h55. Sala dos diretores. Bastos folheia papéis. Almeida parece tenso."
    play sound "ui.ogg"
    scene bg almeida_serio at pan_right_slow:
        zoom 1.1
    pause 2

    # 2 — CENÁRIOS DEPENDENDO DA PROVA
    if prova_bastos and origem_cabo:
        scene bg pendrive
        play music "end.ogg" fadein 1
        pov "Diretor Bastos, chegou a hora de explicar isto."
        play sound "ui.ogg"    # (apenas referência a ação)
        scene bg saladiretor2:
            zoom 1.4
        show bastos at center:
            zoom 0.6
        b "Que pen-drive é esse?"
        play sound "ui.ogg"
        hide bastos
        show adv at right:
            zoom 0.6
            ypos 1500
        adv "Cópia forense de um registro que envia documentos da Solemar para um servidor Guava \
            numa pasta chamada ‘bastos_docs’."
        adv "o que indica sua relação com o vazamento de dados"
        play sound "ui.ogg"
        hide adv
        show bastos at center:
            zoom 0.6
        b "Isso é ridículo! Deve ser montagem."
        play sound "ui.ogg"
        hide bastos 
        scene bg entrance
        show delegado serio at left:
                zoom 0.5
                ypos 1300
        d "Polícia Federal. Temos mandado para apreender dispositivos do diretor."
        hide delegado
        play sound "ui.ogg"
        hide douglas
        scene bg saladiretor2:
            zoom 1.4
        show bastosaterrorizado at center:
            zoom 0.6
        n "Agentes entram. Bastos tenta falar, mas Almeida ergue a mão pedindo silêncio."
        play sound "ui.ogg"
        scene bg bastospreso
        b "Você armou pra mim, [povname]!"
        play sound "ui.ogg"
        pov "Não precisei armar nada, diretor. Os dados falaram."
        play sound "ui.ogg"
        scene bg almeida_tranquilo
        n "Enquanto Bastos é conduzido, Almeida suspira aliviado. O caso do vazamento finalmente ganha um rosto."
        play sound "ui.ogg"

        # Epílogo Herói
        jump epilogo_heroi

    elif denunciar_pf:

        
        scene black with fade
        scene bg delegacia with dissolve
        n "Delegacia da Polícia Federal, 08h12."
        scene bg policias with fade
        n "Sala fria, mesa metálica. Dois agentes sentam-se à sua frente."
        play sound "ui.ogg"
        scene bg policias2
        v "Você teve acesso direto ao servidor de matrícula?"
        play sound "ui.ogg"
        scene policias
        pov "Sim. Descobrimos um tráfego estranho ligado à Guava."
        play sound "ui.ogg"
        scene policias2
        d "E por que não registrou o registro oficialmente no mesmo momento?"
        play sound "ui.ogg"
        scene policias
        pov "Achei melhor conversar com o diretor antes..."
        play sound "ui.ogg"
        scene policias2
        v "Essa decisão comprometeu a investigação. O único registro possível foi sobrescrito no backup noturno."
        play sound "ui.ogg"
        d "Sr. [povname], há indícios de que o vazamento partiu da sua máquina. E nenhuma prova formal de que tentou denunciá-lo."
        play sound "ui.ogg"

        pov "Isso não faz sentido! Eu queria proteger—"
        play sound "ui.ogg"

        d "—Infelizmente, as provas apontam para sua omissão. Está detido para investigação."
        play sound "ui.ogg"
        scene bg policias3
        show fx at saltitar:
            zoom 1.7
            xpos -150
        n "Enquanto algemas se fecham em seus pulsos, você repensa 'o que fiz de errado?'."
        play sound "ui.ogg"
        scene black with fade
        pov "(pensando) A verdade é frágil quando não se registra no tempo certo."
        play sound "ui.ogg"

        # Epílogo Cinza
        jump epilogo_cinza

    else:
        scene bg saladiretor2:
            zoom 1.4
        show bastos at center:
            zoom 0.6
        b "Bom trabalho em Solemar, equipe. A crise acabou sem manchetes negativas."
        play sound "ui.ogg"
        
        pov "(engolindo seco) Sim, senhor."
        play sound "ui.ogg"
        show bastos sorri at center:
            zoom 0.6
        n "Você sente o peso de suas escolhas. Bastos oferece um sorriso raro."
        play sound "ui.ogg"

        b "Pessoas leais crescem rápido por aqui. Vamos conversar sobre uma promoção."
        play sound "ui.ogg"

        # Epílogo Corrupto
        jump epilogo_corrupto

###############################################################################
# SEÇÃO 9 — EPÍLOGOS                                                           #
# Chamado a partir do label “confronto_final”                                  #
###############################################################################

# ─────────────────────────────────────────────────────────────────────────────
label epilogo_heroi:
    scene bg jornal at pan_left_slow:
        zoom 1.2
    n "Uma semana depois, manchetes estampam todos os portais: \
    ‘Diretor da BRComorg preso por venda de dados a gigante tech’."
    play sound "ui.ogg"
    scene bg recepcao_2andar
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Com a apreensão do registro e do cabo, fechamos o inquérito. \
    Obrigado pela colaboração, [povname]."
    play sound "ui.ogg"
    hide douglas
    show adv at center:
            zoom 0.6
            ypos 1500
    adv "Seu nome foi retirado do processo. Eu cuido do resto."
    play sound "ui.ogg"
    hide adv
    scene bg clap at pan_left_slow with dissolve:
        zoom 1.2
    play sound "claps.ogg" fadein 1
    n "No corredor, colegas de trabalho reconhecem você e batem palmas."
    play sound "ui.ogg"
    stop music fadeout 1
    n "Fim."
    play sound "ui.ogg"
    # --- Ponto de Envio dos Dados ---
    # Quando você quiser enviar os dados para a planilha
    $ final_choices_string = _log_to_string() # Obtém a string formatada do log

    # Cria o dicionário com os dados a serem enviados.
    # As CHAVES (playerName, choicesLog) aqui devem corresponder ao que você espera no Apps Script.
    $ data_to_send = {
        "playerName": povname,
        "choicesLog": final_choices_string
    }

    # Chama a função JavaScript para enviar os dados
    $ send_to_sheet(data_to_send)
    pause 2

    return



# ─────────────────────────────────────────────────────────────────────────────

## Epílogo: Cinzas
label epilogo_cinza:
    scene bg prisao1 with fade
    play music "greyend.ogg"
    n "Três meses se passaram. O caso 'Guava' ainda assombra os noticiários, mas, sem provas definitivas, o Ministério Público não apresentou denúncia."
    play sound "ui.ogg"
    scene bg prisao2 with dissolve
    n "Ainda assim, o juiz te considerou culpado e você foi preso."
    n "Na prisão, você recebe uma carta anônima com uma única frase: 'Há mais cabos soltos por aí. Vai ignorá-los de novo?'"
    play sound "ui.ogg"


    pov "*suspira* A linha é tênue entre cautela e covardia."
    play sound "ui.ogg"
    scene black with fade
    show text "Fim...?"
    play sound "ui.ogg"
    # --- Ponto de Envio dos Dados ---
    # Quando você quiser enviar os dados para a planilha
    $ final_choices_string = _log_to_string() # Obtém a string formatada do log

    # Cria o dicionário com os dados a serem enviados.
    # As CHAVES (playerName, choicesLog) aqui devem corresponder ao que você espera no Apps Script.
    $ data_to_send = {
        "Nome do Jogador": povname,
        "Seção": final_choices_string
    }

    # Chama a função JavaScript para enviar os dados
    $ send_to_sheet(data_to_send)
    pause 2

    return



# ─────────────────────────────────────────────────────────────────────────────
label epilogo_corrupto:
    play music "blackend.ogg"
    scene bg aeroporto with fade
    n "Dois meses após a crise, você chega ao aeroporto com passagem só de ida."
    play sound "ui.ogg"
    b "*por telefone* Transferência confirmada. \
            A Guava aprecia discrição — e paga bem por ela."
    play sound "ui.ogg"

    n "No bolso, um contrato de consultoria internacional. \
    Na tela do saguão, um breaking news: ‘Vazamento de dados de votações sigilosas é confirmado’."
    play sound "ui.ogg"

    pov "*sorri* Nada pessoal, é só o meu trabalho."
    play sound "ui.ogg"
    scene black with dissolve
    show text "Fim"
    
    # --- Ponto de Envio dos Dados ---
    # Quando você quiser enviar os dados para a planilha
    $ final_choices_string = _log_to_string() # Obtém a string formatada do log

    # Cria o dicionário com os dados a serem enviados.
    # As CHAVES (playerName, choicesLog) aqui devem corresponder ao que você espera no Apps Script.
    $ data_to_send = {
        "Nome do Jogador": povname,
        "Seção": final_choices_string
    }

    # Chama a função JavaScript para enviar os dados
    $ send_to_sheet(data_to_send)

    pause 2
    return
