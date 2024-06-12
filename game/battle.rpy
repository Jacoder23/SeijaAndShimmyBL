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

    queued_say_statements = []

    def SkipTurn():
        pass

    def ChooseTarget(target):
        chosen_target = (1, target) # only the player actually uses this
        pass

    def SayDialogueData(dialogue):
        lines = dialogue.split("\n")

        for line in lines:
            sections = line.split(":", 1)
            if len(sections) == 1:
                queued_say_statements.append((n, sections[0]))
            else:
                queued_say_statements.append((globals()[sections[0]], sections[1]))

    def ApplyEffect(effect): # TODO: add vfx support to this 
                            # Just gonna have to assume everything in here is a variable change for now so I can add in the global keyword
                            # TODO: Figure out a smarter way than what I just described
        effects = effect.split(";")
        for line in effects:
            complete_line = "global " + line.split()[0] + "; " + line.strip()
            renpy.log(complete_line)
            exec(complete_line)

    def RollDice(dice_result, dc): # visual effect
        pass

    def DoOption(party, member, option): # maybe this should've been a dict or a custom class... eh it makes the writing part easier in trade for making the debugging a fucking ticking bomb
        # effect before outcome [0], effect on success [1], effect on failure [2], DC [3], stat [4], initial dialogue [5], post-success [6], post-failure [7], name of action [8]

        # TODO: assign each of these to its own variable instead of being part of an array; like just some variable declarations to make it clearer what is what

        current_option = option[0]

        exec(current_option[0])
        
        dice_roll = renpy.random.randint(1,20) + current_option[4]

        SayDialogueData(current_option[5])

        RollDice(dice_roll, current_option[3])

        if dice_roll >= current_option[3]:
            ApplyEffect(current_option[1])
            SayDialogueData(current_option[6])
        else:
            ApplyEffect(current_option[2])
            SayDialogueData(current_option[7])

        renpy.log(dmg_to_target)

        global dmg_to_target
        if dmg_to_target != 0:
            if chosen_target[0] == 1: # idk why this is 1 and not 0
                party_one[chosen_target[1]]["hp"] = max(party_one[chosen_target[1]]["hp"] - dmg_to_target, 0)
            else:
                party_two[chosen_target[1]]["hp"] = max(party_two[chosen_target[1]]["hp"] - dmg_to_target, 0)

            dmg_to_target = 0

        option.pop(0)
        
        if len(option) == 0:
            member["options"].remove(option)

        return False

screen battle_screen:
    vbox:
        xalign 0.03 yalign 0.05
        spacing 5

        for member in party_one:
            frame:
                size_group "party"
                xminimum 250 xmaximum 250
                yminimum 75
                vbox:
                    text "[member['name']]" size 36 xalign 0.5
                    null height 5
                    hbox:
                        bar:
                            xmaximum 130
                            value member["hp"]
                            range member["max_hp"]
                            left_gutter 0
                            right_gutter 0
                            thumb None
                            thumb_shadow None

                        null width 5

                        text "[member['hp']] / [member['max_hp']]" size 26
            vbox:
                frame:
                    size_group "party"
                    yminimum 30
                    text "Action" yalign 0.5 xalign 0.5
                for option in member["options"]:
                    textbutton "[option[0][-1]]":
                        text_size 30
                        action Function(DoOption, party_one, member, option)
                        yminimum 30
                        sensitive turn == "party_one"

    vbox:
        xalign 0.97 yalign 0.05
        spacing 5

        if party_two != []:
            for i, member in enumerate(party_two):
                hbox:
                    if selecting_target and member["hp"] > 0:
                        textbutton "Choose ->" action Function(ChooseTarget, i) yminimum 75

                    frame:
                        size_group "enemies"
                        xminimum 250 xmaximum 250
                        yminimum 75
                        vbox:
                            text "[member['name']]" size 36 xalign 0.5
                            null height 5
                            hbox:
                                bar:
                                    xmaximum 130
                                    value member["hp"]
                                    range member["max_hp"]
                                    left_gutter 0
                                    right_gutter 0
                                    thumb None
                                    thumb_shadow None

                                null width 5

                                text "[member['hp']] / [member['max_hp']]" size 26

    # on "show" action Function(RunBattleTurn)