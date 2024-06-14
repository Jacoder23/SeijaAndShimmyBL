# https://www.reddit.com/r/RenPy/comments/18z3v7v/renpy_tooltip_position/kgf0ri9/

default mouse_xy = (0, 0)

screen test:
    imagebutton:
        focus_mask True
        idle "images/computer/browser_idle.png"
        anchor (0.5, 0.5)
        pos (285,1008)
        tooltip "Burning Chrome"
        action NullAction()

    $ tooltip = GetTooltip()

    if tooltip:
        timer 0.1 repeat True action Function(get_mouse)
        $ mx = mouse_xy[0] - 30 # LR
        $ my = mouse_xy[1] + 30 # UD
        text tooltip:
            pos(mx, my)
            color "#fff"
            size 15
            outlines [(2, "#000005", 0, 0)]

init python:
    def get_mouse():
        global mouse_xy
        mouse_xy = renpy.get_mouse_pos()