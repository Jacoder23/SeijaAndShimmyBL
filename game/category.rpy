#-----------------------------------------------------
# How this basically works:
#   -Player clicks on the "Codex" button in the main menu/quick menu.
#   -Show "category_welcome" screen where they can select a category.
#   -that brings them to the welcome page/main page of the selected category. Ex.: people_welcome in people.rpy
#   -there they can select an entry to read.


##-----------------------------------------------
##-------CATEGORY NAVIGATION---------------------
##-----------------------------------------------
screen category_nav():

    #This is where we create the menu where we can select the category.

    #Add background image
    add "gui/overlay/game_menu.png"

    viewport:
        xpos 25 ypos 400
        xsize 350 ysize 350
        mousewheel True
        scrollbars "vertical"
        draggable True
        pagekeys True
        vbox:
            spacing 10
            xoffset 350

            ##Here you list the categories
            textbutton "People" action ShowMenu("people_welcome")
            ##people_welcome is the main screen/welcome screen of the "People" category, defined in people.rpy. I suggest you create seperate files
            # for all categories so it's easier to edit.

            ##The buttons below don't do anything. Set up your category as seen in people.rpy then
            ## switch "NullAction" with the "ShowMenu("screen name")" command like above.

            textbutton "Locations" action NullAction()
            textbutton "Historical events" action NullAction()
            textbutton "Books and tales" action NullAction()
            textbutton "Rumors" action NullAction()
            textbutton "Culture and Religion" action NullAction()
            textbutton "Miscellaneous" action NullAction()

    textbutton "Return" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen category_welcome():
    #This is the "Welcome screen", the first screen the player sees when they go into the codex menu.

    tag menu
    add VBox(Transform("#000000AA", ysize=110), "#000000AA", yalign=0)
    use category_nav #instead of the usual menu, we'll use the one we created above

    style_prefix "codex"

    vbox:
            xsize 850
            xalign 0.5 yalign 0.5
            xoffset 200
            #xoffset 400
            text _p("""Welcome to the codex!{p}If you click on any of the buttons besides 'People' and nothing happens, don't worry!
                    It is because setting those up would involve a lot of unnecessary copy-paste work. Same goes for some entries in the
                    'People' category. Start the game to unlock the hidden entries.""")
            #text _p("""Welcome to the codex!""")


            #Really short text might not be centered correctly, you have to adjust the xoffset.

style codex_label is gui_label:
    xalign 0.5
    xoffset 150
    yoffset 100
    size 50
style codex_label_text is gui_label_text
style codex_text is gui_text:
    justify True
style codex_label_text:
    size gui.label_text_size
style codex_scrollbar is gui_vscrollbar:
    xoffset 100
