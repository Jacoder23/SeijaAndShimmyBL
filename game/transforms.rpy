define longfade = Fade(0, 0.5, 3)

define flash = Fade(1, 0.0, 0.5, color="#fff")

define longflash = Fade(1, 1, 1, color="#fff")

transform glowing_interactable:
    outline_transform(1, "#bdbdbd", 3.0)
    on idle:
        ## This animates the outline increasing/decreasing in size,
        ## but you can omit the `ease 0.1` part also for no animation.
        ease 0.4 outline_transform(1, "#bdbdbd", 3.0, end_color="#00859c")
        ease 0.4 outline_transform(2, "#bdbdbd", 3.0, end_color="#00859c")
        repeat
    on hover:
        ease 0.05 outline_transform(1, "#00ff55", 3.0)

define x_pos_stack_spacing = 200

init python:

    # TODO: track character/images disappearing (including on scene changes) and when a character already shown in the stack is shown again

    n_in_left_stack = 0

    n_in_right_stack = 0

    # TODO: check if this is frame rate dependent
    # uh yeah it is, lets not make a renpy game with a locked fps

    def left_stack_inc(*arg):
        global n_in_left_stack
        n_in_left_stack += 1

    def right_stack_inc(*arg):
        global n_in_right_stack
        n_in_right_stack += 1

    def reset_stacks():
        global n_in_left_stack
        global n_in_right_stack
        n_in_left_stack = 0
        n_in_right_stack = 0

transform left_stack:
    xpos 340 - n_in_left_stack * x_pos_stack_spacing
    yalign 1 - n_in_left_stack**2/25
    zoom 0.95 + n_in_left_stack**2/25
    function left_stack_inc

transform right_stack:
    xpos 740 + n_in_right_stack * x_pos_stack_spacing
    yalign 1 - n_in_right_stack/25
    zoom 0.95 + n_in_right_stack/25
    function right_stack_inc

transform face_left:
    xzoom 1.0

transform face_right:
    xzoom -1.0

transform damaged:
    yalign 0.5
    xalign 0.5
    ease .08 xoffset 40
    ease .08 xoffset -40
    ease .07 xoffset 30
    ease .07 xoffset -30
    ease .06 xoffset 20
    ease .06 xoffset -20
    ease .05 xoffset 15
    ease .05 xoffset -15
    ease .04 xoffset 10
    ease .04 xoffset -10
    ease .03 xoffset 5
    ease .03 xoffset -5
    ease .02 xoffset 2
    ease .02 xoffset -2
    ease .01 xoffset 0

transform thrown_offscreen:
    ease .5 xoffset 100 yoffset -100
    ease .4 xoffset 200 yoffset -200
    ease .3 xoffset 400 yoffset -400
    ease .3 xoffset 800 yoffset -800
    ease .2 xoffset 1600 yoffset -1600
    ease .2 xoffset 3200 yoffset -3200
    ease .1 xoffset 6400 yoffset -6400

transform flip:
    xzoom -1.0

transform unflip:
    xzoom 1.0

transform idle_vertical:
    yoffset 0
    ease 0.06
    yoffset 1
    ease 0.08
    yoffset 2
    ease 10
    yoffset 3
    ease 12
    yoffset 4
    ease 14
    yoffset 5
    ease 16
    yoffset 6
    ease 18
    yoffset 7
    ease 0.20
    yoffset 8
    ease 0.22
    yoffset 9
    ease 0.48
    yoffset 10
    ease 0.22
    yoffset 9
    ease 0.20
    yoffset 8
    ease 18
    yoffset 7
    ease 16
    yoffset 6
    ease 14
    yoffset 5
    ease 12
    yoffset 4
    ease 10
    yoffset 3
    ease 0.08
    yoffset 2
    ease 0.06
    yoffset 1
    ease 0.04
    repeat

transform idle_horizontal:
    xoffset 0
    ease 0.06
    xoffset 1
    ease 0.08
    xoffset 2
    ease 10
    xoffset 3
    ease 12
    xoffset 4
    ease 14
    xoffset 5
    ease 16
    xoffset 6
    ease 18
    xoffset 7
    ease 0.20
    xoffset 8
    ease 0.22
    xoffset 9
    ease 0.48
    xoffset 10
    ease 0.22
    xoffset 9
    ease 0.20
    xoffset 8
    ease 18
    xoffset 7
    ease 16
    xoffset 6
    ease 14
    xoffset 5
    ease 12
    xoffset 4
    ease 10
    xoffset 3
    ease 0.08
    xoffset 2
    ease 0.06
    xoffset 1
    ease 0.04
    repeat

transform disappear:
    linear 0.25 alpha 0

transform spin:
    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 1 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.75 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.5 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.25 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 125 rotate 360

transform dice_text1:
    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.1 rotate 10

transform dice_text2:
    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 10
    ease 0.1 rotate 0

transform dice_text3:
    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.1 rotate -10

transform dice_text4:
    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate -10
    ease 0.1 rotate 0

transform dice_text5:
    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.6 rotate 360

transform dice_text_center:
    xalign 0.5
    yalign 0.5

transform dice_shake:
    # repeat 4
    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.1 rotate 10

    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 10
    ease 0.1 rotate 0
    
    
    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.1 rotate 10

    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 10
    ease 0.1 rotate 0

    
    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.1 rotate 10

    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 10
    ease 0.1 rotate 0


    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.1 rotate 10

    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 10
    ease 0.1 rotate 0
    #

    #
    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.1 rotate -10

    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate -10
    ease 0.1 rotate 0


    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.1 rotate -10

    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate -10
    ease 0.1 rotate 0


    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.1 rotate -10

    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate -10
    ease 0.1 rotate 0


    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.1 rotate -10

    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate -10
    ease 0.1 rotate 0
    #

    around (.5, .5)
    alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    ease 0.6 rotate 360