screen flowchart:
    vbox:
        xalign 0.05
        yalign 0.95
        label "Upgrade Points: [upgrade_points]"
    vbox:
        xalign 0.95
        yalign 0.95
        textbutton "Continue":
            action Function(renpy.call_in_new_context, "continue_storylets")
    vbox:
        # label "Progress"
        # label " "
        label "Party"
        frame:
            size_group "party"
            xminimum 250 xmaximum 250
            yminimum 75
            vbox:
                textbutton "{font=[gui.name_text_font]}[shin_battler.name]{/font}":
                    text_size 36
                    xalign 0.5
                    action ToggleScreen("characters_screen", transition=Dissolve, character=shin_battler)
                    tooltip "Open character sheet"
                if chapter == 2:
                    textbutton "{font=[gui.name_text_font]}[seija_battler.name]{/font}":
                        text_size 36
                        xalign 0.5
                        action ToggleScreen("characters_screen", transition=Dissolve, character=seija_battler)
                        tooltip "Open character sheet"
    hbox:
        viewport:
            xalign 0.5
            mousewheel True
            draggable True
            scrollbars "vertical"
            vbox:
                xfill True
                xalign 0.5
                yalign 0.1
                spacing -10
                for i in range(0, 100):
                    if len([x.urgency == 100 - i for x in storylets]) > 0:
                        hbox:
                            xalign 0.5
                            spacing 50
                            for storylet in [x for x in storylets if x.urgency == 100 - i]:
                                $ previewColor = "FFF" if storylet.completed else "999"
                                if persistent.showStoryletPreviews or storylet.completed:
                                    label "{color=[previewColor]}[storylet.preview]{/color}"
                                else:
                                    label "{color=[previewColor]}???{/color}"