screen characters_screen:
    #add "gui/character sheet background.png"
    add "gui/DX_button/CharacterSheet_BG_NoText.png"
    label "[current_character.name]":
        text_size 100
        xalign 0.5
        ypos 20
    frame:
        xalign 0.5 yalign 0.5
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
                            label "HP: [current_character.max_hp]"
                            label "Power: [current_character.power]"
                            label "Agility: [current_character.agility]"
                            label "Technique: [current_character.tech]"
                    label "PERSONALITY" text_size 40
                    frame:
                        xpos 50
                        ypos -5
                        vbox:
                            hbox:
                                label "{space=85}VIOLENT "
                                bar value StaticValue(current_character.violence, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                label " "
                                bar value StaticValue(current_character.pacifism, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                    at transform:
                                        xzoom -1
                                label " PACIFIST"
                            hbox:
                                label "TEAM PLAYER "
                                bar value StaticValue(current_character.team_player, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                label " "
                                bar value StaticValue(current_character.isolation, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                    at transform:
                                        xzoom -1
                                label " ISOLATED"
                            hbox:
                                label "{space=93}PRECISE "
                                bar value StaticValue(current_character.precision, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                label " "
                                bar value StaticValue(current_character.tenderness, 7):
                                    unscrollable "insensitive"
                                    xmaximum 150
                                    at transform:
                                        xzoom -1
                                label " TENDER"
