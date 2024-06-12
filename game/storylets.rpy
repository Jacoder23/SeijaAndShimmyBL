init python:
    import functools
    class Storylet:
        def __init__(self, label, prerequisites, results, urgency, completed):
            self.label = label                      # which label to jump to; the content of the storylet
            self.prerequisites = prerequisites      # what has to be fulfilled in order for the storylet to be drawn
            self.results = results                  # what completing the storylet does to the game's variables/qualities; does not take into account choices made in the storylet, if any
            self.urgency = urgency                  # how the list is sorted, even after being shuffled
            self.completed = completed              # whether or not the storylet has been completed and thus can be ignored in the future; removed from the "draw pile" so to say

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

        if(len(label_traversal_list) > 0):
            storylets.append(storylet)
            renpy.log("Initialized " + label)
            InitializeNextLabel()

    def FinishStorylet(label):
        for idx, item in enumerate(storylets):
            if item.label == label:
                item.completed = True
                storylets[idx] = item
                for x in item.results:
                    exec(x)
                break
        renpy.log("Jumping back to storylets...")
        renpy.jump("storylets")

    def CheckStoryletCompletion(label):
        for idx, item in enumerate(storylets):
            if item.label == label:
                return item.completed
        return False

    def StoryletUrgency(storylet):
        renpy.log(storylet.urgency)
        return int(storylet.urgency)

    def NextStorylet():
        default_value = None
        shuffled_storylets = copy.deepcopy(storylets)

        #if(randomize_storylets):
            # random.shuffle(shuffled_storylets)

        shuffled_storylets = sorted(shuffled_storylets, reverse=True, key=StoryletUrgency)
        storylet = next((x for x in iter(shuffled_storylets) if CheckPrequisites(x)), default_value)

        if(storylet == None):
            renpy.notify("No storylet found. Returning to main menu.")
            renpy.pause()
        else:
            renpy.jump(storylet.label)

    def InitializeStorylets(randomize = True):
        global storylets
        storylets = []

        global randomize_storylets
        randomize_storylets = randomize

        global label_traversal_list
        label_traversal_list = sorted([x for x in renpy.get_all_labels() if x[:3] == "st_"])
        label_traversal_list.append("Non-existent filler storylet")

        InitializeNextLabel()

    def InitializeNextLabel():
        global label_traversal_list
        if(len(label_traversal_list) > 0):
            next_label = label_traversal_list.pop(0)
            if(next_label == "Non-existent filler storylet"):
                label_traversal_list = []
                InitializeNextLabel()
            else:
                renpy.jump(next_label)
        else:
            renpy.log("Done with initialization at label: " + label_tracker)
            renpy.jump("storylets")