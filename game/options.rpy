﻿## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Double Dealing Heroes")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "DoubleDealingHeroes"


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""A game created for Touhou Pride Jam 6.

By Jacoder23, Joel, DX5536, JerryStuffRo, and BurlyBurly.

-------------------------------------------------------------

This game uses assets from many different creators:

- {a=https://speakthesky.itch.io/typeface-dicier}Dicier{/a} by Speak the Sky, licensed under CC BY 4.0

- {a=https://siyokoy.itch.io/astrology-renpy-gui-kit}Astrology GUI{/a} by Siyokoy

- {a=https://feniksdev.itch.io/outline-shader-renpy}Outline Shader{/a} and {a=https://feniksdev.itch.io/achievements-for-renpy}Achievements{/a}, and {a=https://feniksdev.itch.io/inline-conditions-for-renpy}Inline Conditions{/a} by Feniks

- {a=https://dmochas-assets.itch.io/dmochas-bleeps-pack}Bleeps Pack{/a} by dmochas, licensed under CC BY 4.0

- {a=https://game-icons.net/1x1/delapouite/dice-twenty-faces-twenty.html}D20 Dice{/a} by Delapouite under CC BY 3.0

- {a=https://skolaztika.itch.io/renpy-codex-screen}Ren'py Codex{/a} by Skolaztika

- {a=https://kigyo.itch.io/renpy-word-counter}Lint+{/a} by KigyoDev

- {a=https://wattson.itch.io/renpy-auto-highlight}Renpy Auto Highlight{/a} and {a=https://wattson.itch.io/kinetic-text-tags}Kinetic Text Tags{/a} by Wattson

- {a=https://remort-studios.itch.io/make-visual-novels-sep}Staging Enhancement Pack{/a} and {a=https://remort-studios.itch.io/make-visual-novels-rspv1}Shader Pack{/a} by Nai @ MakeVisualNovels

A large amount of SFX came from {a=https://www.shapeforms.com/}Shapeforms Audio{/a}. Their license doesn't require mention but so much was used that I feel the need to credit them. They are very good at what they do.

-------------------------------------------------------------

Any fans of the Parahumans series by Wildbow will note major similarities in this game, most specifically with Worm. If given time, I'd make this a true Touhou x Worm crossover.

As it is, I can't call this a Worm fangame without any Worm characters and divergences from the setting due to many details being irrelevant to this specific story.

""")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "TouhouVillains"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"

## Layers ######################################################################
# define config.layer_clipping['master'] = (0, 102, 1920, 876)
define config.layers = [ 'master', 'UI', 'transient', 'screens', 'overlay', 'particles' ]

## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = arrowUp
define config.exit_transition = arrowDown


## Between screens of the game menu.

define config.intra_transition = arrowUp


## A transition that is used after a game has been loaded.

define config.after_load_transition = arrowDown


## Used when entering the main menu after the game has ended.

define config.end_game_transition = arrowDown


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"

## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 50


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "DoubleDealingHeroes-9943655072"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('server/**', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)
    build.classify('game/cache/**', None)
    ## NOTE: This excludes markdown and txt files. If you use these formats
    ## for README or instructions, you may want to remove these lines.
    build.classify('**.txt', None)
    build.classify('**.md', None)
    build.classify('**.rpy', None)

    ## To archive files, classify them as 'archive'.

    build.classify("game/**.rpy", "archive")
    build.classify("game/**.rpym", "archive")

    build.classify("game/**.webp", "archive")
    build.classify("game/**.webm", "archive")
    build.classify("game/**.mp4", "archive")
    build.classify("game/**.png", "archive")
    build.classify("game/**.jpg", "archive")
    build.classify("game/**.ttf", "archive")
    build.classify("game/**.otf", "archive")
    build.classify("game/**.mp3", "archive")
    build.classify("game/**.wav", "archive")
    build.classify("game/**.ogg", "archive")
    build.classify("game/**.opus", "archive")
    build.classify("game/**.rpyc", "archive")
    build.classify("game/**.rpymc", "archive")

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "jacoder23/doujins-and-dragons-2"

define config.log = "PrideJam6_log.txt"

# volumes

define config.default_music_volume = 0.6
define config.default_sfx_volume = 1