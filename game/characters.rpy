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
        if isinstance(current_character, collections.Mapping): # somehow it changes from a custom object to a dict; happens if you show without using the action Show but the show_screen statement; I do not know why
            $ current_character = current_character['character']
    add "gui/DX_button/CharacterSheet_BG_NoText.png"
    label f"{current_character.name.upper()}":
        text_size 100
        text_font "fonts/ITC Eras Std Bold.otf"
        xalign 0.5
        ypos 65
    frame:
        xalign 0.5 yalign 0.5
        if renpy.exists(f"images/{current_character.name.lower()}.png"):
            add f"images/{current_character.name.lower()}.png":
                    xpos 720
                    ypos 250
                    at TakeOnMe
                    at transform:
                        outline_transform(2, "#fff", 12.0, num_passes=4)
                        alpha 0.1
        if renpy.exists(f"images/{current_character.name.lower()}.png"):
            imagebutton idle f"images/{current_character.name.lower()}.png" hover f"images/{current_character.name.lower()} talk happy.png":
                action NullAction()
                xpos 950
                ypos 220
                at transform:
                    outline_transform(2, "#fff", 12.0, num_passes=4)
                    zoom 0.5
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
                            if can_upgrade and upgrade_points > 0:
                                textbutton "HP: [current_character.max_hp] (+ 2)":
                                    action Function(UpgradeAttribute, current_character, "HP")
                                    tooltip "Your health. CLICK TO UPGRADE."
                                    text_color "#000000"
                                    at glowing_interactable
                                textbutton "Power: [current_character.power] (+ 1)":
                                    action Function(UpgradeAttribute, current_character, "Power")
                                    tooltip "Your raw ability to inflict pain. CLICK TO UPGRADE."
                                    text_color "#000000"
                                    at glowing_interactable
                                textbutton "Agility: [current_character.agility] (+ 1)":
                                    action Function(UpgradeAttribute, current_character, "Agility")
                                    tooltip "Your raw ability to avoid pain. CLICK TO UPGRADE."
                                    text_color "#000000"
                                    at glowing_interactable
                                textbutton "Technique: [current_character.tech] (+ 1)":
                                    action Function(UpgradeAttribute, current_character, "Tech")
                                    tooltip "Your ability to be crafty. CLICK TO UPGRADE."
                                    text_color "#000000"
                                    at glowing_interactable
                            else:
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
                                    left_bar Frame("gui/DX_button/stats_bar/bar_Violent_Fill.png", 10, 0)
                                    right_bar Frame("gui/DX_button/stats_bar/bar_Violent_BG.png", 10, 0)
                                label " "
                                bar value StaticValue(current_character.pacifism, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                    at transform:
                                        xzoom -1
                                    left_bar Frame("gui/DX_button/stats_bar/bar_Pacifist_Fill.png", 10, 0)
                                    right_bar Frame("gui/DX_button/stats_bar/bar_Pacifist_BG.png", 10, 0)
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
                                    left_bar Frame("gui/DX_button/stats_bar/bar_TeamPlayer_Fill.png", 10, 0)
                                    right_bar Frame("gui/DX_button/stats_bar/bar_TeamPlayer_BG.png", 10, 0)
                                label " "
                                bar value StaticValue(current_character.isolation, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                    at transform:
                                        xzoom -1
                                    left_bar Frame("gui/DX_button/stats_bar/bar_Isolation_Fill.png", 10, 0)
                                    right_bar Frame("gui/DX_button/stats_bar/bar_Isolation_BG.png", 10, 0)
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
                                    left_bar Frame("gui/DX_button/stats_bar/bar_Precise_Fill.png", 10, 0)
                                    right_bar Frame("gui/DX_button/stats_bar/bar_Precise_BG.png", 10, 0)
                                label " "
                                bar value StaticValue(current_character.tenderness, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                    at transform:
                                        xzoom -1
                                    left_bar Frame("gui/DX_button/stats_bar/bar_Tender_Fill.png", 10, 0)
                                    right_bar Frame("gui/DX_button/stats_bar/bar_Tender_BG.png", 10, 0)
                                textbutton " TENDER":
                                    action NullAction()
                                    tooltip "Your solutions are emotional, considerate, and empathetic."
    
    vbox:
        xalign 0.65
        yalign 0.85
        textbutton "Return":
            action Hide("characters_screen", transition=dissolve)
