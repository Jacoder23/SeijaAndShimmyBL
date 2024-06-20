
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------
screen organizations_nav():
    add "gui/overlay/game_menu.png"

    viewport:
        xpos 25 ypos 400
        xsize 350 ysize 350
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        scrollbars "vertical"
        vbox:
            spacing 10
            xoffset 350
            textbutton "Hero HQ" action ShowMenu("herohq") # the more commonly used name over City OATH Mobile Intervention for Crises or COMIC
            textbutton "Local Gangs" action ShowMenu("gangs")
            textbutton "OATH" action ShowMenu("origins") # Office for the Accomodation and Training of Heroes
            textbutton "CAPES" action ShowMenu("capes") # Central Agency for the Profiling of Supers

    textbutton "Return to categories" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Return" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen organizations_welcome():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    add VBox(Transform("#000000AA", ysize=110), "#000000AA", yalign=0)
    use organizations_nav

    style_prefix "codex"
    vbox:
            xsize 850
            xalign 0.5 yalign 0.5
            xoffset 200
            text _("Select a file.")



##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------


screen zack():

    tag menu
    add VBox(Transform("#000000AA", ysize=110), "#000000AA", yalign=0)
    use people_nav

    style_prefix "codex"
    label "Zack Moss"

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 200 yoffset 200
        side_yfill True
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True


        vbox:
            #You write the actual entry here. I suggest you split your text into smaller text _p sections, otherwise the text might overlap with
            #the scrollbars. If you're sure that your text fits the screen and scrolling is not needed then comment out everything starting from "scrollbars vertical" to
            #"pagekeys True" as seen in the next entry. If you do this, splitting the text is not needed.

            vbox:
                text _p("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non massa iaculis, mattis urna at,
                eleifend augue. Vivamus non finibus velit. Suspendisse sit amet luctus turpis.{p}Nullam felis orci, maximus luctus aliquam eget,
                cursus nec lectus.Donec sollicitudin auctor urna, non rutrum sem aliquet et. Duis dignissim molestie luctus.""")

                text _p("""Aliquam nec neque risus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam tempor, nisl vitae fermentum
                tempus, metus nibh bibendum augue, et fermentum turpis massa eget ligula. Donec feugiat neque sit amet molestie ultrices. Vestibulum
                lacinia mi eros, in maximus neque sagittis vitae. Cras vestibulum cursus nulla eu rhoncus. Sed hendrerit faucibus dignissim. Vivamus
                sed mattis dui. Nunc eu finibus sem. Morbi malesuada lectus nec arcu auctor fermentum. """)

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

screen nelson():

    tag menu
    add VBox(Transform("#000000AA", ysize=110), "#000000AA", yalign=0)
    use people_nav

    style_prefix "codex"
    label "Nelson Shea"

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 200 yoffset 200
        side_yfill True
        #scrollbars "vertical"
        #mousewheel True
        #draggable True
        #pagekeys True

        vbox:
            text _p("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non massa iaculis, mattis urna at,
            eleifend augue. Vivamus non finibus velit. Suspendisse sit amet luctus turpis.{p}Nullam felis orci, maximus luctus aliquam eget,
            cursus nec lectus.Donec sollicitudin auctor urna, non rutrum sem aliquet et. Duis dignissim molestie luctus.""")

            text _p("""Aliquam nec neque risus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam tempor, nisl vitae fermentum
            tempus, metus nibh bibendum augue, et fermentum turpis massa eget ligula. Donec feugiat neque sit amet molestie ultrices. Vestibulum
            lacinia mi eros, in maximus neque sagittis vitae. Cras vestibulum cursus nulla eu rhoncus. Sed hendrerit faucibus dignissim. Vivamus
            sed mattis dui. Nunc eu finibus sem. Morbi malesuada lectus nec arcu auctor fermentum. """)