#### KEYBOARD-FRIENDLY CURSOR by Devil Spiδεr####
# This file enables a special displayable to dynamically move between focused displayables, working as an animated cursor.
# In some games controlled by a keyboard/controller, the cursor comes in the form of a frame-like object highlighting the focused button
# and this script enables such functionality in Ren'Py

# All you need is an image (for gui.focus_frame_image). To enable the displayable, put the following into any screen you want to add it to, preferrably to the bottom:
# add "focus_frame"

define gui.focus_frame_image = "gui/example.png" # an image path as a string - make sure it exists!
define gui.slide_time = 0.2 # how long should the movement take
define gui.focus_warper = "linear" #  what easing function to use?
define gui.focus_padding = (0, 0) # how far away in pixels the corners of the displayable are from the actual focused button

## UPDATE 3/2/2024: Added a "pulse" feature which periodically makes the frame pulse in a sine-like pattern
define gui.focus_pulse_amp = 0 # how much (in pixels) the frame "pulses". Set to 0 to disable
define gui.focus_pulse_time = 1.0 # the period of the frame's "pulse"

## CODE RESPONSIBLE FOR THE FUNCTIONALITY

init python:
    import math

    def get_size(img):
        ren = renpy.render(Transform(img), 0, 0, 0, 0)
        w, h = ren.get_size()
        return int(w), int(h)

    class MoveFocus(object):
        def __init__(self, anchor_point=(0.0,0.0)):
            global slide_time
            self.anchor_point = anchor_point
            self.speed = gui.slide_time # how much time will the transition take?
            # INTERNAL VARIABLES
            self.old_focus = (0, 0, 0, 0) # store the old focus point
            self.new_focus = None # store the new focus point
            self.start_t = 0.0 # Start time of the animation
            self.in_movement = False # are we moving?
            self.first_time = True #Is this the first time we start the animation?

        def __call__(self, trans, st, at):
            trans.xoffset = -self.anchor_point[0]*get_size(Image(gui.focus_frame_image))[0] + 2*gui.focus_padding[0]*(self.anchor_point[0]-0.5) + 2*gui.focus_pulse_amp*math.sin(2*math.pi*st/gui.focus_pulse_time)*(self.anchor_point[0]-0.5)
            trans.yoffset = -self.anchor_point[1]*get_size(Image(gui.focus_frame_image))[1] + 2*gui.focus_padding[1]*(self.anchor_point[1]-0.5) + 2*gui.focus_pulse_amp*math.sin(2*math.pi*st/gui.focus_pulse_time)*(self.anchor_point[1]-0.5)
            if self.in_movement: # Check if we're in movement
                #print("Moving!")
                if self.first_time:
                    trans.xpos = int(self.new_focus[0] + self.anchor_point[0]*self.new_focus[2])
                    trans.ypos = int(self.new_focus[1] + self.anchor_point[1]*self.new_focus[3])
                    trans.alpha = 1.0
                    self.first_time = False
                    self.in_movement = False
                    self.old_focus = self.new_focus
                else:
                    prog = (st - self.start_t) / self.speed
                    progw = eval(f"_warper.{gui.focus_warper}({prog})")
                    # damp = max(2 - 5*self.speed,1.1)
                    if prog > 1.0: # have we hit our new point?
                        trans.xpos = int(self.new_focus[0] + self.anchor_point[0]*self.new_focus[2])
                        trans.ypos = int(self.new_focus[1] + self.anchor_point[1]*self.new_focus[3])
                        self.in_movement = False
                        self.old_focus = self.new_focus
                    else:
                        # setting influence
                        old_i = 0 if prog >= 1 else 1-progw
                        new_i = 1 if prog >= 1 else progw
                        trans.xpos = int((self.old_focus[0] + self.anchor_point[0]*self.old_focus[2])*old_i + new_i*(self.new_focus[0] + self.anchor_point[0]*self.new_focus[2]))
                        trans.ypos = int((self.old_focus[1] + self.anchor_point[1]*self.old_focus[3])*old_i + new_i*(self.new_focus[1] + self.anchor_point[1]*self.new_focus[3]))

            else: # if we're not
                # we get our focused displayable
                if self.first_time:
                    trans.alpha = 0.0
                self.new_focus = renpy.focus_coordinates()
                if (self.new_focus == (None, None, None, None)) or (self.new_focus == self.old_focus):
                    pass #if no change or no displayable
                else:
                    # We start the animation, setting the needed things
                    self.start_t = st
                    self.in_movement = True
            return 0

image focus_frame:
    contains: # top left
        gui.focus_frame_image
        function MoveFocus((0.0, 0.0))
    contains: # bottom right
        gui.focus_frame_image
        anchor (0.0, 0.0)
        zoom -1.0
        function MoveFocus((1.0, 1.0))
    contains: # bottom left
        gui.focus_frame_image
        anchor (0.0, 0.0)
        yzoom -1.0
        function MoveFocus((0.0, 1.0))
    contains: # top right
        gui.focus_frame_image
        anchor (0.0, 0.0)
        xzoom -1.0
        function MoveFocus((1.0, 0.0))
