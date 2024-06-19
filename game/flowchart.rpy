screen flowchart:
    label "Progress"
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