#Missão3

default origem_cabo       = False   # laudo reconhecido
default suspeita_guava    = False   # jogador percebe implicação maior
default denunciar_pf      = False   # decidiu avisar a PF imediatamente


###Characters
image reporter = "solemar/reporter.png"
image caio = "solemar/caio 1.png"
image caio bravo = "solemar/caio 2bravo.png"
image bastos sorri = "solemar/levesorrizo.png"

### BACKGROUNDS
image bg solemar externo = "solemar/Universidade Solemar Externo.png"
image bg solemar externo_manifestacao = "solemar/manifestacao.png"
image bg solemar externo_noite = "solemar/campusnoite.png"
image bg solemar sala = "solemar/salaaula.png"
image bg salaquadro = "solemar/salaquadro.png"
image bg salaquadro2 = "solemar/salaquadro2.png"
image bg salaquadro3 = "solemar/salaquadro3.png"
image bg informatica = "solemar/informatica.png"
image bg auditorio = "solemar/auditorio.png"
image bg auditorio2 = "solemar/auditorio2.png"
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


###############################################
# LABEL – BRIEFING COM DIRETORIA E ADVOGADO   #
###############################################
###############################################
# LABEL – BRIEFING ENTRE PROTAGONISTA & ADV.  #
###############################################
if cabo_entregue = True:
    label briefing_cabo_guava:

        scene black with fade
        n "{b}Sala de reuniões{/b}\n{b}07h45{/b}"

        # --- AMBIENTE -----------------------------------------------------------

        show adv at center:
            zoom 0.6
            ypos 1500
        adv "{b}Bom dia, [povname].{/b} Tenho algo que muda o tabuleiro."
        adv "O laboratório concluiu a análise do {i}cabo SALO{/i} que você encontrou."

        # --- REVELAÇÃO ----------------------------------------------------------
        adv "Esse cabo é fabricado {b}exclusivamente{/b} pela {b}Guava{/b}."
        adv "— sim, {i}a{/i} Guava que todo mundo usa."

        $ origem_cabo = True               # flag global

        pov "Guava faz cabos de rede também? Achei que eles só vendessem eletrônicos de consumo..."
        
        adv "Justamente. Cabos com esse sistema são raríssimos fora de laboratórios de segurança."

        # --- DECISÃO DO PROTAGONISTA ------------------------------------------
        menu:
            n "{b}Próximo passo?{/b}"

            "Protocolar o laudo hoje mesmo na Polícia Federal":
                $ denunciar_pf = True
                pov "Quero isso registrado na cadeia de custódia oficial antes que alguém sumam com a prova."
                show adv at center:
                    zoom 0.6
                    ypos 1500
                adv "Perfeito. Faço o ofício para o Delegado Silva agora de manhã."
                $ kpi += 5

            "Checar antes se existe nota fiscal ou ordem de compra interna":
                $ suspeita_guava = True
                pov "Melhor ver se esse lote aparece em algum pedido legítimo da BRComorg."
                show adv at center:
                    zoom 0.6
                    ypos 1500
                adv "Solicitarei acesso ao ERP e às declarações de importação. Se não houver registro, o buraco é mais fundo."
                $ kpi += 3

            "Guardar o laudo e capturar mais tráfego de rede Guava primeiro":
                pov "Quero mais pacotes que provem a assinatura da Guava antes de expor isso."
                show adv at center:
                    zoom 0.6
                    ypos 1500
                adv "Concordo. Posso instalar um sniffer nos switches durante a madrugada para rastrear MAC-prefixos da Guava."
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

    scene black with fade
    pause 1
    scene bg solemar externo with dissolve
    n "{b}Universidade Solemar – Portão Principal{/b}\n{b}08h52{/b}"
    scene bg solemar externo_manifestacao with dissolve
    n "O campus fervilha. Centenas de estudantes entoam gritos de protesto:\n ‘Portal fora do ar, queremos estudar!’"
    scene bg solemar externo_manifestacao:
        matrixcolor SaturationMatrix(0)
    show reporter zorder 10
    # Repórter da TV local
    show caio at center:
        zoom 0.6
    # Líder estudantil

    "{b}Caio Mendes – DCE{/b}" "Sem transparência, sem aula! Portal bugado e boato de corte de vagas!"
    # equipe chega
    show laura_cochichando at left:
        xzoom -1
    l "{i}(sussurra){/i} Situação sensível… Precisamos decidir como avançar."
    hide laura_cochichando
    # --- MENU DE ABORDAGEM ---------------------------------------------------
    menu:
        n "{b}Seu primeiro movimento?{/b}"

        "Dialogar com o aluno Caio para entender a dor":
            $ solemar_abordagem = "dce_"
            $ alterar_kpi(8)
            pov "O que está acontecendo aqui?"
            show caio at center:
                zoom 0.6

            "{b}Aluno Caio{/b}" "A galera não consegue confirmar disciplinas, e a reitoria não posta um único aviso claro."
            show lauracontraposto at left:
                zoom 0.6
                ypos 1400
            l "Prometo que traremos respostas hoje. Mas precisamos de detalhes."
            hide lauracontraposto
            
        "Dar entrevista imediata à imprensa para acalmar o público":
            $ solemar_abordagem = "imprensa"
            $ alterar_kpi(3)
            pov "Se não controlarmos a narrativa, a crise explode."
            show reporter
            "{b}Reporter{/b}" "Qual a falha real do portal? A universidade fala em ‘picos de acesso’."
            pov "Estamos levantando informação técnica agora, mas garantimos canal único de atualizações\
                 a cada 2 horas — transparência total."
            n "O repórter agradece, mas alunos atrás de você continuam gritando."
            hide reporter

        "Contornar o protesto pelos fundos do campus":
            $ solemar_abordagem = "contornar"
            $ alterar_kpi(-5)
            pov "Melhor evitar confusão. Entramos pela garagem e falamos direto com a TI."
            n "Vocês dão a volta. A mídia registra a manobra em live: ‘BRComorg fugindo do diálogo!’"

    # --- CONSEQUÊNCIA VISUAL -------------------------------------------------
    if solemar_abordagem == "dce_":
        hide lauracontraposto
        scene bg solemar externo with dissolve
        n "A tensão baixa levemente; algumas faixas de protesto são recolhidas."
    elif solemar_abordagem == "imprensa":
        scene bg solemar externo_manifestacao
        n "A imprensa se afasta satisfeita, mas o coro estudantil aumenta:\
           ‘{b}Queremos falar! Sem discurso pra TV!’"
    else:
        # contornar
        scene bg solemar externo with dissolve
        n "Vocês entram por uma porta lateral sem serem notados... por enquanto."

    # --- TRANSIÇÃO PARA FASE DE EMPATIA --------------------------------------
    n "Próximo passo: mapear as dores de alunos, TI e Pró-reitoria."
    scene black with fade
    pause 0.8
    jump audit_map          # → Seção de Empatia / Mapa de Dores

###############################################################################
# SEÇÃO 2 — AUDIT_MAP  (Empatia: levantamento de dores)                       #
# Continuação direta após “jump audit_map” da Seção 1                         #
###############################################################################

label audit_map:

    scene black with fade
    show text "{b}Fase:{/b} Empatia" with fade
    pause 1
    scene bg solemar sala with dissolve
    n "Uma sala de aula vazia foi improvisada para ouvir os envolvidos no colapso da matrícula."

    # ── Roda-rápida de entrevistas ─────────────────────────────────────────
    show caio at center:
        zoom 0.6
    "{b}Aluno Caio{/b}" "Sistema cai toda madrugada. Quem tenta logar depois das 6h perde vaga."
    hide caio
    show laura default at center:
        zoom 0.4
    l "Quantos avisos oficiais vocês receberam nesses dois dias?"
    hide laura
    show caio bravo at center:
        zoom 0.6
    "{b}Aluno Caio{/b}" "Nenhum, claro! Só prints no grupo do WhatsApp."
    hide caio
    "{b}Prof. Raquel{/b}" "O sistema antigo não suportava o novo módulo de bolsa. O pessoal da TI alertou, mas o contrato já estava assinado."
    pov "Existe cronograma público dessas etapas?"
    "{b}Prof. Raquel{/b}" "Ficou num PDF interno que nunca subiu ao site."

    "{b}Profissional de TI{/b}" "A origem do proeblema, na verdade, é o relatório em PDF que é gerado a cada confirmação. Trava o servidor por 4 s a cada aluno."
    show maxx at center:
        zoom 0.4
    m "Se tirarmos esse gerador de PDF do fluxo, o portal funciona?"
    hide maxx
    "{b}Profissional de TI{/b}" "Respira, mas fica sem informações."

    "{b}Reporter{/b}" "A reitoria manda e-mails de contas diferentes, mas alunos não reconhecem que são oficiais. Comunicação cruzada, ninguém entende nada."

    # ── Mapeamento visual (narrado) ────────────────────────────────────────
    scene bg salaquadro
    n "Anotações preenchem o quadro: ‘Falha de performance’, ‘Canal disperso’, ‘Falta de cronograma público’."
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Os três maiores probelmas são: PERFORMANCE do portal, CANAIS divergentes e FALTA de TRANSPARÊNCIA de prazos."
    hide douglas
    show bg salaquadro2 with dissolve
    show gio at center:
        zoom 0.34
    gi "Boa. Vamos transformar em pergunta ‘How Might We’ depois."

    # ── Encerramento da fase de Empatia ────────────────────────────────────
    n "Com as dores mapeadas, a equipe se prepara para convergir num problema-chave."

    jump solemar_problem

###############################################################################
# SEÇÃO 3 — SOLEMAR_PROBLEM  (Definição: escolher o 'How Might We')                       #
# Continua logo após “jump solemar_problem” da Seção 2                         #
###############################################################################

label solemar_problem:

    scene black with fade
    show text "{b}Fase:{/b} Problematização" with fade
    pause 1
    show bg salaquadro3 with dissolve
    n "Cartões de dores e ganhos agora formam três grandes colunas no quadro."
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Problema 1: portal sobrecarregado por processo de PDF de cada matrícula."
    hide douglas
    show maxx at center:
        zoom 0.4
    m "Problema 2: mensagens dispersas — e-mail oficial, X, Instagram, grupo de Telegram."
    hide maxx
    show gio at center:
        zoom 0.34
    gi "Problema 3: nenhum cronograma público; boatos preenchem o vácuo."
    hide gio
    show lauracontraposto at left:
                zoom 0.6
                ypos 1400
    l "Precisamos de uma pergunta ‘How Might We’ que una as três dores."
    hide lauracontraposto

    menu:
        n "Qual enunciado representa melhor o problema?"

        "Como garantir um único fluxo de informações claras e em tempo real sobre matrícula?":
            n "A equipe concorda em uníssono."
            show douglas at center:
                zoom 0.5
                ypos 1300
            doug "Amarra performance (status ao vivo) + canal único + cronograma público."
            hide douglas
            show gio at center:
                zoom 0.34
            gi "Perfeito — esse 'How Might We' resolve causa, não sintoma."
            hide gio
            jump brainstorm_solemar

        "Como aumentar o limite do sistema do servidor?":
            show maxx at center:
                zoom 0.4
            n "Max balança a cabeça."
            m "Escalar hardware sem repensar processo repete o erro do SISU: \
                em 48 h a quantidade de pessoas na fila derruba o sistema."
            hide maxx

        "Como lançar uma campanha divertida para distrair os alunos até o portal voltar?":
            show gio at center:
                zoom 0.34
            gi "Isso só atraza a bomba. Precisamos transparência, não fumaça de marketing."
            hide gio

        "Como terceirizar todo o sistema para uma big tech estrangeira?":
            show lauracontraposto at left:
                zoom 0.6
                ypos 1400
            l "Além de caríssimo, não resolve comunicação interna."
            pov "Sem falar que os dados podem ser... roubados (crise)"
            hide lauracontraposto

    n "Tentem de novo: a pergunta precisa englobar performance, canal e cronograma."
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
    n "Agora o time fará um Brainstorm para decidir as melhores soluções."
    n "Nesse jogo da memória"
    
    $ reset_memory_game_solemar() 
    call screen memory_game_solemar
    scene bg postits with dissolve

    n "As ideias se acumulam nos post-its: lista de espera que não trava, \
       banner fixo no Instagram, cronograma em PDF só de leitura."
    scene bg salaquadro
    show caio at center:
        zoom 0.6
    "{b}Aluno Caio{/b}" "Se vocês colocarem tudo num só lugar, a galera já agradece."
    hide caio
    "{b}Reporter{/b}" "E para a imprensa, um painel público com número de matrículas feitas em tempo real."

    show maxx at center:
        zoom 0.4
    m "Essas ideias cobrem tudo."
    hide maxx
    show gio at center:
        zoom 0.34
    gi "Perfeito. Bora transformar isso em algo que as pessoas possam usar."
    n "Com as ideias escolhidas, o grupo se divide para criar rascunhos rápidos."
    hide gio

    jump proto_solemar

###############################################################################
# SEÇÃO 5 — PROTO_SOLEMAR  (Prototipação)                                      #
# Continua direto após “jump proto_solemar”                                     #
###############################################################################

label proto_solemar:

    scene black with fade
    show text "{b}Fase:{/b} Prototipagem" with fade
    pause 1
    scene bg informatica with dissolve
    n "A equipe se reúne numa pequena sala de informática, laptops abertos e café esfriando ao lado."
    show lauracontraposto at left:
                zoom 0.6
                ypos 1400

    l "Meta do dia: rascunho funcional de cada solução digital."
    hide lauracontraposto
    show maxx at center:
        zoom 0.4
    m "Eu fico com os textos. O painel precisa dizer tudo em vinte palavras."
    hide maxx
    show gio at center:
        zoom 0.34

    gi "Eu crio um conjunto de ícones simples para o painel público: verde sorrindo, vermelho preocupado."
    hide gio
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Vou substituir do sistema deles o gerador de PDF por algo mais simples."
    hide douglas

    pov "E eu encaixo tudo num layout que qualquer pessoa entenda sem rolar a tela."

    call screen minigame_solemar
    scene bg pcmade with dissolve
    n "Parabéns, você criou o cronograma dos alunos"
    n "Agora eles podem acessar suas matrículas rapidamente"

    scene bg informatica
    
    show maxx at center:
        zoom 0.4

    m "Eu escrevi os textos do painel e criei os canais oficiais, email oficial e redes sociais oficiais ."
    hide maxx
    show gio at center:
        zoom 0.34

    gi "Montei um sistema que indica se o sistema foi atualizado ou não e que horas atualizará"
    hide gio
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "removi o gerador de PDF e troquei por um registro leve no banco de dados"
    hide douglas

    pov "Criei um cronograma dos alunos, avisando se estão matriculados e uma agenda pública"
    show lauracontraposto at left:
                zoom 0.6
                ypos 1400
    l "Perfeito. Amanhã testamos com alunos, técnicos e imprensa."
    hide lauracontraposto

    n "Eles respiram aliviados."

    jump teste_solemar

###############################################################################
# SEÇÃO 6 — TESTE_SOLEMAR  (Validação)                                         #
# Chega aqui após “jump teste_solemar”                                         #
###############################################################################

label teste_solemar:

    scene black with fade
    show text "{b}Fase:{/b} Testagem" with fade
    pause 1
    scene bg auditorio with dissolve
    n "Dia seguinte, 10h00. Auditório da universidade, cadeiras ocupadas por alunos, técnicos e dois repórteres."
    show lauracontraposto at left:
                zoom 0.6
                ypos 1400
    l "Obrigado por virem. Vamos mostrar três telas e ouvir a opinião de vocês."
    hide lauracontraposto

    # — Teste do Painel de Status —
    scene auditorio2 at pan_left_slow:
        zoom 1.2
    n "A imagem projeta a nova cara do sistema."

    "{b}Aluno 1{/b}" "Gostei, dá pra ver que tá funcionando agora, né?"

    
    "{b}Profissional de TI{/b}" "Quando ficar vermelho é porque caiu?"

    pov "Isso mesmo. Amarelo = até cinco minutos de espera para entrar. Vermelho = sistema caiu e está desatualizado."
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Exato. Mas lembrando: nós já trocamos o gerador de PDF; o indicador serve só pra mostrar a saúde do sistema em tempo real."
    hide douglas

    # — Teste do Aviso Único —
    scene auditorio:
        zoom 1.4
        xpos -300
    n "A segunda tela mostra o mesmo aviso repostado nas redes sociais, email oficial e no site."

    "rep1" "Ótimo. Agora não tem texto diferente em cada lugar."

    "{b}Aluno 2{/b}" "Só publiquem rápido. Ontem demorou horas pra gente saber de algo."

    # — Teste do Calendário Público —
    n "Na terceira tela aparece um calendário colorido com as datas importantes."

    "{b}Prof. Raquel{/b}" "Ajustes no dia 18, confirmação final no dia 22. Bem claro."

    "{b}Aluno 3{/b}" "Coloquem um lembrete que sincronize com o celular. A gente vive de notificação."

    # — Coleta de feedback —
    show lauracontraposto at left:
        zoom 0.6
        ypos 1400
    l "Respondam rápido: deu pra entender tudo? ‘Sim’ ou ‘Não’."
    hide lauracontraposto
    scene auditorio2

    n "Dois minutos depois, Laura lê o resultado."

    show lauracontraposto at left:
        zoom 0.6
        ypos 1400
    l "18 de 20 marcaram ‘Sim’. Nota média: 9."
    hide lauracontraposto

    "rep2" "Com esse índice, a matéria de amanhã vai ser bem mais positiva."

    "{b}Profissional de TI{/b}" "Se colocarmos no ar ainda hoje, o portal já deve receber metade das ligações de reclamação."

    # — Encerramento —
    show maxx at center:
        zoom 0.4
    m "Missão quase cumprida. Falta só colocar no ar e divulgar o link."
    hide maxx
    show gio at center:
        zoom 0.34

    gi "E um lembrete automático para o celular, como o aluno pediu."

    n "A equipe troca olhares de satisfação. Problema de matrícula encaminhado, mas a sombra da Guava ainda paira."
    hide gio

    jump hack_servidor        # próxima cena onde surge o tráfego suspeito

###############################################################################
# SEÇÃO 7 — HACK_SERVIDOR  (Descoberta do tráfego suspeito)                    #
# Chega aqui após “jump hack_servidor” da seção de Teste                       #
###############################################################################

label hack_servidor:
    scene bg informatica with dissolve
    n "No fim da tarde, a maioria já foi embora. Doug ainda digita, olhos fixos na tela do antigo servidor de matrícula."
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Estranho… o painel nem subiu e já tem um fluxo de arquivos saindo para um endereço externo."
    hide douglas

    pov "Endereço de quem?"
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Domínio ‘guava-relay.com’. Nunca deveria falar com a universidade."
    hide douglas

    n "Você lembra do laudo do cabo SALO, também ligado à Guava."
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Olha isso. O nome do subdiretório é ‘/bastos_docs’."
    hide douglas

    pov "Não é coincidência. Consegue salvar uma cópia desse log?"
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Já estou baixando. Dois minutos."
    hide douglas

    # ─── NOTIFICAÇÃO DO ADVOGADO ──────────────────────────────────────────
    scene bg advcelular
    #show adv at center:
    #        zoom 0.6
    #        ypos 1500
    adv "(na chamada de voz) Estou na delegacia. Alguma novidade sobre Guava?"
    scene black
    pause 0.1
    scene bg informatica
    show douglas at center:
                zoom 0.5
                ypos 1300
    pov "Acabamos de achar tráfego saindo do portal para um relay Guava, pasta chamada ‘bastos_docs’."
    scene black
    pause 0.1
    scene bg advcelular
    adv "Isso liga o diretor diretamente ao vazamento. Se tiver log, guarde na hora \
         e mande só por pen-drive, nada de e-mail."

    # ─── ESCOLHA CRUCIAL ─────────────────────────────────────────────────
    menu:
        n "{b}O que você faz?{/b}"

        "Gravar o log e entregar ao advogado pessoalmente":
            $ prova_bastos = True
            scene bg informatica
            pov "Doug, copia pro pen-drive e me encontra na portaria em cinco."
            show douglas at center:
                zoom 0.5
                ypos 1300
            doug "Feito. Arquivo seguro."
            hide douglas
            adv "Perfeito. Cadeia de custódia intacta."

        "Avisar Bastos antes, pedindo explicação":
            $ prova_bastos = False
            $ denunciar_pf = True
            scene bg informatica
            pov "Vou ligar para o diretor e ver o que ele diz."
            show douglas at center:
                zoom 0.5
                ypos 1300
            doug "Você tem certeza?"
            hide douglas
            n "Bastos atende em viva-voz. Ao saber do log, pede que tudo seja ‘tratado internamente’ até amanhã."

            n "Na manhã seguinte, você é convocado à sede da Polícia Federal para esclarecer o acesso ao servidor."

            jump confronto_final


        "Apagar o log; é melhor não se meter":
            $ prova_bastos = False
            scene bg informatica
            pov "Não quero virar alvo. Delete tudo e finge que não viu."
            show douglas at center:
                zoom 0.5
                ypos 1300
            doug "Seu call…"
            hide douglas
            n "O arquivo some da tela. Mas a sensação de perigo permanece."
    scene bg solemar externo_noite
    n "O relógio marca 19h10. Lá fora, o campus escurece. Dentro da sala, a história tomou um rumo que não dá para desfazer."

    jump confronto_final

###############################################################################
# SEÇÃO 8 — CONFRONTO_FINAL                                                    #
# Continua a partir de “jump confronto_final” da seção Hack_Servidor           #
###############################################################################

label confronto_final:

    # 1 — CHEGADA À SEDE DA BRComorg NA MANHÃ SEGUINTE
    scene bg bastospego
    n "Manhã seguinte, 07h55. Sala dos diretores. Bastos folheia papéis. Almeida parece tenso."
    scene bg almeida_serio

    # 2 — CENÁRIOS DEPENDENDO DA PROVA
    if prova_bastos:

        pov "Diretor Bastos, chegou a hora de explicar isto."
        show pen_drive in hand    # (apenas referência a ação)
        scene bg saladiretor2:
            zoom 1.4
        show bastos at center:
            zoom 0.6
        b "Que pen-drive é esse?"
        hide bastos
        show adv at center:
            zoom 0.6
            ypos 1500
        adv "Cópia forense de um log que envia documentos da Solemar para um servidor Guava \
              num diretório chamado ‘bastos_docs’."
        hide adv
        show bastos at center:
            zoom 0.6
        b "Isso é ridículo! Deve ser montagem."
        hide bastos 
        show douglas at center:
                zoom 0.5
                ypos 1300
        doug "Polícia Federal. Temos mandado para apreender dispositivos do diretor."
        hide douglas
        show bastosaterrorizado at center:
            zoom 0.6
        n "Agentes entram. Bastos tenta falar, mas Almeida ergue a mão pedindo silêncio."
        scene bg bastospreso
        b "Você armou pra mim, [povname]!"
        pov "Não precisei armar nada, diretor. Os dados falaram."
        scene bg almeida_tranquilo
        n "Enquanto Bastos é conduzido, Almeida suspira aliviado. O caso do vazamento finalmente ganha um rosto."

        # Epílogo Herói
        jump epilogo_heroi

    elif denunciar_pf:

        
        scene black with fade
        n "Delegacia da Polícia Federal, 08h12. Sala fria, mesa metálica. Dois agentes sentam-se à sua frente."

        "{b}Policial 1{/b}" "Você teve acesso direto ao servidor de matrícula?"
        pov "Sim. Descobrimos um tráfego estranho ligado à Guava."

        "{b}Policial 2{/b}" "E por que não registrou o log oficialmente no mesmo momento?"
        pov "Achei melhor conversar com o diretor antes..."

        "{b}Policial 1{/b}" "Essa decisão comprometeu a cadeia de custódia. O único log possível foi sobrescrito no backup noturno."

        n "A porta se abre. O delegado entra com expressão grave."

        d "Sr. [povname], há indícios de que o vazamento partiu da sua máquina. E nenhuma prova formal de que tentou denunciá-lo."

        pov "Isso não faz sentido! Eu queria proteger—"

        d "—Infelizmente, as provas apontam para sua omissão. Está detido para investigação."

        n "Enquanto algemas se fecham em seus pulsos, você vê pela janela o campus da Solemar ao longe."

        pov "(pensando) A verdade é frágil quando não se registra no tempo certo."

        # Epílogo Cinza
        jump epilogo_cinza

    else:
        scene bg saladiretor2:
            zoom 1.4
        show bastos at center:
            zoom 0.6
        b "Bom trabalho em Solemar, equipe. A crise acabou sem manchetes negativas."
        
        pov "(engolindo seco) Sim, senhor."
        show bastos sorri at center:
            zoom 0.6
        n "Você sente o peso do arquivo deletado. Bastos oferece um sorriso raro."

        b "Pessoas leais crescem rápido por aqui. Vamos conversar sobre uma promoção."

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
    scene bg recepcao_2andar
    show douglas at center:
                zoom 0.5
                ypos 1300
    doug "Com a apreensão do log e do cabo, fechamos o inquérito. \
       Obrigado pela colaboração, [povname]."
    hide douglas
    show adv at center:
            zoom 0.6
            ypos 1500
    adv "Seu nome foi retirado do processo. E a Solemar já colocou o painel no ar, \
         98 porcento de acesso sem queda."
    hide adv

    n "No corredor, colegas de trabalho reconhecem você e batem palmas discretas."

    pov "(pensando) Ética dá trabalho, mas dorme melhor."

    n "Fim."
    pause 2

    return



# ─────────────────────────────────────────────────────────────────────────────
label epilogo_cinza:
    scene bg prisao1 with fade
    n "Três meses se passam. O caso Guava ainda ronda os noticiários, \
       mas sem provas definitivas o Ministério Público não apresenta denúncia."
    scene bg prisao2 with dissolve
    n "Você recebe uma carta anônima: \
       ‘Há mais cabos espalhados. Vai ignorar de novo?’"

    pov "(suspiro) A linha é tênue entre cautela e covardia."
    scene black with fade
    show text "Fim...?"
    pause 2

    return



# ─────────────────────────────────────────────────────────────────────────────
label epilogo_corrupto:
    scene bg aeroporto with fade
    n "Dois meses após a crise, você chega ao aeroporto com passagem só de ida."
    b "(por telefone) Transferência confirmada. \
            A Guava aprecia discrição — e paga bem por ela."

    n "No bolso, um contrato de consultoria internacional. \
       Na tela do saguão, um breaking news: ‘Vazamento de dados de votações sigilosas é confirmado’."

    pov "(sorri) Nada pessoal, é só o meu trabalho."
    scene black with dissolve
    show text "Fim"
    pause 2
    return
