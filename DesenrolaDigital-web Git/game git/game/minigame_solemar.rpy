# ---------- INTERFACE ----------------
default placed_1_solemar = False
default placed_2_solemar = False
default placed_3_solemar = False
default placed_4_solemar = False
default placed_5_solemar = False
default placed_6_solemar = False

transform tilt:
    anchor (0.0, 1.0)     # pivô no canto inferior-esquerdo
    rotate 19.24          # graus positivos = sentido horário
    rotate_pad False      # bounding box mínima p/ evitar cliques fantasmas


init python:
        # Callback: cola a placa no centro da caixa‑alvo e marca o par
    def drag_placed_solemar(dragged_items, dropped_on):
        if not dropped_on:
            return  # solto fora de um alvo

        # ---- Checagens de cada par CANILn → Qn ----
        if dropped_on is not None:
            if dragged_items[0].drag_name == "1grab" and dropped_on.drag_name == "1drop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_1_solemar = True
            elif dragged_items[0].drag_name == "2grab" and dropped_on.drag_name == "2drop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_2_solemar = True
            elif dragged_items[0].drag_name == "3grab" and dropped_on.drag_name == "3drop":
                dragged_items[0].snap(dropped_on.x, dropped_on.y,0.25)
                store.placed_3_solemar = True

        else:
            return  # combinação incorreta, não faz nada

        # ---- Verifica se todos estão corretos ----
        if (store.placed_1_solemar and store.placed_2_solemar and
            store.placed_3_solemar):
            return True  # sinaliza conclusão do minigame



screen minigame_solemar():

    add "solemar/minigame/pc.png"

    draggroup:
        # ---------- TARGETS (Q1–Q4) ----------
        drag:
            drag_name "1drop"
            draggable False
            droppable True
            drag_offscreen True
            xpos 230  ypos 236
            frame:
                background None
                xysize (307, 711)


        drag:
            drag_name "2drop"
            draggable False
            droppable True
            drag_offscreen True
            xpos 235  ypos 123
            frame:
                background None
                xysize (1028, 118)
            

        drag:
            drag_name "3drop"
            draggable False
            droppable True
            drag_offscreen True
            xpos 532  ypos 242
            frame:
                background None
                xysize (721, 690)
            
        # ---------- DRAGGABLES ----------
        drag:
            drag_name "1grab"
            child "solemar/minigame/1.png"
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_solemar
            drag_offscreen True
            xpos 1300 ypos 640

        drag:
            drag_name "2grab"
            child "solemar/minigame/2.png" 
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_solemar
            drag_offscreen True
            xpos 1300 ypos 150

        drag:
            drag_name "3grab"
            child "solemar/minigame/3.png" 
            draggable True
            drag_raise True
            droppable False
            dragged drag_placed_solemar
            drag_offscreen True
            xpos 1300 ypos 40

    frame:
        xalign 0.5 yalign 1.00
        background "#090909"
        xpadding 180 ypadding 45
        text "Estruture o layout do cronograma" size 36 color "#FFFFFF"