init python:
    import random
    import functools
    import copy
    # from the beeps bleeps thing credited in about
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
define narrator = Character("", callback = [name_callback], cb_name = "")

image sei neutral = At('this sprite does not exist', sprite_highlight('sei'))

image placeholder:
    "placeholder.jpg"

label splashscreen:

    $ label_tracker = "splashscreen"

    show text "This is a fan-made video game not affiliated\nwith or endorsed by the original creators.\n\n{color=e63d3c}Touhou Project{/color} original concept, characters, and elements are property of\n{color=e63d3c}ZUN{/color} and {color=e63d3c}Team Shanghai Alice{/color}. Please support the official series."
    with Pause(11)

    return

# The game starts here.

label dice_animation:
    
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

            renpy.pause(0.1 - 0.0305, hard = True) # tiny bit of delay messes up the sync, hand adjusted the delay, hopefully consistent across platforms (oh no)

            if dice_animation_counter >= 23:
                dice_animation_counter = 0
            else:
                renpy.jump("dice_animation_section")

        show dice at truecenter

        show text "{vspace=25}{size=70}{color=000000}[dice_result]{/color}{/size}" at dice_text_center

        $ renpy.jump(continue_label)

label start:

    $ label_tracker = "start"

    $ continue_label = "start_continue"

    $ dice_animation_counter = 0

    $ dice_result = 1

    jump dice_animation

    label start_continue:
        pause

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

    "[label_tracker]"

    $ FinishStorylet("st_shin_solo_1")

label st_chapter_start_1:

    $ label_tracker = "st_chapter_start_1"

    $ DeclareStorylet("st_chapter_start_1",["chapter == 1"], [""], 100, False)

    # POV: Shin

    # CG: Shin hiding behind a wall with his signature weapon as a villain in a mascot suit (does not look like Seija) approaches, in search for him

    scene bg black

    "There's shattered glass in the stage curtain, shimmering in blue. Your enemy calls from the skies."

    seija_secret "Come out, come out wish boy!"

    "Now... now is the time to strike!"

    # CG: Shin strikes!

    shin "May even your wish come true, someday."

    "{sc}WOOOOOOOOOOOOO!{/sc}"

    "The sound of tiny applause and unenthused parents rings out from your audience. It's a sea of small hands pointing to you."
    "You hear the cue to bow so you do."

    "We love you Wishmaker!"

    "{i}The smiles, the games, the acting... it's all...{/i}"

    seija_secret "Kids shit."

    "The fallen mascot suit, in upstage left, took to its feet{nw}{done} and removed its oversized head."

    # CG: Seija reveals herself

    "The fallen mascot suit, in upstage left, took to its feet{fast} and removed its oversized head to reveal Wishmaker."

    "Minor villain, major nuisance."
    
    "She's been around the block, making waves with her gravity flipping powers. As a relative newbie, this is your first time face-to-face with a villain."

    "Despite the excited gasps from the audience, the staff begin ushering everyone out."

    shin "{i}Okay, this is fine. Drop the banter for now, focus on keeping it together.{/i}"

    seija_costumed "I was wonderin' about the noise following some new hero. Looks like noise was all it was."

    seija_costumed "Don't you agree, {bt=6}wish boy?{/bt}"

    # JUMP TO FIRST BATTLE #

    # TODO: Make this battle stuff into its own single file

    $ violence = 0

    $ pacifism = 0

    $ team_player = 0

    $ isolation = 0

    $ precision = 0

    $ tenderness = 0

    $ dmg_to_target = 0

    $ dmg_to_self = 0

    $ chosen_target = (0, 0) # party index, member index

    $ turn = 1

    $ whose_turn = "party_one"

    $ battle_result = ""

    # TODO: reformat all this into a dict

    $ end_of_battle_conditions = [("double knockout", "all(x['hp'] == 0 for x in party_two) and all(x['hp'] == 0 for x in party_one)"),
                                ("party_one win", "all(x['hp'] == 0 for x in party_two)"),
                                ("party_two win", "all(x['hp'] == 0 for x in party_one)"),
                                ("stalemate", "all(len(x['options']) == 0 for x in party_one)")]

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
                                ["selecting_target = True", "violence += 1; dmg_to_target = 4", "violence += 0.5; dmg_to_self = 1 if precision == 0 else 0", 13, shin_battler.power,
                                    "You throw your weight behind your weapon, bringing it down in a wide arc.",
                                    "[party_two[chosen_target[1]]['name']] is hit squarely in the chest.\nHe backs away a step while gasping for air.",
                                    "[party_two[chosen_target[1]]['name']] sidesteps your swing and sends a prop sword flying at your face.\n{if precision == 0}You parry it as well as you can but still get a bit roughed up.\n[party_two[chosen_target[1]]['sayer']]:Iiiiiiidiot.{else}You parry the prop sword, reading [party_two[chosen_target[1]]['name']]'s rhythm.",
                                    "Hit harder"],
                                ["selecting_target = True", "violence += 1; dmg_to_target = 5", "violence += 0.5; dmg_to_self = 3 if precision == 1 else 4; dmg_to_target = 5 if precision == 1 else 0", 16, shin_battler.power,
                                    "You swing with a little too much oomph, nearly lifting you off your feet.",
                                    "[party_two[chosen_target[1]]['name']] blocks the telegraphed attack but the sheer force sends him backpedaling, wincing.",
                                    "[party_two[chosen_target[1]]['name']] steps into range before you complete the swing, throwing a counterpunch.\nYou eat it with your jaw and the world becomes blurry.\n{if precision == 0}You nearly lose your footing but try for a counterattack.\nBut your timing's been read and [party_two[chosen_target[1]]['name']] lays into you.\n[party_two[chosen_target[1]]['sayer']]:Dumbfuck.{else}You grit your way through the pain.\nWhile dazed, you tackle [party_two[chosen_target[1]]['name']] and land a shot to his knees that make him buckle.\n[party_two[chosen_target[1]]['sayer']]:Fuck!",
                                    "Go for a wild swing"]],
                                [["", "pacifism += 1", "dmg_to_self = 2", 12, shin_battler.agility,
                                    "You duck [party_two[chosen_target[1]]['name']]'s blows, weaving in and out of his range.\nSeeing this, [party_two[chosen_target[1]]['name']] makes a gesture and from across the street, a manhole cover goes flying in your direction.",
                                    "You manage to avoid it, leaping from your low position, as it flies underneath you and crashes into backstage.",
                                    "You move even lower, a poor move, as the manhole cover sweeps your legs and you land with your back against the ground.\nThe scramble afterwards to get back into a fighting stance is less graceful than you'd hoped.",
                                    "Duck"],
                                ["", "pacifism += 1; dmg_to_self = -1", "dmg_to_self = 3", 15, 0,
                                    "You roll for cover, stage props and lighting equipment becoming temporary shelter for you to catch your breath.\nIt's a balancing act to not stay in one place for too long however as your protections could become projectiles with just a gesture from [party_two[chosen_target[1]]['name']].",
                                    "A balancing act{cps=1.5}... {/cps}that you manage to keep as you catch your breath between daring manuevers, much to [party_two[chosen_target[1]]['name']]'s ire.",
                                    "A balancing act{cps=1.5}... {/cps}gone wrong as a wardrobe full of costumes goes flying right as you roll, straight into your face.",
                                    "Roll for cover"],
                                ["", "team_player += 1", "", 0, 0,
                                    "In a brief respite you get as you dodge [party_two[chosen_target[1]]['name']]'s onslaught, leaving him panting for a moment, you tap your communicator and send out backup signal.\nLet's hope your fellow heroes get here in time.",
                                    "",
                                    "",
                                    "Call for backup"]],
                                [["", "precision += 1", "", 0, 0,
                                    "You hold a defensive stance, keeping distance from [party_two[chosen_target[1]]['name']].\nAfter dodging one or two hits, you start to get a feel for his timing, his rhythm.",
                                    "",
                                    "",
                                    "Wait and see"]]],
                    "dialogue":[("battle_started == False and battle_dialogue == 0", "Really? Don't you villains have better things to do than show up to kids' shows?")],
                    "sayer": "shin_costumed"}]

    # every two actions of Wishmaker we get one action from Backswitch

    $ party_two =[{"name":"Backswitch",
                    "max_hp":seija_battler.max_hp, 
                    "hp":seija_battler.max_hp,
                    "power":seija_battler.power,
                    "agility":seija_battler.agility,
                    "tech":seija_battler.tech,
                    "effects":[],
                    "options":[["", "", "dmg_to_self = 3", 10, 0,                                     # opponent interrupts vs player actions, ran by player context but overwrite your previous action (though that means the action is still there for you to use later instead of being used up)
                                    "",
                                    "But before you can, you notice the floorboard beneath your feet about to fly off. You leap backwards out of harms way.\n[party_two[chosen_target[1]]['sayer']]:Not as dumb as you look?",
                                    "But you fail to notice the floorboard beneath your feet fly off, likely under [party_two[chosen_target[1]]['name']] power.\n You fall without any ground beneath you.\nYou land under the stage with a thud before climbing out unceremoniously; a jeering [party_two[chosen_target[1]]['name']] there to greet you as you rise.\n[party_two[chosen_target[1]]['sayer']]:Had a nice trip?",
                                    ""]],
                    "dialogue":[("battle_started == False and battle_dialogue == 1", "Maybe if you heroes did something other than kids shows, I'd have something else to crash!")],
                    "sayer": "seija_costumed"}]

    label battle_st_chapter_start_1:

        $ label_tracker = "battle_st_chapter_start_1"

        $ end_battle_label = "exit_battle_st_chapter_start_1"

        $ queued_say_statements = []

        call screen battle_screen

        window hide

        python:
            selecting_target = False
            # result = ui.interact()

            for statement in queued_say_statements:
                renpy.say(statement[0], statement[1])
            
            queued_say_statements = []

            turn += 1

        jump battle_st_chapter_start_1

    label exit_battle_st_chapter_start_1:

        $ label_tracker = "exit_battle_st_chapter_start_1"

        $ renpy.hide_screen("battle_screen")

        scene bg black with fade

        if battle_result == "double knockout":
            shin_costumed "And... shut..."

            "You collapse onto the ground after knocking Backswitch on her ass."
        elif battle_result == "party_one win":
            shin_costumed "And shut it!"
        elif battle_result == "party_two win":
            "The last thing you see before you collapse onto the ground is their mask. You can't see it but you can tell they've got the ugliest smirk behind it."
        elif battle_result == "stalemate":
            seija_costumed "Hmm. Not as talkative as your stage persona, are ya?"

            shin_costumed "Quit it with the remarks, Backswitch."
        $ FinishStorylet("st_chapter_start_1")

