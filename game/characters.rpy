init python:
    def UpgradeAttribute(character, upgrade_type):

        global upgrade_points;
        global can_upgrade;

        can_upgrade = can_upgrade and upgrade_points > 0

        if not can_upgrade:
            return NullAction()

        if upgrade_type == "HP":
            character.max_hp += 2
            upgrade_points -= 1
        elif upgrade_type == "Power":
            character.power += 1
            upgrade_points -= 1
        elif upgrade_type == "Agility":
            character.agility += 1
            upgrade_points -= 1
        elif upgrade_type == "Tech":
            character.tech += 1
            upgrade_points -= 1

        return NullAction()


screen characters_screen(character = None):
    #add "gui/character sheet background.png"
    if character is not None:
        $ current_character = character
    add "gui/DX_button/CharacterSheet_BG_NoText.png"
    label "[current_character.name]":
        text_size 100
        xalign 0.5
        ypos 20
    frame:
        xalign 0.5 yalign 0.5
        if renpy.exists("images/character sheets/" + current_character.name + ".png"):
            add "images/character sheets/[current_character.name].png":
                zoom 0.5
                xpos 1000
                ypos 250
        hbox:
            xalign 0.5 yalign 0.5
            frame:
                xalign 0.5 yalign 0.5
                vbox:
                    spacing -9
                    label "ROLE" text_size 40
                    frame:
                        xpos 50
                        ypos -5
                        vbox:
                            if current_character.name == "Seija":
                                label "Villain"
                            elif current_character.name == "Shin" and chapter == 1:
                                label "Hero"
                            elif current_character.name == "Shin" and chapter != 1:
                                label "Villain"
                            elif current_character.name == "Kogasa":
                                label "Rogue"
                            elif current_character.name == "Raiko":
                                label "Grunt" # TODO: update this in case he leaves
                            elif current_character.name == "Sekibanki":
                                label "Hero"
                            else:
                                label "Unknown"
                    label "ATTRIBUTES" text_size 40
                    frame:
                        xpos 50
                        ypos -5
                        vbox:
                            textbutton "HP: [current_character.max_hp]":
                                action Function(UpgradeAttribute, current_character, "HP")
                                tooltip "Your health."
                            textbutton "Power: [current_character.power]":
                                action Function(UpgradeAttribute, current_character, "Power")
                                tooltip "Your raw ability to inflict pain."
                            textbutton "Agility: [current_character.agility]":
                                action Function(UpgradeAttribute, current_character, "Agility")
                                tooltip "Your raw ability to avoid pain."
                            textbutton "Technique: [current_character.tech]":
                                action Function(UpgradeAttribute, current_character, "Tech")
                                tooltip "Your ability to be crafty."
                    label "PERSONALITY" text_size 40
                    frame:
                        xpos 50
                        ypos -5
                        vbox:
                            hbox:
                                textbutton "{space=85}VIOLENT ":
                                    action NullAction()
                                    tooltip "You solve problems with physical force."
                                bar value StaticValue(current_character.violence, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                label " "
                                bar value StaticValue(current_character.pacifism, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                    at transform:
                                        xzoom -1
                                textbutton " PACIFIST":
                                    action NullAction()
                                    tooltip "You solve problems without physical force."
                            hbox:
                                textbutton "TEAM PLAYER ":
                                    action NullAction()
                                    tooltip "You work better with others in solving problems."
                                bar value StaticValue(current_character.team_player, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                label " "
                                bar value StaticValue(current_character.isolation, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                    at transform:
                                        xzoom -1
                                textbutton " ISOLATED":
                                    action NullAction()
                                    tooltip "You work better alone in solving problems."
                            hbox:
                                textbutton "{space=93}PRECISE ":
                                    action NullAction()
                                    tooltip "Your solutions are precise, measured, and rational."
                                bar value StaticValue(current_character.precision, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                label " "
                                bar value StaticValue(current_character.tenderness, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                    at transform:
                                        xzoom -1
                                textbutton " TENDER":
                                    action NullAction()
                                    tooltip "Your solutions are emotional, considerate, and empathetic."
    
    vbox:
        xalign 0.65
        yalign 0.85
        textbutton "Return":
            action Hide("characters_screen", transition=Dissolve)
