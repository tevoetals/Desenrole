# ---------- INTERFACE ----------------
default placed_1 = False
default placed_2 = False
default placed_3 = False
default placed_4 = False
default placed_5 = False
default placed_6 = False

transform tilt:
    anchor (0.0, 1.0)     # pivô no canto inferior-esquerdo
    rotate 19.24          # graus positivos = sentido horário
    rotate_pad False      # bounding box mínima p/ evitar cliques fantasmas


init python:
        # Callback: cola a placa no centro da caixa‑alvo e marca o par
    def drag_placed_lumi(dragged_items, dropped_on):
        if not dropped_on:
            return  # solto fora de um alvo

        # ---- Checagens de cada par CANILn → Qn ----
        if dropped_on is not None:
            if dragged_items[0].drag_name == "1grab" and dropped_on.drag_name == "1drop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_1 = True
            elif dragged_items[0].drag_name == "2grab" and dropped_on.drag_name == "2drop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_2 = True
            elif dragged_items[0].drag_name == "3grab" and dropped_on.drag_name == "3drop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_3 = True
            elif dragged_items[0].drag_name == "4grab" and dropped_on.drag_name == "4drop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_4 = True
            elif dragged_items[0].drag_name == "5grab" and dropped_on.drag_name == "5drop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_5 = True
            elif dragged_items[0].drag_name == "6grab" and dropped_on.drag_name == "6drop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_6 = True
        else:
            return  # combinação incorreta, não faz nada

        # ---- Verifica se todos estão corretos ----
        if (store.placed_1 and store.placed_2 and
            store.placed_3 and store.placed_4 and store.placed_5 and store.placed_6):
            return True  # sinaliza conclusão do minigame



screen minigame_lumi():

    add "lumi/minigame/folha.png"

    draggroup:
        # ---------- TARGETS (Q1–Q4) ----------
        drag:
            drag_name "1drop"
            draggable False
            droppable True
            drag_offscreen True
            xpos 557  ypos 190
            frame:
                background None
                xysize (600, 20)


        drag:
            drag_name "2drop"
            draggable False
            droppable True
            drag_offscreen True
            xpos 557  ypos 245
            frame:
                background None
                xysize (600, 100)
            

        drag:
            drag_name "3drop"
            draggable False
            droppable True
            drag_offscreen True
            xpos 557  ypos 390
            frame:
                background None
                xysize (600, 60)
            

        drag:
            drag_name "4drop"
            draggable False
            droppable True
            drag_offscreen True
            xpos 557  ypos 485
            frame:
                background None
                xysize (600, 100)
            
        
        drag:
            drag_name "5drop"
            draggable False
            droppable True
            drag_offscreen True
            xpos 557  ypos 650
            frame:
                background None
                xysize (600, 100)

        drag:
            drag_name "6drop"
            draggable False
            droppable True
            drag_offscreen True
            xpos 557  ypos 795
            frame:
                background None
                xysize (600, 100)

        # ---------- DRAGGABLES ----------
        drag:
            drag_name "1grab"
            child "lumi/minigame/1.png"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_lumi
            drag_offscreen True
            xpos 1300 ypos 640

        drag:
            drag_name "2grab"
            child "lumi/minigame/2.png" 
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_lumi
            drag_offscreen True
            xpos 1300 ypos 150

        drag:
            drag_name "3grab"
            child "lumi/minigame/3.png" 
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_lumi
            drag_offscreen True
            xpos 1300 ypos 40


        drag:
            drag_name "4grab"
            child "lumi/minigame/4.png" 
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_lumi
            drag_offscreen True
            xpos 1300 ypos 700


        drag:
            drag_name "5grab"
            child "lumi/minigame/5.png" 
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_lumi
            drag_offscreen True
            xpos 1300 ypos 500

        drag:
            drag_name "6grab"
            child "lumi/minigame/6.png" 
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_lumi
            drag_offscreen True
            xpos 1300 ypos 300
    
    frame:
        xalign 0.5 yalign 1.00
        background "#090909"
        xpadding 180 ypadding 45
        text "Escreva o texto que o C.E.O. irá falar = Coloque na ordem certa" size 36 color "#FFFFFF"