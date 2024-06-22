init python:
    if not renpy.emscripten:
        import requests
        import zlib

        # TODO: better web bug reports

    config.underlay.append(
    renpy.Keymap( 
        K_BACKQUOTE = Function(renpy.call_in_new_context, "bug_reporter_label")  ) ) # press ` to report a bug

    import base64
    screenshot = b''
    mini_screenshot = b''
    compressed_mini_screenshot = b''
    screenshot_1 = b''
    screenshot_2 = b''

    bug_reporting = False
    discord_character_limit = 1870 # not 2000 due to padding around it and whatever, 3740 when doubled

    def GetScreenshot():
        result = renpy.screenshot_to_bytes((1280, 720))
        if result:
            global screenshot;
            global mini_screenshot;
            global compressed_mini_screenshot;
            global screenshot_1;
            global screenshot_2;
            global screenshot;
            mini_screenshot = renpy.screenshot_to_bytes((32+10, 18+6)) # 42, 24
            mini_screenshot = mini_screenshot
            compressed_mini_screenshot = str(base64.b64encode(zlib.compress(base64.b64encode(mini_screenshot))))
            if len(compressed_mini_screenshot) > discord_character_limit * 2:
                renpy.notify(f"{len(compressed_mini_screenshot)} vs. {len(str(base64.b64encode(mini_screenshot)))}") # should never be seen by players tbh
                compressed_mini_screenshot = renpy.screenshot_to_bytes((32, 18)) # fallback
                compressed_mini_screenshot = str(base64.b64encode(bytes(mini_screenshot)))[2:3740].replace("'", "")
            screenshot_1 = compressed_mini_screenshot[:len(compressed_mini_screenshot)//2]
            screenshot_2 = compressed_mini_screenshot[len(compressed_mini_screenshot)//2:]
        else:
            renpy.notify("Failed to get screenshot.")

label bug_reporter_label:

    if bug_reporting: # TODO: the toggle doesn't actually work due to the ` being captured by the input
        return

    python:

        bug_reporting = True

        GetScreenshot()
        
        token = renpy.input("", screen=u'token_insert')

        bug_report_text = renpy.input("", screen=u'bug_reporter')

        contact_point = renpy.input("", screen=u'email_getter')

        bug_reporting = False

        current_platforms = [] # I know it's supposed to just be one platform because that's how reality works, but on the nanoscopic chance...

        if renpy.windows:
            current_platforms.append("Windows")
        if renpy.macintosh:
            current_platforms.append("Mac")
        if renpy.linux:
            current_platforms.append("Linux")
        if renpy.android:
            current_platforms.append("Android")
        if renpy.ios:
            current_platforms.append("iOS")
        if renpy.emscripten:
            current_platforms.append("Web")
        if renpy.mobile:
            current_platforms.append("Mobile")

        current_platforms = ", ".join(current_platforms)

        post_data = {"avatar_url": "https://i.imgur.com/Ke7NX56.png",
        "content" : f"Got a report for ya! They were on the \"{label_tracker}\" label.",
        "username" : "Wriggle Nightbug",
        "embeds": [
            {
            "title": "Bug Report",
            "description": f"From: {contact_point}",
            "color": 16711680,
            "footer": {
                "text": f"From {current_platforms}"
            },
            "author": {
                "name": "Wriggle Nightbug"
            },
            "fields": [
                {
                "name": "Description",
                "value": f"{bug_report_text}",
                "inline": "true"
                }
            ]
            }
        ],
        }

    scene bg black

    # show text "{bt=10}Uploading...{/bt}"

    python:

        webhook = "https://discord.com/api/webhooks/1253630046778822719/" + token.strip()

        web_result = renpy.fetch(webhook, method="POST", timeout=15, json=post_data, result="text")

        if renpy.emscripten:

            renpy.fetch(webhook, method="POST", timeout=30, json={"avatar_url": "https://i.imgur.com/Ke7NX56.png","content" : f"```{screenshot_1}```","username" : "Wriggle Nightbug"}, result="text")

            renpy.fetch(webhook, method="POST", timeout=30, json={"avatar_url": "https://i.imgur.com/Ke7NX56.png","content" : f"```{screenshot_2}```","username" : "Wriggle Nightbug"}, result="text")

            renpy.fetch(webhook, method="POST", timeout=30, json={"avatar_url": "https://i.imgur.com/Ke7NX56.png","content" : "```" + export_log()[:discord_character_limit] + "```","username" : "Wriggle Nightbug"}, result="text")

            renpy.fetch(webhook, method="POST", timeout=30, json={"avatar_url": "https://i.imgur.com/Ke7NX56.png","content" : "```" + export_history()[:discord_character_limit] + "```","username" : "Wriggle Nightbug"}, result="text")
        
        elif not renpy.emscripten:
            result = requests.post(webhook,
            data={"avatar_url": "https://i.imgur.com/Ke7NX56.png",
            "content" : " ",
            "username" : "Wriggle Nightbug"},
            files={'file': ('screenshot.png', screenshot, 'image/png', {'Expires': '0'}),'file2': ('dev_log.txt', export_log(), 'text/plain', {'Expires': '0'}), 'file3': ('history_log.txt', export_history(), 'text/plain', {'Expires': '0'})})

    if not renpy.emscripten:
        "[result]"

    if web_result == "":
        hide text with dissolve(1.5)
        "Successfully submitted."
    else:
        hide text with dissolve(1.5)
        "Unsuccessful."

    #python:

        #result = renpy.fetch(webhook, method="POST", timeout=30, json=post_data, result="text")

        # TODO: figure out how to send images over discord webhooks, like properly

    return

screen bug_reporter:
    modal True
    add "gui/overlay/game_menu.png"

    vbox:
        xalign 0.05
        yalign 0.05
        label "Bug Report":
            text_size 36
        label "Shift + Enter to make a new line. The report will be submitted with what you write below, a screenshot, and the game's logs.":
            text_size 22

    viewport:
        xpos 100
        ypos 150
        xysize (660,700)
        input length 1000 pos (5,5) color "#fff" xmaximum 900 ymaximum 700 caret_blink True multiline True copypaste True

    vbox:
        xalign 0.95
        yalign 0.85
        textbutton "Return":
            action [Hide("bug_reporter", transition=Dissolve), Return()]

screen email_getter:
    modal True
    add "gui/overlay/game_menu.png"

    vbox:
        xalign 0.05
        yalign 0.05
        label "Bug Report":
            text_size 36
        label "And where should we contact you if we need to investigate (email preferred)?":
            text_size 22

    viewport:
        xpos 100
        ypos 150
        xysize (660,700)
        input length 320 pos (5,5) color "#fff" xmaximum 900 ymaximum 700 caret_blink True multiline False copypaste True

    vbox:
        xalign 0.95
        yalign 0.85
        textbutton "Return":
            action [Hide("email_getter", transition=Dissolve), Return()]

screen token_insert:
    modal True
    add "gui/overlay/game_menu.png"

    vbox:
        xalign 0.05
        yalign 0.05
        label "Bug Report":
            text_size 36
        label "Paste a valid token to access the bug reporter.":
            text_size 22

    viewport:
        xpos 100
        ypos 150
        xysize (660,700)
        input length 320 pos (5,5) color "#fff" xmaximum 900 ymaximum 700 caret_blink True multiline False copypaste True mask "*" default ""

    vbox:
        xalign 0.95
        yalign 0.85
        textbutton "Return":
            action [Hide("token_insert", transition=Dissolve), Return()]