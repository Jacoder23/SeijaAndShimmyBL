################################################################################
##
## Parallax Viewport for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains an example screen demonstrating how to use the
## parallax_viewport screen language statement. You are free to delete this
## file if you don't need the examples; all the backend code is in
## 01_parallax_viewport.rpy.
##
## To see the example parallax viewport screen, jump to the included
## test_parallax_vp label e.g.
##
# label start:
#     jump test_parallax_vp
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################

## NOTE: If you're having trouble with Ren'Py claiming your Fixed is past the
## maximum size, you can use this config value to increase the maximum size.
# define config.max_fit_size = 10000

################################################################################
## Example images for the parallax viewport
################################################################################
## This would look nicer as a gradient of course but I'm trying to avoid
## including images!
image chunky_background = VBox(
    Transform("#2b175a", xysize=(700, 400), alpha=1.0),
    Transform("#17295a", xysize=(700, 400), alpha=0.5),
    Transform("#19338a", xysize=(700, 400), alpha=0.5),
    Transform("#303ba1", xysize=(700, 400), alpha=0.5),
    Transform("#2b6fa7", xysize=(700, 400), alpha=0.5),
    Transform("#2b8ea7", xysize=(700, 400), alpha=0.5),
    Null(height=200),
    Transform("#2b8ea7", xysize=(700, 200), alpha=1.0),
    spacing=-200
)
image stars_back = Fixed(
    *[Transform("#fffb", xysize=(5, 5), align=(renpy.random.random(), renpy.random.random())) for x in range(100)],
    xysize=(700, 1300)
)
image stars_mid = Fixed(
    *[Transform("#fffd", xysize=(5, 5), align=(renpy.random.random(), renpy.random.random())) for x in range(200)],
    xysize=(700, 1800)
)

## Simplified "forest" background for demonstration
image forest_back_t = Fixed(
    Transform("#4F6379FF"),
    Transform("#54697FFF", ysize=130, yalign=0.5),
    Transform("#596E84FF", ysize=80, yalign=0.5),
    HBox(*[Transform("#4F6379FF", xsize=15) for x in range(10)], xfill=True),
    xysize=(928, 272)
)
image forest_mid_t = Fixed(
    HBox(*[Transform("#232B42FF", xsize=10) for x in range(6)], xfill=True),
    HBox(*[Transform("#232B42FF", xsize=18) for x in range(18)], xfill=True),
    HBox(*[Transform("#232B42FF", xsize=100, ysize=50, xoffset=-35) for x in range(18)], xfill=True),
    xysize=(928*2, 272)
)
image forest_front_t = Fixed(
    HBox(*[Transform("#0C1122FF", xsize=9) for x in range(6)], xfill=True),
    HBox(*[Transform("#0C1122FF", xsize=38) for x in range(12)], xfill=True),
    HBox(*[Transform("#0C1122FF", xsize=150, ysize=80, xoffset=-55) for x in range(12)], xfill=True),
    HBox(*[Transform("#18402AFF", xsize=110, ysize=120) for x in range(8)], xfill=True, yalign=1.0),
    xysize=(928*3, 272)
)

################################################################################
## EXAMPLE SCREEN
################################################################################
screen test_parallax_screen():

    default auto_scroll_forest = False

    vbox:
        align (1.0, 0.5) spacing 10
        textbutton "Click me to auto scroll to the top":
            xalign 0.5 text_hover_color "#FFF" text_idle_color "#c3a5fa"
            action AnimateScroll("parallax_vp_ex1", "vertical decrease",
                ## Scrolls it to the start
                "min", 15.0, "linear")

        ## Here's how you can declare a parallax viewport in screen language.
        parallax_viewport:
            ## Here you can put regular viewport properties. Anything you'd use
            ## for a regular viewport works here, like draggable, mousewheel,
            ## edgescroll, etc. I suggest you also set the size of the viewport.
            ## Notably, edgescroll and dragging tend to look nicer than
            ## mousewheel, which jumps the scrolling in chunks.
            mousewheel True draggable True
            edgescroll (100, 600)
            xysize (700, int(config.screen_height*0.8))
            ## This is used for the AnimatedScroll action later.
            id 'parallax_vp_ex1'
            ########################################
            ## IMPORTANT!!!
            ## Your parallax viewport MUST have this line in order to work.
            has fixed style "vparallax_fixed"
            ## End of Important
            ########################################

            ## Here is where your parallax layers will go. They must go in
            ## back-to-front order, and should typically go from smallest to
            ## largest for a proper parallax effect.
            add "chunky_background"
            add "stars_back"
            add "stars_mid"
            ## You can also include screen language elements in the parallax. Note
            ## that for them to work properly, anything that moves as a group must
            ## be in a container of some kind, typically with `xfit True yfit True`
            ## if it's a fixed container.
            frame:
                background None
                xsize 700 xalign 0.5 xpadding 10
                has vbox
                spacing 50 xalign 0.5
                text "This looks nicest when clicking and dragging or using edgescroll":
                    xalign 0.5 text_align 0.5 color "#fff"
                for i in range(60):
                    text "{} You could put credits\nor something here".format(i):
                        xalign 0.5 text_align 0.5 color "#fff"

        textbutton "Click me to auto scroll to the bottom":
            xalign 0.5 text_hover_color "#FFF" text_idle_color "#c3a5fa"
            ## This is a custom Scroll action which takes a warper and
            ## special arguments "max" or "min" for the amount to scroll.
            action AnimateScroll("parallax_vp_ex1", "vertical increase",
                ## Scrolls it to the end
                "max", 15.0, "linear")

    vbox:
        align (0.0, 0.5)
        ## Here's another viewport, which scrolls horizontally. It has some
        ## buttons on each parallax layer which scroll with the layer itself.
        parallax_viewport:
            mousewheel "horizontal" draggable True
            edgescroll (100, 600)
            xysize (800, 272)
            id "parallax_vp_ex2"
            ## Important!! This line is required just before you add your layers.
            has fixed style "vparallax_fixed"
            ## End of important

            ## Here we use a fixed container to hold each parallax layer. It
            ## uses fit_first so it's the size of the image, and then includes a
            ## textbutton.
            fixed:
                fit_first True
                add "forest_back_t"
                textbutton "This is a button in the background":
                    action Notify("BG pressed") align (0.2, 0.8)
            fixed:
                fit_first True
                add "forest_mid_t"
                textbutton "This is a button in the midground":
                    action Notify("MG pressed") align (0.5, 0.5)
            fixed:
                fit_first True
                add "forest_front_t"
                textbutton "This is a button in the foreground":
                    action Notify("FG pressed") align (0.9, 1.0)

        textbutton "Toggle auto scroll":
            xalign 0.5 text_hover_color "#f93c3e" text_idle_color "#fff"
            text_selected_idle_color "#ff8335"
            action ToggleScreenVariable("auto_scroll_forest")

    textbutton _("Return") action Return()

    if auto_scroll_forest:
        ## Initial timer makes it scroll when the button is pressed
        timer 0.01 action AnimateScroll("parallax_vp_ex2", None, "horizontal toggle", 5.0, "ease")
        ## This timer repeats so it scrolls over and over
        timer 5.5 action AnimateScroll("parallax_vp_ex2", None, "horizontal toggle", 5.0, "ease") repeat True


label test_parallax_vp():
    "Start of parallax viewport test"

    call screen test_parallax_screen()

    "End of test"
    return