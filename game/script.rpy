﻿init python:
    import random
    import functools
    import copy
    def boopy_voice(event, interact=True, boopfile="bleeps/bleep001.ogg", **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play(boopfile, loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(fadeout=1)

define seija = Character("Seija", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep002.ogg")], cb_name = "Seija")
define seija_costumed = Character("Backswitch", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep002.ogg")], cb_name = "Backswitch")
define seija_secret = Character("???", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep002.ogg")], cb_name = "???")
define shin = Character("Shin", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep025.ogg")], cb_name = "Shin")
define n = Character("", callback = name_callback, cb_name = "")

image sei neutral = At('this sprite does not exist', sprite_highlight('sei'))

image placeholder:
    "placeholder.jpg"

label splashscreen:
    show text "This is a fan-made video game not affiliated\nwith or endorsed by the original creators.\n\n{color=e63d3c}Touhou Project{/color} original concept, characters, and elements are property of\n{color=e63d3c}ZUN{/color} and {color=e63d3c}Team Shanghai Alice{/color}. Please support the official series."
    with Pause(11)

    return

# The game starts here.

label start:

    # $ cinematic = True

    # ------------------------------------------------------------------------------------------------------------------- #

    ## NARRATIVE STATE VARIABLES ##

    $ time = 0 # move on to end of chapter/next chapter once we hit 7
            # (with a theoretical 13 storylets per chapter, meaning we can only see half in each playthrough)

    $ chapter = 1

    $ seija_relationship_devotion = 5

    $ shin_relationship_devotion = 5

    $ seija_cause_devotion = 5

    $ shin_cause_devotion = 5

    # ------------------------------------------------------------------------------------------------------------------- #

    $ InitializeStorylets()

    jump storylets

label storylets:

    # TODO: add in a whole board game theme to this part

    $ NextStorylet()

    return

label st_chapter_start_1:

    $ DeclareStorylet("st_chapter_start_1",["chapter == 1"], [""], 100, False)

    # POV: Shin

    # CG: Shin hiding behind a wall with his signature weapon as a villain in a mascot suit (does not look like Seija) approaches, in search for him

    scene bg black

    $ cinematic = True

    "There's shattered glass in the stage curtain, shimmering in blue. Your enemy calls from the skies."
    
    $ cinematic = False

    "???" "Come out, come out wish boy!"

    $ cinematic = True
    "Now... now is the time to strike!"
    $ cinematic = False

    # CG: Shin strikes!

    shin "May even your wish come true, someday."

    "Children" "{sc}WOOOOOOOOOOOOO!{/sc}"

    $ cinematic = True
    "The sound of tiny applause and unenthused parents rings out from your audience. It's a sea of small hands pointing to you."
    "You hear the cue to bow so you do."
    $ cinematic = False

    "We love you Wishmaker!"

    "{i}The smiles, the games, the acting... it's all...{/i}"

    seija_secret "Kids shit."

    seija_secret "I was wonderin' about the noise following some a new hero. Looks like noise was all it was."

    $ cinematic = True
    "The fallen mascot suit, in upstage left, took to its feet{nw}{done} and removed its oversized head."

    # CG: Seija reveals herself

    "The fallen mascot suit, in upstage left, took to its feet{fast} and removed its oversized head."
    $ cinematic = False

    seija_costumed "Don't you agree, {i}wish boy?{/i}"

    # JUMP TO FIRST BATTLE #

    # TODO: Make this battle stuff into its own single file

    $ party_one =[{"name":"Wishmaker",
                    "max_hp":8, 
                    "hp":8,
                    "agility":4,
                    "power":2,
                    "tech":4,
                    "effects":[],
                    "options":["Hammer!", "Duck!", "Run away!", "Wait and see."]}]

    $ party_two =[{"name":"Backswitch",
                    "max_hp":10,
                    "hp":10,
                    "agility":5,
                    "power":2,
                    "tech":2,
                    "effects":[],
                    "options":[]}]

    $ selecting_target = True
     
    show screen battle_screen

    pause

    $ FinishStorylet("st_chapter_start_1")

label st_shin_solo_1:

    $ DeclareStorylet("st_shin_solo_1", ["time >= 0", "chapter == 1"], ["global time; time += 1"], 0, False)

    

    $ FinishStorylet("st_shin_solo_1")

