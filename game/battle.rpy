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

    def SkipTurn():
        pass

    def ChooseTarget(target):
        pass

    def DoOption(party, member, option):
        option.pop(0)

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
                    text "Choices" yalign 0.5 xalign 0.5
                for option in member["options"]:
                    textbutton "[option[0][-1]]" text_size 30 action Function(DoOption, party_one, member, option) yminimum 30

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

                                text "[member['hp']] / [member['max_hp']]" size 16

    # on "show" action Function(RunBattleTurn)