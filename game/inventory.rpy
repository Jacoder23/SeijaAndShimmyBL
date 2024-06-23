# inventory system taken from a deranged reddit post
# https://www.reddit.com/r/RenPy/comments/wanes3/how_to_do_an_inventory_system/ii2vp6i/
screen inventory_display_toggle:
    zorder 200
    frame:
        background "#000000cc"
        xalign 0.98
        yalign 0.98

        textbutton "INV":
            action ToggleScreen("inventory")

    on "hide" action Hide("inventory")

default all_possible_items = [("Key", "Test")]
default inventory_items = [("Key", "Test")]
default item_selected = ""
default item_item_description = ""

style inv_button_text:
    xalign 0.5
    yalign 0.5

screen inventory:
    window:
        background "#000000cc"
        xsize 600
        ysize 300
        xalign 0.5
        yalign 0.15
        grid 3 3:
            xalign 0.5
            yalign 0.5
            spacing 15
            style_prefix "inv"
            for item in inventory_items:
                textbutton item[0]:
                    text_font gui.name_text_font
                    action SetVariable("item_selected", item[0])
                    tooltip f"{item[1]}"