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
define narrator = Character("", callback = [name_callback], cb_name = "")

# TODO: sprite highlights

image sei neutral = At('this sprite does not exist', sprite_highlight('sei'))

image placeholder:
    "placeholder.jpg"

label splashscreen:

    $ label_tracker = "splashscreen"

    # TODO: have kogasa explain this all very cutely

    show text "This is a fan-made video game not affiliated\nwith or endorsed by the original creators.\n\n{color=e63d3c}Touhou Project{/color} original concept, characters, and elements are property of\n{color=e63d3c}ZUN{/color} and {color=e63d3c}Team Shanghai Alice{/color}. Please support the official series."
    with Pause(11)

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

            renpy.pause(0.1 - 0.0315, hard = True) # tiny bit of delay messes up the sync, hand adjusted the delay, hopefully consistent across platforms (oh no)

            if dice_animation_counter >= 23:
                dice_animation_counter = 0
            else:
                renpy.jump("dice_animation_section")

        show text "{vspace=25}{size=70}{color=000000}[dice_result]{/color}{/size}" at dice_text_center

        if dice_modifier_formatted != "" and dice_result != 1 and dice_result != 20:
            $ renpy.pause(0.4, hard=True)

            show text "{vspace=50}{size=70}{color=000000}[dice_result]{/color}{/size}{color=000000}\n[dice_modifier_formatted]{/color}" at dice_text_center with dissolve

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

    ## TUTORIAL VARIABLES ##

    $ first_time_countered = True
    
    # ------------------------------------------------------------------------------------------------------------------- #

    $ InitializeStorylets()

label storylets:

    $ label_tracker = "storylets"

    # TODO: add in a whole board game theme to this part

    $ NextStorylet()

label st_shin_hospitalized:

    $ label_tracker = "st_shin_solo_1"

    $ DeclareStorylet("st_shin_solo_1", ["time >= 0", "chapter == 1", "hospitalized == True"], ["global time; time += 1"], 99, False)

    # shin ALSO has to file a report on her battle but to take her mind off things, instead of a supplies trip, sekibanki keeps her company at her bed for a while and the two have a chat about heroism, shin expresses doubts that what he's doing matters much when her first break went that poorly (or that she got knocked out even if she knocked out seija)

    "[label_tracker]"

    $ FinishStorylet("st_shin_solo_1")

label st_shin_not_hospitalized:

    $ label_tracker = "st_shin_solo_1"

    $ DeclareStorylet("st_shin_solo_1", ["time >= 0", "chapter == 1", "hospitalized == False"], ["global time; time += 1"], 99, False)

    # shin has to file a report on her battle but to take her mind off things, sekibanki sends her on a supplies trip to the mall to buy food

    # along the way he finds a certain someone whose name rhymes with shmeija but neither know the other's identity, they become acquainted with each other; not friends nor foes yet

    "[label_tracker]"

    $ FinishStorylet("st_shin_solo_1")

label st_chapter_start_1:

    $ label_tracker = "st_chapter_start_1"

    $ DeclareStorylet("st_chapter_start_1",["chapter == 1"], [""], 100, False)

    # POV: Shin

    # CG: The focus is shin hiding behind a wall with his signature weapon (gotta wait on shin hero design or at least sillouhette); a villain in a mascot suit (does not look like Seija) approaches, in search for him

    #scene bg black

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

    "The fallen mascot suit, in upstage left, took to its feet{nw}{done} and removed its oversized head to reveal Backswitch."

    # Seija reveals herself by the sprite moving up, no need for a CG

    "The fallen mascot suit, in upstage left, took to its feet{fast} and removed its oversized head to reveal Backswitch."

    "Minor villain, major nuisance."
    
    "He's been around the block, making waves with her gravity flipping powers. As a relative newbie, this is your first time face-to-face with a villain."

    "Despite the excited gasps from the audience, the staff begin ushering everyone out."

    shin "{i}Okay, this is fine. Drop the banter for now, focus on keeping it together.{/i}"

    seija_costumed "I was wonderin' about the noise following some new hero. Looks like noise was all it was."

    seija_costumed "Don't you agree, {bt=6}{color=000000}wish boy?{/color}{/bt}"

    # BATTLE STUFF START #

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

    $ party_one = [{"name":"Wishmaker",
                    "max_hp":shin_battler.max_hp, 
                    "hp":shin_battler.max_hp,
                    "power":shin_battler.power,
                    "agility":shin_battler.agility,
                    "tech":shin_battler.tech,
                    "effects":[],
                    "options":[[["selecting_target = True", "violence += 1; dmg_to_target = 3; noglobal QueueSFX('PUNCH_PERCUSSIVE_HEAVY_09.opus')", "noglobal QueueSFX('WHOOSH_ARM_SWING_01.opus'); violence += 0.5", 10, ("Power", shin_battler.power),               # run prior to outcome, effect on success, effect on failure, DC (1d20), relevant stat (if any)
                                    "You bring your weapon in for a swing at [party_two[chosen_target[1]]['name']]'s midriff.",                          # initial dialogue
                                    "[party_two[chosen_target[1]]['name']] stifles a pained grunt.",                                                     # post-roll success dialogue
                                    "[party_two[chosen_target[1]]['name']] points at your weapon and sends it flying out of your hands.\nYou manage to get ahold of it before it goes offstage.\n[party_two[chosen_target[1]]['name']]'s laugh booms from his echoing demon mask.\n[party_two[chosen_target[1]]['sayer']]:Idiot.",
                                    "violence",
                                    FormatOption("STRIKE", "violence")],   # post-roll failure dialogue, action text
                                ["selecting_target = True", "violence += 1; dmg_to_target = 4; noglobal QueueSFX('PUNCH_DESIGNED_HEAVY_23.opus')", "noglobal QueueSFX('WHOOSH_ARM_SWING_01.opus'); violence += 0.5; dmg_to_self = 1 if precision == 0 else 0", 13, ("Power", shin_battler.power),
                                    "You throw your weight behind your weapon, bringing it down in a wide arc.",
                                    "[party_two[chosen_target[1]]['name']] is hit squarely in the chest.\nHe backs away a step while gasping for air.",
                                    "[party_two[chosen_target[1]]['name']] sidesteps your swing and sends a prop sword flying at your face.\n{if precision == 0}You parry it as well as you can but still get a bit roughed up.\n[party_two[chosen_target[1]]['sayer']]:Iiiiiiidiot.{else}You parry the prop sword, reading [party_two[chosen_target[1]]['name']]'s rhythm.",
                                    "violence",
                                    FormatOption("HIT HARDER", "violence")],
                                ["selecting_target = True", "violence += 1; dmg_to_target = 5; noglobal QueueSFX('PUNCH_INTENSE_HEAVY_03.opus')", "noglobal QueueSFX('WHOOSH_ARM_SWING_01.opus'); noglobal QueueSFX('PUNCH_DESIGNED_HEAVY_23.opus', 2); noglobal QueueSFX('PUNCH_INTENSE_HEAVY_03.opus', 4); violence += 0.5; dmg_to_self = 3 if precision == 1 else 4; dmg_to_target = 5 if precision == 1 else 0", 16, ("Power", shin_battler.power),
                                    "You swing with a little too much oomph, nearly lifting you off your feet.",
                                    "[party_two[chosen_target[1]]['name']] blocks the telegraphed attack but the sheer force sends him backpedaling, wincing.",
                                    "[party_two[chosen_target[1]]['name']] steps into range before you complete the swing, throwing a counterpunch.\nYou take it on your jaw and the world becomes blurry.\n{if precision == 0}You nearly lose your footing but try for a counterattack.\nBut your timing's been read and [party_two[chosen_target[1]]['name']] lays into you.\n[party_two[chosen_target[1]]['sayer']]:Dumbfuck.{else}You grit your way through the pain.\nWhile dazed, you tackle [party_two[chosen_target[1]]['name']] and land a shot to his knees that make him buckle.\n[party_two[chosen_target[1]]['sayer']]:Fuck!",
                                    "violence",
                                    FormatOption("THROW WILD SWING", "violence")]],
                                [["", "pacifism += 1", "dmg_to_self = 2", 12, ("Agility", shin_battler.agility),
                                    "You duck [party_two[chosen_target[1]]['name']]'s blows, weaving in and out of his range.\nSeeing this, [party_two[chosen_target[1]]['name']] makes a gesture and from across the street, a manhole cover goes flying in your direction.",
                                    "You manage to avoid it, leaping from your low position, as it flies underneath you and crashes into backstage.",
                                    "You move even lower, a poor move, as the manhole cover sweeps your legs and you land with your back against the ground.\nThe scramble afterwards to get back into a fighting stance is less graceful than you'd hoped.",
                                    "pacifism",
                                    FormatOption("DUCK", "pacifism")],
                                ["", "pacifism += 1; dmg_to_self = -1", "dmg_to_self = 3", 15, ("Agility", shin_battler.agility),
                                    "You roll for cover, stage props and lighting equipment becoming temporary shelter for you to catch your breath.\nIt's a balancing act to not stay in one place for too long however as your protections could become projectiles with just a gesture from [party_two[chosen_target[1]]['name']].",
                                    "A balancing act{cps=1.5}... {/cps}that you manage to keep as you catch your breath between daring manuevers, much to [party_two[chosen_target[1]]['name']]'s ire.",
                                    "A balancing act{cps=1.5}... {/cps}gone wrong as a wardrobe full of costumes goes flying right as you roll, straight into your face.",
                                    "pacifism",
                                    FormatOption("ROLL FOR COVER", "pacifism")],
                                ["", "team_player += 1", "", 0, ("", 0),
                                    "In a brief respite you get as you dodge [party_two[chosen_target[1]]['name']]'s onslaught, leaving him panting for a moment, you tap your communicator and send out backup signal.\nLet's hope your fellow heroes get here in time.",
                                    "",
                                    "",
                                    "team_player",
                                    FormatOption("CALL FOR BACKUP", "team_player")]],
                                [["", "precision += 1", "", 0, ("", 0),
                                    "You hold a defensive stance, keeping distance from [party_two[chosen_target[1]]['name']].\nAfter dodging one or two hits, you start to get a feel for his timing, his rhythm.",
                                    "",
                                    "",
                                    "precision",
                                    FormatOption("WAIT AND SEE", "precision")]]],
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
                    "options":[["", "", "dmg_to_self = 3", 10, ("", 0),                                     # opponent interrupts vs player actions, ran by player context but overwrite your previous action (though that means the action is still there for you to use later instead of being used up)
                                    "You attempt to-",
                                    "But before you can, you notice the floorboard beneath your feet about to fly off. You leap backwards out of harms way. [party_two[chosen_target[1]]['name']] seems genuinely surprised.\n[party_two[chosen_target[1]]['sayer']]:Not as dumb as you look?",
                                    "But you fail to notice the floorboard beneath your feet fly off, likely under [party_two[chosen_target[1]]['name']]'s power.\n You fall without any ground beneath you.\nYou land under the stage with a thud before climbing out unceremoniously; a jeering [party_two[chosen_target[1]]['name']] there to greet you as you rise.\n[party_two[chosen_target[1]]['sayer']]:Had a nice trip?",
                                    ""]],
                    "boss_turn":[], # it's called a boss turn because only bosses get their own non-interrupt actions
                    "dialogue":[("battle_started == False and battle_dialogue == 1", "Maybe if you heroes did something other than kids shows, I'd have something else to crash!")],
                    "sayer": "seija_costumed"}]

    label battle_st_chapter_start_1:

        $ label_tracker = "battle_st_chapter_start_1"

        $ end_battle_label = "exit_battle_st_chapter_start_1"

        $ queued_statements = []

        call screen battle_screen

        window hide

        $ selecting_target = False

        $ continue_label = "battle_st_chapter_start_1_continue"

        label battle_st_chapter_start_1_continue:

            python:
                while len(queued_statements) > 0:
                    statement = queued_statements[0]
                    if statement[0] == "say":
                        renpy.say(statement[1][0], statement[1][1])
                        queued_statements.pop(0)
                    elif statement[0] == "exec":
                        renpy.log("")
                        renpy.log("exec: " + statement[0])
                        queued_statements.pop(0)
                        exec(statement[1])
                    else:
                        renpy.log("")
                        renpy.log("unknown: " + str(statement))
                        queued_statements.pop(0)

                queued_statements = [] 

                turn += 1

        jump battle_st_chapter_start_1

    label exit_battle_st_chapter_start_1:

        $ label_tracker = "exit_battle_st_chapter_start_1"

        $ renpy.hide_screen("battle_screen")

        scene bg black with fade

        $ seija_hurt = True if party_two[0]["hp"] / party_two[0]["max_hp"] <= 0.5 else False

        if battle_result == "double knockout":
            shin_costumed "And... shut... your..."

            "You both collapse onto the ground."

            "The last thing you see is Backswitch like a puppet with cut strings, no tension in his fallen limbs."

            $ seija_got_away = True and team_player > 0

            $ hospitalized = True

        elif battle_result == "party_one win":

            shin_costumed "And shut it!"

            # TODO: Write the outcome of this

            $ seija_got_away = False

            $ hospitalized = False

        elif battle_result == "party_two win":

            "The last thing you see before you collapse onto the ground is his mask. You can tell he's got the ugliest smirk behind it."

            $ seija_got_away = True

            $ hospitalized = True

        elif battle_result == "stalemate":

            seija_costumed "Hmm. Not as talkative as your stage persona, are ya?"

            shin_costumed "Shut it with the backtalk, Backswitch."

            seija_costumed "uhhh author note: write something here witty that sekibanki can counter but that also confuses shin"

            if team_player > 0: # called for backup
                sekibanki_secret "sekibanki's counter"
            else:
                shin_costumed "What does that-"

                "But Backswitch was already running away."

                "Shin began to run after him but not before incoming traffic became INCOMING traffic with Backswitch sent a truck, its tires squealing, toppling sidewards towards Shin."

            # TODO: Write the outcome of this

            $ seija_got_away = True

            $ hospitalized = False

        scene bg black with fade

        $ FinishStorylet("st_chapter_start_1")

