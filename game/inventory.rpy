# inventory system taken from a deranged reddit post
# https://www.reddit.com/r/RenPy/comments/wanes3/how_to_do_an_inventory_system/ii2vp6i/
screen inventory_display_toggle:
    zorder 200
    frame:
        background "resize_frame"
        xalign 0.98
        yalign 0.98

        imagebutton idle "gui/DX_button/Inventory.png":
            action ToggleScreen("inventory")
            at choice_hover
            at transform:
                zoom 0.15

    on "hide" action Hide("inventory")

default all_possible_items = [("Key", "Test")]
default inventory_items = [("Key", "Test")]
default item_selected = ""
default item_item_description = ""

style inv_button_text:
    xalign 0.5
    yalign 0.5

image resize_frame = Frame("gui/DX_button/TextBox.png", 95, 75)

screen inventory:
    window:
        background "resize_frame"
        xsize 600
        ysize 300
        xalign 0.5
        yalign 0.15
        padding (50, 100)
        grid 3 3:
            yoffset 20
            xalign 0.5
            yalign 0.5
            spacing 15
            style_prefix "inv"
            for item in inventory_items:
                textbutton item[0]:
                    text_font gui.name_text_font
                    text_idle_color black
                    text_hover_color gold
                    action SetVariable("item_selected", item[0])
                    tooltip f"{item[1]}"

        textbutton "X" action Hide("inventory") xalign 0.97 yalign 1 yoffset -67 xoffset 23 text_size 20