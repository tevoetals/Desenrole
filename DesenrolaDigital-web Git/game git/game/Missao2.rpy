#declaração de personagens

define adv = Character("{b}Advogado Giuliano{/b}", color="#ffffff")
define ceoL = Character("{b}Sr. Andre{/b}", color="#ffffff")
default cabo_entregue = False
transform saltitar:
    ypos 0
    linear 0.2 ypos -20
    linear 0.2 ypos 0
    repeat

transform pan_left_slow:
    xalign 1.0 yalign 0.5  # Começa na direita
    linear 10.0 xalign 0.0  # Move para a esquerda em 10 segundos

transform pan_right_slow:
    xalign 0.0 yalign 0.5  # Começa na direita
    linear 10.0 xalign 1.0  # Move para a esquerda em 10 segundos

transform flash_effect:
    #anchor (0.5, 0.5)
    align (0.5, 0.5)
    alpha 0.0
    zoom 0.1
    linear 0.1 alpha 1.0
    linear 0.1 zoom 0.5
    alpha 0.0
    zoom 1.0
    pause 1.99
    repeat


transform quickshow:
    alpha 0.0
    linear 0.1 alpha 1
    linear 0.1 alpha 0.0
    pause 2
    repeat

#sprites dos personagens

image adv = "lumi/adv1.png"
image adv feliz = "lumi/adv2.png"
image lceo triste = "lumi/lceo triste.png"
image lceo seapresentando = "lumi/lceo se apresentando.png"
image lceo = "lumi/lceo.png"
image lceo sentadotriste = "lumi/lceo sentado triste.png"
image lceo feliz = "lumi/lceofeliz.png"
image lceo sentado = "lumi/lceo sentado.png"
image diretorwelcome = "Personagens/almeidawelcome.png"
image diretorsus = "Personagens/almeidasus.png"
image invest_costa default = "lumi/invest1.png"
image invest_costa falando = "lumi/invest11.png"
image invest_costa espantada = "lumi/invest12.png"
image call_invest = "lumi/call_invest.png"
image ramirez = "lumi/ramirez1.png"
image ramirez falando = "lumi/ramirez2.png"
image gio espantada = "Personagens/gio espantada.png"
image maxx espantado = "Personagens/max espantado.png"
image laura espantada = "Personagens/laura espantada.png"
image douglas espantado = "Personagens/doug espantado.png"
image fx = "Misc/effect.png"
image cadeirareuniaofrente1 = "lumi/cadeira reuniao frente 1.png"
image cadeirareuniaofrente2 = "lumi/cadeira reuniao frente 2.png"
image gio triste = "lumi/gio triste.png"
image flash = "lumi/flash.png"
image flashc = "lumi/flash copy.png"
image flashed = "lumi/flashed.png"


#backgrounds e imgs

image bg lumi_externo = "lumi/lumi_externo.png"
image bg internolumiofficevazio = "lumi/internolumiofficevazio.png" 
image bg officecheio = "lumi/officecheio.png"
image bg saladiretorlumidia = "lumi/saladiretorlumidia.png"
image bg cadeira reuniao 2 = "lumi/cadeira reuniao 2.png"
image bg saladiretorluminoite = "lumi/saladiretorluminoite.png"
image bg cadeira reuniao = "lumi/cadeira reuniao.png"
image bg salaleuniaolumi = "salareuniaolumi.png"
image bg fundocall = "lumi/fundo call.png"
image bg hub_externo = "lumi/hub externo.png"
image bg hub_interno = "lumi/hub interno.png"
image bg salalumibg = "lumi/saladiretorlumidiabg.png"
image bg remedio = "lumi/remedio.png"
image bg reuniaolumi = "lumi/reuniaolumi.png"
image bg cadeira_reuniao_lumi = "lumi/cadeira reuniao.png"
image bg cadeira_reuniao_lumi2 = "lumi/cadeira reuniao 2.png"
image bg datashow1 = "lumi/datashow1.png"
image bg datashow2 = "lumi/datashow2.png"
image bg mesa_lumi = "lumi/cards/mesa.png"
image bg lumi_cafe = "lumi/cafeinternolumi.png"
image lumi_cafe_mesa = "lumi/cafeinternolumi_mesa.png"
image cabo_salo = "lumi/cabo salo.png"
image bg reuniaonoite = "lumi/reuniaonoite.png"
image bg coletiva1 = "lumi/coletiva imprensa.png"
image coletiva2 = "lumi/coletiva imprensa2.png"
image bg auditorio = "lumi/auditoriofinal.png"
image bg lablumi = "lumi/lab lumi.png"
image bg relatorio = "lumi/scene relatorio.png"
image bg anvisa = "lumi/Anvisa resposta.png"
image bg dougpresentation1 = "lumi/8.png"
image bg dougpresentation2 = "lumi/9.png"
image bg maxpres1 = "lumi/10.png"
image bg maxpres2 = "lumi/11.png"
image bg aulamedico = "lumi/scene medicos.png"
image bg remedioefeitos = "lumi/12.png"
image bg gianvisa = "lumi/scene relatorio.png"
image bg anvisa = "lumi/Anvisa resposta.png"
image bg folha = "lumi/minigame/folha.png"
image bg folhacheia = "lumi/minigame/folhacheia.png"
image bg folhastetic = "lumi/minigame/folhastetic.png"

label missao2:
    scene black with fade
    pause 1
    scene bg brcomorg_externo
    play music "1.ogg"
    play sound "2.ogg"
    n "Local: BRComorg\nHorário: 14h"
    play sound "ui.ogg"
    scene bg saladiretor2:
        zoom 1.4
    show almeida_sorriso at right:
        zoom 0.4
        xzoom -1
    hide almeida_sorriso
    show almeidawelcome at right:
        zoom 0.8
        ypos 1500
        xzoom -1
    a "{b}Entre, por favor.{/b} Sente-se."
    play sound "ui.ogg"
    scene bg saladiretor2:
        zoom 1.4
    show almeida_sorriso at right:
        zoom 0.5
        ypos 1300
    show bastos at left with dissolve:
        zoom 0.6
        ypos 1200
    b "{i}Bom... Você fez um trabalho surpreendente na primeira missão.{/i}"
    play sound "ui.ogg"

    pov "Obrigado, Diretores. Fico feliz em ajudar."
    play sound "ui.ogg"
    hide almeida_sorriso
    show diretorsus at right:
        zoom 0.7
        ypos 1300
        xzoom -1
    a "{b}O Delegado Silva e o Agente Vieira confirmaram que, por enquanto, não há provas concretas contra você.{/b} Conseguimos um advogado de confiança para garantir sua tranquilidade."
    play sound "ui.ogg"

    n "Nesse instante, um assistente de Diretoria entra, conduzindo um homem de terno claro pelo corredor."
    stop music fadeout 1
    play sound "ui.ogg"
    scene diretoriabastos:
        zoom 1.3
        ypos -260
    show adv feliz at center:
        zoom 0.6
        ypos 1500
    n "O advogado se apresenta com postura confiante, ajustando os óculos antes de falar."
    play sound "ui.ogg"

    adv "Prazer em conhecê-lo, sou Dr. Giuliano. {i}Tenho vasta experiência em casos de vazamento de dados.{/i}"
    play sound "ui.ogg"
    scene bg saladiretor2:
        zoom 1.4
    show almeida_sorriso at right:
        zoom 0.5
        ypos 1300
        xzoom -1
    show bastos at left:
        zoom 0.5
    a "{b}Dr. Torres tem um histórico impecável.{/b} Foi ex-procurador público e nunca perdeu um caso relevante."
    play sound "ui.ogg"
    scene bg saladiretor2:
        zoom 1.4
    show diretorsus at right:
        zoom 0.7
        ypos 1300
        xzoom -1
    show bastos at left:
        zoom 0.5
    b "{i}Recomendo fortemente seus serviços. Ele é incisivo na defesa e conhece todos os meandros jurídicos.{/i}"
    play sound "ui.ogg"

    pov "Muito obrigado pela ajuda diretores."
    play sound "ui.ogg"
    scene bg almeida_tranquilo
    a "{b}Com o Dr. Torres cuidando do aspecto jurídico, podemos focar na comunicação externa da Lumi.{/b}"
    play sound "ui.ogg"
    scene bg saladiretor2:
        zoom 1.4
    show almeida_sorriso at right:
        zoom 0.4
    show bastos at left:
        zoom 0.5
    b "{i}Eles estão enfrentando problemas de imagem e relacionamento com investidores. Precisamos reverter isso o quanto antes.{/i}"
    play sound "ui.ogg"

    n "Os diretores trocam olhares e assentem, demonstrando confiança em você, [povname]."
    play sound "ui.ogg"
    scene bg almeida_tranquilo
    a "{b}Você irá se reunir com o CEO da Lumi amanhã de manhã. Prepare uma proposta de estratégia de comunicação externa.{/b}"
    play sound "ui.ogg"
    pov "{i}Entendido. Irei analisar o histórico da empresa e elaborar um plano direcionado aos stakeholders certos.{/i}"
    play sound "ui.ogg"
    scene black with fade
    n "Após a reunião, você se retira da sala dos diretores, carregando as expectativas de um novo desafio à frente."
    play sound "ui.ogg"

    scene lumi_externo:
        zoom 0.8
    play music "lumi.ogg" fadein 0.5
    n "{b}Dia seguinte:{/b} 14h"
    play sound "ui.ogg"
    n "O prédio da Lumi ergue-se imponente à sua frente. No hall de entrada, o logotipo prateado reluz sob as luzes frias. Você e o time de comunicação seguem até a sala de reuniões no 10º andar."
    play sound "ui.ogg"
    scene bg saladiretorlumidia
    show lceo sentado:
        zoom 0.25
        ypos 270
        xpos 770
    show lauracontraposto at right:
        zoom 0.34
        xzoom -1
    show douglas at left:
        zoom 0.34
        xzoom -1
    n "Ao entrar, avista Sr. Andre sentado em seu escritório.\nO time já está lá para a reunião"
    play sound "ui.ogg"

    ceoL "{b}Sejam bem-vindos à Lumi.{/b} Obrigado por virem tão rapidamente"  
    play sound "ui.ogg"
    ceoL "{b}Há algo que precisam saber{/b} antes de qualquer estratégia."
    play sound "ui.ogg"
    stop music fadeout 0.3
    show lceo sentadotriste:
        zoom 0.25
        ypos 270
        xpos 770
    ceoL "{i}Ontem à noite, um paciente que tomou um de nossos compostos morreu repentinamente...{/i}"
    play sound "ui.ogg"
    play music "jump.ogg"
    # pessoal espantado
    hide lauracontraposto
    scene bg salalumibg
    show fx at saltitar:
        zoom 1.4
    show laura espantada at center:
        zoom 0.6
    pause 0.4
    hide laura
    show douglas espantado at center:
        zoom 0.7
    pause 0.4
    hide douglas
    show gio espantada at center:
        zoom 0.6
    pause 0.5
    hide gio
    show maxx espantado at center:
        zoom 0.6
    pause 0.5
    n "Todos na sala se entreolham, visivelmente espantados."
    play sound "ui.ogg"
    scene bg saladiretorlumidia
    show lceo sentado:
        zoom 0.25
        ypos 270
        xpos 770
    # mostrar paciente no leito e medicos ao redor
    stop music fadeout 0.5
    ceoL "{i}Os médicos confirmam que o paciente tinha uma rara predisposição cardíaca...{/i}"
    play sound "ui.ogg"
    # voltar para a cena
    ceoL "{b}Isso não pode vazar para o público sob hipótese alguma.{/b}"
    play sound "ui.ogg"
    scene bg remedio at pan_right_slow with dissolve:
        zoom 1.2
    play music "guitar.ogg"
    ceoL "{i}Todos os nossos medicamentos passam por rigorosos testes e são aprovados pela ANVISA, garantindo sua segurança e eficácia.{/i}"
    play sound "ui.ogg"
    ceoL "{i}Este, porém, foi um caso excepcional — não se trata de uma falha no nosso processo de farmacovigilância, mas sim de uma ocorrência isolada que não pode vazar ao público.{/i}"
    play sound "ui.ogg"
    scene bg saladiretorlumidia
    show lceo sentadotriste:
        zoom 0.25
        ypos 270
        xpos 770
    n "Sr. Andre conclui, visivelmente exausto. Você sente que não há mais perguntas."
    play sound "ui.ogg"

    pov "{i}Agradecemos pelo seu tempo, Sr. Andre. Vamos nos reunir agora para definir o próximo passo.{/i}"
    play sound "ui.ogg"

    ceoL "{b}Confio em vocês. A sala de reuniões no fim do corredor está reservada.{/b}"
    play sound "ui.ogg"

    n "O grupo se levanta: Laura recolhe os crachás de visitante, Gi fecha o laptop, Max guarda o tablet e Doug desliga o projetor."
    play sound "ui.ogg"
    scene black with dissolve
    pause 2
    scene salareuniaolumi at pan_left_slow with fade:
        zoom 1.2
    n "Alguns minutos depois, vocês entram numa sala com janelas de vidro. A vista de Brasília se mostra deslumbrante, enquanto cadeiras giratórias rangem discretamente."
    play sound "ui.ogg"

    l "{i}Ok, pessoal — hora de decidir por onde começamos.{/i}"
    play sound "ui.ogg"
    jump empatia_lumi

# --- FASE DE EMPATIA ------------------------------------------------------

default errou_um = False
default errou_dois = False

label empatia_lumi:
    scene reuniaolumi with fade
    stop music fadeout 1
    menu:
        n "Qual deve ser nosso primeiro passo?"

        "Ouvir investidores e pacientes":
            play sound "correct.ogg"
            $ choices_log.append(("menu7", "Clicou investidores e pacientes", renpy.get_game_runtime()))
            pov "Vamos começar ouvindo pacientes e investidores antes de qualquer suposição."
            play sound "ui.ogg"
            l "{i}Perfeito. Marcarei entrevistas com médicos e familiares do caso excepcional, vamos ouvir investidores e afetados.{/i}"
            play sound "ui.ogg"

            n "A equipe se dispersa, iniciando oficialmente a {b}Fase de Empatia{/b}."
            play sound "ui.ogg"

            scene black with fade
            play music "blackscreen.ogg" fadein 1
            show text "{b}Fase:{/b} Definição" with fade
            pause 2
            hide text with dissolve
            pause 1

            show call_invest zorder 11:
                zoom 1.4
                ypos -300
            n "Algumas horas depois, você e Laura entram em videoconferência com a investidora {i}Sra. Costa{/i}."
            play sound "ui.ogg"
            show bg fundocall with fade
            show call_invest zorder 11:
                zoom 1.4
                ypos -300
            show invest_costa default:
                zoom 0.3
                xpos 800
                ypos 100

            l "{i}Sra. Costa, o que a preocupa mais sobre a Lumi neste momento?{/i}"
            play sound "ui.ogg"
            show invest_costa falando:
                zoom 0.3
                xpos 800
                ypos 100
            "{b}Sra. Costa{/b}" "{b}Três coisas{/b}, na verdade.\n{b}Primeiro,{/b} {i}não entendo o que aconteceu{/i}:"
            play sound "ui.ogg"
            show invest_costa default:
                zoom 0.3
                xpos 800
                ypos 100
            "{b}Sra. Costa{/b}" "A imprensa fala de morte suspeita, mas o comunicado da empresa veio curto e cheio de palavras bonitas."
            play sound "ui.ogg"
            show invest_costa espantada:
                zoom 0.3
                xpos 800
                ypos 100
            "{b}Sra. Costa{/b}" "{b}Segundo,{/b} {i}ninguém assumiu a linha de frente{/i}:\nAté agora não vi o CEO olhando na câmera e dizendo o que fez para evitar outra tragédia."
            play sound "ui.ogg"
            show invest_costa default:
                zoom 0.3
                xpos 800
                ypos 100
            "{b}Sra. Costa{/b}" "{b}Terceiro,{/b} {i}medo de punição oficial{/i}:\nSe a Anvisa ou o Ministério Público abrir processo, a ação {b}afundaria mais ainda{/b} e meus clientes perdem confiança em mim."
            play sound "ui.ogg"
            pov "Entendo. O que a ajudaria a recuperar essa confiança?"
            play sound "ui.ogg"
            show invest_costa espantada:
                zoom 0.3
                xpos 800
                ypos 100
            "{b}Sra. Costa{/b}" "Meus clientes precisam saber se estou investindo na empresa certa, pra dar segurança para eles, precisamos de mais informações sobre sua gestão de crise."
            play sound "ui.ogg"
            show invest_costa default:
                zoom 0.3
                xpos 800
                ypos 100
            "{b}Sra. Costa{/b}" "Primeiro, {i}linha do tempo clara{/i}. Quero saber, dia a dia, o que a Lumi descobriu, quando avisou a família do paciente e que medidas tomou logo depois. Sem lacunas."
            play sound "ui.ogg"
            show invest_costa falando:
                zoom 0.3
                xpos 800
                ypos 100
            "{b}Sra. Costa{/b}" "Segundo, {i}números na mesa{/i}. Quantas caixas desse remédio já foram vendidas?"
            "{b}Sra. Costa{/b}" "Quantas reclamações sérias apareceram? e como esse número compara com outros laboratórios do mesmo porte?"
            "{b}Sra. Costa{/b}" "Tudo em frações fáceis de entender, tipo ‘1 caso grave a cada 50 mil caixas’."
            play sound "ui.ogg"
            show invest_costa default:
                zoom 0.3
                xpos 800
                ypos 100
            "{b}Sra. Costa{/b}" "Terceiro, {i}voz independente{/i}. Não quero apenas o porta-voz da empresa; quero ver um médico de fora, alguém sem salário da Lumi, explicar o ocorrido e dizer se o remédio continua seguro."
            play sound "ui.ogg"
            show invest_costa falando:
                zoom 0.3
                xpos 800
                ypos 100
            "{b}Sra. Costa{/b}" "Quarto, {i}plano de ação visível{/i}. Preciso saber o que muda a partir de agora:"
            "{b}Sra. Costa{/b}" "Se vão revisar lotes, criar embalagem nova ou reservar dinheiro para eventuais indenizações."
            "{b}Sra. Costa{/b}" "Sem promessas vagas — prazos, valores e responsáveis pelo cumprimento."
            play sound "ui.ogg"
            show invest_costa default:
                zoom 0.3
                xpos 800
                ypos 100
            pov "Perfeito. Linha do tempo, números crus, especialista externo e plano de ação com datas. Vamos trabalhar nesses quatro pontos e voltaremos a você em breve."
            play sound "ui.ogg"
            stop music fadeout 1
            scene black with fade
            pause 1
            hide invest_costa
            hide call_invest
            scene bg hub_externo with fade
            play music "hub.ogg"
            
            # Depoimento de paciente
            show gio at center:
                zoom 0.34
            n "Mais tarde, Gi entrevista {i}Sr. Ramires{/i}, paciente crônico que usa o medicamento."
            play sound "ui.ogg"
            scene bg hub_interno
            stop music fadeout 1
            show gio feliz:
                zoom 0.6
            gi "{i}Como está seu dia a dia desde que começou a tomar o remédio?{/i}"
            play sound "ui.ogg"
            hide gio
            show ramirez at center:
                zoom 0.47
                ypos 1000
            "{b}Sr. Ramires{/b}" "Minhas dores diminuíram bastante, mas notei umas palpitações leves de vez em quando."
            play sound "ui.ogg"
            hide ramirez
            show gio at center:
                zoom 0.34
            gi "{i}E o que passou pela sua cabeça quando viu as notícias recentes?{/i}"
            play sound "ui.ogg"
            hide gio
            show ramirez falando at center:
                zoom 0.47
                ypos 1000
            "{b}Sr. Ramires{/b}" "Fiquei confuso. Não sei se as palpitações são efeito do remédio ou coisa da minha saúde mesmo."
            play sound "ui.ogg"
            hide ramirez
            show gio at center:
                zoom 0.34
            gi "{i}O que você gostaria que a Lumi fizesse agora?{/i}"
            play sound "ui.ogg"
            hide gio
            show ramirez at center:
                zoom 0.47
                ypos 1000
            "{b}Sr. Ramires{/b}" "Queria ter um número pra ligar e alguém explicar direitinho se isso é esperado, sabe? Preciso de orientação clara, não só um panfleto."
            play sound "ui.ogg"
            scene black with fade
            pause 1
            scene salareuniaolumi with fade


            # Síntese
            n "De volta à sala ..."
            play sound "ui.ogg"
            scene bg cadeira_reuniao_lumi
            show maxx at center:
                zoom 0.4
            show cadeirareuniaofrente1 zorder 10
            m "{i}Ponto principal: as pessoas estão com medo de tomar algo que possa matá-las e sentem que a empresa esconde informações.{/i}"
            play sound "ui.ogg"
            scene bg cadeira_reuniao_lumi2
            show douglas at center:
                zoom 0.5
                ypos 1300
            show cadeirareuniaofrente2 zorder 10
            doug "{i}Nas anotações, três ideias aparecem o tempo todo: ‘não confio mais’, ‘o que estão escondendo?’ e ‘quem vai pagar se der errado?’.{/i}"
            play sound "ui.ogg"
            scene salareuniaolumi with fade
            pov "{i}Entendido. Dor pura e desconfiança total. Vamos transformar isso numa pergunta que conduza o próximo passo.{/i}"
            play sound "ui.ogg"
            jump definicao_lumi



        "Gerar ideias de campanha agora":
            play sound "menu.ogg"
            $ choices_log.append(("menu7", "Clicou Gerar ideias de campanha agora", renpy.get_game_runtime()))
            pov "Acho que podemos pular direto para gerar ideias de campanha."
            play sound "ui.ogg"
            scene bg cadeira_reuniao_lumi
            show gio feliz at center:
                zoom 0.6
            show cadeirareuniaofrente1 zorder 10
            n "Gi sorri, animada; Laura ergue a sobrancelha, desconfiada."
            play sound "ui.ogg"
            gi "{i}Vamos lançar uma hashtag: #LumiTransparente — chamar influenciadores e pronto!{/i}"
            play sound "ui.ogg"
            scene bg cadeira_reuniao_lumi2
            show laura brava at center:
                zoom 0.6
            show cadeirareuniaofrente2 zorder 10
            l "{i}Não temos base de insights. E se a hashtag já existe?{/i}"
            play sound "ui.ogg"
            hide laura
            show maxx feliz at center:
                zoom 0.7
            show cadeirareuniaofrente2 zorder 10
            m "{i}Vou esboçar um vídeo 3D mostrando nossas fábricas e um jingle motivacional.{/i}"
            play sound "ui.ogg"
            scene bg cadeira_reuniao_lumi
            show douglas raiva at center:
                zoom 0.6
            show cadeirareuniaofrente1 zorder 10
            doug "{i}Sem dados de dor, dificilmente convenceremos o público crítico.{/i}"
            play sound "ui.ogg"
            scene bg saladiretorlumidia
            show lceo seapresentando at center:
                zoom 0.57
                ypos 1500
                xpos 900
            n "Duas horas depois, o time apresenta o rascunho ao Sr. Andre."
            play sound "ui.ogg"
            show lceo at center:
                zoom 0.5
            ceoL "{b}Isso é… colorido. Mas onde estão as evidências? Onde estão as vozes dos pacientes?{/b}"
            play sound "ui.ogg"
            n "O CEO suspira, frustrado."
            play sound "ui.ogg"
            ceoL "{b}Voltem e comecem do início. Precisamos ouvir antes de falar.{/b}"
            play sound "ui.ogg"
            n "Você sente que a pressa custou credibilidade. Talvez seja hora de reconsiderar a ordem natural do Design Thinking."
            play sound "ui.ogg"
            $ errou_um = True
            jump checa_fracasso1

        "Testar público imediatamente":
            play sound "menu.ogg"
            $ choices_log.append(("menu7", "Clicou Testar público imediatamente", renpy.get_game_runtime()))
            pov "Se fizermos testes de público agora, poderemos medir reação real."
            play sound "ui.ogg"
            scene bg cadeira_reuniao_lumi
            show douglas at center:
                zoom 0.52
                ypos 1300
            show cadeirareuniaofrente1 zorder 10
            doug "{i}Sem protótipo estruturado, o que exatamente vamos testar?{/i}"
            play sound "ui.ogg"
            scene bg datashow1
            n "Mesmo assim, um focus group emergencial é montado num auditório virtual com 20 stakeholders."
            play sound "ui.ogg"

            n "O público vê apenas slides genéricos e um script indeciso. Os rostos na tela se contraem em confusão."
            play sound "ui.ogg"
            scene bg datashow2
            "{b}Stakeholder 1{/b}" "Isso não responde ao caso de ontem. Parece que escondem algo."
            play sound "ui.ogg"
            "{b}Stakeholder 2{/b}" "Falta empatia. É só marketing vazio."
            play sound "ui.ogg"

            n "Tweets negativos surgem em tempo real. A hashtag #LumiOcultaVerdades sobe nos trends locais."
            play sound "ui.ogg"
            scene bg saladiretorlumidia
            show lceo sentado:
                zoom 0.25
                ypos 270
                xpos 770
            ceoL "{b}Testar sem conteúdo sólido só piorou nossa situação.{/b}"
            play sound "ui.ogg"
            show gio triste at left:
                zoom 0.6
            gi "{i}O dano foi maior que o aprendizado. Precisamos voltar várias casas.{/i}"
            play sound "ui.ogg"
            n "A lição é clara: sem Empatia, Ideação e Protótipo, {b}Teste{/b} é prematuro — e perigoso."
            play sound "ui.ogg"
            $ errou_dois = True
            jump checa_fracasso1

label checa_fracasso1:
    if errou_um and errou_dois:               # <<< ALTERADO ─ dois erros ⇒ fracasso
        jump missao_fracassada_lumi           # <<< ALTERADO
    else:
        jump empatia_lumi                     # <<< ALTERADO ─ volta ao menu

label missao_fracassada_lumi:
    scene black with dissolve
    play sound "gameover.ogg"
    show text "{b}Você fracassou{/b} na missão Lumi" with fade
    pause 2
    stop sound fadeout 1
    call screen missoes



# --- FASE DE DEFINIÇÃO ------------------------------------------------------

label definicao_lumi:
    play music "guitar.ogg"
    scene black with fade
    show text "{b}Fase:{/b} Empatia" with fade
    pause 1

    $ escolha_correta4 = False
    while not escolha_correta4:
        scene reuniaolumi with fade

        menu:
            n "Com tudo que ouvimos, {b}qual declaração de problema reflete melhor a crise da Lumi?{/b}"

            "Como podemos provar nossa segurança de forma transparente e imediata?":
                play sound "correct.ogg"
                $ choices_log.append(("menu8", "Clicou Como podemos provar nossa segurança de forma transparente e imediata?", renpy.get_game_runtime()))
                scene bg cadeira_reuniao_lumi
                show maxx at center:
                    zoom 0.4
                show cadeirareuniaofrente1 zorder 10
                m "{b}Perfeito!{/b} Essa pergunta foca na dor real: medo de segurança e falta de transparência."
                play sound "ui.ogg"
                scene bg cadeira_reuniao_lumi2
                show gio feliz at center:
                    zoom 0.6
                show cadeirareuniaofrente2 zorder 10
                gi "{i}Com isso, já posso pensar em lives nos laboratórios, perguntas e respostas diariamente com pesquisadores e dashboards abertos.{/i}"
                play sound "ui.ogg"
                scene bg cadeira_reuniao_lumi
                show laura default at center:
                    zoom 0.46
                show cadeirareuniaofrente1 zorder 10
                l "{i}E eu organizo médicos externos para corroborarem os dados em linguagem leiga.{/i}"
                play sound "ui.ogg"
                scene bg cadeira_reuniao_lumi2
                show douglas at center:
                    zoom 0.46
                    ypos 1200
                show cadeirareuniaofrente2 zorder 10
                doug "{i}Estatísticas em tempo real vão reforçar a narrativa de abertura total.{/i}"
                play sound "ui.ogg"
                n "Vocês convergem para a solução correta, prontos para entrar na {b}Fase de Ideação{/b}."
                play sound "ui.ogg"
                $ escolha_correta4 = True

            "Como podemos sinalizar mudança genuína com um rebranding parcial?":
                play sound "menu.ogg"
                stop music fadeout 1
                $ choices_log.append(("menu8", "Clicou Como podemos sinalizar mudança genuína com um rebranding parcial?", renpy.get_game_runtime()))
                scene reuniaolumi with dissolve:
                    matrixcolor SaturationMatrix(0)
                show laura brava at center with moveinleft:
                    zoom 0.46
                
                l "Rebranding pode ajudar, mas é caro e não resolve o medo imediato de segurança."
                play sound "ui.ogg"
                hide laura

                show douglas raiva at center with moveinleft:
                    zoom 0.46
                
                doug "{i}Sem provas médicas claras, renomear a marca parece cortina de fumaça.{/i}"
                play sound "ui.ogg"
                hide douglas
                scene reuniaolumi with dissolve
                n "A equipe conclui que essa não é a raiz do problema."
                play sound "ui.ogg"

            "Como podemos desviar o foco do incidente com uma campanha heroica?":
                play sound "menu.ogg"
                stop music fadeout 1
                $ choices_log.append(("menu8", "Clicou Como podemos desviar o foco do incidente com uma campanha heroica?", renpy.get_game_runtime()))
                scene reuniaolumi with dissolve:
                    matrixcolor SaturationMatrix(0)
                show gio raiva at center with moveinleft:
                    zoom 0.46
                
                gi "{i}Campanha heroica sem explicar a morte soa manipuladora.{/i}"
                play sound "ui.ogg"
                hide gio
                scene reuniaolumi with dissolve
                n "Fica claro que o público perceberia a manobra e o efeito seria reverso."
                play sound "ui.ogg"

            "Como podemos aumentar nosso orçamento de marketing para abafar críticas?":
                play sound "menu.ogg"
                stop music fadeout 1
                $ choices_log.append(("menu8", "Clicou Como podemos aumentar nosso orçamento de marketing para abafar críticas?", renpy.get_game_runtime()))
                scene reuniaolumi with dissolve:
                    matrixcolor SaturationMatrix(0)
                show maxx at center with moveinleft:
                    zoom 0.34
                m "Abafar críticas sem transparência só aumenta a desconfiança."
                play sound "ui.ogg"
                hide maxx
                show gio raiva at center with moveinleft:
                    zoom 0.46
                gi "{i}Seria um tiro no pé. Precisamos de verdade, não de barulho pago.{/i}"
                play sound "ui.ogg"
                hide gio
                scene reuniaolumi with dissolve
                n "Vocês descartam a ideia por ser antiética e ineficaz."
                play sound "ui.ogg"

    jump ideacao_lumi

label ideacao_lumi:
    scene black with dissolve
    stop music fadeout 1
    play music "memorygame.ogg"
    show text "{b}Fase:{/b} Ideação" with fade
    pause 1
    scene bg mesa_lumi with fade
    n "Neste jogo da memória {i}Brainstorm{/i}, encontre a solução que corresponde a cada problema para avançar."
    play sound "ui.ogg"
    n "Leia atentamente ao conteúdo em cada carta e tente combinar adequadamente"
    play sound "ui.ogg"
    $ reset_memory_game_lumi() 
    call screen memory_game_lumi
    scene reuniaonoite with fade
    stop music fadeout 1
    n "Já está tarde, o expediente acabou e a equipe continuará o trabalho amanhã."
    play sound "ui.ogg"


    jump pausa_advogado_lumi

# ---------------------------------------------------------------------------
#  PAUSA NARRATIVA – ENCONTRO COM DR. TORRES
#  Conecta a linha judicial com a Missão Lumi
# ---------------------------------------------------------------------------

label pausa_advogado_lumi:

    scene bg lumi_cafe with dissolve
    play music "sus.ogg"
    n "{b}Local:{/b} Café interno da Lumi\n{b}Horário:{/b} 19h"
    play sound "ui.ogg"

    show adv at center with moveinleft:
        zoom 0.6
        ypos 1500
    adv "{b}Boa Noite.{/b} Acabei de sair de uma reunião com o Delegado Silva."
    play sound "ui.ogg"
    show lumi_cafe_mesa
    show adv at center:
        zoom 0.54
        ypos 1400
        xpos 600
    adv "{i}O inquérito avança devagar, mas continuo bloqueando qualquer indiciamento.{/i}"
    play sound "ui.ogg"

    pov "{i}Ótimo saber. Alguma novidade?{/i}"
    play sound "ui.ogg"

    adv "{i}Na perícia digital, nada liga você ao vazamento. Ainda assim, preciso de qualquer pista estranha que tenha notado.{/i}"
    play sound "ui.ogg"
    adv "Algum detalhe — por menor que seja — pode mudar o rumo do processo."
    play sound "ui.ogg"

    # --- MENU: entregar ou não o cabo estranho --------------------------------
    menu:
        "Entregar o cabo de rede suspeito":
            play sound "menu.ogg"
            $ choices_log.append(("menu9", "Clicou Entregar o cabo de rede suspeito", renpy.get_game_runtime()))
            $ cabo_entregue = True
            show cabo_salo at right:
                xzoom -1
                zoom 0.4
                ypos 700
            pov "Na verdade, encontrei isto conectado ao meu monitor no dia da batida policial."
            play sound "ui.ogg"
            adv "{b}Interessante…{/b} Cabo blindado com serial raspado."
            play sound "ui.ogg"
            adv "{i}Vou levar ao laboratório forense agora mesmo. Pode ser a chave para provar sua inocência.{/i}"
            play sound "ui.ogg"
            n "Dr. Torres guarda cuidadosamente o cabo em um envelope antiestático."
            play sound "ui.ogg"
            adv "{i}Avisarei assim que tiver resultados. Continue concentrado na Lumi.{/i}"
            play sound "ui.ogg"

        "Não mencionar o cabo ainda":
            play sound "menu.ogg"
            $ cabo_entregue = False
            $ choices_log.append(("menu9", "Clicou Não mencionar o cabo ainda", renpy.get_game_runtime()))
            pov "{i}Por ora nada de diferente, doutor.{/i}"
            play sound "ui.ogg"
            adv "{i}Entendo. Se lembrar de algo, me avise. Cada detalhe conta.{/i}"
            play sound "ui.ogg"
            n "Você sente o peso da decisão de manter o cabo guardado — talvez precise dele mais adiante."
            play sound "ui.ogg"

    # --- TRANSIÇÃO DE VOLTA À MISSÃO -----------------------------------------
    scene salareuniaolumi with fade
    stop music fadeout 1
    n "No dia seguinte, a equipe retorna à sala espelhada para sintetizar os insights de Empatia."
    play sound "ui.ogg"
    scene salareuniaolumi with dissolve:
        matrixcolor SaturationMatrix(0)
    show lauracontraposto at center with dissolve:
        zoom 0.5
    l "Muitas boas ideias! vamos prototipar"
    play sound "ui.ogg"
    hide lauracontraposto with dissolve
    show gio at center with dissolve:
        zoom 0.37
    gi "Gente, tudo isso poderia acontecer em um evento"
    play sound "ui.ogg"
    hide gio
    show lauracontraposto at center:
        zoom 0.5
    l "Também acho, até porque uma das dores era falta de presença humana"
    play sound "ui.ogg"
    l "O principal deve ser o CEO admitindo o erro, depois mostramos números, médicos convidados e, por fim, as próximas ações."
    play sound "ui.ogg"
    hide lauracontraposto
    show douglas at center:
        zoom 0.4
    doug "Gostei, Sugiro dividir-mos as tarefas de cada solução primeiro"
    play sound "ui.ogg"
    doug "E eu posso colocar um portal no ar ao mesmo tempo, assim, quem assiste já testa os dados na hora."
    play sound "ui.ogg"
    hide douglas
    show maxx feliz at center:
        zoom 0.5
    m "• Eu cuido de chamar {b}Influencers{/b} para {b}refutar fake news{/b}."
    play sound "ui.ogg"
    hide maxx
    show gio at center:
        zoom 0.3
    gi "• Eu monto os {b}infográficos com o parecer da ANVISA sobre se vai multar a Lumi ou não{/b} — linguagem simples para os investidores."
    play sound "ui.ogg"
    hide gio
    show douglas at center:
        zoom 0.4
    doug "• Eu desenvolvo o {b}Portal de Transparência{/b} com dados brutos e filtros em tempo real."
    play sound "ui.ogg"
    l  "• Eu entro em contato para organizarem um {b}curso rápido para médicos{/b} poderem administrar o remédio com menos risco."
    play sound "ui.ogg"
    hide doug
    scene salareuniaolumi with dissolve
    pov "• E eu, [povname], redijo o {b}discurso de abertura{/b} que o CEO lerá na conferência."
    play sound "ui.ogg"

    jump prototipacao_lumi


label prototipacao_lumi:
    scene black with dissolve
    play music "blackscreen.ogg"
    show text "{b}Fase:{/b} Protoripação" with fade
    pause 1
    scene bg folha with fade
    n "O CEO da Lumi, Sr. Andra, irá falar publicamente pela primeira vez desde o incidente."
    play sound "ui.ogg"
    n "Mas ele não pode improvisar. As palavras precisam ser calculadas"
    n "devem ser baseadas nos relatos que você e sua equipe colheram: {b}a dor dos pacientes, o medo dos investidores e a urgência de clareza pública.{/b}"
    play sound "ui.ogg"
    n "Sua tarefa é redigir o {b}discurso oficial{/b} que será lido ao vivo. Estruture-o com lógica, tom humano e informações verificáveis."
    play sound "ui.ogg"
    call screen minigame_lumi
    scene bg folhacheia with dissolve
    pause 2
    n "Parabéns! Texto finalizado."
    play sound "ui.ogg"
    scene bg folhastetic at pan_left_slow with dissolve:
        zoom 1.2
    
    n "O conteúdo que você entregou será lido por Sr. Andre diante da imprensa nacional e internacional."
    play sound "ui.ogg"
    n "Esse texto marca a primeira exposição pública da Lumi após a crise, servindo como base para reposicionar a narrativa da empresa."
    stop music fadeout 2
    play sound "ui.ogg"
    #Protótipo de coletiva de imprensa improvisada
    #– Personagens-repórteres lançam perguntas em balões flutuantes; jogador escolhe uma de três respostas pré-escritas e vê instantaneamente um medidor de credibilidade subir ou cair (protótipo de diálogo).
    #– Inspira-se em “wizard-of-oz” testing: simula interação real sem back-end.
    jump testagem_lumi



# ---------------------------------------------------------------------------
#  Fase de Teste – Missão Lumi
#  Objetivo: Validar os protótipos de transparência com stakeholders reais
#  (investidores, pacientes, influenciadores científicos e imprensa).
# ---------------------------------------------------------------------------

label testagem_lumi:

    scene black with fade
    show text "{b}Fase: {/b}Testagem" with fade
    pause 2

    # --- CHEGADA DOS STAKEHOLDERS ----------------------------------------
    scene bg lumi_externo with dissolve:
        ypos 1
        zoom 0.7
    play music "lumi.ogg" fadein 0.5
    n "{b}Dia Seguinte{/b}\n{b}Local:{/b} Auditório Lumi – Ala de Pesquisa\n{b}Horário:{/b} 10h00"
    play sound "ui.ogg"
    scene bg auditorio at pan_left_slow with dissolve:
        zoom 1.3
    n "Um público aguarda no salão: investidores, pacientes, jornalistas de saúde e dois influenciadores científicos."
    play sound "ui.ogg"

    # ───────────────────────── SOLUÇÃO 3 — ROSTO HUMANO (CEO) + 5 — COMUNICADO OFICIAL ─────────────────────────

    scene bg coletiva1 with dissolve
    show coletiva2 zorder 11
    show lceo at center with dissolve:
        zoom 0.2
        ypos 560
        xpos 1200
    n "O salão fervilha: hashtags sobre a ‘pílula venenosa’ dominam a internet e repórteres especulam ao vivo. Todos aguardam, ansiosos, a palavra oficial do CEO da Lumi, {b}Sr. Andre{/b}."
    play sound "ui.ogg"
    stop music fadeout 1

    ceoL "Boa tarde a todos."
    play sound "ui.ogg"
    play music "discusso.ogg" fadein 1
    show lceo triste
    ceoL "Nos últimos dias, circularam rumores alarmantes sobre nosso medicamento e a triste morte do Sr. Elias."
    play sound "ui.ogg"
    show lceo
    ceoL "Hoje trago fatos claros e assumo total responsabilidade por esclarecê-los..."
    play sound "ui.ogg"
    scene black with fade
    pause 2
    scene bg coletiva1 with dissolve
    show coletiva2 zorder 11
    show lceo at center:
        zoom 0.2
        ypos 560
        xpos 1200
    show flash at flash_effect zorder 12:
        ypos 550
        xpos 300
    show flashed at quickshow:
        zoom 2
    # Reação da plateia
  # (silhueta de plateia murmurando)
    play sound "flashes.ogg"
    n "Câmeras disparam flashes. Murmúrios diminuem à medida que as palavras do CEO soam firmes e diretas."
    play sound "ui.ogg"
    "{b}Repórter Silva{/b}" "Sr. Andre, o portal mostrará também os eventos adversos futuros?"
    play sound "ui.ogg"
    ceoL "Sim. Todos os dados, bons ou ruins, aparecerão lá em tempo real."
    play sound "ui.ogg"
    play sound "claps.ogg" fadein 2
    n "Uma salva de palmas ecoa; manchetes em tempo real trocam ‘silêncio suspeito’ por ‘CEO se explica’."
    play sound "ui.ogg"
    scene bg dougpresentation1 with dissolve
    stop music fadeout 1
    n "mais tarde, Doug anuncia o portal de dados da Lumi"
    play sound "ui.ogg"
    play music "lumi.ogg"
    doug "{b}Senhoras e senhores, este é o novo Portal de Transparência da Lumi.{/b}"
    play sound "ui.ogg"
    scene bg dougpresentation2
    doug "{i}Por que isso importa?{/i} Porque até ontem, quem quisesse entender nossos números precisava confiar em um PDF de sete páginas e muita linguagem técnica."
    play sound "ui.ogg"
    doug "Agora, qualquer pessoa — paciente, médico ou investidor — pode ver, em tempo real, "
    play sound "ui.ogg"
    scene bg dougpresentation1
    doug "{i}quantas caixas foram vendidas, quantas reações graves ocorreram e como isso se compara à média do mercado.{/i}"
    play sound "ui.ogg"
    doug "Isso resolve nosso maior gargalo de confiança: {b}a sensação de que escondíamos dados.{/b}"
    play sound "ui.ogg"
    scene bg dougpresentation2
    doug "Transparência não é caridade, é estratégia: quando o público entende a proporção real — as fake news param"
    play sound "ui.ogg"
    scene bg dougpresentation2 at pan_left_slow:
        zoom 1.2
    n "Investidores passeiam pelo painel; ao aplicar filtros, o gráfico exibe a taxa 0,1 porcento em destaque e um comparativo com outras farmacêuticas."
    play sound "ui.ogg"
    scene bg dougpresentation2 with dissolve:
        matrixcolor SaturationMatrix(0)
    show invest_costa default at center with dissolve:
        zoom 0.4
    "{b}Investidora Sra. Costa{/b}" "Ver números crus sem nem fazer login já muda o jogo. Adicionem um botão de download para eu anexar nos meus relatórios, por favor."
    play sound "ui.ogg"
    hide invest_costa with dissolve
    scene bg dougpresentation2 with dissolve
    n "Resultado: {b}93 porcento{/b} dos participantes disseram ‘agora entendo os dados’; a equipe anotou o pedido de exportação para a próxima versão."
    play sound "ui.ogg"
    scene bg maxpres1 with dissolve
    # MAX
    m "Convidamos médicos populares na internet para explicar, em termos simples, por que o remédio continua seguro."
    play sound "ui.ogg"
    scene bg maxpres2
    n "Clipes curtos aparecem no telão:"
    "{b}Dr. Pedro – Cardiologista{/b}" "O caso triste não foi culpa do remédio. O paciente já tinha um problema no coração que quase ninguém tem."
    play sound "ui.ogg"
    "{b}Dra. Braga – Influencer de Saúde{/b}" "Hospital errou ao aplicar sem checar histórico genético. O produto da Lumi, dentro da bula, é confiável."
    play sound "ui.ogg"
    scene bg maxpres1
    n "Os clipes encerram com a hashtag {i}#FatoNãoFicção{/i}."
    play sound "ui.ogg"
    scene bg maxpres1 with dissolve:
        matrixcolor SaturationMatrix(0)
    n "Resultado: {b}88 porcento{/b} dizem sentir ‘mais clareza’; queda de 30 porcento nos comentários culpando a Lumi nas redes."
    play sound "ui.ogg"

# ───────────────────────── SOLUÇÃO 4 — CURSO PARA MÉDICOS - LAURA ─────────────────────────
    scene bg aulamedico at pan_right_slow with dissolve:
        zoom 1.3
    n "Professores convidados ministram uma aula completa de 45 minutos para alunos de Medicina: demonstram a dose correta, o monitoramento do paciente e o momento de checar histórico genético."
    play sound "ui.ogg"
    scene bg remedioefeitos at pan_left_slow with dissolve:
        zoom 1.3
    n "No telão, slides simples mostram a ação do remédio no corpo e destacam, em vermelho, o aviso sobre predisposição rara."
    play sound "ui.ogg"
    "{b}Enfermeira Rosa{/b}" "Gostei: conteúdo direto ao ponto. Se puderem pôr legenda maior, fica perfeito."
    play sound "ui.ogg"
    n "Resultado: {b}92 porcento{/b} dos presentes aprovam o material; legenda maior será implementada."
    play sound "ui.ogg"

# ───────────────────────── SOLUÇÃO 6 — PROTOCOLO ANVISA EXPLICADO - GI ─────────────────────────
    scene bg gianvisa at pan_right_slow with fade:
        zoom 1.1
    gi "{b}Solução 6 — Parecer dos Órgãos de Saúde{/b}\nMostramos o papel que recebemos da ANVISA e outras autoridades."
    play sound "ui.ogg"
    scene bg anvisa with dissolve
    gi "Ele diz, em palavras simples: ‘Produto segue liberado. Empresa agiu certo. Vamos só acompanhar de perto nos próximos meses’."
    play sound "ui.ogg"
    "{b}Investidor Almeida{/b}" "Então nada de multa, nem suspensão?"
    play sound "ui.ogg"
    gi "Não. A agência confirmou que, com essas medidas, não há punição."
    play sound "ui.ogg"
    scene bg anvisa with dissolve:
        matrixcolor SaturationMatrix(0)
    n "Resultado: {b}77 porcento{/b} dos investidores afirmam que o medo de sanção caiu; cópia do documento será publicada no portal."
    play sound "ui.ogg"


    # Bastidores — equipe BRComorg
    scene salareuniaolumi with fade
    show lauracontraposto at center:
        zoom 0.34
    stop music fadeout 1
    l "{i}Texto saiu como planejado. Boa, time!{/i}"
    play sound "ui.ogg"
    show gio feliz at left:
        zoom 0.34
    gi "{i}A mídia deu bom retorno. Agora é monitorar as redes.{/i}"
    play sound "ui.ogg"
    show maxx at right:
        zoom 0.34
    m "{i}Roteiro aprovado e entregue. Vamos acompanhar os indicadores de confiança em tempo real.{/i}"
    play sound "ui.ogg"
    n "Você sente um leve alívio: o discurso que a BRComorg escreveu atingiu o tom exato entre empatia e responsabilidade."
    play sound "ui.ogg"



    scene black with fade
    play sound "missaoconcluida.ogg"
    show text "{b}MISSÃO LUMI CONCLUÍDA!{/b}" at truecenter with fade
    pause 2
    $ lumicompleto = True
    call screen missoes
    return
