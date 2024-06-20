label st_kogasa_first_time:

    $ label_tracker = "st_kogasa_first_time"

    $ DeclareStorylet("st_kogasa_first_time", ["time >= 0", "chapter == 1"], ["global time; time += 1"], 95, "Event with Kogasa", False)
        
    "One wrong turn on the streets on your day off and you find yourself lost."

    "The everpresence of the Hero HQ over the city would make for a good landmark, especially given how close you live to it..."
    
    "But you feel like you're heading farther from it rather than closer."

    shin "{i}Ah crap.{/i}"

    $ left_turns = 0

    $ right_turns = 0

    $ got_directions = False

    $ following_going_right = False

    label lost_st_kogasa_first_time:

        $ label_tracker = "lost_st_kogasa_first_time"

        menu:
            "Which way do you go?"

            "Left" if not following_going_right:
                if left_turns == 0:

                    "You pass by a series of shanties, haphazardly constructed."

                    "They're built so close to each other you wonder if they support each others load: the other shanties-- the only reason they haven't all collapsed."

                    "Like dominos."

                    "You leave, hoping no one knocks them over."

                elif left_turns == 1:

                    # TODO: make this easier to understand without knowing what an infoshop is

                    "You see a storefront with pages on pages but it isn't a bookstore."

                    "Hanging by its doorstep is a black flag with two arrows wrapping around each other like a yin-yang in its center. One is going up, one is going down."

                    "You don't really know what the flag supposed to mean other than marking territory."

                    "That someone would put this on their store is utterly confounding to you."

                    "You walk on by with a bad taste in your mouth."

                elif got_directions:
                    "You keep going left, and then left again, and then again, and again."

                    "Eventually, you come to a dead end."

                    "You follow Kogasa's instructions to turn around and start heading right."

                    $ following_going_right = True

                $ left_turns += 1

            "Right" if not got_directions or following_going_right:
                if right_turns == 0:

                    "You pass by a tall, concrete apartment. Cracks form not only at its base but all throughout, giving the feeling that it hasn't been well maintained in a long time."

                    "Your family once lived somewhere like this, subsidized, paid in part by the government. DIfferent cities, same idea."

                    "Now you're a world away from who you were then."

                    "Familiar as it is, it's not the familiar you're looking for so you move on."

                elif right_turns == 1:

                    "You pass by a series of posters, slashed at until you're unable to tell what the ink was advocating. You knew only its demise."

                    "In its place, the beginnings of a mural are being painted in luscious strokes of aerosol. You think you can make out some words but it's clearly at a reading level above your age."

                    "Like \"DVCK\" sprawled out in some kind of cursive. You think it might resemble another word, mispelled on purpose."

                    "Of course, you mean duck."

                elif following_going_right:

                    "Eventually, you make your way back to Hero HQ."

                    shin "{i}Home, just the sweetest, of homes.{/i}"

                    $ FinishStorylet("st_kogasa_first_time")

                $ right_turns += 1

        if left_turns + right_turns < 2 or got_directions:
            jump lost_st_kogasa_first_time

    "Eventually, your eye is caught by a splash of color. A doorway with…"

    shin "{i}Shower curtains?{/i}"

    "You stop and stare for a second at the colorful little storefront, an anachronism, something fit for the backside of a community center from last decade."

    "Your better sense tells you to move on before you get scammed."

    "But you decide you've been lost long enough to ask for directions."

    shin "Hello?"

    "The sound of boxes on boxes being dug through comes from behind the counter."

    kogasa_secret "Oh, a customer? I'll be right there!"

    "A man with bright blue hair and striking blue and red eyes stands up a bit too fast, accidentally taking a mouthful of wind chimes."

    kogasa_secret "WhIgjs-{nw}"

    "He spits the chimes out."

    kogasa "Welcome to the Rainshade, I'm Kogasa! What can I do you for? I mean, do for you?"

    shin "Uh, hi? I just needed directions, I'm headed to the Hero HQ. Well, thereabouts."

    "Kogasa deflates."

    kogasa "Oh, just exit then go left until you can't anymore and then turn around and start going right."

    shin "Wouldn't that just="

    kogasa "I know it sounds like you'll end up back here but trust me. It just works out."

    shin "Okay... thanks?"

    "You move to leave but…"

    shin "{i}I am off-duty, wouldn't it be fine to stick around a little?{/i}"

    shin "{i}And plus, it'd be nice to do a good thing even outside of work hours.{/i}"

    shin "Also, you sell stuff here?"

    "Kogasa seems to perk up."

    kogasa "Yeah, we do! You wanna see?"

    # TODO: shop menu

    kogasa "Thanks for stopping by!"

    shin "And thank you, Kogasa. I'm Shin by the way."

    kogasa "I see. It's nice to meet you, Shin!"

    shin "I'll be seeing you around. Goodbye."

    kogasa "Buh-bye!"

    $ got_directions = True

    jump lost_st_kogasa_first_time

    $ FinishStorylet("st_kogasa_first_time")

label st_shin_meets_sekibanki:

    $ label_tracker = "st_shin_meets_sekibanki"

    $ DeclareStorylet("st_shin_meets_sekibanki", ["time >= 0", "chapter == 1"], ["global time; time += 1"], 99, "Event with Sekibanki", False)

    # shin has to file a report on her battle but to take her mind off things, sekibanki sends her on a supplies trip to the mall to buy food

    # along the way he finds a certain someone whose name rhymes with shmeija but neither know the other's identity, they become acquainted with each other; not friends nor foes yet
    # handling the second half in another storylet

    "You're in the lounge of Hero HQ, chicken pecking at your keyboard."

    shin "And as I finished… my… signature… line…"

    shin "..."

    shin "This report's going nowhere."

    "You got up and left the building. On your way out, somebody taps you on the shoulder."

    sekibanki_secret "Hey."

    "You turn around, only to get a cold drink to the face as you do."

    sekibanki "Want a drink?"

    "You take the can of carbonated sweet sickness from his hands before placing it and your laptop off to the side."

    shin "Good guess, but water's my preference."

    # they talk about the out of town on cross-city training exercises and Sekibanki's mild dislike of those

    shin "So how was it? The training exercises."

    sekibanki "Usual. The other city's team leader kept arguing with Reimu and we didn't get anything done."

    shin "Ah."

    "You went back to typing to try and keep your thought off the fact they didn't bother bring you."

    sekibanki "Not trying to exaggerate for your sake by the way. It was truly awful."

    # chat about the report, the news based on what happened in the fight, shin can touch a bandage reminding him of the fight

    sekibanki "What about you? You finish the report?"

    shin "Yeah, well, part of it at least."

    sekibanki "Run me through it then. Maybe I can help jog your memory."

    shin "Well at first. it went about as normal as usual."

    shin "A normal kids event, you know, cause-"

    "You glanced at his reaction, squirming a sliver, knowing your next words."

    shin "I'm not allowed {nw}{done}to actually patrol."

    sekibanki "I'm not allowed {fast}to actually patrol."

    sekibanki "I know, we all know."

    # TODO: lots of ifs here for determining what details there are

    if battle_result == "double knockout":

        # TODO: does this flow well?

        sekibanki "I mean, you knocked out Backswitch after all. But management won't allow it."

        shin "He also knocked me out."

        if seija_got_away:

            shin "And, he got away."
            
            sekibanki "You did good! From what I can tell, your only real mistake was that you should have called for backup."

            shin "You were all a city away. I didn't think anyone would get there in time."

            sekibanki "Even so, a first responder could've packed him up while he was still out."

            "You sigh."

            sekibanki "I don't want to be the one to lecture you."

            "He pauses."

            sekibanki "So I won't."

            shin "If I had more experience, maybe I would've known what to do."

            sekibanki "Well, you got your taste of experience."

            "You touch your cheek, a bandage over a scrape you got during the fight."

            shin "Tastes like asphalt."

            sekibanki "Savor it. We take our losses and we learn. Leave the bragging for PR."
        else:
            sekibanki "You did good! You even called for backup."

            sekibanki "He's where he belongs now."

            shin "In processing?"

            sekibanki "Well, he'll be where he belongs after processing is through with him."

            "You touch your cheek, a bandage over a scrape you got during the fight."

            shin "I always said I wanted to know what it was like to really BE a hero."

            sekibanki "You got your taste."

            "You can feel the soreness throughout your body, throbbing like a bodywide headache."

            shin "Tastes like pain."

            sekibanki "Savor it. Leave the bragging for PR to handle."      

    elif battle_result == "party_one_win":
        ""

    elif battle_result == "party_two_win":
        ""

    elif battle_result == "stalemate":
        ""

    sekibanki "Let's put the aside though. Where're you headed?"

    $ FinishStorylet("st_shin_meets_sekibanki")

label st_supply_run:

    $ label_tracker = "st_supply_run"

    $ DeclareStorylet("st_supply_run", ["time >= 0", "chapter == 1"], ["global time; time += 1"], 95, "Event with Sekibanki", False)

    "After training's over at Hero HQ, you head out when Sekibanki catches up to you."

    sekibanki "Good work today, got another order of supplies for tomorrow. Energy drinks and the like."

    shin "Another supply run? Is there no one else available?"

    sekibanki "You and I both know the others are just giving you things to do around here."
    
    sekibanki "They're trying to make you feel a part of the team, yknow?"

    shin "But what about you?"

    "It would be an understatement to say it was bit of a shock for you when you got your powers a month ago."

    "It would be another understatement to say it was surprising to find out that the heroes of the city lived in..."
    
    "...something less like the sci-fi movie military headquarters and more like a recreation room that got stretched out to fill an entire floor."

    "And it would be an even bigger understatement to say that Aegaeon wasn't the team player everyone made him out to be: chatty in public, shy behind doors."

    "He was less the glue holding everyone together and more so the introvert who could put in the effort to reach out from time to time."
    
    "Even so, the lion's share of your interactions with heroes have been with Sekibanki."

    sekibanki "That's just who I am. I don't hate people, I just like being alone sometimes."

    shin "But that's not really the case for me."

    sekibanki "No it's not."

    "Sekibanki turns towards you."

    sekibanki "I can't force the others to warm up to you but honestly?"

    sekibanki "I think I just plain old like you."

    shin "{i}I- uh? Did I hear that right?{/i}"

    sekibanki "You're a good person. That's more than most of us can say."

    shin "{i}Oh. He meant that.{/i}"

    shin "Wait, \"most of us\"?"

    "There was something a little solemn about his expression when he answered me."

    sekibanki "Yeah."

    "You could see him bite his lip, maybe thinking what to say."

    sekibanki "Make sure you always walk the high road, Shin."

    "You weren't sure how to respond to that. You just kept walking."

    shin "I... I will."

    sekibanki "Good."

    "You shook off any further thoughts."

    shin "I'll get going so I can get a head start on these supplies tomorrow."

    sekibanki "ALright, then see you later!"

    shin "See you!"

    shin "..."

    shin "How odd..."

    $ shin_suspicion += 1

    $ at_the_mall = True

    $ FinishStorylet("st_supply_run")

label st_shin_and_seija_first_encounter:

    $ label_tracker = "st_shin_and_seija_first_encounter"

    $ DeclareStorylet("st_shin_and_seija_first_encounter", ["time >= 0", "chapter == 1", "at_the_mall == True"], ["global time; time += 1"], 95, "Event with Seija", False)

    # characters use slightly wrong versions of common aphorisms, will call into attention the AU feel of the universe since superheroes are a relatively recent development (since the 70s)

    # i think its funny too

    "As you walked with your head buried in the list, you ran into a previous acquaintance: head first actually, you bounced off of them. Nearly fell too."

    if seija_hurt:
        seija_secret "Shit."

        "They groaned in pain before glaring at you. But the spark of recognition flashed across their face and it softened."
    else:
        seija_secret "Idiot."

    "They glared at you before the spark of recognition flashed across their face and it softened."

    seija_secret "It's Shin, right? Sorry ‘bout that."

    shin "No need. I wasn’t looking where I was going."

    shin "You know my name, miss…?" # the like one misgendering in the entire story, I’d rather not bring the topic of misgendering up again but it should help reinforce Seija’s gender to the player

    seija_secret "It’d be mister, actually. I used to get my coffee from you?"

    shin "Oh, uh, you’re…"

    "You paused, hoping that they would fill in the details but they just stood there with a smile."
    
    "If you didn’t know better, you’d think they were eating up the awkward atmosphere."

    seija_secret "Starts with an S, dude."

    menu:
        "His name was…"

        "Coleslaw":
            seija "Hah, close but no quarter. It’s Seija."

        "Say ya?":
            seija "Hah, close but no quarter. It’s Seija."

        "Bonesaw?": # worm reference (could also be a sam raimi’s spider man reference)
            seija "Hah, close but no quarter. It’s Seija."

        "ajieS":
            seija "Hah, close but no quarter. It’s Seija."

    shin "{i}I recognize the name. He usually ordered a long black, late at night before my shift ended.{/i}"

    shin "{i}Did we ever talk? Even if we did, I’d think I’d remember him being this friendly…{/i}"

    seija "I don’t mind. Anyways, how’ve you been? You move or something?"

    shin "Oh, well…"

    "You glanced at the list you were given."

    shin "…you could say something like that. New job, new place."

    seija "Makes sense, makes sense."

    # seija gets shin’s number in trade for a secret that seija knows something without revealing that seija is a villain; that or just a trade for a phone number but with a subtle implication that shin picks up on; shin tries to excuse himself

    shin "Sorry about the name thing, by the way."

    seija "Eh, it's no skin. But if you're giving out apologies I'd rather trade something with you."

    "Seija pulled out his phone."

    seija "Your number for mine?"

    # shin either blushes slightly then shakes off the thought

    shin "{i}Ah.{/i}"

    shin "{i}Hold on, better not to make anymore assumptions and get caught with my foot in my mouth again.{/i}"

    shin "Sure!{nw}{done} I mean, sure."

    # change of expression as he reins in his expression

    shin "Sure!{fast} I mean, sure."

    "The two of you exchange numbers."

    shin "Gotta go. Hope to hear from you, Seija."

    seija "Same here!"

    "You walk off, back to your supply run."

    # a tiny sneak peak of seija bullying

    seija "Same here{cps=1.5}… {/cps}wish boy."

    $ at_the_mall = False

    $ FinishStorylet("st_shin_and_seija_first_encounter")

label st_chapter_start_1:

    $ label_tracker = "st_chapter_start_1"

    $ DeclareStorylet("st_chapter_start_1",["chapter == 1"], [""], 100, "Start", False)

    $ upgrade_points += 3

    # POV: Shin

    # CG: The focus is shin hiding behind a wall with his signature weapon (gotta wait on shin hero design or at least sillouhette); a villain in a mascot suit (does not look like Seija) approaches, in search for him

    #scene bg black

    "There's shattered glass in the stage curtain, shimmering in blue. Your enemy calls from the skies."

    seija_secret "Come out, come out wish boy!"

    "Now... now is the time to strike!"

    # CG: Shin strikes!

    shin "May even your wish come true, someday."

    "{sc}WOOOOOOOOOOOOO!{/sc}"

    "The sound of tiny applause and unenthused parents rings out from your audience. It's a sea of small hands pointing to you."
    "You hear the cue to bow so you do."

    "We love you Wishmaker!"

    "{i}The smiles, the games, the acting... it's all...{/i}"

    seija_secret "Kids shit."

    "The fallen mascot suit, in upstage left, took to its feet{nw}{done} and removed its oversized head to reveal Backswitch."

    # Seija reveals herself by the sprite moving up, no need for a CG

    "The fallen mascot suit, in upstage left, took to its feet{fast} and removed its oversized head to reveal Backswitch."

    "Minor villain, major nuisance."
    
    "He's been around the block, making waves with her gravity flipping powers. As a relative newbie, this is your first time face-to-face with a villain."

    "Despite the excited gasps from the audience, the staff begin ushering everyone out."

    shin "{i}Okay, this is fine. Drop the banter for now, focus on keeping it together.{/i}"

    seija_costumed "I was wonderin' about the noise following some new hero. Looks like noise was all it was."

    play music "Battle_Enemy_Grounds.ogg"

    seija_costumed "Don't you agree, {bt=6}{color=000000}wish boy?{/color}{/bt}"

    # BATTLE STUFF START #

    $ violence = 0

    $ pacifism = 0

    $ team_player = 0

    $ isolation = 0

    $ precision = 0

    $ tenderness = 0

    $ dmg_to_target = 0

    $ dmg_to_self = 0

    $ chosen_target = (0, 0) # party index, member index

    $ turn = 1

    $ whose_turn = "party_one"

    $ battle_result = ""

    $ end_of_battle_conditions = [("double knockout", "all(x['hp'] == 0 for x in party_two) and all(x['hp'] == 0 for x in party_one)"),
                                ("party_one win", "all(x['hp'] == 0 for x in party_two)"),
                                ("party_two win", "all(x['hp'] == 0 for x in party_one)"),
                                ("stalemate", "all(len(x['options']) == 0 for x in party_one)"),
                                ("stalemate", "turn > 6")]

    # TODO: reformat all this into a dict

    # Battle Word Estimate: 808 words

    $ party_one = [{"name":"Wishmaker",
                    "max_hp":shin_battler.max_hp, 
                    "hp":shin_battler.max_hp,
                    "power":shin_battler.power,
                    "agility":shin_battler.agility,
                    "tech":shin_battler.tech,
                    "effects":[],
                    "options":[[["selecting_target = True", "violence += 1; dmg_to_target = 3; noglobal QueueSFX('PUNCH_PERCUSSIVE_HEAVY_09.opus')", "noglobal QueueSFX('WHOOSH_ARM_SWING_01.opus'); violence += 0.5", 10, ("Power", shin_battler.power),               # run prior to outcome, effect on success, effect on failure, DC (1d20), relevant stat (if any)
                                    "You bring your weapon in for a swing at [party_two[chosen_target[1]]['name']]'s midriff.",                          # initial dialogue
                                    "[party_two[chosen_target[1]]['name']] stifles a pained grunt.",                                                     # post-roll success dialogue
                                    "[party_two[chosen_target[1]]['name']] points at your weapon and sends it flying out of your hands.\nYou manage to get ahold of it before it goes offstage.\n[party_two[chosen_target[1]]['name']]'s laugh booms from his echoing demon mask.\n[party_two[chosen_target[1]]['sayer']]:Idiot.",
                                    "violence",
                                    FormatOption("STRIKE", "violence")],   # post-roll failure dialogue, action text
                                ["selecting_target = True", "violence += 1; dmg_to_target = 4; noglobal QueueSFX('PUNCH_DESIGNED_HEAVY_23.opus')", "noglobal QueueSFX('WHOOSH_ARM_SWING_01.opus'); violence += 0.5; dmg_to_self = 1 if precision == 0 else 0", 13, ("Power", shin_battler.power),
                                    "You throw your weight behind your weapon, bringing it down in a wide arc.",
                                    "[party_two[chosen_target[1]]['name']] is hit squarely in the chest.\nHe backs away a step while gasping for air.",
                                    "[party_two[chosen_target[1]]['name']] sidesteps your swing and sends a prop sword flying at your face.\n{if precision == 0}You parry it as well as you can but still get a bit roughed up.\n[party_two[chosen_target[1]]['sayer']]:Iiiiiiidiot.{else}You parry the prop sword, reading [party_two[chosen_target[1]]['name']]'s rhythm.",
                                    "violence",
                                    FormatOption("HIT HARDER", "violence")],
                                ["selecting_target = True", "violence += 1; dmg_to_target = 5; noglobal QueueSFX('PUNCH_INTENSE_HEAVY_03.opus')", "noglobal QueueSFX('WHOOSH_ARM_SWING_01.opus'); noglobal QueueSFX('PUNCH_DESIGNED_HEAVY_23.opus', 2); noglobal QueueSFX('PUNCH_INTENSE_HEAVY_03.opus', 4); violence += 0.5; dmg_to_self = 3 if precision == 1 else 4; dmg_to_target = 5 if precision == 1 else 0", 16, ("Power", shin_battler.power),
                                    "You swing with a little too much oomph, nearly lifting you off your feet.",
                                    "[party_two[chosen_target[1]]['name']] blocks the telegraphed attack but the sheer force sends him backpedaling, wincing.",
                                    "[party_two[chosen_target[1]]['name']] steps into range before you complete the swing, throwing a counterpunch.\nYou take it on your jaw and the world becomes blurry.\n{if precision == 0}You nearly lose your footing but try for a counterattack.\nBut your timing's been read and [party_two[chosen_target[1]]['name']] lays into you.\n[party_two[chosen_target[1]]['sayer']]:Dumbfuck.{else}You grit your way through the pain.\nWhile dazed, you tackle [party_two[chosen_target[1]]['name']] and land a shot to his knees that make him buckle.\n[party_two[chosen_target[1]]['sayer']]:{sc}{color=000}FUCK!{/color}{/sc}",
                                    "violence",
                                    FormatOption("THROW WILD SWING", "violence")]],
                                [["", "pacifism += 1", "dmg_to_self = 2", 12, ("Agility", shin_battler.agility),
                                    "You duck [party_two[chosen_target[1]]['name']]'s blows, weaving in and out of his range.\nSeeing this, [party_two[chosen_target[1]]['name']] makes a gesture and from across the street, a manhole cover goes flying in your direction.",
                                    "You manage to avoid it, leaping from your low position, as it flies underneath you and crashes into backstage.",
                                    "You move even lower, a poor move, as the manhole cover sweeps your legs and you land with your back against the ground.\nThe scramble afterwards to get back into a fighting stance is less graceful than you'd hoped.",
                                    "pacifism",
                                    FormatOption("DUCK", "pacifism")],
                                ["", "pacifism += 1; dmg_to_self = -1", "dmg_to_self = 3", 15, ("Agility", shin_battler.agility),
                                    "You roll for cover, stage props and lighting equipment becoming temporary shelter for you to catch your breath.\nIt's a balancing act to not stay in one place for too long however as your protections could become projectiles with just a gesture from [party_two[chosen_target[1]]['name']].",
                                    "A balancing act{cps=1.5}... {/cps}that you manage to keep as you catch your breath between daring manuevers, much to [party_two[chosen_target[1]]['name']]'s ire.",
                                    "A balancing act{cps=1.5}... {/cps}gone wrong as a wardrobe full of costumes goes flying right as you roll, straight into your face.",
                                    "pacifism",
                                    FormatOption("ROLL FOR COVER", "pacifism")],
                                ["", "team_player += 1", "", 0, ("Tech", shin_battler.tech),
                                    "In a brief respite you get as you dodge [party_two[chosen_target[1]]['name']]'s onslaught, leaving him panting for a moment, you tap your communicator and send out backup signal.\nLet's hope your fellow heroes get here in time.",
                                    "",
                                    "",
                                    "team_player",
                                    FormatOption("CALL FOR BACKUP", "team_player")]],
                                [["", "precision += 1", "", 0, ("Tech", shin_battler.tech),
                                    "You hold a defensive stance, keeping distance from [party_two[chosen_target[1]]['name']].\nAfter dodging one or two hits, you start to get a feel for his timing, his rhythm.",
                                    "",
                                    "",
                                    "precision",
                                    FormatOption("WAIT AND SEE", "precision")]]],
                    "dialogue":[("battle_started == False and battle_dialogue == 0", "Really? Don't you villains have better things to do than show up to kids' shows?")],
                    "source": shin_battler,
                    "sayer": "shin_costumed"}]

    # every two actions of Wishmaker we get one action from Backswitch

    $ party_two =[{"name":"Backswitch",
                    "max_hp":seija_battler.max_hp, 
                    "hp":seija_battler.max_hp,
                    "power":seija_battler.power,
                    "agility":seija_battler.agility,
                    "tech":seija_battler.tech,
                    "effects":[],
                    "options":[["", "", "dmg_to_self = 3", 10, ("", 0),                                     # opponent interrupts vs player actions, ran by player context but overwrite your previous action (though that means the action is still there for you to use later instead of being used up)
                                    "You attempt to-",
                                    "But before you can, you notice the floorboard beneath your feet about to fly off. You leap backwards out of harms way. [party_two[chosen_target[1]]['name']] seems genuinely surprised.\n[party_two[chosen_target[1]]['sayer']]:Not as dumb as you look?",
                                    "But you fail to notice the floorboard beneath your feet fly off, likely under [party_two[chosen_target[1]]['name']]'s power.\n You fall without any ground beneath you.\nYou land under the stage with a thud before climbing out unceremoniously; a jeering [party_two[chosen_target[1]]['name']] there to greet you as you rise.\n[party_two[chosen_target[1]]['sayer']]:Had a nice trip?",
                                    ""]],
                    "boss_turn":[], # it's called a boss turn because only bosses get their own non-interrupt actions
                    "dialogue":[("battle_started == False and battle_dialogue == 1", "Maybe if you heroes did something other than kids shows, I'd have something else to crash!")],
                    "source": seija_battler,
                    "sayer": "seija_costumed"}]

    label battle_st_chapter_start_1:

        $ label_tracker = "battle_st_chapter_start_1"

        $ end_battle_label = "exit_battle_st_chapter_start_1"

        $ queued_statements = []

        call screen battle_screen

        window hide

        $ selecting_target = False

        $ continue_label = "battle_st_chapter_start_1_continue"

        label battle_st_chapter_start_1_continue:

            python:
                while len(queued_statements) > 0:
                    statement = queued_statements[0]
                    if statement[0] == "say":
                        renpy.say(statement[1][0], statement[1][1])
                        queued_statements.pop(0)
                    elif statement[0] == "exec":
                        renpy.log("")
                        renpy.log("exec: " + statement[0])
                        queued_statements.pop(0)
                        exec(statement[1])
                    else:
                        renpy.log("")
                        renpy.log("unknown: " + str(statement))
                        queued_statements.pop(0)

                queued_statements = [] 

                turn += 1

        jump battle_st_chapter_start_1

    label exit_battle_st_chapter_start_1:

        $ label_tracker = "exit_battle_st_chapter_start_1"

        $ renpy.hide_screen("battle_screen")

        stop music

        scene bg black with fade

        $ seija_hurt = True if party_two[0]["hp"] / party_two[0]["max_hp"] <= 0.5 else False

        if battle_result == "double knockout":
            shin_costumed "And... shut... your..."

            "You both collapse onto the ground."

            "The last thing you see is Backswitch like a puppet with cut strings, no tension in his fallen limbs."

            $ seija_got_away = True and team_player > 0

            $ shin_knocked_out = True

        elif battle_result == "party_one win":

            shin_costumed "And shut it!"

            "Seija lies at your feet in a collapsed heap of exhaust and hacking coughs."

            seija_costumed "H-heh. You're better than expected, for a kids show hero."

            seija_costumed "Don't you think you could achieve more if they-"

            "You give her a light kick to the ribs to shut her up. Very light."

            shin_costumed "Nice of you to choose an ambush right outside of Hero HQ. The commute to jail's going to be a lot faster."

            $ seija_got_away = False

            $ shin_knocked_out = False

        elif battle_result == "party_two win":

            "The last thing you see before you collapse onto the ground is his mask. You can tell he's got the ugliest smirk behind it."

            $ seija_got_away = True

            $ shin_knocked_out = True

        elif battle_result == "stalemate":

            seija_costumed "Hmm. Not as talkative as your stage persona, are ya?"

            shin_costumed "Shut it with the backtalk, Backswitch."

            seija_costumed "Backtalk, smacktalk."

            seija_costumed "You know who you really need to watch out for? Truck drivers."

            shin_costumed "Wait, what does that m-{nw}"

            "But Backswitch was already running away."

            "You began to run after him but not before incoming traffic became INCOMING traffic with Backswitch sent a truck, its tires squealing, toppling sidewards towards you."

            shin_costumed "What does that-"

            "But Backswitch was already running away."

            "You began to run after him but not before incoming traffic became INCOMING traffic with Backswitch sent a truck, its tires squealing, toppling sidewards towards you."
            
            python:
                dice_result = 20
                dice_modifier_formatted = FormatModifier(0)
                dice_animation_counter = 0
                continue_label = "exit_battle_st_chapter_start_1_stalemate_continue"
                renpy.jump('dice_animation')

            label exit_battle_st_chapter_start_1_stalemate_continue:
                # TODO: make asking for backup matter here
                "Everyone's thought about it once."

                "Being the hero."

                shin "{i}But despite getting superpowers...{/i}"

                "You dive out of the way of the truck as its thrown into a nearby freeway, crashing into traffic. You see smoke. You hear screaming."

                shin "{i}...and I HATE admitting this...{/i}"

                "You run over to one of the nearby pedestrians, picking the one who looks the most physically capable; the most likely choice."

                shin "{i}...I never get to be the hero.{/i}"

                "You clasp his hands and ask."

                shin "Do you {gradient2=6-E40303-FF8C00-2-FF8C00-FFED00-2-FFED00-008026-2-008026-004CFF-2-004CFF-732982-2-732982-E40303-2}WISH{/gradient2} to be a hero?"

            $ seija_got_away = True

            $ shin_knocked_out = False

        $ FinishStorylet("st_chapter_start_1")

