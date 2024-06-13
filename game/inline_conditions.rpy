################################################################################
##
## Inline Conditions for Ren'Py by Feniks (feniksdev.com)
##
################################################################################
## Adding this file to your game will allow you to write dialogue that includes
## conditional checks to show enclosed text only if the provided condition(s)
## are met. This can help avoid multiple repeated lines with small tweaks
## or excessive variable declarations.
##
## If you use this file in your project, credit me as Feniks @ feniksdev.com
##
## There are three text tags included, which have slightly different behaviour
## for how they are treated while the player is skipping if they have the
## preference setting to only skip seen text on.
## {skip_if} - This tag (and any attached {elif} or {else} tags) means that all
##             variants of this line are treated as the same line for skipping.
##             If the player has seen this line once in any playthrough,
##             regardless of which of the conditions were met when it was seen,
##             it will be skipped if the player is skipping only seen text.
##             It also has a "pretty" form - {same: if}. This has the exact
##             same behaviour, but is intended to be more readable. It
##             communicates that all variants of this line are the same when
##             it comes to skipping unread text only.
## {stop_if} - This tag (and any attached {elif} or {else} tags) means that all
##             variants of this line are treated as separate lines for skipping.
##             If the first time the player encounters this line, the {stop_if}
##             condition is True, if on a second playthrough they encounter
##             this line again but the condition is False, the game will stop
##             skipping at this line. If the player has seen a particular
##             variant of the line before, it is treated as "seen" and does not
##             stop skipping.
##             It also has a "pretty" form - {diff: if}. This has the exact
##             same behaviour, but is intended to be more readable. It
##             communicates that all variants of this line are different when
##             it comes to skipping unread text only.
## {if}      - This tag can have the behaviour of either {skip_if} or {stop_if}.
##             You will set which one in the `init python in myconfig` block
##             below. It is intended as a convenience, so you can assign {if}
##             to whichever behaviour your project will need more often. You
##             cannot change this behaviour in the middle of gameplay, so if
##             you require the opposite behaviour, use {skip_if} or {stop_if}
##             directly (or their "pretty" forms).
##
## Usage:
## {skip_if}, {stop_if}, {if}, and {elif} all require a condition to work. The
## condition can be any arbitrary expression, including function calls, so long
## as it can be evaluated in Python. It is evaluated just before the line is
## shown, but may be evaluated occasionally beforehand for prediction, so you
## should be sure to declare any values you're using with define or default
## as appropriate and ensure your function calls do not cause side effects.
##
## The structure of a tag with a condition looks like:
## "{if condition}This text will only show if the condition is True.{/if}"
## The condition comes after the `if` and is evaluated as a Python expression.
##
## The condition may take many forms:
## {if num_apples > 5}
## {diff: if pronouns == 'she/her'}
## {same: if xia_points > 2 and zoran_points < 10}
## {if persistent.good_end}...{elif persistent.bad_end}...
##
## While {if}, {same: if}, and {diff: if} can all be used to start a conditional
## statement, (as with the {skip_if} and {stop_if} versions), {elif} and {else}
## can only be used after an initial if tag of some kind.
## {elif} and {else} work as they do in Python, so if a previous clause in an
## if/elif/else chain is True, the rest of the chain is False and skipped.
##
## The {else} tag does not take any condition. It is shown only if none of
## the previous conditions were True.
##
## These text tags ONLY work inside dialogue and choice menus. If you would
## like similar behaviour for screens or inside functions, you should use
## the more flexible fstring notation from Python:
## https://realpython.com/python-f-strings/
##
## You may also be interested in https://feniksdev.itch.io/inline-python-for-renpy,
## which brings general Python expressions to Ren'Py dialogue and choices.
##
################################################################################
## Examples:
##
## "You set {same: if apples == 1}it{else}them{/else} on the table."
##      If the player has more than one apple, the dialogue changes slightly
##      to indicate it is plural. This is nearly inconsequential, so {same: if}
##      is specified so the game does not stop skipping for any variant of this
##      line once the player has seen one version of it. (This may also be the
##      default behaviour for a regular {if} tag, if desired). The {/else} tag
##      closes the conditional statement so the two possible versions of this
##      line are:
##          "You set it on the table." (if apples == 1)
##          "You set them on the table." (if apples != 1)
##
## "Zoran slowly walked away.{if perception > 10} His gait was awkward, as though from an injury."
##      Here, there is some bonus dialogue if the player is perceptive. Whether
##      the game considers a variant of this line to be "seen" or not depends
##      on how you set up the behaviour of {if} at the top of this file.
##      The {if} tag does not need to be closed at the end of this line, as
##      reaching the end of the line automatically closes it.
##
## "You have {if apples>1}many{elif apples==1}one{else}no{/else} apple{if apples!=1}s{/if}."
##      Another example using an if/elif/else structure. The three possibilities
##      for this line are:
##          "You have many apples." (if apples > 1)
##          "You have one apple." (if apples == 1)
##          "You have no apples." (if apples < 1)
##      You can add as many elif statements as needed for your conditional.
##      The full condition is closed with an {/else} tag, as that's the final
##      text tag used in the if/elif/else chain.
##
## "You checked, and it was locked.{if has_key or has_lockpick} That wouldn't be an issue.{if has_key} The key fit smoothly into the lock.{else} Your lockpick made quick work of it."
##      You can also nest conditions. Here, the nesting is roughly equivalent to:
##          "You checked, and it was locked."
##          if has_key or has_lockpick:
##              extend " That wouldn't be an issue."
##              if has_key:
##                   extend " The key fit smoothly into the lock."
##              else:
##                  extend " Your lockpick made quick work of it."
##      Unlike the above code, however, the inline conditional version does not
##      require clicks to advance through each line.
##
## "You mean you don't{same: if is_drunk} {i}*hic*{/i}{/if} {diff: if zoran_points<5}hate me?{else}think I'm a bother?"
##      A single line can have multiple inline conditions, and they don't have
##      to have the same structure. Both conditions can be tracked differently
##      for skipping purposes, if you want. So for this line, whether the player
##      is drunk or not will not matter when the line is considered for
##      skipping, only whether they have more or less than 5 points with Zoran.
##      This behaviour can be particularly helpful for translation, where some
##      languages may need to break up sentences in different ways to
##      communicate the same point.
##      The above line is approximately equivalent to:
##          if is_drunk:
##              if zoran_points < 5:
##                  "You mean you don't {i}*hic*{/i} hate me?"
##              else:
##                  "You mean you don't {i}*hic*{/i} think I'm a bother?"
##          else:
##              if zoran_points < 5:
##                  "You mean you don't hate me?"
##              else:
##                  "You mean you don't think I'm a bother?"
##      As you can see, the inline conditions clean this up considerably.
##
## "It's a{if gift == 'apron'}n{elif gift == 'earrings'} pair of{/elif} [gift]."
##      To use string values in your conditions, you have to use whichever
##      quotations you're not using for the dialogue (so, in this case, single
##      quotes since double quotes are used for the dialogue).
##      To close an if/elif conditional which doesn't have an {else}, you'll use
##      {/elif} to close it.
##      You can interpolate variables regularly inside dialogue with [var].
##      The possible outcomes of this line are:
##          "It's an apron." (if gift == "apron")
##          "It's a pair of earrings." (if gift == "earrings")
##          "It's a [gift]." (if gift is anything else e.g. "It's a camera.")
##
## You can also use the skip_if and stop_if special tags as described earlier
## instead of the same: if and diff: if format e.g.
## "You mean you don't{same: if is_drunk} {i}*hic*{/i}{/if} {diff: if zoran_points<5}hate me?{else}think I'm a bother?"
##     is equivalent to:
## "You mean you don't{skip_if is_drunk} {i}*hic*{/i}{/if} {stop_if zoran_points<5}hate me?{else}think I'm a bother?"
##
## Which one you use doesn't matter, it's just what makes more sense to you.
################################################################################
## CONFIGURATION
################################################################################
## You can change this configuration value below!
init -10 python in myconfig:
    _constant = True # This is a constant store

    ## The default behaviour for the if/elif/else tags is to consider all
    ## line variations the same "line" for the purposes of skipping. If you
    ## want to consider all line variations a different line, set this to False.
    inline_conditions_same_for_skipping = True

################################################################################
## PYTHON
################################################################################
## The meat of the code. Aside from the initial code in the block above, you
## shouldn't need to modify any of this. Feel free to look through it if you'd
## like to get an idea of how it all works, however!
################################################################################
init python:
    ## Used by if/elif/else text tags to determine which clause will be
    ## executed. Not a config value; used internally. Do not modify.
    PREVIOUS_CONDITIONS_TRUE = False
    ## Used for error checking, so we can tell if the user tries to
    ## close a text tag that wasn't already open. Do not modify.
    LAST_OPEN_TAG = None
    ## Used to reset whether the game is on a new line, in case a line has
    ## multiple if/elif/else tags in it. Used for saving seen/unseen variants.
    ## Do not modify.
    NEW_LINE = True

    def add_to_seen_lines(cond, save_variants):
        """
        Remember whether the player has seen this version of the line or not.

        Parameters:
        -----------
        cond : bool
            Whether the condition for this particular text tag was True or
            False.
        save_variants : bool
            True if saving variants on this line (e.g. for a stop_if tag).
        """
        ## Don't add a line to seen if we're predicting or not saving variants
        ## for this line (e.g. a skip_if tag)
        if renpy.predicting() or not save_variants:
            return

        ## If we're tracking what the player has seen, add it to the persistent
        try:
            ## Grab the line ID so we can have a unique identifier for the
            ## line dictionary
            line_id = renpy.game.context().current
        except Exception as e:
            print("Error with seen lines")
            return

        ## If this is a new line, make a new entry
        if store.NEW_LINE:
            current_seen_lines[line_id] = [cond]
        ## Otherwise, this is the second or later condition in the line, so
        ## just append it.
        else:
            current_seen_lines[line_id].append(cond)

        ## Indicate this line is ongoing unless otherwise reset.
        store.NEW_LINE = False

    def conditional_dialogue_c(tag, argument, contents, save_variants):
        """
        Text tag that allows for conditional checks in the middle of
        dialogue.

        Parameters:
        -----------
        tag, argument, contents
            Automatically passed in by Ren'Py for text tags. See Ren'Py docs:
            https://www.renpy.org/doc/html/custom_text_tags.html#custom-text-tags
        save_variants : bool
            True if we should save the variants of this line for seen/unseen
            skipping purposes. stop_if saves variants, skip_if does not.
        """
        ## Grab the condition and try evaluating it
        condition = argument.strip()
        try:
            ## Try to evaluate the condition
            include_dialogue = eval(condition)
            ## Add this to previous conditions and reset them
            store.PREVIOUS_CONDITIONS_TRUE = include_dialogue
            store.LAST_OPEN_TAG = "if"
        except Exception as e:
            if config.developer: ## Alert the developer
                raise Exception("ERROR Evaluating text tag conditional:", condition, e)
            include_dialogue = True ## Default to including the dialogue

        ## If we're tracking what the player has seen, add it to the persistent
        add_to_seen_lines(include_dialogue, save_variants)

        if not include_dialogue:
            return [ ]
        else:
            return contents

    def elif_dialogue_c(tag, argument, contents, save_variants):
        """
        Text tag that allows for "elif" style conditional checks
        in the middle of dialogue.

        Parameters:
        -----------
        tag, argument, contents
            Automatically passed in by Ren'Py for text tags. See Ren'Py docs:
            https://www.renpy.org/doc/html/custom_text_tags.html#custom-text-tags
        save_variants : bool
            True if we should save the variants of this line for seen/unseen
            skipping purposes. stop_elif saves variants, skip_elif does not.
        """
        ## Grab the condition
        condition = argument.strip()

        if store.LAST_OPEN_TAG is None:
            if config.developer:
                ## There has to be an if/elif before this
                raise Exception("ERROR: {{elif} text tag without corresponding {{if}")
            else:
                return contents

        store.LAST_OPEN_TAG = "elif"

        ## Only include this if previous conditions were not True
        if store.PREVIOUS_CONDITIONS_TRUE:
            add_to_seen_lines(False, save_variants)
            return [  ]

        ## Otherwise, evaluate the condition
        try:
            include_dialogue = eval(condition)
            ## Add this to previous conditions
            store.PREVIOUS_CONDITIONS_TRUE = store.PREVIOUS_CONDITIONS_TRUE or include_dialogue
        except Exception as e:
            if config.developer: ## Alert the developer
                raise Exception("ERROR Evaluating text tag conditional:", condition, e)
            include_dialogue = True ## Default to including the dialogue

        add_to_seen_lines(include_dialogue, save_variants)

        if not include_dialogue:
            return [ ]
        else:
            return contents

    def else_dialogue_c(tag, argument, contents, save_variants):
        """
        Text tag that allows for "else" style conditional checks in the middle
        of dialogue.

        Parameters:
        -----------
        tag, argument, contents
            Automatically passed in by Ren'Py for text tags. See Ren'Py docs:
            https://www.renpy.org/doc/html/custom_text_tags.html#custom-text-tags
        save_variants : bool
            True if we should save the variants of this line for seen/unseen
            skipping purposes. stop_else saves variants, skip_else does not.
        """
        if store.LAST_OPEN_TAG is None:
            if config.developer:
                ## There has to be an if/elif before this
                raise Exception("ERROR: {{else} text tag without corresponding {{if}")
            else:
                return contents

        ## No open tags
        store.LAST_OPEN_TAG = None

        ## Only include this if previous conditions were not True
        if store.PREVIOUS_CONDITIONS_TRUE:
            add_to_seen_lines(False, save_variants)
            return [ ]
        else:
            add_to_seen_lines(True, save_variants)
            return contents

    ## Curry these functions for ease of adding the skip_if and stop_if tags
    conditional_dialogue = renpy.curry(conditional_dialogue_c)
    elif_dialogue = renpy.curry(elif_dialogue_c)
    else_dialogue = renpy.curry(else_dialogue_c)

    def tokens_to_text(tokens):
        """
        Put together a list of (Tag, Contents) tokens into a single string
        and return it.
        """
        rv = [ ]
        for num, txt in tokens:
            if num == renpy.TEXT_TEXT:
                ## Add wholesale
                rv.append(txt)
            elif num == renpy.TEXT_TAG:
                ## Add with the curly braces
                rv.append("{" + txt + "}")
            elif num == renpy.TEXT_DISPLAYABLE:
                ## Add wholesale
                rv.append(txt)
            elif num == renpy.TEXT_PARAGRAPH:
                ## Add a newline
                rv.append("\n")
        return ''.join(rv)

    from re import findall
    def parse_conditional_tags(s):
        """
        Adds in the = syntax after if/elif/stop_if/skip_if tags, and replaces
        the "pretty" versions of the skip_if and stop_if tags (same/diff).

        Technically, {if some_condition} is not proper Ren'Py syntax, but Ren'Py
        gives us a go at dialogue and menu texts with a config option, so we can
        turn it into the proper syntax.
        """
        for pattern, mch, rep in zip(
            ['{if +[^=\}]+[^\}]*}', '{skip_if +[^=\}]+[^\}]*}', '{stop_if +[^=\}]+[^\}]*}',
            '{same: if +[^=\}]+[^\}]*}', '{diff: if +[^=\}]+[^\}]*}', '{elif +[^=\}]+[^\}]*}'],
            ["{if ", "{skip_if ", "{stop_if ", "{same: if ", "{diff: if ",
            "{elif "],
            ["{if=", "{skip_if=", "{stop_if=", "{skip_if=", "{stop_if=",
            "{elif="]
        ):
            ## This uses regular expression matching to quickly find
            ## lines that match the "pretty" format and turn them into the
            ## "proper" text tag format.
            matches = findall(pattern, s)
            for match in matches:
                s = s.replace(match, match.replace(mch, rep))
        return s

    def add_conditional_tags(s):
        """
        Adds in closing {/if}, {/elif}, and {/else} tags as appropriate.
        Used so the user doesn't have to close every if/elif tag manually.
        Without this, the user would write lines like:
            "{if cond1}Text 1{/if}{elif con2} Text2 {/elif}{else} Text3{/else}"
        Obviously that's ugly, and elif/else only come after an {if}, so we
        can add them in without requiring the user to do so. Thus lines can
        be written like:
            "{if cond1}Text 1{elif con2} Text2 {else} Text3"
        and this function will turn it into the earlier format.
        """

        ## Replace the "pretty" versions of the text tags
        s = parse_conditional_tags(s)

        ## Go through only if there are {if}, {elif}, or {else} tags.
        ## Just saves us a bit of bother if there aren't even conditionals.
        if "{if" not in s and "{stop_if" not in s and "{skip_if" not in s:
            return s

        ## Otherwise, we have some conditions. Make sure we're closing them
        ## up properly.
        ## Tokenize the string to iterate over.
        contents = renpy.text.textsupport.tokenize(s)
        new_contents = [ ]
        last_open_tag = [ ]

        which_if = ""

        for tag, tag_c in contents:
            if tag == renpy.TEXT_TAG:
                ## Remember which sort of if/elif/else to use
                if tag_c.startswith("if"):
                    last_open_tag.append("if")
                    which_if = ""
                elif tag_c.startswith("skip_if"):
                    last_open_tag.append("skip_if")
                    which_if = "skip_"
                elif tag_c.startswith("stop_if"):
                    last_open_tag.append("stop_if")
                    which_if = "stop_"

                elif tag_c.startswith("elif"):
                    if last_open_tag:
                        new_contents.append( (renpy.TEXT_TAG, "/{}".format(last_open_tag[-1])) )
                        last_open_tag.pop()
                    last_open_tag.append("{}elif".format(which_if))
                elif tag_c.startswith("else"):
                    if last_open_tag:
                        new_contents.append( (renpy.TEXT_TAG, "/{}".format(last_open_tag[-1])) )
                        last_open_tag.pop()
                    last_open_tag.append("{}else".format(which_if))

                else:
                    ## The proper open tags
                    for tg in ("skip_elif", "stop_elif", "skip_else", "stop_else"):
                        if tag_c.startswith(tg):
                            if last_open_tag:
                                new_contents.append( (renpy.TEXT_TAG, "/{}".format(last_open_tag[-1])) )
                                last_open_tag.pop()
                            last_open_tag.append(tg)

                ## Manually closing tags
                if tag_c.startswith("/if"):
                    if (last_open_tag
                            and last_open_tag[-1] in ("if", "stop_if",
                                "skip_if")):
                        last_open_tag.pop()
                    else:
                        raise Exception("ERROR: Closing {/if} tag without corresponding {if}")
                elif tag_c.startswith("/elif"):
                    if (last_open_tag
                            and last_open_tag[-1] in ("elif", "stop_elif",
                                "skip_elif")):
                        last_open_tag.pop()
                    else:
                        raise Exception("ERROR: Closing {/elif} tag without corresponding {elif}")
                elif tag_c.startswith("/else"):
                    if (last_open_tag
                            and last_open_tag[-1] in ("else", "stop_else",
                                "skip_else")):
                        last_open_tag.pop()
                    else:
                        raise Exception("ERROR: Closing {/else} tag without corresponding {else}")

                else:
                    ## The proper closing tags
                    for tg in ("skip_if", "stop_if", "skip_elif", "stop_elif", "skip_else", "stop_else"):
                        if tag_c.startswith("/{}".format(tg)):
                            if (last_open_tag and last_open_tag[-1] == tg):
                                last_open_tag.pop()
                            else:
                                raise Exception("ERROR: Closing {{/{0}}} tag without corresponding {{{0}}}".format(tg))

            if tag == renpy.TEXT_TAG and any([
                tag_c.startswith("elif"), tag_c.startswith("else"),
                tag_c.startswith("/if"), tag_c.startswith("/elif"),
                tag_c.startswith("/else"),
            ]):
                ## Add the stop_ or skip_ version if needed
                if tag_c.startswith("/"):
                    prefix = "/"
                    tag_c = tag_c[1:]
                else:
                    prefix = ""
                new_contents.append( (renpy.TEXT_TAG, "{}{}{}".format(prefix, which_if, tag_c)) )
            else:
                new_contents.append( (tag, tag_c) )

        while last_open_tag:
            ## We need to close the last open tag
            new_contents.append( (renpy.TEXT_TAG, "/{}".format(last_open_tag[-1])) )
            last_open_tag.pop()

        ## Apply conditional tags right away, before Ren'Py gets to them,
        ## because we don't want dialogue tags like {p} or {w} being processed
        ## for the conditions which shouldn't appear.
        ## But don't evaluate the conditions when linting (can cause problems
        ## if variables aren't set up or defined, and we want to be able to
        ## optionally report those, not crash).
        if renpy.predicting() or renpy.game.lint:
            ret = tokens_to_text(new_contents)
        else:
            ## When it isn't predicting, apply the text tags to remove the
            ## dialogue timing ones
            ret = tokens_to_text(apply_conditional_tags(new_contents))
        return ret

    def check_for_seen_conditional():
        """
        A per-interaction callback to coordinate with the conditional text
        tags for saving line variants and stopping skipping if appropriate.
        Stops skipping if a line with a conditional should be considered unseen
        and the player is skipping only seen text.
        """

        ## A new interaction means a new line for saving to the
        ## saved variants dictionary.
        store.NEW_LINE = True

        ## Save the last line seen, since this is a new interaction.
        if store.just_seen_conditional:
            line_id, last_seen = store.just_seen_conditional
            persistent.seen_conditional_lines[line_id].add(last_seen)
            store.just_seen_conditional = None

        try:
            line_id = renpy.game.context().current
        except Exception as e:
            ## Likely not in-game yet
            return

        ## This will be put together by the text tag functions earlier
        last_seen = current_seen_lines.get(line_id, None)

        ## If last_seen is not None, then it has a list of the conditions
        ## the player saw when encountering this line.
        if last_seen is not None:
            ## Turn it into a tuple to compare with the set
            last_seen = tuple(last_seen)
            ## Check if the player has seen this variant
            has_seen = last_seen in persistent.seen_conditional_lines.setdefault(line_id, set())
            ## Add this combination to the "seen" combinations
            store.just_seen_conditional = (line_id, last_seen)
            ## Stop skipping, if relevant
            if (config.skipping and not preferences.skip_unseen and not has_seen
                    and config.allow_skipping and store._skipping
                    and config.skipping != "fast"):
                config.skipping = None

    def apply_conditional_tags(tokens):
        """
        Apply conditional custom text tags. A copy of the engine function that
        only pays attention to if/elif/else and their skip_ and stop_ variants.
        """

        rv = [ ]

        while tokens:

            t = tokens.pop(0)
            kind, text = t

            if kind == renpy.TEXT_TEXT and renpy.config.replace_text:
                rv.append((renpy.TEXT_TEXT, str(renpy.config.replace_text(text))))

            elif kind != renpy.TEXT_TAG:
                rv.append(t)

            else:

                tag, _, value = text.partition("=")

                if tag not in ("if", "elif", "else", "stop_if", "stop_elif",
                        "stop_else", "skip_if", "skip_elif", "skip_else"):
                    ## Not a conditional tag
                    rv.append(t)
                    continue

                func = renpy.config.custom_text_tags.get(tag, None)

                # The contents of this tag.
                contents = [ ]

                # The close tag we're looking for.
                close = "/" + tag

                # The number of open tags.
                count = 1

                while tokens:

                    # Count the number of `tag` tags that are still open.
                    t2 = tokens.pop(0)

                    kind2, text2 = t2

                    if kind2 == renpy.TEXT_TAG:
                        tag2, _, _ = text2.partition("=")

                        if tag2 == tag:
                            count += 1
                        elif tag2 == close:
                            count -= 1
                            if not count:
                                break

                    contents.append(t2)

                new_contents = func(tag, value, contents)

                new_tokens = [ ]

                for kind2, text2 in new_contents:
                    if isinstance(text2, bytes):
                        text2 = str(text2)

                    new_tokens.append((kind2, text2))

                new_tokens.extend(tokens)
                tokens = new_tokens

        return rv

    config.start_interact_callbacks.append(check_for_seen_conditional)


################################################################################
## DO NOT MODIFY
################################################################################
init 999 python:

    OldSkip = Skip

    class Skip(OldSkip):
        """
        A small override to the Skip class to have skip buttons behave
        correctly when encountering conditional text tags in lines.
        """
        def get_sensitive(self):
            if not config.allow_skipping:
                return False

            if not _skipping:
                return False

            if store.main_menu:
                return False

            if _preferences.skip_unseen:
                return True

            try:
                line_id = renpy.game.context().current
            except Exception as e:
                ## Likely not in-game yet
                return False

            ## This will be put together by the text tag functions earlier
            last_seen = current_seen_lines.get(line_id, None)

            ## If last_seen is not None, then it has a list of the conditions
            ## the player saw when encountering this line.
            if last_seen is not None:
                ## Turn it into a tuple to compare with the set
                last_seen = tuple(last_seen)
                ## Check if the player has seen this variant
                has_seen = last_seen in persistent.seen_conditional_lines.setdefault(line_id, set())
                ## Stop skipping, if relevant
                return has_seen

            if renpy.game.context().seen_current(True):
                return True

            return False

    ## This bit of code ensures you can still have a say_menu_text_filter
    ## that won't conflict with the one needed to automatically close
    ## conditional text tags.
    if config.say_menu_text_filter is None:
        config.say_menu_text_filter = add_conditional_tags
    else:
        ORIGINAL_FILTER = config.say_menu_text_filter
        config.say_menu_text_filter = lambda s: ORIGINAL_FILTER(add_conditional_tags(s))

## This text tag guarantees the game will consider a line seen if any variant
## of it has been seen. Useful for tiny modifications to the line.
define config.custom_text_tags["skip_if"] = conditional_dialogue(save_variants=False)
define config.custom_text_tags["skip_elif"] = elif_dialogue(save_variants=False)
define config.custom_text_tags["skip_else"] = else_dialogue(save_variants=False)

## This tag means a line will only be considered seen if the player has seen
## the exact variant before. Useful for lines you would want to stop skipping
## if the player hasn't seen them before.
define config.custom_text_tags["stop_if"] = conditional_dialogue(save_variants=True)
define config.custom_text_tags["stop_elif"] = elif_dialogue(save_variants=True)
define config.custom_text_tags["stop_else"] = else_dialogue(save_variants=True)

## Like with regular dialogue lines, this keeps track specifically of which
## dialogue variants the player has seen of a given line. It is used to stop
## skipping if the player encounters a variant they haven't seen before.
default persistent.seen_conditional_lines = dict()
## A variable that keeps track of which variants of a line the player has
## just seen, to be added to the above dictionary when the line is finished.
default just_seen_conditional = None
## Used to temporarily store which lines the player has seen,
## for saving variants.
default current_seen_lines = dict()

## Sets up the behaviour of the default {if} tag, based on the config
## value at the top of this file.
define config.custom_text_tags["if"] = conditional_dialogue(
    save_variants=not myconfig.inline_conditions_same_for_skipping)
define config.custom_text_tags["elif"] = elif_dialogue(
    save_variants=not myconfig.inline_conditions_same_for_skipping)
define config.custom_text_tags["else"] = else_dialogue(
    save_variants=not myconfig.inline_conditions_same_for_skipping)

################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**inline_conditions.rpy", None)
    build.classify("**inline_conditions.rpyc", "archive")
################################################################################