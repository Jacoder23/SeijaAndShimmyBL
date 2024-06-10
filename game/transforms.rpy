define longfade = Fade(0, 0.5, 3)

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define longflash = Fade(0.1, 1, 1, color="#fff")

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
    ease 0.10
    yoffset 3
    ease 0.12
    yoffset 4
    ease 0.14
    yoffset 5
    ease 0.16
    yoffset 6
    ease 0.18
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
    ease 0.18
    yoffset 7
    ease 0.16
    yoffset 6
    ease 0.14
    yoffset 5
    ease 0.12
    yoffset 4
    ease 0.10
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
    ease 0.10
    xoffset 3
    ease 0.12
    xoffset 4
    ease 0.14
    xoffset 5
    ease 0.16
    xoffset 6
    ease 0.18
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
    ease 0.18
    xoffset 7
    ease 0.16
    xoffset 6
    ease 0.14
    xoffset 5
    ease 0.12
    xoffset 4
    ease 0.10
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
    linear 0.125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.125 rotate 360

    around (.5, .5)
    alignaround (.5, .5)
    rotate 0
    linear 0.125 rotate 360