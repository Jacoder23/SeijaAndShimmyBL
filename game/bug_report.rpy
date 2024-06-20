init python:
    if not renpy.emscripten:
        import requests

        # TODO: better web bug reports

    config.underlay.append(
    renpy.Keymap( 
        K_BACKQUOTE = Function(renpy.call_in_new_context, "bug_reporter_label")  ) ) # press ` to report a bug


    import base64
    screenshot = b''
    mini_screenshot = b''

    bug_reporting = False

    def GetScreenshot():
        result = renpy.screenshot_to_bytes((1280, 720))
        if result:
            global screenshot;
            global mini_screenshot;
            screenshot = result
            mini_screenshot = renpy.screenshot_to_bytes((25-4, 14-3))
        else:
            renpy.notify("Failed to get screenshot.")

label bug_reporter_label:

    if bug_reporting: # TODO: the toggle doesn't actually work due to the ` being captured by the input
        return

    python:

        bug_reporting = True

        GetScreenshot()

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

        # post_data = bytearray(str.encode(f'''
        # --boundary
        # Content-Disposition: form-data; name="payload_json"
        # Content-Type: application/json

        # {{"content" : "Got a report for ya!",
        # "username" : "Wriggle Nightbug",
        # "embeds": [
        #     {{
        #     "title": "Bug Report",
        #     "description": "From: \\n{contact_point}",
        #     "color": 16711680,
        #     "footer": {{
        #         "text": "From {", ".join(current_platforms)}"
        #     }},
        #     "author": {{
        #         "name": "Wriggle Nightbug"
        #     }},
        #     "fields": [
        #         {{
        #         "name": "Description",
        #         "value": "{bug_report_text}",
        #         "inline": true
        #         }}
        #     ],
        #     "thumbnail": {{
        #         "url": "https://i.imgur.com/Ke7NX56.png"
        #     }}
        #     }}
        # ],
        # }}

        # --boundary
        # Content-Disposition: form-data; name="files[0]"; filename="screenshot.png"
        # Content-Type: image/png
        # '''))

        # post_data.extend(bytearray(screenshot))

        # post_data.extend(bytearray(str.encode(f'''
        # --boundary
        # Content-Disposition: form-data; name="files[1]"; filename="dev_log.txt"
        # Content-Type: text/plain

        # {export_log()}
        # --boundary
        # Content-Disposition: form-data; name="files[2]"; filename="history.txt"
        # Content-Type: text/plain

        # {export_history()}
        # --boundary--
        # ''')))

        # post_data = bytes(post_data)

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

        webhook = "https://discord.com/api/webhooks/1253394169318342718/eBvNVaoRkUDpj38Ea75fjqc-7bMAKr2XzIK5YKuiR2vzY-tsVDS-maCHtgdJBGgbJViF"

        # https://stackoverflow.com/questions/12385179/how-to-send-a-multipart-form-data-with-requests-in-python?rq=4

        web_result = renpy.fetch(webhook, method="POST", timeout=15, json=post_data, result="text")

        if renpy.emscripten:
            discord_character_limit = 1870

            renpy.fetch(webhook, method="POST", timeout=30, json={"avatar_url": "https://i.imgur.com/Ke7NX56.png","content" : "```" + str(base64.b64encode(bytes(mini_screenshot)))[2:discord_character_limit].replace("'", "") + "```","username" : "Wriggle Nightbug"}, result="text")

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
        input length 1000 pos (5,5) color "#fff" xmaximum 900 ymaximum 700 caret_blink True multiline True

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