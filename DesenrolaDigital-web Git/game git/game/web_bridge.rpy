# game/web_bridge.rpy
init python:                                  #  ← dentro de um .rpy
    import json                               # único import obrigatório

    def send_to_sheet(payload):
        # renpy.variant("web") só é True no build HTML5
        if renpy.variant("web"):
            import importlib
            emscripten = importlib.import_module("emscripten")
            emscripten.run_script(
                "sendDataToGoogleSheet(" + json.dumps(payload) + ")"
            )
        else:
            renpy.log("[DEBUG] " + json.dumps(payload))