default persistent.showStoryletPreviews = False
default persistent.askedOnSplashscreen = False

init python:
    import random
    import functools
    import copy

    # https://lemmasoft.renai.us/forums/viewtopic.php?t=62280
    # Check if we already initialized preferences
    if not persistent.initialized:
        # Mark first-time initialization done
        persistent.initialized = True
        # Set volume preference if this is first launch
        preferences.set_volume("voice1", 0.7)

    renpy.music.register_channel("voice1", "voice1")

    # from the beeps bleeps thing credited in about
    def boopy_voice(event, interact=True, boopfile="bleeps/bleep001.ogg", **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play(boopfile, loop=True, channel='voice1')
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(fadeout=1, channel='voice1')

    class Battler:
        def __init__(self, name, max_hp, power, agility, tech, upgrades, violence, pacifism, team_player, isolation, precision, tenderness):
            self.name = name
            self.max_hp = max_hp
            self.power = power
            self.agility = agility
            self.tech = tech
            self.upgrades = upgrades
            self.violence = violence
            self.pacifism = pacifism
            self.team_player = team_player
            self.isolation = isolation
            self.precision = precision
            self.tenderness = tenderness

        def ListPersonalityTraits(self):
            return [self.violence, self.pacifism, self.team_player, self.isolation, self.precision, self.tenderness]

define seija = Character("Seija", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep002.ogg")], cb_name = "Seija")
define seija_costumed = Character("Backswitch", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep002.ogg")], cb_name = "Backswitch")
define seija_secret = Character("???", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep002.ogg")], cb_name = "???")
define shin = Character("Shin", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep025.ogg")], cb_name = "Shin")
define shin_costumed = Character("Wishmaker", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep011.ogg")], cb_name = "Wishmaker")
define sekibanki = Character("Sekibanki", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep011.ogg")], cb_name = "Sekibanki") # TODO: add sekibanki's cape name
define sekibanki_costumed = Character("Sekibanki", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep011.ogg")], cb_name = "Sekibanki")
define sekibanki_secret = Character("???", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep011.ogg")], cb_name = "???")
define kogasa = Character("Kogasa", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep014.ogg")], cb_name = "Kogasa")
define kogasa_secret = Character("Kogasa", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep018.ogg")], cb_name = "Kogasa")
define narrator = Character("", callback = [name_callback], cb_name = "")

# TODO: sprite highlights

image sei neutral = At('this sprite does not exist', sprite_highlight('sei'))

image placeholder:
    "placeholder.jpg"

label splashscreen:

    $ label_tracker = "splashscreen"

    # TODO: have kogasa explain this all very cutely

    if not persistent.askedOnSplashscreen:
        menu:
            "Would you like to have possible future and past events shown in the progress menu?"

            "Yes (spoilers, not recommended for first-time players)":
                $ persistent.showStoryletPreviews = True

            "No":
                $ persistent.showStoryletPreviews = False

        "You can change your mind by going to Preferences."

        $ persistent.askedOnSplashscreen = True

        $ renpy.pause(0.8, hard = True)

    show text "This is a fan-made video game not affiliated\nwith or endorsed by the original creators.\n\n{color=e63d3c}Touhou Project{/color} original concept, characters, and elements are property of\n{color=e63d3c}ZUN{/color} and {color=e63d3c}Team Shanghai Alice{/color}. Please support the official series." with fade
    $ renpy.pause(11)

    return

# The game starts here.

label interrupt_animation:

    play audio "countered.opus"

    show text "{sc}{size=120}COUNTERED!{/size}{/sc}"

    pause

    if first_time_countered:
        play audio "question.opus"

        $ cinematic = True
        "Tutorial" "Often times, opponents will COUNTER or INTERRUPT your action and force you to make an unknown roll."
        $ cinematic = False

        $ first_time_countered = False

    hide text

    $ renpy.jump(continue_label)

label dice_animation:

    play audio "dice sfx.ogg"
    
    show dice at dice_shake, truecenter

    label dice_animation_section:

        $ random_num = renpy.random.randint(1,20)

        if dice_animation_counter == 16:
            show text "{vspace=25}{size=70}{color=000000}[dice_result]{/color}{/size}" at dice_text5
        elif dice_animation_counter % 2 == 0 and dice_animation_counter < 8:
            show text "{vspace=25}{size=70}{color=000000}[random_num]{/color}{/size}" at dice_text1
        elif dice_animation_counter % 2 == 1 and dice_animation_counter < 8:
            show text "{vspace=25}{size=70}{color=000000}[random_num]{/color}{/size}" at dice_text2
        elif dice_animation_counter % 2 == 0 and dice_animation_counter >= 8 and dice_animation_counter < 16:
            show text "{vspace=25}{size=70}{color=000000}[random_num]{/color}{/size}" at dice_text3
        elif dice_animation_counter % 2 == 1 and dice_animation_counter >= 8 and dice_animation_counter < 16:
            show text "{vspace=25}{size=70}{color=000000}[random_num]{/color}{/size}" at dice_text4

        python:
            dice_animation_counter += 1

            renpy.pause(0.1 - 0.0315, hard = True, ) # tiny bit of delay messes up the sync, hand adjusted the delay, hopefully consistent across platforms (oh no)

            if dice_animation_counter >= 23:
                dice_animation_counter = 0
            else:
                renpy.jump("dice_animation_section")

        show text "{vspace=25}{size=70}{color=000000}[dice_result]{/color}{/size}" at dice_text_center

        if dice_modifier_formatted != "" and dice_result != 1 and dice_result != 20:
            $ renpy.pause(0.4, hard=True)

            show text "{vspace=58}{size=70}{color=000000}[dice_result]{/color}{/size}{color=000000}\n{size=25}[dice_modifier_formatted]{/size}{/color}" at dice_text_center with dissolve

        pause

        hide dice
        hide text

        $ renpy.jump(continue_label)

label character_sheet:
    $ current_character = Battler("Seija", 12, 2, 5, 2, 0, 3, 0, 0, 1, 1, 1)

    scene test bg

    show screen characters_screen

    $ renpy.jump(continue_label)

label start:

    $ label_tracker = "start"

    $ continue_label = "start_devtest"

    jump character_sheet

    label start_devtest:

        pause

        $ renpy.hide_screen("characters_screen")

    # $ cinematic = True

    # ------------------------------------------------------------------------------------------------------------------- #

    ## STORY STATE VARIABLES ##

    $ time = 0 # move on to end of chapter/next chapter once we hit 7
            # (with a theoretical 13 storylets per chapter, meaning we can only see half in each playthrough)

    $ chapter = 1

    $ seija_relationship_devotion = 5

    $ shin_relationship_devotion = 5

    $ seija_cause_devotion = 5

    $ shin_cause_devotion = 5

    $ shin_battler = Battler("Shin", 8, 2, 4, 4, 0, 0, 1, 2, 1, 1, 2)

    $ seija_battler = Battler("Seija", 12, 2, 5, 2, 0, 3, 0, 0, 1, 1, 1)

    $ at_the_mall = False

    $ shin_suspicion = 0

    ## TUTORIAL VARIABLES ##

    $ first_time_countered = True
    
    # ------------------------------------------------------------------------------------------------------------------- #

    $ InitializeStorylets()

label storylets:

    $ label_tracker = "storylets"

    scene bg black with fade

    show screen flowchart

    pause

    hide screen flowchart

    # TODO: add in a whole board game theme to this part

    $ NextStorylet()