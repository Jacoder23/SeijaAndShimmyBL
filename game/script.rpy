init python:
    import functools
    def boopy_voice(event, interact=True, boopfile="bleeps/bleep001.ogg", **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play(boopfile, loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(fadeout=1)

define s = Character("Siyokoy", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep010.ogg")], cb_name = "siyokoy")
define n = Character("", callback = name_callback, cb_name = "")

image siyokoy happy = At('sprite1', sprite_highlight('siyokoy'))

image test:
    "bg room.png"
    truecenter
    zpos -20000 zzoom True

init python:
    latest_message = ""
    text_input = ""

# The game starts here.

label start:

    jump test2

label test2:
    $ cinematic = True

    camera:
        reset
        perspective True

    show border onlayer UI

    show test

    show siyokoy happy at truecenter, outline_transform(9, "#FFFFFF", 4.0) with dissolve

    s "Just doing a test."

    s "Trying new things out."

    camera:
        ease 1.0 zpos -500 xoffset -100 yoffset 10

    show test:
        ease 1.0 truecenter zoom 2.0

    s "Was I though?" (cb_name="")

    camera:
        zpos -500 xoffset -100 yoffset 10
        matrixtransform RotateMatrix(0, 0, 0) * OffsetMatrix(0, 0, 0)
        ease 2.0 matrixtransform RotateMatrix(0, -30, 0) * OffsetMatrix(0, 0, 0)

    show test:
        zoom 2.0
        ease 1.0 truecenter zoom 4.0

    show siyokoy happy:
        matrixtransform RotateMatrix(0, 0, 0) * OffsetMatrix(0, 0, 0)
        ease 2.0 matrixtransform RotateMatrix(0, 30, 0) * OffsetMatrix(0, 0, 0)

    s "Or was I ruminating on the nature of thought?"  (cb_name="")

    s "I was doing a test."

    $ name = renpy.input("What's your name?");

    camera:
        smoothreset

    show siyokoy happy:
        matrixtransform RotateMatrix(0, 30, 0) * OffsetMatrix(0, 0, 0)
        ease 2.0 matrixtransform RotateMatrix(0, 0, 0) * OffsetMatrix(0, 0, 0)

    show test:
        truecenter zoom 4.0
        ease 2.0 zpos -20000
        ease 2.0 truecenter zoom 2.0

    n "Well okay, [name]."

    return

label readme:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

    s "So you want to use this GUI?"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sprite1 with dissolve

    s "Good for you! Because I've provided it for free."

    show sprite1 at left with moveinright

    s "I don't mind if you use it for commercial or non-commercial projects as long as you credit me in the game itself."

    s "However, do NOT resell any portion of this GUI as your own."

    s "Anyway, if you {i}are{/i} going to use it in  a commercial project, please consider tipping my kofi."

    show sprite1 at center with moveinleft

    $ cinematic = True

    s "I'm literally just a college student with no income."

    s "Right now we've entered the UI's cinematic mode."

    s "If you want to use this, add \"$ cinematic = True\" to your script turn it on."

    s "And if you don't want to use it anymore..."

    $ cinematic = False

    s "Just change True to False."

    show sprite1 at left with moveinright

    menu:
        s "This is what menu choices look like if you add text."
        
        "test choice 1":
            pass
        "test choice 2":
            pass
        "test choice 3":
            pass
        "test choice 4":
            pass
        "test choice 5":
            pass

    s "And this is what they look like without it."
    
    menu:
        "test choice 1":
            pass
        "test choice 2":
            pass
        "test choice 3":
            pass
        "test choice 4":
            pass
        "test choice 5":
            pass

    
    s "That's it for this portion."

    s "Try screenshotting and opening up the game menu by clicking the sun below."

    s "Ciao!"

    # This ends the game.

    return
