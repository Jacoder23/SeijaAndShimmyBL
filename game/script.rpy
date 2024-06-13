init python:
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

define seija = Character("Seija", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep002.ogg")], cb_name = "Seija")
define seija_costumed = Character("Backswitch", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep002.ogg")], cb_name = "Backswitch")
define seija_secret = Character("???", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep002.ogg")], cb_name = "???")
define shin = Character("Shin", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep025.ogg")], cb_name = "Shin")
define shin_costumed = Character("Wishmaker", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep025.ogg")], cb_name = "Wishmaker")
define n = Character("", callback = name_callback, cb_name = "")

image sei neutral = At('this sprite does not exist', sprite_highlight('sei'))

image placeholder:
    "placeholder.jpg"

label splashscreen:

    $ label_tracker = "splashscreen"

    show text "This is a fan-made video game not affiliated\nwith or endorsed by the original creators.\n\n{color=e63d3c}Touhou Project{/color} original concept, characters, and elements are property of\n{color=e63d3c}ZUN{/color} and {color=e63d3c}Team Shanghai Alice{/color}. Please support the official series."
    with Pause(11)

    return

# The game starts here.

label start:

    $ label_tracker = "start"

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

    $ shin_battler = Battler("Shin", 8, 2, 4, 4, 0, 0, 1, 2, 1, 1, 2)

    $ seija_battler = Battler("Seija", 12, 2, 5, 2, 0, 3, 0, 0, 1, 1, 1)
    
    # ------------------------------------------------------------------------------------------------------------------- #

    $ InitializeStorylets()

label storylets:

    $ label_tracker = "storylets"

    # TODO: add in a whole board game theme to this part

    $ NextStorylet()

label st_shin_solo_1:

    $ label_tracker = "st_shin_solo_1"

    $ DeclareStorylet("st_shin_solo_1", ["time >= 0", "chapter == 1"], ["global time; time += 1"], 0, False)

    "For some reason..."

    "This gets shown"

    "Sometimes, not always"

    "Before initialization is done"

    $ FinishStorylet("st_shin_solo_1")

label st_chapter_start_1:

    $ label_tracker = "st_chapter_start_1"

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

    $ violence = 0

    $ pacifism = 0

    $ precision = 0

    $ dmg_to_target = 0

    $ dmg_to_self = 0

    $ chosen_target = (0, 0) # party index, member index

    $ turn = "party_one"

    # TODO: reformat all this into a dict

    $ party_one =[{"name":"Wishmaker",
                    "max_hp":shin_battler.max_hp, 
                    "hp":shin_battler.max_hp,
                    "power":shin_battler.power,
                    "agility":shin_battler.agility,
                    "tech":shin_battler.tech,
                    "effects":[],
                    "options":[[["selecting_target = True", "violence += 1; dmg_to_target = 3", "violence += 0.5", 10, shin_battler.power,               # run prior to outcome, effect on success, effect on failure, DC (1d20), relevant stat (if any)
                                    "You bring your weapon in for a swing at [party_two[chosen_target[1]]['name']]'s midriff.",                          # initial dialogue
                                    "[party_two[chosen_target[1]]['name']] stifles a pained grunt.",                                                     # post-roll success dialogue
                                    "[party_two[chosen_target[1]]['name']] points at your weapon and sends you it flying out of your hands.\nYou manage to get ahold of it before it goes offstage.\n[party_two[chosen_target[1]]['name']]'s laugh booms from his echoing demon mask.\n[party_two[chosen_target[1]]['sayer']]:Idiot.", "Strike"],   # post-roll failure dialogue, action text
                                ["selecting_target = True", "violence += 1; dmg_to_target = 4", "violence += 0.5; dmg_to_self = 1 if precision == 0 else 0", 99, shin_battler.power,
                                    "You throw your weight behind your weapon, bringing it down in a wide arc.",
                                    "[party_two[chosen_target[1]]['name']] is hit squarely in the chest.\nHe backs away a step while gasping for air.",
                                    "[party_two[chosen_target[1]]['name']] sidesteps your swing and sends a prop sword flying at your face.\n{if precision == 0}You parry it as well as you can but still get a bit roughed up.\n[party_two[chosen_target[1]]['sayer']]:Iiiiiiidiot.{else}You parry the prop sword, reading [party_two[chosen_target[1]]['name']]'s rhythm.",
                                    "Hit harder"],
                                ["selecting_target = True", "violence += 1; dmg_to_target = 5", "violence += 0.5; dmg_to_self = 3 if precision == 0 dmg_to_self = 1", 16, shin_battler.power,
                                    "",
                                    "",
                                    "",
                                    "Go for a wild swing"]],
                                [["", "pacifism += 1", "",
                                    "Duck"],
                                ["", "pacifism += 1", "",
                                    "Roll for cover"],
                                ["", "team_player += 1", "",
                                    "Call for backup"]],
                                [["", "precision += 1", "", 0, 0,
                                    "You hold a defensive stance, keeping distance from [party_two[chosen_target[1]]['name']].\nAfter dodging one or two hits, you start to get a feel for his timing, his rhythm.",
                                    "",
                                    "",
                                    "Wait and see"]]],
                    "dialogue":[("battle_started == False and battle_dialogue == 0", "Really? Don't you villains have better things to do than show up to kids' shows?")],
                    "sayer": "shin_costumed"}]

    $ party_two =[{"name":"Backswitch",
                    "max_hp":seija_battler.max_hp, 
                    "hp":seija_battler.max_hp,
                    "power":seija_battler.power,
                    "agility":seija_battler.agility,
                    "tech":seija_battler.tech,
                    "effects":[],
                    "options":[],
                    "dialogue":[("battle_started == False and battle_dialogue == 1", "Maybe if you heroes did something other than kids shows, I'd have something else to crash!")],
                    "sayer": "seija_costumed"}]

    label battle_st_chapter_start_1:

        $ label_tracker = "battle_st_chapter_start_1"

        call screen battle_screen

        window hide

        python:
            selecting_target = False
            # result = ui.interact()

            for statement in queued_say_statements:
                renpy.say(statement[0], statement[1])
            
            queued_say_statements = []

        jump battle_st_chapter_start_1

    label exit_battle_st_chapter_start_1:

        $ label_tracker = "exit_battle_st_chapter_start_1"

        $ renpy.hide_screen("battle_screen")

        scene bg black with fade

        $ FinishStorylet("st_chapter_start_1")

