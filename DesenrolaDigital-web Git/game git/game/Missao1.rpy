image paulo_triste = "Personagens/Paulo triste.png"

################################################################################
# LABEL CENA 4 – ENTRADA DA ONG PATINHAS, 10h42
################################################################################
default patinhascompleto = False
label cena4:

    # --- CONTEXTO VISUAL E TEMPORAL -------------------------------------------
    play music "1.ogg" fadein 0.5
    play sound "dog.ogg" fadein 0.5
    scene bg patinhasexterno with fade
    n "{b}Local:{/b} Entrada principal da {b}ONG Patinhas{/b}, Asa Norte – Brasília\n{b}Horário:{/b} 10h42 da manhã\n{b}Clima:{/b} Ensolarado, leve cheiro de desinfetante no ar"
    play sound "ui.ogg"

    n "Você e Laura descem do carro da BRComorg. Ao atravessar o portão lateral, percebem uma movimentação incomum."
    play sound "ui.ogg"
    # --- ENTRADA DO VOLUNTÁRIO PAULO ------------------------------------------

    scene bg patinhas_recepção with fade
    show paulo_1 at center:
        zoom 0.34
    show recepcao_patinhas zorder 10
    stop music fadeout 1
    stop sound fadeout 0.5
    n "Um jovem voluntário de uniforme veterinário escrito {i}'Voluntário'{/i} fala alto ao telefone, com expressão desesperada."
    play sound "ui.ogg"
    hide paulo_1
    show paulo_2 at center:
        zoom 0.34
    play sound "talk.ogg"
    p "Sim, senhora, eu entendo! Mas eu não tenho acesso ao calendário de ontem, e o Thor estava agendado como castrado, não como pré-cirurgia! Eu só fiz o que o sistema mostrou!"
    play sound "ui.ogg"
    hide paulo_2
    show paulo_triste at center:
        zoom 0.6
    stop sound fadeout 0.3
    play sound "phone.ogg"
    n "Ele desliga o telefone com força, respira fundo e percebe sua presença. Tenta compor o semblante, mas ainda está visivelmente abalado."
    play sound "ui.ogg"
    hide paulo_triste
    show paulo_3 at center:
        zoom 0.34
    p "Desculpa a cena… vocês são da agência, né? É que isso aqui tá insustentável. O novo sistema... ninguém sabe usar direito, e os cachorros pagam o preço."
    stop sound fadeout 0.5
    play sound "ui.ogg"
    
    show laura_cochichando zorder 11

    n "Laura olha para você discretamente..."
    play sound "ui.ogg"
    play sound "lauracochicho.ogg"
    l "*Cochicha* É melhor escutar..."
    play sound "ui.ogg"
    hide laura_cochichando
    hide paulo_3
    show p default at center:
        zoom 0.34
    p "Hoje cedo deixaram a Amora presa no canil errado. Ontem um doador veio visitar um filhote reservado… e o filhote já tinha ido pra outra casa."
    play sound "ui.ogg"
    p "Eu só tô tentando manter isso de pé…"
    play sound "ui.ogg"

        # --- ESCOLHA DIAGNÓSTICA -------------------------------------------------
    menu:

        "Consegue me explicar melhor o que está acontecendo?":
            play sound "menu.ogg"
            $ alterar_kpi(10)
            $ choices_log.append(("menu3", "Clicou Consegue me explicar melhor o que está acontecendo?", renpy.get_game_runtime()))
            jump cena4_opcao1

        "Precsamos resolver isso com um superior, Vamos direto à coordenação. Isso precisa de gente responsável agora.":
            play sound "menu.ogg"
            $ alterar_kpi(5)
            $ choices_log.append(("menu3", "Clicou Precsamos resolver isso com um superior...", renpy.get_game_runtime()))
            jump cena4_opcao2


label cena4_opcao1:
    p "{b}Claro, posso explicar melhor.{/b}"
    play sound "ui.ogg"
    hide p default
    show p habla at center:
        zoom 0.34
    p "O sistema está confuso e cheio de erros. Alguns cachorros foram agendados para cirurgias que não foram feitas."
    play sound "ui.ogg"
    hide p habla
    show p default at center:
        zoom 0.34
    p "Alguns doadores estão frustrados porque os filhotes que vieram visitar não estão mais aqui. O problema é que ninguém entende direito como operar o sistema novo."
    play sound "ui.ogg"

    l "{b}Isso é grave, Paulo.{/b} Precisamos entender exatamente onde o processo está falhando para ajudar."
    play sound "ui.ogg"
    l "Você poderia mostrar onde e como o sistema confunde mais os voluntários?"
    play sound "ui.ogg"
    p "Sim, claro! Tem umas funções que ninguém sabe usar direito, e o manual é confuso."
    play sound "ui.ogg"
    l "Ótimo, vamos anotar tudo para discutir na reunião com a diretoria."
    play sound "ui.ogg"
    n "Você e Laura anotam as dores do voluntário em uma prancheta e vão para a reunião com a diretoria" # Adicionar cena de papo e anotações em uma prancheta
    play sound "ui.ogg"
    jump reuniao1_diretora

label cena4_opcao2:
    scene bg patinhas_corredor with fade
    show p default at center:
        zoom 0.34
    play sound "dog.ogg"
    p "Talvez se vocês conversarem com a coordenação, algo mude. Mas eu estou preocupado que só vão empurrar com a barriga."
    play sound "ui.ogg"
    n "Paulo os acompanha até a {b}sala da diretoria{/b} da Ong Patinhas"
    play sound "ui.ogg"
    jump reuniao1_diretora

label reuniao1_diretora:
    scene bg patinhas_reuniao with fade
    show lise brava at center:
       zoom 0.34
    li "Vocês são da BRComorg? Precisamos de ajuda {b}urgente.{/b}"
    play sound "ui.ogg"
    li "O sistema novo está um caos. Os voluntários não conseguem usar direito, os agendamentos estão errados e os doadores estão frustrados."
    play sound "ui.ogg"
    li "Não sabemos nem por onde começar a resolver. Por isso chamei vocês."
    play sound "ui.ogg"
    hide lise brava
    show laura meiga at right with fade:
        zoom 0.42
        ypos 1200
        xpos 1500
        xzoom -1
    l "{b}Entendemos a situação, diretora.{/b} Vamos ouvir tudo para ajudar da melhor forma."
    play sound "ui.ogg"

    n "Você explica que a BRComorg possui uma metodologia incrível para lidar com problemas complexos de comunicação interna, chamada {b}Design Thinking{/b}."
    play sound "ui.ogg"
    pov "Sugiro reunir os profissionais da BRComorg para uma reunião geral, onde possamos aplicar essa abordagem para encontrar soluções colaborativas."
    play sound "ui.ogg"
    hide laura
    show lise feliz at center:
       zoom 0.5
       ypos 1200
    play sound "achievement.ogg"
    li "{b}Ótima ideia!{/b}. Quanto antes começarmos, melhor para os animais e para a equipe."
    play sound "ui.ogg"
    scene black                    # logo centralizado na tela
    with fade
    pause 1
    jump reuniao2_geral

label reuniao2_geral:
    scene bg patinhas_reuniao with fade
    play music "prereuniao.ogg" fadein 1
    n "{b}Local:{/b} Sala de Reuniões da ONG Patinhas\n{b}Horário:{/b} 11h00"
    play sound "ui.ogg"
    scene bg patinhas_reuniao2
    pause 1
    scene bg patinhas_reuniao3
    pause 1
    scene bg patinhas_reuniao4
    pause 1
    scene bg patinhas_reuniao5
    show laura feliz at left:
        zoom 0.5
        xpos 200
    n "{b}Laura\nGestora de Relacionamento{/b} \nEntra na sala com um sorriso no rosto, pronta para facilitar o diálogo."
    play sound "ui.ogg"
    scene bg patinhas_reuniao2
    pause 1
    scene bg patinhas l
    pause 1
    scene bg patinhas_reuniao4
    pause 1
    scene bg patinhas_reuniao3
    pause 1
    
    scene bg patinhas_reuniao5
    show maxx feliz at left:
        zoom 0.4
        xpos 500
    n "{b}Max{/b}\n{b}Planejamento Estratégico{/b}\nChega em seguida, carregando um sorrizo no rosto."
    play sound "ui.ogg"
    scene bg patinhas lm
    pause 0.5
    scene bg patinhas_reuniao2
    pause 0.5
    scene bg patinhas_reuniao3
    pause 0.5
    scene bg patinhas_reuniao4
    pause 0.5
    scene bg patinhas_reuniao5
    show gio feliz at left:
        zoom 0.4
        xpos 500
    n "{b}Gi{/b},\nEspecialista em Criação de Conteúdo"
    n "Surge na porta com um sorriso determinado e ideias borbulhando na mente."
    play sound "ui.ogg"
    scene bg patinhas lmg
    pause 0.2
    scene bg patinhas_reuniao2
    pause 0.2
    scene bg patinhas_reuniao3
    pause 0.2
    scene bg patinhas_reuniao4
    show douglas feliz at left:
        zoom 0.4
        xpos 500
    n "{b}Doug{/b}\n{b}Analista de Comunicação{/b}"
    n "Junta-se ao grupo, trazendo consigo gráficos que já havia preparado previamente."
    play sound "ui.ogg"
    scene bg patinhas lmgd
    n "Todos se posicionam ao redor da mesa, prontos para começar o trabalho colaborativo usando Design Thinking."
    play sound "ui.ogg"
    scene bg patinhas_reuniao4
    pause 1
    scene bg patinhas_reuniao5
    show lise at left:
        zoom 0.4
    li "{b}Bom dia a todos.{/b} Sou Lise, diretora da ONG Patinhas, e agradeço por terem vindo tão rapidamente."
    play sound "ui.ogg"
    scene bg patinhas principal
    show mesareuniaopt zorder 10
    show lise at center:
        zoom 0.4
    stop music fadeout 1
    li "Nossa comunicação está horrível. As falhas estão causando confusão nos procedimentos veterinários e gerando insatisfação nos doadores."
    play sound "ui.ogg"
    show lise triste at center:
        zoom 0.4
    li "Em apenas uma semana, houve pelo menos cinco casos de agendamentos duplicados e dois cães que ficaram retidos em canis errados por falta de atualização de dados."
    play sound "ui.ogg"
    show lise at center:
        zoom 0.4
    scene bg patinhas principal
    show mesareuniaopt zorder 10
    show lise at center:
        zoom 0.4
    li "O que devemos fazer primeiro?"
    play sound "ui.ogg"

$ escolha_correta = False
while not escolha_correta:
    menu:
        "Propor ideias de solução":
            play sound "menu.ogg"
            $ choices_log.append(("menu4", "Clicou Propor ideias de solução", renpy.get_game_runtime()))
            pov "Talvez devêssemos já começar a esboçar possíveis ajustamentos no {b}fluxo de trabalho.{/b}"
            play sound "ui.ogg"
            scene bg patinhas lmgd
            doug "{b}Discordo{/b},Sem entender profundamente o problema ou ouvir os usuários, qualquer ideia será apenas palpite, não uma solução estruturada."
            play sound "ui.ogg"
        
        "Empatizar com os voluntários e usuários do sistema":
            play sound "correct.ogg"
            $ choices_log.append(("menu4", "Clicou Empatizar com os voluntários e usuários do sistema", renpy.get_game_runtime()))
            pov "{b}Tudo bem.{/b} Vamos começar conversando diretamente com os voluntários para entender suas dificuldades."
            play sound "ui.ogg"
            scene bg patinhas lmgd
            l "{b}Concordo.{/b} Precisamos ouvir quem lida com o sistema diariamente antes de qualquer outra coisa."
            play sound "ui.ogg"
            $ escolha_correta = True

        "Definir claramente o problema":
            play sound "menu.ogg"
            $ choices_log.append(("menu4", "Clicou Definir claramente o problema", renpy.get_game_runtime()))
            pov "Podemos revisar os relatórios de agendamento e logs do sistema para {b}identificar padrões de erro.{/b}"
            play sound "ui.ogg"
            scene bg patinhas lmgd
            gi "Gente, {i}sem antes ouvir quem lida com o sistema,{/i} {b}não saberemos os problemas reais.{/b}"
            play sound "ui.ogg"

scene bg patinhas principal
show mesareuniaopt zorder 10
show lise feliz at center:
    zoom 0.6
play sound "achievement.ogg"
li "Caramba, vocês são profissionais mesmo!"

jump empatizar_patinhas

label empatizar_patinhas:
    scene black
    with fade
    play music "blackscreen.ogg"
    show text "{b}Fase:{/b} Empatia" with fade
    pause 3
    show text "{b}Objetivo:{/b} Mergulhar no universo dos usuários, entendendo suas necessidades, sentimentos e dificuldades por meio da escuta ativa e da observação atenta." with fade
    pause 9
    show text "Somente ao compreender profundamente o ponto de vista dos voluntários poderemos definir problemas reais e relevantes." with fade
    pause 9
    scene bg patinhas_recepção with fade
    show recepcao_patinhas zorder 10
    show p default at center:
        zoom 0.34
    n "Vocês chegam ao local onde Paulo, voluntário da ONG Patinhas, está organizando a entrada dos cães. Ele parece apreensivo, mas disposto a colaborar."
    play sound "ui.ogg"
    show p habla at center:
        zoom 0.34
    stop music fadeout 1
    p "{b}Vocês vieram me ouvir? Obrigado.{/b} \nTento dar meu melhor, mas este sistema me confunde demais."
    play sound "ui.ogg"
    show lauracontraposto at right zorder 11:
        zoom 0.5
        ypos 1300
        xzoom -1
    l "Paulo, estamos aqui para entender {b}como você lida com o sistema na prática{/b} e quais partes lhe causam mais dificuldade."
    play sound "ui.ogg"
    p "Às vezes, eu erro um clique e o sistema muda a data sem aviso. Fico inseguro se o agendamento foi mesmo gravado."
    play sound "ui.ogg"
    hide lauracontraposto
    show gio at left zorder 11:
        zoom 0.3
        ypos 1200
        xzoom -1
    gi "{i}Entendi. você já recebeu algum treinamento para usar essa parte do sistema?{/i} Teve algum manual ou orientação?"
    play sound "ui.ogg"
    hide gio
    p "Recebi um tutorial por e-mail, mas é muito genérico. Não mostra o passo a passo real do que precisamos no dia a dia."
    play sound "ui.ogg"
    show maxx at center zorder 11:
        zoom 0.34
    m "{i}Estou anotando que há falha de visibilidade e possível inconsistência nos dados. Tudo isso será crucial para definir o problema real.{/i}"
    play sound "ui.ogg"
    hide maxx
    show douglas at left:
        zoom 0.34
        ypos 1200
        xzoom -1
    doug "Com licença, posso {b}ver o sistema?{/b} {i}parece que tem algo errado...{/i}"
    play sound "ui.ogg"
    hide p
    show douglas at center:
        zoom 0.34
        ypos 1200
        xzoom 1
    play sound "typing.ogg"
    doug "..."
    play sound "ui.ogg"
    pause 2
    doug "Realmente, botões não respondem ao clique e informações importantes estão ocultas em menus confusos."
    play sound "ui.ogg"
    show gio at right zorder 11:
        zoom 0.3
        ypos 1200
        xzoom 1

    gi "{i}Se desenharmos uma interface mais clara e intuitiva, talvez os voluntários consigam usar o sistema sem tanta dificuldade.{/i}"
    play sound "ui.ogg"
    hide gio
    show maxx at right zorder 11:
        zoom 0.34
    m "{i}Antes de pensar na solução, precisamos definir exatamente quais partes do sistema causam esses erros e qual é o problema central.{/i}"
    play sound "ui.ogg"
    scene black with fade
    pause 1
    scene bg patinhas lmgd with fade
    n "De volta à sala de reuniões, todos se posicionam ao redor da mesa com as anotações em mãos. Lise, a diretora aguarda o relatório."
    play sound "ui.ogg"

    m "Com base nas observações, os agendamentos duplicados ocorrem porque {b} o voluntário confirma sem ver a tela de resumo, indicando que não entendeu o treinamento{/b}"
    play sound "ui.ogg"
    gi "{b}Além disso, alguns campos essenciais não estão visíveis na tela principal,{/b} o que cria confusão na hora de inserir dados."
    play sound "ui.ogg"
    doug "{b}Também há inconsistências no banco de dados:{/b} as datas e horários não são sincronizados corretamente, gerando agendamentos que não existem na realidade."
    play sound "ui.ogg"
    scene bg patinhas principal
    show mesareuniaopt zorder 10
    show lise brava at center:
        zoom 0.4
    li "{b}Gente, tudo isso?!{/b}"
    play sound "ui.ogg"
    scene bg patinhas lmgd
    
$ escolha_correta2 = False
while not escolha_correta2:
    menu:
        n "O que devemos fazer agora?"
                
        "Iniciar imediatamente a fase de ideação de soluções":
            play sound "menu.ogg"
            $ choices_log.append(("menu5", "Clicou Iniciar imediatamente a fase de ideação de soluções", renpy.get_game_runtime()))
            gi "{i}Noção precipitada: sem problema bem definido, qualquer ideia seria arbitrária e provavelmente inútil.{/i}"
            play sound "ui.ogg"
                
        "Ajuntar todas as anotações e criar um protótipo básico":
            play sound "menu.ogg"
            $ choices_log.append(("menu5", "Clicou Ajuntar todas as anotações e criar um protótipo básico", renpy.get_game_runtime()))
            doug "{i}Sem definir o problema, o protótipo não terá foco nem atenderá às necessidades reais.{/i}"
            play sound "ui.ogg"
        
        "Definir claramente o problema principal antes de criar soluções":
            play sound "correct.ogg"
            $ choices_log.append(("menu5", "Clicou Definir claramente o problema principal antes de criar soluções", renpy.get_game_runtime()))
            m "{b}Certo. Vamos formular precisamente qual é o problema central, com base nas observações coletadas.{/b}"
            play sound "ui.ogg"
            $ escolha_correta2 = True

jump problematizar_patinhas

label problematizar_patinhas:
    scene black with fade
    play music "blackscreen.ogg"
    show text "{b}Fase: {/b}Problematização" with fade 
    pause 3
    show text "{b}Objetivo: {/b}transformar as observações coletadas na etapa de empatia em um entendimento claro e conciso do problema central." with fade
    pause 6
    show text "Sem uma formulação precisa, qualquer solução proposta poderá ser desconectada das reais necessidades, gerando desperdício de tempo e recursos." with fade
    pause 6
    scene bg patinhas lmgd

$ escolha_correta3 = False
while not escolha_correta3:
    menu:
        n "Como devemos formalizar o problema?"

        "Treinamento inadequado dos voluntários":
            play sound "menu.ogg"
            $ choices_log.append(("menu6", "Clicou Treinamento inadequado dos voluntários", renpy.get_game_runtime()))
            scene bg patinhasmesatalkback
            show patinhastalkbackmesa zorder 11
            show maxx at center:
                zoom 0.4
            m "Discordo, não é exatamente isso que está acontecendo."
            stop music fadeout 1
            play sound "ui.ogg"
            m "Paulo mencionou explicitamente que recebeu um tutorial por e-mail, mas mesmo após o treinamento ele continuou confuso ao usar o sistema."
            play sound "ui.ogg"
            scene ongpatinhas_recepcao with fade:
                matrixcolor SaturationMatrix(0)
            show p habla at center:
                matrixcolor SaturationMatrix(0)
                zoom 0.34
            show recepcao_patinhas zorder 10:
                matrixcolor SaturationMatrix(0)
            p "{i}'Recebi um tutorial por e-mail, mas é muito genérico. Não mostra o passo a passo real do que precisamos no dia a dia.'{/i}"
            play sound "ui.ogg"
            scene bg patinhasmesatalkback
            show patinhastalkbackmesa zorder 11
            show maxx at center:
                zoom 0.4
            m "{i}Isso mostra que, mesmo com algum treinamento, o problema persiste devido a outros fatores, não apenas a falta de instrução.{/i}"
            play sound "ui.ogg"
            n "Vocês percebem que a raiz do problema não está no treinamento, mas em algo mais profundo."
            play sound "ui.ogg"


        "Inconsistência de dados no banco de informações":
            # Flashback e correção
            play sound "correct.ogg"
            $ choices_log.append(("menu6", "Clicou Inconsistência de dados no banco de informações", renpy.get_game_runtime()))
            scene bg reuniao_gi
            gi "Na verdade Doug apontou que houve duplicação de agendamentos e falhas de sincronização, {i} mas também destacou que a interface não deixa claro o que está realmente acontecendo com os dados.{/i}"
            stop music fadeout 1
            play sound "ui.ogg"
            scene ongpatinhas_recepcao with fade:
                matrixcolor SaturationMatrix(0)
            show douglas at center:
                matrixcolor SaturationMatrix(0)
                zoom 0.34
            show recepcao_patinhas zorder 10:
                matrixcolor SaturationMatrix(0)
            doug "{i}'As datas e horários não se sincronizam, mas mesmo quando os dados existem, a tela não mostra corretamente.'{/i}"
            play sound "ui.ogg"
            scene bg reuniao_gi
            gi "Se o problema fosse apenas a base de dados, a interface deixaria claro o status real. Na verdade, muitas inconsistências só são percebidas porque a {i}interface oculta informações críticas.{/i}"
            play sound "ui.ogg"
            n "Parece que a inconsistência de dados é consequência, mas não a causa principal."
            play sound "ui.ogg"


        "Usabilidade confusa da interface do sistema":
            play sound "menu.ogg"
            $ choices_log.append(("menu6", "Clicou Usabilidade confusa da interface do sistema", renpy.get_game_runtime()))
            scene bg reuniao_gi
            stop music fadeout 1
            gi "{b}Concordo.{/b} Isso descreve com precisão o que ouvimos e vimos."
            play sound "ui.ogg"
            scene bg patinhasmesatalkback
            show patinhastalkbackmesa zorder 11
            show douglas feliz at center:
                zoom 0.6
                ypos 1300
            doug "{b}Sim!{/b} Agora temos um foco claro para começar a gerar ideias."
            play sound "ui.ogg"
            scene bg patinhas lmgd
            m "{b}Vou anotar:{/b} {i} 'Interface confusa dificulta visualização e gera erros nos agendamentos'.{/i}"
            play sound "ui.ogg"
            m "Podemos então definir a diretriz da solução assim:"
            m "'{b}Diretriz ‘How Might We’:{/b}{i}• Como poderíamos tornar as informações essenciais de agendamento imediatamente visíveis e compreensíveis para os voluntários?{/i}"
            play sound "ui.ogg"
            m "• {i}Como poderíamos fornecer feedback e alertas que impeçam erros antes da confirmação?{/i}"
            play sound "ui.ogg"
            m "• {i}Como poderíamos simplificar o fluxo para que novos voluntários se sintam confiantes em menos de cinco minutos?{/i}"
            play sound "ui.ogg"
            scene bg patinhas principal
            show mesareuniaopt zorder 10
            show lise feliz at center:
                zoom 0.6
            play sound "achievement.ogg"
            li "{b}Excelente trabalho, equipe!{/b} A definição está bem apurada e nos dá um caminho claro para avançar."
            show lise at center:
                zoom 0.5
                ypos 1200
            li "Mas e aí? Como vocês vão {b}solucionar o problema?{/b}"
            play sound "ui.ogg"
            $ escolha_correta3 = True


        "Falta de recursos financeiros na ONG":
            # Flashback e correção
            play sound "menu.ogg"
            $ choices_log.append(("menu6", "Clicou Falta de recursos financeiros na ONG", renpy.get_game_runtime()))
            scene bg patinhasmesatalkback
            show patinhastalkbackmesa zorder 11
            show lauracontraposto at center:
                zoom 0.6
                ypos 1400
            stop music fadeout 1
            l "Em nenhum momento foi mencionado falta de verba. Lise deixou claro que havia orçamento para treinamento e melhorias, e Paulo nunca citou orçamento como causa da confusão."
            play sound "ui.ogg"
            scene bg patinhasmesatalkback
            show patinhastalkbackmesa zorder 11
            show douglas at center:
                zoom 0.6
                ypos 1600
            doug "{i}A entrevista com Paulo não indicou escassez financeira.{/i} Os recursos existem, mas estão sendo mal utilizados por causa do sistema falho."
            play sound "ui.ogg"
            n "O problema financeiro não aparece nas observações, então não é a raiz da questão."
            play sound "ui.ogg"
jump patinhas_brainstorm

label patinhas_brainstorm:
    scene black with fade
    play music "blackscreen.ogg" fadein 0.3
    show text "{b}Fase:{/b} Ideação\n" with fade
    pause 2
    show text "{b}Objetivo: {/b}Gerar ideias para solucionar o problema." with fade
    pause 2
    show text "Aqui, a equipe explora soluções criativas e diversificadas, combinando diferentes perspectivas para resolver o problema identificado." with fade
    pause 6
    stop music fadeout 1
    scene bg cardgametable1 at center with fade:
        zoom 1.5
    play music "memorygame.ogg" fadein 0.5
    n "Na fase de ideação precisamos gerar várias ideias e, depois, filtrar as que se alinham ao projeto."
    play sound "ui.ogg"
    scene bg cardgametable1tutorial at center:
        zoom 1.5
    n "Neste jogo da memória {i}Brainstorm{/i}, encontre a solução que corresponde a cada problema para avançar."
    play sound "ui.ogg"
    n "Leia atentamente ao conteúdo de em cada carta e tente combinar adequadamente"
    play sound "ui.ogg"
    scene bg cardgametable1 at center with fade:
        zoom 1.5

    $ reset_memory_game()        # embaralha e zera variáveis
    call screen memory_game
    if _return:
        jump feedbacks_brainstorm_patinhas

label feedbacks_brainstorm_patinhas:
    scene bg patinhas lmgd
    stop music fadeout 1
    n "O time reuniu-se em volta da mesa, analisando cada par problema-solução encontrado em seu {i}Brainstorm{/i}"
    play sound "ui.ogg"
    n "Eles discutiram as seis propostas escolhidas, verificaram a coerência de cada uma e apontaram pontos fortes e fracos antes de decidir quais ideias seguir em frente."
    play sound "ui.ogg"
    scene bg patinhasmesatalkback
    show patinhastalkbackmesa zorder 11
    show maxx at center:
        zoom 0.55
        ypos 1400
    m "{b}Nossa, essa sessão foi produtiva!{/b}\nFormulamos soluções potenciais para cada problema!"
    play sound "ui.ogg"
    scene bg reuniao_gi
    gi "Realmente, agora temos {i}opções claras{/i} para desenvolver o protótipo e testar na prática!"
    play sound "ui.ogg"
    jump cutscenepatinhas

label cutscenepatinhas:
    scene bg patinhasmesatalkback
    show patinhastalkbackmesa zorder 11
    show laura feliz at center:
        zoom 0.55
        ypos 1400
    l "{b}Está na hora do almoço.{/b} Vamos fazer uma pausa e recarregar as energias antes de avançarmos, certo?"
    play sound "ui.ogg"
    scene bg patinhas lmgd
    doug "Claro, já está ficando tarde"
    play sound "ui.ogg"
    n "Todos concordam e se levantam da mesa de reuniões, seguindo Laura pelo corredor."
    play sound "ui.ogg"

    scene bg brcomorg_externo with dissolve
    play music "1.ogg" loop fadein 0.2
    play sound "2.ogg" fadein 0.3
    n "{b}Local:{/b} BRCOmorg\n{b}Horário:{/b} 12h10m"
    play sound "ui.ogg"
    pause 2
    scene bg refeitoriobrcomorg
    stop music fadeout 1
    play music "restaurante.ogg" fadein 1
    n "{b}Refeitório da BRComorg\n{/b}[povname] e seus colegas de trabalho almoçando"
    play sound "ui.ogg"
    l "{i}Esse almoço foi ótimo para recarregar as energias.{/i}"
    play sound "ui.ogg"
    pov "{i}Realmente, precisava de uma pausa.{/i}"
    play sound "ui.ogg"
    n "Vocês terminam de comer em silêncio, aproveitando o momento de descanso."
    play sound "ui.ogg"
    pov "Com licença galera,{i}vou escovar os dentes{/i}"
    play sound "ui.ogg"
    stop music fadeout 2
    scene bg office_interditado with dissolve
    n "Você lembra que seus pertences estão na gaveta de sua mesa"
    play sound "ui.ogg"
    play music "sus.ogg"
    n "Você nota algo diferente..."
    play sound "ui.ogg"
    scene bg cabovermelhopc
    n "No canto da mesa, algo chama sua atenção: um cabo estranho conectado à porta traseira do monitor."
    play sound "ui.ogg"
    pov "{i}Esse cabo não estava aqui antes…{/i}"
    play sound "ui.ogg"
    scene bg cabosalo
    n "Você se aproxima com cuidado e puxa o cabo. Ele tem um conector pouco familiar e, ao olhar a marca impressa, percebe algo incomum."
    play sound "ui.ogg"
    n "A etiqueta indica uma fabricante desconhecida que você nunca viu ser usada na empresa."
    play sound "ui.ogg"
    pov "{i}Vou guardar este cabo por enquanto. Pode ser uma pista importante sobre quem está por trás do vazamento.{/i}"
    play sound "ui.ogg"
    n "Você enrola o cabo e coloca no bolso, sentindo o peso da suspeita enquanto caminha de volta para a sala de reuniões."
    play sound "ui.ogg"
    stop music fadeout 1
    jump prototipacao_patinhas

label prototipacao_patinhas:
    scene black with fade
    play music "blackscreen.ogg" fadein 3
    show text"{b}Fase:{/b} Prototipação" with fade
    pause 1
    show text "{b}Objetivo: {/b}Transformar as ideias selecionadas em protótipos tangíveis para avaliar e ajustar antes da implementação final." with fade
    pause 5
    scene bg patinhas lmgd
    n "Cada membro da equipe ficou com dois problemas para prototipar:"
    play sound "ui.ogg"
    n "• {b}Max recebeu:{/b} criar texto para fornecedores do software e um sistema de agendamento analógico de suporte."
    play sound "ui.ogg"
    n "• {b}Gi recebeu:{/b} Treinamento de voluntários e melhora da arte do PDF."
    play sound "ui.ogg"
    n "• Você, {b}[povname]{/b} recebeu: Marcação de canis e tornar a interface intuitiva."
    play sound "ui.ogg"
    n "• {b}Doug recebeu:{/b} Criar notas de fluxos do sistema."
    play sound "ui.ogg"

    scene black with fade

    n "Todos começaram a formular seus protótipos imediatamente"
    play sound "ui.ogg"
    stop music fadeout 2
    scene canilnomear with fade
    n "• Você, {b}[povname]{/b} recebeu: Marcação de canis e tornar a interface intuitiva."
    play sound "ui.ogg"
    n "Nomeie os canis na ordem certa para evitar confusões entre os voluntários"
    play music "canil.ogg" fadein 1
    play sound "ui.ogg"


    call screen canis_patinhas
    if _return:
        jump prototipacao_interface

label prototipacao_interface:
    scene bg canilcompleto
    n "Parabéns você ordenou os nomes dos canis!"
    play sound "achievement.ogg"
    scene black with fade
    n "Você, {b}[povname]{/b} recebeu: \n{s}Marcação de canis{/s} \nTornar a interface intuitiva."
    play sound "ui.ogg"
    scene bg montarinterface with dissolve:
        zoom 1.513
    n "Torne a interface do patinhas {b}intuitiva{/b}\nArraste cada {b}elemento da interface{/b} para seu {i}devido local{/i}"
    play sound "ui.ogg"
    call screen interface_patinhas
    scene bg interfacecompleta
    play sound "achievement.ogg"
    n "Parabéns você arrumou a interface do Patinhas!"
    play sound "ui.ogg"
    scene bg patinhas lmgd
    stop music fadeout 2
    n "{b}Local:{/b} Sala de Reuniões da ONG Patinhas\n{b}Horário:{/b} 16:39h"
    play sound "ui.ogg"
    n "Após horas de trabalho intenso, todos retornam à sala de reuniões para apresentar seus resultados de prototipação."
    play sound "ui.ogg"
    
    scene bg reuniao_gi
    gi "Preparei o material de treinamento interativo em PDF, com arte aprimorada e instruções mais claras para voluntários, incluindo fluxogramas coloridos e exemplos práticos de passo a passo."
    play sound "ui.ogg"
    
    scene bg patinhasmesatalkback
    show patinhastalkbackmesa zorder 11
    show maxx at center:
        zoom 0.55
        ypos 1400
    m "Criei o texto de orientação para os fornecedores do software e desenvolvi um sistema de agendamento analógico de suporte, para que voluntários tenham um guia físico caso o sistema digital falhe."
    play sound "ui.ogg"
    
    scene bg patinhas lmgd
    doug "Elaborei notas detalhadas dos fluxos do sistema, documentando cada tela, comportamento esperado e possíveis pontos de falha para orientar testes futuros."
    play sound "ui.ogg"
    
    pov "Marquei corretamente cada canil no protótipo, garantindo que as placas coincidam com as imagens"
    pov "também projetei uma interface mais intuitiva, posicionando campos críticos em destaque e janelas de confirmação antes de salvar."
    play sound "ui.ogg"

    l "Alinhei com a diretora para testarmos as implementações a partir de amanhã. Também prototipei o roteiro de facilitação."
    play sound "ui.ogg"
    scene bg patinhasmesatalkback
    show patinhastalkbackmesa zorder 11
    show lise at center:
        zoom 0.55
        ypos 1400
    li "Sim, vamos testar o protótipo de vocês amanhã!"
    play sound "ui.ogg"
    jump testagem_patinhas

label testagem_patinhas:
    scene black with fade
    play music "blackscreen.ogg" fadein 2
    show text "{b}Fase:{/b} Testes de Usabilidade" with fade
    pause 1
    show text "{b}Objetivo:{/b} Avaliar o protótipo com voluntários reais,\nidentificar pontos de fricção e ajustar antes da implementação." with fade
    pause 6
    scene bg patinhasexterno with dissolve
    play sound "2.ogg"
    n "{b}Dia Seguinte{/b}\n{b}Local:{/b} Exterior da ONG Patinhas\n{b}Horário:{/b} 14h00"
    play sound "ui.ogg"
    n "Um grupo de voluntários aguarda na entrada, prontos para participar dos testes de usabilidade do protótipo."
    play sound "ui.ogg"

    # --- GI APRESENTA O MATERIAL DE TREINAMENTO --------------------------
    scene bg patinhasgi with fade
    show gio at center:
        zoom 0.34
    gi "{b}Boa tarde a todos!{/b} Hoje vocês vão experimentar a nova interface e o material de treinamento interativo."
    play sound "ui.ogg"
    scene bg voluntarios with dissolve
    n "Gi distribui tablets com o PDF de treinamento aprimorado e explica como navegar nas telas."
    play sound "ui.ogg"
    n "Alguns minutos depois, Gi pergunta:"
    play sound "ui.ogg"
    scene bg patinhasgi with fade
    show gio at center:
        zoom 0.34
    gi "{b}O que vocês estão achando do tutorial?{/b}"
    play sound "ui.ogg"
    scene bg voluntarios
    n "Os voluntários comentam que os fluxogramas coloridos ajudam a compreender o passo a passo, mas alguns prefeririam exemplos mais detalhados."
    play sound "ui.ogg"
    scene bg patinhasgi
    show gio feliz at center:
        zoom 0.5
    gi "{i}Ótimo. Vamos anotar esses pontos para melhorar depois.{/i}"
    play sound "ui.ogg"
    scene bg tutorial
    n "Resultado do teste do PDF de treinamento: {b}96 porcento dos voluntários entenderam o fluxo conceitual, mas 40 porcento solicitaram exemplos reais de uso em campo.{/b}"
    play sound "ui.ogg"

    # --- MÁX APRESENTA O SISTEMA ANALÓGICO -----------------------------------
    scene bg patinhas_recepção
    show maxx at center:
        zoom 0.34
    m "Vou demonstrar o sistema de {b}agendamento analógico{/b} de suporte, caso o sistema digital falhe."
    play sound "ui.ogg"
    scene bg solucaomax
    n "Máx mostra quadros brancos com colunas de ‘Data’, ‘Horário’, ‘Veterinário’ e ‘Observações’, preenchidos manualmente pelos voluntários."
    play sound "ui.ogg"

    n "Os voluntários testam o sistema analógico e comentam que é fácil de usar, porém leva mais tempo do que o digital."
    play sound "ui.ogg"
    scene bg patinhas_recepção
    show maxx at center:
        zoom 0.34
    m "{i}Entendi. Então podemos manter o analógico como backup, mas priorizar a interface digital principal.{/i}"
    play sound "ui.ogg"
    scene bg patinhasexterno
    n "Resultado do teste do sistema analógico: {b}100 porcento dos voluntários conseguiram registrar agendamentos, mas o tempo médio foi 3× maior que no protótipo digital.{/b}"
    play sound "ui.ogg"
    scene bg patinhas_recepção
    show recepcao_patinhas zorder 10
    # --- TESTE DO PROTÓTIPO DE INTERFACE (VOCÊ/[povname]) --------------------
    pov "Agora, vamos testar a {b}nova interface digital{/b} com os campos destacados e janelas de confirmação."
    play sound "ui.ogg"
    scene bg pcmx
    n "Um voluntário inicia o agendamento no protótipo: ele clica no campo de data e vê a janela de confirmação antes de salvar."
    play sound "ui.ogg"

    n "{b}Feedback do voluntário:{/b}"
    play sound "ui.ogg"
    n "• ‘Achei intuitivo ver a data em destaque e a confirmação me deu mais segurança.’"
    n "• ‘Porém, às vezes a janela de confirmação demora um pouco para carregar.’"
    play sound "ui.ogg"
    scene bg patinhas_recepção
    pov "{i}Anotado. Vamos reduzir o delay da confirmação no próximo ajuste.{/i}"
    play sound "ui.ogg"
    n "Resultado do teste da interface: {b}85 porcento de sucesso no primeiro clique, 15 porcento precisaram de segunda tentativa devido a leve lentidão.{/b}"
    play sound "ui.ogg"

    # --- TESTE DE MARCAÇÃO DE CANIS (VOCÊ/[povname]) -------------------------
    scene bg canilcompleto
    n "Em seguida, voluntários fazem o teste de marcação de canis usando o protótipo físico de placas e canis."
    play sound "ui.ogg"

    n "O voluntário coloca o cão destinado ao ‘Canil 1’ no lugar correto, depois no ‘Canil 2’, no ‘Canil 3’ e ‘Canil 4’ de maneira rápida."
    play sound "ui.ogg"
    pov "{i}Excelente, parece que a sinalização está clara para os voluntários.{/i}"
    play sound "ui.ogg"
    n "Resultado do teste de marcação de canis: {b}100 porcento de acertos.{/b}"
    play sound "ui.ogg"

    # --- FEEDBACK FINAL NA SALA DE REUNIÃO -----------------------------------
    scene bg patinhas lmgd with fade
    stop music fadeout 2
    n "De volta à sala de reuniões, cada membro compartilha os resultados obtidos:"
    play sound "ui.ogg"
    scene bg patinhasmesatalkback
    show patinhastalkbackmesa zorder 11
    show maxx at center:
        zoom 0.55
        ypos 1400
    m "{b}Resultados gerais:{/b} O sistema digital se mostrou {b}eficiente{/b}, mas requer {b}otimização no tempo de resposta{/b}."
    play sound "ui.ogg"
    scene bg reuniao_gi
    gi "{b}O material de treinamento foi muito bem aceito, mas precisa de exemplos de aplicação prática.\"{/b}"
    play sound "ui.ogg"
    scene bg patinhas lmgd
    pov "{b}A sinalização dos canis funcionou perfeitamente, e a interface digital está quase lá.{/b}"
    play sound "ui.ogg"
    scene bg patinhasmesatalkback
    show patinhastalkbackmesa zorder 11
    show douglas at center:
        zoom 0.55
        ypos 1400
    doug "{b}Minhas notas indicam que alguns fluxos precisam de pequenas correções de texto e posicionamento.{/b}"
    play sound "ui.ogg"
    scene bg patinhasmesatalkback
    show patinhastalkbackmesa zorder 11
    show lise feliz at center:
        zoom 0.7
        ypos 1400
    play sound "achievement.ogg"
    li "{b}Ótimo trabalho, pessoal! Com essas informações, podemos refinar e lançar a solução final.\"{/b}"
    play sound "ui.ogg"
    scene black with fade
    play sound "missaoconcluida.ogg"
    show text "{b}MISSÃO ONG PATINHAS CONCLUÍDA{/b}" at truecenter with fade
    pause 2
    $ patinhascompleto = True
    call screen missoes