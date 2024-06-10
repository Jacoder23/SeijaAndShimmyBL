init python:
    import random
    import functools
    import copy
    def boopy_voice(event, interact=True, boopfile="bleeps/bleep001.ogg", **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play(boopfile, loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(fadeout=1)

define sei = Character("Seija", callback = [name_callback, functools.partial(boopy_voice, boopfile="bleeps/bleep002.ogg")], cb_name = "Seija")
define n = Character("", callback = name_callback, cb_name = "")

image sei neutral = At('this sprite does not exist', sprite_highlight('sei'))

image placeholder:
    "placeholder.jpg"

# The game starts here.

label start:

    # $ cinematic = True

    python:
        import functools

        @functools.total_ordering
        class Storylet:
            def __init__(self, label, prerequisites, results, urgency, completed):
                self.label = label                      # which label to jump to; the content of the storylet
                self.prerequisites = prerequisites      # what has to be fulfilled in order for the storylet to be drawn
                self.results = results                  # what completing the storylet does to the game's variables/qualities; does not take into account choices made in the storylet, if any
                self.urgency = urgency                  # how the list is sorted, even after being shuffled
                self.completed = completed              # whether or not the storylet has been completed and thus can be ignored in the future; removed from the "draw pile" so to say

            def __eq__(self, other):
                if(other == None):
                    return False
                return (self.urgency ==
                        other.urgency)

            def __lt__(self, other):
                return (self.urgency <
                        other.urgency)

            def __str__(self):
                return f"Label: {self.label}, Prereq: {self.prerequisites}, Results: {self.results}, Urgency: {self.urgency}, Completed: {self.completed}"
        
        def CheckPrequisites(storylet):
            if(storylet.completed):
                return False
            elif(storylet.prerequisites == ""):
                return True
            else:
                prerequisitesMet = True
                for x in storylet.prerequisites:
                    prerequisitesMet = prerequisitesMet and eval(x)
                return prerequisitesMet

        def DeclareStorylet(label, prerequisites, results, urgency, completed):
            storylet = Storylet(label, prerequisites, results, urgency, completed)

            if(not next((True for x in storylets if x.label==label), False)):
                storylets.append(storylet)
                renpy.jump("traversal")

        def FinishStorylet(label):
            for idx, item in enumerate(storylets):
                if item.label == label:
                    item.completed = True
                    storylets[idx] = item
                    for x in item.results:
                        exec(x)
                    break
            renpy.jump("storylets")

    $ storylets = []

    $ label_traversal_list = ["urgentTestStorylet1", "testStorylet1", "testStorylet2", "testStorylet3"]

    $ randomize_storylets = True

    $ time = 0

    $ chapter = 1

    jump traversal

label traversal:
    # initialize all the storylets

    python:
        if(len(label_traversal_list) > 0):
            next_label = label_traversal_list.pop(0)
            renpy.jump(next_label)

    jump storylets

label storylets:

    # TODO: add in a whole board game theme to this part

    n "Finding the correct storylet..."

    python:
        default_value = None
        shuffled_storylets = copy.deepcopy(storylets)
        if(randomize_storylets):
            random.shuffle(shuffled_storylets)
        shuffled_storylets.sort(reverse=True) # I'm fairly sure that the shuffle will remain for storylets with the same urgency
        storylet = next((x for x in iter(shuffled_storylets) if CheckPrequisites(x)), default_value)

    if(storylet == None):
        n "No storylet found. Returning to main menu."
    else:
        $ renpy.jump(storylet.label)

    return

label urgentTestStorylet1:
    $ DeclareStorylet("urgentTestStorylet1", ["chapter == 1"], [""], 100, False)

    n "urgentTestStorylet1"

    $ FinishStorylet("urgentTestStorylet1")

label testStorylet1:

    $ DeclareStorylet("testStorylet1", ["time >= 0", "chapter == 1"], ["global time; time += 1"], 0, False)

    n "testStorylet1"

    $ FinishStorylet("testStorylet1")

label testStorylet2:

    $ DeclareStorylet("testStorylet2", ["time >= 0", "chapter == 1"], ["global time; time += 1"], 0, False)

    n "testStorylet2"

    $ FinishStorylet("testStorylet2")

label testStorylet3:

    $ DeclareStorylet("testStorylet3", ["time >= 0", "chapter == 1"], ["global time; time += 1"], 0, False)

    n "testStorylet3"

    $ FinishStorylet("testStorylet3")































# ------------------------------------------------------------------------------------------------------------------- #
