################################################################################
## Inicialização
################################################################################

init offset = -1


################################################################################
## Estilos
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Telas no jogo
################################################################################


## Diga a tela #################################################################
##
## A tela say é usada para exibir o diálogo para o jogador. Ela recebe dois
## parâmetros, who e what, que são o nome do personagem que fala e o texto a ser
## exibido, respectivamente. (O parâmetro who pode ser None (Nenhum) se nenhum
## nome for fornecido).
##
## Essa tela deve criar um texto exibível com o id "what", pois o Ren'Py o
## utiliza para gerenciar a exibição de texto. Ela também pode criar exibíveis
## com id "who" e id "window" para aplicar propriedades de estilo.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Se houver uma imagem lateral, exiba-a acima do texto. Não exiba na
    ## variante do telefone - não há espaço.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Disponibilize a caixa de nome para estilização por meio do objeto Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    top_padding 20

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False


## Tela de entrada #############################################################
##
## Essa tela é usada para exibir renpy.input. O parâmetro prompt é usado para
## passar um prompt de texto.
##
## Essa tela deve criar um displayable de entrada com id "input" para aceitar os
## vários parâmetros de entrada.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Tela de escolha #############################################################
##
## Essa tela é usada para exibir as opções no jogo apresentadas pela instrução
## de menu. O único parâmetro, itens, é uma lista de objetos, cada um com campos
## de legenda e ação.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Tela do menu rápido #########################################################
##
## O menu rápido é exibido no jogo para fornecer acesso fácil aos menus fora do
## jogo.

screen quick_menu():

    ## Certifique-se de que isso apareça na parte superior de outras telas.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Voltar") action Rollback()
            textbutton _("Histórico") action ShowMenu('history')
            textbutton _("Pular") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Automotivo") action Preference("auto-forward", "toggle")
            textbutton _("Salvar") action ShowMenu('save')
            textbutton _("Q.Salvar") action QuickSave()
            textbutton _("Q. Carga") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## Esse código garante que a tela quick_menu seja exibida no jogo, sempre que o
## jogador não tiver ocultado explicitamente a interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Telas do menu principal e do menu do jogo
################################################################################

## Tela de navegação ###########################################################
##
## Essa tela está incluída nos menus principal e do jogo e fornece navegação
## para outros menus e para iniciar o jogo.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Início") action Start()

        else:

            textbutton _("Histórico") action ShowMenu("history")

            textbutton _("Salvar") action ShowMenu("save")

        textbutton _("Carga") action ShowMenu("load")

        textbutton _("Preferências") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Fim da reprodução") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menu principal") action MainMenu()

        textbutton _("Sobre") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## A ajuda não é necessária ou relevante para dispositivos móveis.
            textbutton _("Ajuda") action ShowMenu("help")

        if renpy.variant("pc"):

            ## O botão Sair é proibido no iOS e desnecessário no Android e na
            ## Web.
            textbutton _("Sair") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Tela do menu principal ######################################################
##
## Usado para exibir o menu principal quando o Ren'Py é iniciado.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu










# ---------------------------------------------------------------------------
# memory_game.rpy  –  Minigame de Memória (Problema ⇄ Solução)
# Grid 4×3 (12 cartas, 6 pares). Cada carta original: 979×1510 px.
# As cartas são redimensionadas para caber em 1280×720 (16:9) usando
# largura≈123 px, altura≈190 px, com espaçamento de 15 px.
# Verso: imagem "card-back.png" em images/.
# Faces viradas: imagens "prob01.png", "sol01.png", etc.
# Destaque de match: variantes "prob01h.png", "sol01h.png", etc., em cards/.
# ---------------------------------------------------------------------------

init:
    transform highlight:
        # aumenta e retorna ao normal em loop
        linear 0.25 zoom 1.03
        linear 0.25 zoom 1.00
        repeat

# --------------------  DECLARAÇÕES DE IMAGEM  ------------------------------
init python:
    # verso genérico
    renpy.image("card_back", "cards/card-back.png")

    # Faces dos pares: problemas e soluções
    renpy.image("prob01",  "cards/prob01.png")
    renpy.image("sol01",   "cards/sol01.png")
    renpy.image("prob02",  "cards/prob02.png")
    renpy.image("sol02",   "cards/sol02.png")
    renpy.image("prob03",  "cards/prob03.png")
    renpy.image("sol03",   "cards/sol03.png")
    renpy.image("prob04",  "cards/prob04.png")
    renpy.image("sol04",   "cards/sol04.png")
    renpy.image("prob05",  "cards/prob05.png")
    renpy.image("sol05",   "cards/sol05.png")
    renpy.image("prob06",  "cards/prob06.png")
    renpy.image("sol06",   "cards/sol06.png")

    # Variantes destacadas para match_found
    renpy.image("prob01h", "cards/prob01h.png")
    renpy.image("sol01h",  "cards/sol01h.png")
    renpy.image("prob02h", "cards/prob02h.png")
    renpy.image("sol02h",  "cards/sol02h.png")
    renpy.image("prob03h", "cards/prob03h.png")
    renpy.image("sol03h",  "cards/sol03h.png")
    renpy.image("prob04h", "cards/prob04h.png")
    renpy.image("sol04h",  "cards/sol04h.png")
    renpy.image("prob05h", "cards/prob05h.png")
    renpy.image("sol05h",  "cards/sol05h.png")
    renpy.image("prob06h", "cards/prob06h.png")
    renpy.image("sol06h",  "cards/sol06h.png")

# --------------------  VARIÁVEIS GLOBAIS  ----------------------------------
default card_rows       = 4
default card_cols       = 3
default card_amount     = card_rows * card_cols   # 12

# --------------------  FUNÇÕES PYTHON  -------------------------------------
init python:
    import random

    # Estado do jogo
    cards           = []
    selected_cards  = []
    hidden_cards    = 0
    match_found     = False
    game_finished   = False

    def randomize_cards():
        """Preenche 'cards' com 6 pares e embaralha."""
        global cards, selected_cards, hidden_cards, match_found, game_finished
        cards, selected_cards = [], []
        hidden_cards  = 0
        match_found   = False
        game_finished = False

        pairs = [
            ("prob01", "sol01"),
            ("prob02", "sol02"),
            ("prob03", "sol03"),
            ("prob04", "sol04"),
            ("prob05", "sol05"),
            ("prob06", "sol06"),
        ]
        for idx, (prob, sol) in enumerate(pairs, start=1):
            cards.append([prob, idx, "deselected", "visible"])
            cards.append([sol,  idx, "deselected", "visible"])
        random.shuffle(cards)

    def select_card(card_index):
        """Seleciona carta caso ainda haja menos de duas selecionadas."""
        global selected_cards, match_found

        if len(selected_cards) >= 2:
            return
        if cards[card_index][3] == "hidden" or cards[card_index][2] == "selected":
            return

        cards[card_index][2] = "selected"
        selected_cards.append(card_index)

        if len(selected_cards) == 2:
            i, j = selected_cards
            match_found = (cards[i][1] == cards[j][1])

    def deselect_cards():
        """Desvira cartas não correspondentes."""
        global selected_cards
        for idx in selected_cards:
            if cards[idx][3] != "hidden":
                cards[idx][2] = "deselected"
        selected_cards = []

    def hide_matches():
        """Oculta pares corretos e verifica fim de jogo."""
        global selected_cards, hidden_cards, match_found, game_finished
        for idx in selected_cards:
            cards[idx][3] = "hidden"
            cards[idx][2] = "deselected"
        hidden_cards += 2
        selected_cards = []
        match_found     = False
        if hidden_cards >= card_amount:
            game_finished = True

    def reset_memory_game():
        """Reinicia o jogo."""
        randomize_cards()

    # Inicializa cartas
    randomize_cards()

# --------------------  SCREEN DO JOGO  -------------------------------------
screen memory_game():
    tag memory

    # Dimensões da carta
    $ CW = 314
    $ CH = 204

    vbox:
        align (0.5, 0.05)
        # Use markup Ren'Py correto {b}…{/b}
        text "Encontre os pares {b}Problema ⇄ Solução{/b}" size 40

    fixed:
        align (0.5, 0.5)

        grid card_rows card_cols spacing 15 xalign 0.5 yalign 0.5:
            transpose False

            for i, card in enumerate(cards):
                $ hidden   = (card[3] == "hidden")
                $ face_up  = (card[2] == "selected") or hidden
                $ is_high  = (match_found and i in selected_cards)

                if hidden:
                    null width CW height CH

                elif face_up:
                    button:
                        background None
                        xysize (CW, CH)
                        if is_high:
                            # usa a imagem ending em 'h' com animação
                            add card[0] + "h" at highlight
                        else:
                            add card[0]
                        action None
                        sensitive False


                else:
                    imagebutton:
                        idle "card_back"
                        hover "card_back"
                        xysize (CW, CH)
                        action Function(select_card, i)

    if len(selected_cards) == 2:
        # delay maior para match_found, menor caso contrário
        $ delay = 3.0 if match_found else 0.7
        timer delay action If(match_found, Function(hide_matches), Function(deselect_cards))

    if game_finished:
        frame:
            align (0.5, 0.5)
            padding (100, 100)
            vbox:
                textbutton "Parabéns!\nVocê completou a fase da ideação!\nContinuar" action Return(True)





# MEMORY GAME 2

# --------------------  DECLARAÇÕES DE IMAGEM  ------------------------------
init python:
    # verso genérico
    renpy.image("card_back", "cards/card-back.png")

    # Faces dos pares: problemas e soluções
    renpy.image("lumi/prob01",  "lumi/cards/prob01.png")
    renpy.image("lumi/sol01",   "lumi/cards/sol01.png")
    renpy.image("lumi/prob02",  "lumi/cards/prob02.png")
    renpy.image("lumi/sol02",   "lumi/cards/sol02.png")
    renpy.image("lumi/prob03",  "lumi/cards/prob03.png")
    renpy.image("lumi/sol03",   "lumi/cards/sol03.png")
    renpy.image("lumi/prob04",  "lumi/cards/prob04.png")
    renpy.image("lumi/sol04",   "lumi/cards/sol04.png")
    renpy.image("lumi/prob05",  "lumi/cards/prob05.png")
    renpy.image("lumi/sol05",   "lumi/cards/sol05.png")
    renpy.image("lumi/prob06",  "lumi/cards/prob06.png")
    renpy.image("lumi/sol06",   "lumi/cards/sol06.png")

    # Variantes destacadas para match_found
    renpy.image("lumi/prob01h", "lumi/cards/prob01h.png")
    renpy.image("lumi/sol01h",  "lumi/cards/sol01h.png")
    renpy.image("lumi/prob02h", "lumi/cards/prob02h.png")
    renpy.image("lumi/sol02h",  "lumi/cards/sol02h.png")
    renpy.image("lumi/prob03h", "lumi/cards/prob03h.png")
    renpy.image("lumi/sol03h",  "lumi/cards/sol03h.png")
    renpy.image("lumi/prob04h", "lumi/cards/prob04h.png")
    renpy.image("lumi/sol04h",  "lumi/cards/sol04h.png")
    renpy.image("lumi/prob05h", "lumi/cards/prob05h.png")
    renpy.image("lumi/sol05h",  "lumi/cards/sol05h.png")
    renpy.image("lumi/prob06h", "lumi/cards/prob06h.png")
    renpy.image("lumi/sol06h",  "lumi/cards/sol06h.png")

# --------------------  VARIÁVEIS GLOBAIS  ----------------------------------
default card_rows_lumi       = 4
default card_cols_lumi       = 3
default card_amount_lumi     = card_rows_lumi * card_cols_lumi   # 12

# --------------------  FUNÇÕES PYTHON  -------------------------------------
init python:
    import random

    # Estado do jogo
    cards_lumi           = []
    selected_cards_lumi  = []
    hidden_cards_lumi    = 0
    match_found_lumi     = False
    game_finished_lumi   = False

    def randomize_cards_lumi():
        """Preenche 'cards' com 6 pares e embaralha."""
        global cards_lumi, selected_cards_lumi, hidden_cards_lumi, match_found_lumi, game_finished_lumi
        cards_lumi, selected_cards_lumi = [], []
        hidden_cards_lumi  = 0
        match_found_lumi   = False
        game_finished_lumi = False

        pairs_lumi = [
            ("lumi/prob01", "lumi/sol01"),
            ("lumi/prob02", "lumi/sol02"),
            ("lumi/prob03", "lumi/sol03"),
            ("lumi/prob04", "lumi/sol04"),
            ("lumi/prob05", "lumi/sol05"),
            ("lumi/prob06", "lumi/sol06"),
        ]
        for idx_lumi, (prob_lumi, sol_lumi) in enumerate(pairs_lumi, start=1):
            cards_lumi.append([prob_lumi, idx_lumi, "deselected", "visible"])
            cards_lumi.append([sol_lumi,  idx_lumi, "deselected", "visible"])
        random.shuffle(cards_lumi)

    def select_card_lumi(card_index_lumi):
        """Seleciona carta caso ainda haja menos de duas selecionadas."""
        global selected_cards_lumi, match_found_lumi

        if len(selected_cards_lumi) >= 2:
            return
        if cards_lumi[card_index_lumi][3] == "hidden" or cards_lumi[card_index_lumi][2] == "selected":
            return

        cards_lumi[card_index_lumi][2] = "selected"
        selected_cards_lumi.append(card_index_lumi)

        if len(selected_cards_lumi) == 2:
            i_lumi, j_lumi = selected_cards_lumi
            match_found_lumi = (cards_lumi[i_lumi][1] == cards_lumi[j_lumi][1])

    def deselect_cards_lumi():
        """Desvira cartas não correspondentes."""
        global selected_cards_lumi
        for idx_lumi in selected_cards_lumi:
            if cards_lumi[idx_lumi][3] != "hidden":
                cards_lumi[idx_lumi][2] = "deselected"
        selected_cards_lumi = []

    def hide_matches_lumi():
        """Oculta pares corretos e verifica fim de jogo."""
        global selected_cards_lumi, hidden_cards_lumi, match_found_lumi, game_finished_lumi
        for idx_lumi in selected_cards_lumi:
            cards_lumi[idx_lumi][3] = "hidden"
            cards_lumi[idx_lumi][2] = "deselected"
        hidden_cards_lumi += 2
        selected_cards_lumi = []
        match_found_lumi     = False
        if hidden_cards_lumi >= card_amount_lumi:
            game_finished_lumi = True

    def reset_memory_game_lumi():
        """Reinicia o jogo."""
        randomize_cards_lumi()

    # Inicializa cartas
    randomize_cards_lumi()

# --------------------  SCREEN DO JOGO  -------------------------------------
screen memory_game_lumi():
    tag memory_lumi

    # Dimensões da carta
    $ CW_lumi = 314
    $ CH_lumi = 204

    vbox:
        align (0.5, 0.05)
        # Use markup Ren'Py correto {b}…{/b}
        text "Seção {b}BrainStorm{/b}" size 40

    fixed:
        align (0.5, 0.5)

        grid card_rows_lumi card_cols_lumi spacing 15 xalign 0.5 yalign 0.5:
            transpose False

            for i_lumi, card_lumi in enumerate(cards_lumi):
                $ hidden_lumi   = (card_lumi[3] == "hidden")
                $ face_up_lumi  = (card_lumi[2] == "selected") or hidden_lumi
                $ is_high_lumi  = (match_found_lumi and i_lumi in selected_cards_lumi)

                if hidden_lumi:
                    null width CW_lumi height CH_lumi

                elif face_up_lumi:
                    button:
                        background None
                        xysize (CW_lumi, CH_lumi)
                        if is_high_lumi:
                            # usa a imagem ending em 'h' com animação
                            add card_lumi[0] + "h" at highlight
                        else:
                            add card_lumi[0]
                        action None
                        sensitive False


                else:
                    imagebutton:
                        idle "card_back"
                        hover "card_back"
                        xysize (CW_lumi, CH_lumi)
                        action Function(select_card_lumi, i_lumi)

    if len(selected_cards_lumi) == 2:
        # delay maior para match_found, menor caso contrário
        $ delay = 3.0 if match_found_lumi else 0.7
        timer delay action If(match_found_lumi, Function(hide_matches_lumi), Function(deselect_cards_lumi))

    if game_finished_lumi:
        frame:
            align (0.5, 0.5)
            padding (100, 100)
            vbox:
                textbutton "Parabéns!\nVocê completou a fase da ideação!\nContinuar" action Return(True)







# MEMORY GAME 3

# --------------------  DECLARAÇÕES DE IMAGEM  ------------------------------
init python:
    # verso genérico
    renpy.image("card_back", "cards/card-back.png")

    # Faces dos pares: problemas e soluções
    renpy.image("solemar/prob01",  "solemar/cards/prob01.png")
    renpy.image("solemar/sol01",   "solemar/cards/sol01.png")
    renpy.image("solemar/prob02",  "solemar/cards/prob02.png")
    renpy.image("solemar/sol02",   "solemar/cards/sol02.png")
    renpy.image("solemar/prob03",  "solemar/cards/prob03.png")
    renpy.image("solemar/sol03",   "solemar/cards/sol03.png")
    renpy.image("solemar/prob04",  "solemar/cards/prob04.png")
    renpy.image("solemar/sol04",   "solemar/cards/sol04.png")
    renpy.image("solemar/prob06",  "solemar/cards/prob06.png")
    renpy.image("solemar/sol06",   "solemar/cards/sol06.png")

    # Variantes destacadas para match_found
    renpy.image("solemar/prob01h", "solemar/cards/prob01h.png")
    renpy.image("solemar/sol01h",  "solemar/cards/sol01h.png")
    renpy.image("solemar/prob02h", "solemar/cards/prob02h.png")
    renpy.image("solemar/sol02h",  "solemar/cards/sol02h.png")
    renpy.image("solemar/prob03h", "solemar/cards/prob03h.png")
    renpy.image("solemar/sol03h",  "solemar/cards/sol03h.png")
    renpy.image("solemar/prob04h", "solemar/cards/prob04h.png")
    renpy.image("solemar/sol04h",  "solemar/cards/sol04h.png")
    renpy.image("solemar/prob06h", "solemar/cards/prob06h.png")
    renpy.image("solemar/sol06h",  "solemar/cards/sol06h.png")

# --------------------  VARIÁVEIS GLOBAIS  ----------------------------------
default card_rows_solemar       = 4
default card_cols_solemar       = 3
default card_amount_solemar     = 10  # 12

# --------------------  FUNÇÕES PYTHON  -------------------------------------
init python:
    import random

    # Estado do jogo
    cards_solemar           = []
    selected_cards_solemar  = []
    hidden_cards_solemar    = 0
    match_found_solemar     = False
    game_finished_solemar   = False

    def randomize_cards_solemar():
        """Preenche 'cards' com 5 pares e embaralha."""
        global cards_solemar, selected_cards_solemar, hidden_cards_solemar, match_found_solemar, game_finished_solemar
        cards_solemar, selected_cards_solemar = [], []
        hidden_cards_solemar  = 0
        match_found_solemar   = False
        game_finished_solemar = False

        #random.shuffle(cards_solemar) #Editado

        pairs_solemar = [
            ("solemar/prob01", "solemar/sol01"),
            ("solemar/prob02", "solemar/sol02"),
            ("solemar/prob03", "solemar/sol03"),
            ("solemar/prob04", "solemar/sol04"),
            ("solemar/prob06", "solemar/sol06"),
        ]
        for idx_solemar, (prob_solemar, sol_solemar) in enumerate(pairs_solemar, start=1):
            cards_solemar.append([prob_solemar, idx_solemar, "deselected", "visible"])
            cards_solemar.append([sol_solemar,  idx_solemar, "deselected", "visible"])
        random.shuffle(cards_solemar)

    def select_card_solemar(card_index_solemar):
        """Seleciona carta caso ainda haja menos de duas selecionadas."""
        global selected_cards_solemar, match_found_solemar

        if len(selected_cards_solemar) >= 2:
            return
        if cards_solemar[card_index_solemar][3] == "hidden" or cards_solemar[card_index_solemar][2] == "selected":
            return

        cards_solemar[card_index_solemar][2] = "selected"
        selected_cards_solemar.append(card_index_solemar)

        if len(selected_cards_solemar) == 2:
            i_solemar, j_solemar = selected_cards_solemar
            match_found_solemar = (cards_solemar[i_solemar][1] == cards_solemar[j_solemar][1])

    def deselect_cards_solemar():
        """Desvira cartas não correspondentes."""
        global selected_cards_solemar
        for idx_solemar in selected_cards_solemar:
            if cards_solemar[idx_solemar][3] != "hidden":
                cards_solemar[idx_solemar][2] = "deselected"
        selected_cards_solemar = []

    def hide_matches_solemar():
        """Oculta pares corretos e verifica fim de jogo."""
        global selected_cards_solemar, hidden_cards_solemar, match_found_solemar, game_finished_solemar
        for idx_solemar in selected_cards_solemar:
            cards_solemar[idx_solemar][3] = "hidden"
            cards_solemar[idx_solemar][2] = "deselected"
        hidden_cards_solemar += 2
        selected_cards_solemar = []
        match_found_solemar     = False
        if hidden_cards_solemar >= 10:
            game_finished_solemar = True

    def reset_memory_game_solemar():
        """Reinicia o jogo."""
        randomize_cards_solemar()

    # Inicializa cartas
    randomize_cards_solemar()

# --------------------  SCREEN DO JOGO  -------------------------------------
screen memory_game_solemar():
    tag memory_solemar

    # Dimensões da carta
    $ CW_solemar = 314
    $ CH_solemar = 204

    vbox:
        align (0.5, 0.05)
        # Use markup Ren'Py correto {b}…{/b}
        text "Seção de {b}BrainStorm{/b}" size 40

    fixed:
        align (0.5, 0.5)

        grid card_rows_solemar card_cols_solemar spacing 15 xalign 0.5 yalign 0.5:
            transpose False

            for i_solemar, card_solemar in enumerate(cards_solemar):
                $ hidden_solemar   = (card_solemar[3] == "hidden")
                $ face_up_solemar  = (card_solemar[2] == "selected") or hidden_solemar
                $ is_high_solemar  = (match_found_solemar and i_solemar in selected_cards_solemar)

                if hidden_solemar:
                    null width CW_solemar height CH_solemar

                elif face_up_solemar:
                    button:
                        background None
                        xysize (CW_solemar, CH_solemar)
                        if is_high_solemar:
                            # usa a imagem ending em 'h' com animação
                            add card_solemar[0] + "h" at highlight
                        else:
                            add card_solemar[0]
                        action None
                        sensitive False


                else:
                    imagebutton:
                        idle "card_back"
                        hover "card_back"
                        xysize (CW_solemar, CH_solemar)
                        action Function(select_card_solemar, i_solemar)

    if len(selected_cards_solemar) == 2:
        # delay maior para match_found, menor caso contrário
        $ delay = 3.0 if match_found_solemar else 0.7
        timer delay action If(match_found_solemar, Function(hide_matches_solemar), Function(deselect_cards_solemar))

    if game_finished_solemar:
        frame:
            align (0.5, 0.5)
            padding (100, 100)
            vbox:
                textbutton "Parabéns!\nVocê completou a fase da ideação!\nContinuar" action Return(True)








screen main_menu():

    ## Isso garante que qualquer outra tela de menu seja substituída.
    tag menu

    add gui.main_menu_background

    ## Esse quadro vazio escurece o menu principal.
    frame:
        style "main_menu_frame"

    ## A instrução de uso inclui outra tela dentro desta. O conteúdo real do
    ## menu principal está na tela de navegação.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Tela do menu do jogo ########################################################
##
## Isso estabelece a estrutura básica comum de uma tela de menu de jogo. Ela
## é chamada com o título da tela e exibe o plano de fundo, o título e a
## navegação.
##
## O parâmetro de rolagem pode ser Nenhum ou um dos parâmetros "viewport"
## ou "vpgrid". Essa tela deve ser usada com um ou mais filhos, que são
## transcluídos (colocados) dentro dela.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve espaço para a seção de navegação.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Voltar"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Sobre a tela ################################################################
##
## Essa tela fornece informações de crédito e direitos autorais sobre o jogo e
## Ren'Py.
##
## Não há nada de especial nessa tela e, portanto, ela também serve como exemplo
## de como criar uma tela personalizada.

screen about():

    tag menu

    ## Essa instrução de uso inclui a tela game_menu dentro desta. O filho vbox
    ## é então incluído na janela de visualização dentro da tela game_menu.
    use game_menu(_("Sobre"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versão [config.version!t]\n")

            ## gui.about é normalmente definido em options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Feito com {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] .\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Carregar e salvar telas #####################################################
##
## Essas telas são responsáveis por permitir que o jogador salve o jogo
## e o carregue novamente. Como elas têm quase tudo em comum, ambas são
## implementadas em termos de uma terceira tela, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Salvar"))


screen load():

    tag menu

    use file_slots(_("Carga"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Página {}"), auto=_("Salvamentos automáticos"), quick=_("Salvamentos rápidos"))

    use game_menu(title):

        fixed:

            ## Isso garante que a entrada receberá o evento enter antes de
            ## qualquer um dos botões.
            order_reverse True

            ## O nome da página, que pode ser editado clicando em um botão.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## A grade de slots de arquivo.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("slot vazio")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Botões para acessar outras páginas.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) fornece os números de 1 a 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Baixar o Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Tela de preferências ########################################################
##
## A tela de preferências permite que o jogador configure o jogo para se adequar
## melhor.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferências"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Tela")
                        textbutton _("Janela") action Preference("display", "window")
                        textbutton _("Tela cheia") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Pular")
                    textbutton _("Texto invisível") action Preference("skip", "toggle")
                    textbutton _("Após as escolhas") action Preference("after choices", "toggle")
                    textbutton _("Transições") action InvertSelected(Preference("transitions", "toggle"))

                ## Vboxes adicionais do tipo "radio_pref" ou "check_pref" podem
                ## ser adicionadas aqui para acrescentar outras preferências
                ## definidas pelo criador.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Velocidade do texto")

                    bar value Preference("text speed")

                    label _("Tempo de encaminhamento automático")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Volume da música")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volume do som")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Teste") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Volume da voz")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Teste") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Silenciar tudo"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Tela de histórico ###########################################################
##
## Essa é uma tela que exibe o histórico de diálogo para o jogador. Embora não
## haja nada de especial nessa tela, ela precisa acessar o histórico de diálogo
## armazenado em _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Evite prever essa tela, pois ela pode ser muito grande.
    predict False

    use game_menu(_("Histórico"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Isso organiza as coisas corretamente se history_height for
                ## None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Pegue a cor do texto who do caractere, se definido.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("O histórico de diálogo está vazio.")


## Isso determina quais tags podem ser exibidas na tela de histórico.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Tela de ajuda ###############################################################
##
## Uma tela que fornece informações sobre as combinações de teclas e mouse. Ela
## usa outras telas (keyboard_help, mouse_help e gamepad_help) para exibir a
## ajuda real.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Ajuda"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Teclado") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Controle de jogo") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Entrar")
        text _("Avança o diálogo e ativa a interface.")

    hbox:
        label _("Espaço")
        text _("Avança o diálogo sem selecionar opções.")

    hbox:
        label _("Teclas de seta")
        text _("Navegue pela interface.")

    hbox:
        label _("Fuga")
        text _("Acessa o menu do jogo.")

    hbox:
        label _("Ctrl")
        text _("Pula o diálogo quando pressionado.")

    hbox:
        label _("Tab")
        text _("Alterna o salto de diálogo.")

    hbox:
        label _("Página para cima")
        text _("Volta ao diálogo anterior.")

    hbox:
        label _("Página para baixo")
        text _("Rola para frente o diálogo posterior.")

    hbox:
        label "H"
        text _("Oculta a interface do usuário.")

    hbox:
        label "S"
        text _("Faz uma captura de tela.")

    hbox:
        label "V"
        text _("Alterna a assistência {a=https://www.renpy.org/l/voicing}auto-voz{/a}.")

    hbox:
        label "Shift+A"
        text _("Abre o menu de acessibilidade.")


screen mouse_help():

    hbox:
        label _("Clique com o botão esquerdo do mouse")
        text _("Avança o diálogo e ativa a interface.")

    hbox:
        label _("Clique no meio")
        text _("Oculta a interface do usuário.")

    hbox:
        label _("Clique com o botão direito do mouse")
        text _("Acessa o menu do jogo.")

    hbox:
        label _("Roda do mouse para cima\nClique em Rollback Side")
        text _("Volta ao diálogo anterior.")

    hbox:
        label _("Roda do mouse para baixo")
        text _("Rola para frente o diálogo posterior.")


screen gamepad_help():

    hbox:
        label _("Gatilho direito\nBotão A/inferior")
        text _("Avança o diálogo e ativa a interface.")

    hbox:
        label _("Gatilho esquerdo\nOmbro esquerdo")
        text _("Volta ao diálogo anterior.")

    hbox:
        label _("Ombro direito")
        text _("Rola para frente o diálogo posterior.")

    hbox:
        label _("D-Pad, bastões")
        text _("Navegue pela interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Acessa o menu do jogo.")

    hbox:
        label _("Botão Y/Top")
        text _("Oculta a interface do usuário.")

    textbutton _("Calibrar") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Telas adicionais
################################################################################


## Confirmar tela ##############################################################
##
## A tela de confirmação é chamada quando Ren'Py quer fazer uma pergunta de sim
## ou não ao jogador.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Certifique-se de que outras telas não recebam entrada enquanto essa tela
    ## estiver sendo exibida.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Sim") action yes_action
                textbutton _("Não") action no_action

    ## Clique com o botão direito do mouse e escape a resposta "não".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Pular a tela do indicador ###################################################
##
## A tela skip_indicator é exibida para indicar que o salto está em andamento.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Pular")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Essa transformação é usada para piscar as setas uma após a outra.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Temos que usar uma fonte que tenha o glifo BLACK RIGHT-POINTING SMALL
    ## TRIANGLE.
    font "DejaVuSans.ttf"


## Tela de notificação #########################################################
##
## A tela de notificação é usada para mostrar uma mensagem ao jogador. (Por
## exemplo, quando o jogo é salvo rapidamente ou quando uma captura de tela é
## feita).
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Tela NVL ####################################################################
##
## Essa tela é usada para o diálogo e os menus do modo NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Exibe o diálogo em uma vpgrid ou na vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Exibe o menu, se fornecido. O menu poderá ser exibido incorretamente
        ## se config.narrator_menu estiver definido como True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Isso controla o número máximo de entradas do modo NVL que podem ser exibidas
## de uma vez.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Tela de bolhas ##############################################################
##
## A tela de balão é usada para exibir o diálogo para o jogador ao usar balões
## de fala. A tela de bolhas recebe os mesmos parâmetros que a tela de dizer,
## deve criar um exibível com o ID de "what" e pode criar exibíveis com os IDs
## "namebox", "who" e "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Variantes do celular
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Como o mouse pode não estar presente, substituímos o menu rápido por uma
## versão que usa menos botões e maiores, que são mais fáceis de tocar.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Voltar") action Rollback()
            textbutton _("Pular") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Automotivo") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900








screen missoes():
    add "Misc/Mission Menu unlocked.png"

    # 1º botão: sempre ativo
    imagebutton:
        idle "Misc/Frame 2.png"
        hover "Misc/Frame 3.png"
        xpos 41
        ypos 41
        action Jump("cena4")

    # 2º botão: desbloqueia somente se patinhascompleto for True
    if patinhascompleto:  # condição correta, sem “=”, e com “:” no final :contentReference[oaicite:2]{index=2}
        imagebutton:
            idle "Misc/Frame 2.png"
            hover "Misc/Frame 3.png"
            xpos 664
            ypos 41
            action Jump("missao2")
    else:  # qualquer outro caso (aqui patinhascompleto == False)
        # Botão bloqueado (sem ação)
        imagebutton:
            idle "Misc/locked black.png"
            hover "Misc/locked black highlight.png"
            xpos 664
            ypos 41
            sensitive False  # impede cliques e hover de triggerar ação

        # Ícone de cadeado sobreposto, apenas trocando imagem no hover
        imagebutton:
            idle "Misc/cadeado.png"
            hover "Misc/cadeado aberto.png"
            xpos 880
            ypos 450   # ajustar para posicionar acima do botão bloqueado
            insensitive False  # mantém o hover mas sem ação

    # 3º botão: exemplo genérico usando outra variável (substitua 'minha_variavel' conforme o seu caso)
    if lumicompleto:  # se a variável for True
        imagebutton:
            idle "Misc/Frame 2.png"
            hover "Misc/Frame 3.png"
            xpos 1292
            ypos 41
            action Jump("briefing_cabo_guava")
    else:  # patinhascompleto == False ou qualquer outro caso
        imagebutton:
            idle "Misc/locked black.png"
            hover "Misc/locked black highlight.png"
            xpos 1292
            ypos 41
            sensitive False

        imagebutton:
            idle "Misc/cadeado.png"
            hover "Misc/cadeado aberto.png"
            xpos 1540
            ypos 450   # posicionar acima
            insensitive False
        # Texto explicativo no topo da tela
    frame:
        xalign 0.5 yalign 1.00
        background "#090909"
        xpadding 180 ypadding 45
        text "Este menu mostra quais missões estão liberadas. \nAo completar as três missões, você ganha o jogo e se salva da prisão." size 36 color "#FFFFFF"






# ---------- FLAGS GLOBAIS ----------------
default placed_canil1 = False
default placed_canil2 = False
default placed_canil3 = False
default placed_canil4 = False

init python:
        # Callback: cola a placa no centro da caixa‑alvo e marca o par
    def drag_placed(dragged_items, dropped_on):
        if not dropped_on:
            return  # solto fora de um alvo

        # ---- Checagens de cada par CANILn → Qn ----
        if dropped_on is not None:
            if dragged_items[0].drag_name == "CANIL1" and dropped_on.drag_name == "Q1":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_canil1 = True
            elif dragged_items[0].drag_name == "CANIL2" and dropped_on.drag_name == "Q2":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_canil2 = True
            elif dragged_items[0].drag_name == "CANIL3" and dropped_on.drag_name == "Q3":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_canil3 = True
            elif dragged_items[0].drag_name == "CANIL4" and dropped_on.drag_name == "Q4":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_canil4 = True
        else:
            return  # combinação incorreta, não faz nada

        # ---- Verifica se todos estão corretos ----
        if (store.placed_canil1 and store.placed_canil2 and
            store.placed_canil3 and store.placed_canil4):
            return True  # sinaliza conclusão do minigame

screen canis_patinhas():

    add "Fundos/canilnomear.png"

    frame:
        xalign 0.5 yalign 1.00
        background "#090909"
        xpadding 180 ypadding 45
        text "Coloque cada placa no seu devido local" size 36 color "#FFFFFF"


    draggroup:
        # ---------- TARGETS (Q1–Q4) ----------
        drag:
            drag_name "Q1"
            draggable False
            droppable True
            drag_offscreen False
            #dropped drag_placed
            xpos 30  ypos 40
            frame:
                background None
                xysize (300, 100)

        drag:
            drag_name "Q2"
            draggable False
            droppable True
            drag_offscreen False
            #dropped drag_placed
            xpos 514 ypos 40
            frame:
                background None
                xysize (300, 100)

        drag:
            drag_name "Q3"
            draggable False
            droppable True
            drag_offscreen False
            #dropped drag_placed
            xpos 996 ypos 40
            frame:
                background None
                xysize (300, 100)

        drag:
            drag_name "Q4"
            draggable False
            droppable True
            drag_offscreen False
            #dropped drag_placed
            xpos 1473 ypos 40
            frame:
                background None
                xysize (300, 100)

        # ---------- DRAGGABLES ----------
        drag:
            drag_name "CANIL1"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed
            drag_offscreen False
            xpos 1550 ypos 800
            frame:
                background "#FFE4B5"
                xpadding 20 ypadding 20
                text "{b}CANIL 1{/b}" size 56 color "#000000"

        drag:
            drag_name "CANIL2"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed
            drag_offscreen False
            xpos 1550 ypos 560
            frame:
                background "#FFE4B5"
                xpadding 20 ypadding 20
                text "{b}CANIL 2{/b}" size 56 color "#000000"

        drag:
            drag_name "CANIL3"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed
            drag_offscreen False
            xpos 1550 ypos 680
            frame:
                background "#FFE4B5"
                xpadding 20 ypadding 20
                text "{b}CANIL 3{/b}" size 56 color "#000000"

        drag:
            drag_name "CANIL4"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed
            drag_offscreen False
            xpos 1550 ypos 920
            frame:
                background "#FFE4B5"
                xpadding 20 ypadding 20
                text "{b}CANIL 4{/b}" size 56 color "#000000"




# ---------- INTERFACE ----------------
default placed_calendario = False
default placed_filtragem = False
default placed_opcoes = False
default placed_planilha = False
default placed_titulo = False

init python:
        # Callback: cola a placa no centro da caixa‑alvo e marca o par
    def drag_placed_interface(dragged_items, dropped_on):
        if not dropped_on:
            return  # solto fora de um alvo

        # ---- Checagens de cada par CANILn → Qn ----
        if dropped_on is not None:
            if dragged_items[0].drag_name == "titulograb" and dropped_on.drag_name == "titulodrop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_titulo = True
            elif dragged_items[0].drag_name == "calendariograb" and dropped_on.drag_name == "calendariodrop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_calendario = True
            elif dragged_items[0].drag_name == "opcoesgrab" and dropped_on.drag_name == "opcoesdrop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_opcoes = True
            elif dragged_items[0].drag_name == "planilhagrab" and dropped_on.drag_name == "planilhadrop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_planilha = True
            elif dragged_items[0].drag_name == "filtragemgrab" and dropped_on.drag_name == "filtragemdrop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_filtragem = True
        else:
            return  # combinação incorreta, não faz nada

        # ---- Verifica se todos estão corretos ----
        if (store.placed_titulo and store.placed_calendario and
            store.placed_planilha and store.placed_opcoes and store.placed_filtragem):
            return True  # sinaliza conclusão do minigame

screen interface_patinhas():

    add "montar interface/montarinterface.png":
        zoom 1.513

    draggroup:
        # ---------- TARGETS (Q1–Q4) ----------
        drag:
            drag_name "titulodrop"
            draggable False
            droppable True
            drag_offscreen False
            #dropped drag_placed
            xpos 88  ypos 200
            frame:
                background None
                xysize (1090, 100)

        drag:
            drag_name "calendariodrop"
            draggable False
            droppable True
            drag_offscreen False
            #dropped drag_placed
            xpos 88 ypos 304
            frame:
                background None
                xysize (345, 400)

        drag:
            drag_name "filtragemdrop"
            draggable False
            droppable True
            drag_offscreen False
            #dropped drag_placed
            xpos 457 ypos 304
            frame:
                background None
                xysize (700, 100)

        drag:
            drag_name "opcoesdrop"
            draggable False
            droppable True
            drag_offscreen False
            #dropped drag_placed
            xpos 88 ypos 713
            frame:
                background None
                xysize (365, 160)
        
        drag:
            drag_name "planilhadrop"
            draggable False
            droppable True
            drag_offscreen False
            #dropped drag_placed
            xpos 457 ypos 440
            frame:
                background None
                xysize (700, 440)

        # ---------- DRAGGABLES ----------
        drag:
            drag_name "titulograb"
            child "montar interface/1titulogrande.png"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_interface
            drag_offscreen False
            xpos 1300 ypos 605

        drag:
            drag_name "calendariograb"
            child "montar interface/1calendariogrande.png"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_interface
            drag_offscreen False
            xpos 1550 ypos 200

        drag:
            drag_name "opcoesgrab"
            child "montar interface/1opcoesgrande.png"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_interface
            drag_offscreen False
            xpos 1550 ypos 88


        drag:
            drag_name "planilhagrab"
            child "montar interface/1planilhagrande.png"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_interface
            drag_offscreen False
            xpos 1300 ypos 700


        drag:
            drag_name "filtragemgrab"
            child "montar interface/1filtragemgrande.png"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_interface
            drag_offscreen False
            xpos 1219 ypos 500
    
    frame:
        xalign 0.5 yalign 1.00
        background "#090909"
        xpadding 180 ypadding 45
        text "Coloque cada seção da interface no local mais adequado" size 36 color "#FFFFFF"

