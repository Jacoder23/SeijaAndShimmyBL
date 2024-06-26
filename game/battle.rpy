################################### Battle

# Style for damage display
style damage_text:
    size 42
    color "#db3d3d"

# Style for heal display
style heal_text:
    size 42
    color "#4ecf4e"

init python:
    # The [x, y] location for each battle sprite
    sprite_target_mapping = {
        0: [0.15, 300],
        1: [0.35, 300],
        2: [0.55, 300],
        3: [0.75, 300],
        4: [0.50, 550],
    }

image empty_stage = Image("bg black.png")

screen battle:
    modal True
    frame:
        xalign 0.5 yalign 0.5
        hbox:
            xalign 0.5 yalign 0.5
            add empty_stage

define battle_narrator = Character(None, interact=False)

init python:

    selecting_target = False

    queued_statements = []

    def SkipTurn():
        pass

    def ChooseTarget(target):
        chosen_target = (1, target) # only the player actually uses this
        pass

    def SayDialogueData(dialogue):
        if dialogue == "":
            return

        lines = ApplyFilter(config.say_menu_text_filter, dialogue).split("\n")

        for line in lines:
            sections = line.split(":", 1)
            if len(sections) == 1:
                queued_statements.append(("say", (narrator, sections[0])))
            else:
                queued_statements.append(("say", (globals()[eval(sections[0][1:-1])], sections[1])))

    def ApplyEffect(effect, battler_source):
                            # Just gonna have to assume everything in here is a variable change for now so I can add in the global keyword
                            # TODO: Figure out a smarter way than what I just described
        if effect == "":
            return

        effects = effect.split(";")
        for line in effects:
            if not line.strip()[:8] == "noglobal":
                complete_line = "global " + line.split()[0] + "; " + line.strip()
            else:
                complete_line = line[9:].strip()
            exec(complete_line)

    def RollDice(result, modifier, dc): # visual effect
        global dice_result
        global dice_modifier_formatted
        global continue_label
        global dice_animation_counter

        dice_result = result
        dice_modifier_formatted = FormatModifier(modifier)
        dice_animation_counter = 0
        queued_statements.append(("exec", "renpy.jump('dice_animation')"))

    def FormatModifier(modifier):
        if modifier == 0:
            return ""
        elif modifier > 0:
            return "+" + str(abs(modifier))
        else:
            return "-" + str(abs(modifier))

    def QueueSFX(sfx, lines_to_skip = 0):
        if lines_to_skip == 0:
            queued_statements.append(("exec", "renpy.play('" + sfx + "')"))
        else:
            queued_statements.append(("exec", "QueueSFXWithIndex('" + sfx + "', " + str(lines_to_skip) + ")"))

    def QueueSFXWithIndex(sfx, index):
        queued_statements.insert(index, ("exec", "renpy.play('" + sfx + "')")) # TODO: Gotta take into consideration that the addition of more queued SFX messes up the order

    # https://stackoverflow.com/a/53671539/5177938
    def fstr(template):
        return eval(f'f"""{template}"""')

    def OptionDescription(member, option):
        dc = option[0][3]
        modifier = option[0][4][1]
        stat_name = option[0][4][0]
        if type(stat_name) != type(""):
            stat_name = stat_name()
        else:
            stat_name = stat_name if stat_name != "" else "No modifiers"

        # if stat_name == "Tech":
        #     stat_name = "Technique"

        chance = min(round((20 - (dc - modifier)) / 20 * 100),100)
        
        if modifier == 0:
            modifier_formatted = ""
        elif modifier > 0:
            modifier_formatted = ": " + FormatModifier(modifier)
        else:
            modifier_formatted = ": " + FormatModifier(modifier)

        if len(member['effects']) > 0:
            effects_formatted = member['effects'] # TODO: actually format this
        else:
            effects_formatted = ""

        return stat_name + modifier_formatted + effects_formatted + "\n{size=70}" + str(chance) + "%{/size}\n{size=*1.5}DC: {/size}{size=*3.0}{font=Dicier-Round-Heavy.otf}" + str(dc) + "_ON_D20{/font}{/size}\n\nAlways loses: {size=*2.0}{font=Dicier-Round-Heavy.otf}1_ON_D20{/font}{/size}\nAlways wins: {size=*2.0}{font=Dicier-Round-Heavy.otf}20_ON_D20{/font}{/size}"

    def DoOption(party, member, option, interrupting_party): # maybe this should've been a dict or a custom class... eh it makes the writing part easier in trade for making the debugging a fucking ticking bomb
        # effect before outcome [0], effect on success [1], effect on failure [2], DC [3], stat [4], initial dialogue [5], post-success [6], post-failure [7], formatting [8], source [9], name of action [-1]

        # TODO: assign each of these to its own variable instead of being part of an array; like just some variable declarations to make it clearer what is what

        global turn
        interrupt_turn = len(interrupting_party) > 0 and turn % 2 and renpy.random.randint(1, 10) > 3

        if(interrupt_turn):
            interrupt_turn = interrupt_turn and any(len(x["options"]) > 0 for x in interrupting_party)

        if(interrupt_turn):

            interrupting_member = renpy.random.choice([x for x in interrupting_party if len(x["options"]) > 0])

            current_option = renpy.random.choice(interrupting_member["options"])

            interrupting_member["options"].remove(current_option)

            queued_statements.append(("exec", "renpy.jump('interrupt_animation')"))

        else:

            current_option = option[0]

        exec(current_option[0])
        
        dice_roll = renpy.random.randint(1,20)

        SayDialogueData(current_option[5])

        if current_option[3] > 0:
            dev_log(current_option[3])
            RollDice(dice_roll, current_option[4][1], current_option[3])

        auto_success = dice_roll == 20
        auto_fail = dice_roll == 1 and current_option[3] != 0

        if (max(dice_roll + current_option[4][1], 1) >= current_option[3] or auto_success) and not auto_fail:
            ApplyEffect(current_option[1], member['source'])
            SayDialogueData(current_option[6])
        else:
            ApplyEffect(current_option[2], member['source'])
            SayDialogueData(current_option[7])

        global dmg_to_target
        if dmg_to_target != 0:
            if chosen_target[0] == 1: # idk why this is 1 and not 0
                party_one[chosen_target[1]]["hp"] = min(max(party_one[chosen_target[1]]["hp"] - dmg_to_target, 0), party_one[chosen_target[1]]["max_hp"])
            else:
                party_two[chosen_target[1]]["hp"] = min(max(party_two[chosen_target[1]]["hp"] - dmg_to_target, 0), party_two[chosen_target[1]]["max_hp"])

            dmg_to_target = 0

        global dmg_to_self
        if dmg_to_self != 0:
            if chosen_target[0] == 0: # idk why this is 0 and not 1
                party_one[chosen_target[1]]["hp"] = min(max(party_one[chosen_target[1]]["hp"] - dmg_to_self, 0), party_one[chosen_target[1]]["max_hp"])
            else:
                party_two[chosen_target[1]]["hp"] = min(max(party_two[chosen_target[1]]["hp"] - dmg_to_self, 0), party_two[chosen_target[1]]["max_hp"])

            dmg_to_self = 0

        if(not interrupt_turn):

            option.pop(0)
            
            if len(option) == 0:
                member["options"].remove(option)

        return False

    def RunQueuedStatements():
        global queued_statements;
        while len(queued_statements) > 0:
            statement = queued_statements[0]
            if statement[0] == "say":
                renpy.say(statement[1][0], statement[1][1])
                queued_statements.pop(0)
            elif statement[0] == "exec":
                dev_log("")
                dev_log("exec: " + statement[0])
                queued_statements.pop(0)
                exec(statement[1])
            else:
                dev_log("")
                dev_log("unknown: " + str(statement))
                queued_statements.pop(0)

    def ApplyFilter(function, text):
        return function(text)

    def CheckIfBattleOver():
        for condition in end_of_battle_conditions:
            if eval(condition[1]):
                global battle_result
                battle_result = condition[0]
                renpy.jump(end_battle_label)

    def FormatOption(text, option_type):
        if option_type == "violence":
            return "{color=FF0000}{font=ITC Eras Std Bold.otf}{u}" + text + "{/u}{/font}{/color}"
        elif option_type == "pacifism":
            return "{color=2357BC}{font=ITC Eras Std Bold.otf}{u}" + text + "{/u}{/font}{/color}"
        elif option_type == "team_player":
            return "{color=FCED23}{font=ITC Eras Std Bold.otf}{u}" + text + "{/u}{/font}{/color}"
        elif option_type == "isolation":
            return "{color=F36621}{font=ITC Eras Std Bold.otf}{u}" + text + "{/u}{/font}{/color}"
        elif option_type == "precision":
            return "{color=733B97}{font=ITC Eras Std Bold.otf}{u}" + text + "{/u}{/font}{/color}"
        elif option_type == "tenderness":
            return "{color=2FBBB3}{font=ITC Eras Std Bold.otf}{u}" + text + "{/u}{/font}{/color}"
        else:
            return "{color=FFFFFF}{font=ITC Eras Std Bold.otf}{u}" + text + "{/u}{/font}{/color}"

    locked_screens = []

    def ToggleLockScreen(screen, transition, **kwargs):
        global locked_screens
        if screen not in locked_screens:
            renpy.show_screen(screen, kwargs)
            locked_screens.append(screen)
        else:
            renpy.hide_screen(screen)
            locked_screens.remove(screen)

    def HideIfNotLocked(screen, _layer=None):
        global locked_screens
        if screen not in locked_screens:
            renpy.hide_screen(screen, _layer)

    def HideAllLockedScreens():
        global locked_screens
        for x in locked_screens:
            renpy.hide_screen(x)
        locked_screens = []

screen battle_screen:
    add VBox(Transform("#000000AA", ysize=110), "#000000AA", yalign=0)
    vbox:
        xalign 0.03 yalign 0.05
        spacing 5

        for member in party_one:
            frame:
                size_group "party"
                xminimum 250 xmaximum 250
                yminimum 75
                vbox:
                    textbutton "{font=[gui.name_text_font]}[member['name']]{/font}":
                        text_size 36
                        xalign 0.5
                        action Function(ToggleLockScreen, "characters_screen", dissolve, character=member['source'])
                        if "characters_screen" in locked_screens:
                            tooltip "Click to unlock character sheet"
                        else:
                            tooltip "Click to lock character sheet"
                        hovered Show("characters_screen", transition=dissolve, character=member['source'])
                        unhovered Function(HideIfNotLocked, "characters_screen")
                    null height 5
                    hbox:
                        bar:
                            xmaximum 130
                            value member["hp"]
                            range member["max_hp"]
                            left_gutter 0
                            right_gutter 0
                            left_bar Frame("gui/DX_button/stats_bar/bar_Violent_Fill.png", 10, 0)
                            right_bar Frame("gui/DX_button/stats_bar/bar_Violent_BG.png", 10, 0)
                            thumb None
                            thumb_shadow None

                        null width 5

                        text "[member['hp']] / [member['max_hp']]" size 26
            vbox:
                frame:
                    size_group "party"
                    yminimum 30
                    text "Actions" yalign 0.5 xalign 0.5
                for option in member["options"]:
                    # TODO: match the logos and colors up properly
                    button:
                        action [Function(DoOption, party_one, member, option, party_two), Function(HideAllLockedScreens)]
                        sensitive whose_turn == "party_one"

                        at transform:
                            on idle:
                                outline_transform(-1, "#fff", 0.0)
                            on hover:
                                outline_transform(1, "#fff", 8.0, num_passes=4)

                        tooltip OptionDescription(member, option)
                        hbox:
                            text "[option[0][-1]]":
                                size 50
                            add "gui/DX_button/[option[0][-2]].png":
                                xpos 0
                                ypos -8
                                zoom 0.125

    vbox:
        xalign 0.97 yalign 0.05
        spacing 5

        if party_two != []:
            for i, member in enumerate(party_two):
                hbox:
                    if selecting_target and member["hp"] > 0:
                        textbutton "Choose ->" action [Function(ChooseTarget, i), Function(HideAllLockedScreens)] yminimum 75

                    frame:
                        size_group "enemies"
                        xminimum 250 xmaximum 250
                        yminimum 75
                        vbox:
                            text "{font=[gui.name_text_font]}[member['name']]{/font}" size 36 xalign 0.5
                            null height 5
                            hbox:
                                text "[member['hp']] / [member['max_hp']]" size 26
                                null width 5
                                bar:
                                    xmaximum 130
                                    value member["hp"]
                                    range member["max_hp"]
                                    left_gutter 0
                                    right_gutter 0
                                    left_bar Frame("gui/DX_button/stats_bar/bar_Violent_Fill.png", 10, 0)
                                    right_bar Frame("gui/DX_button/stats_bar/bar_Violent_BG.png", 10, 0)
                                    thumb None
                                    thumb_shadow None

    on "show" action Function(CheckIfBattleOver)