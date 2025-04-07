# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Suka Krisa")


# The game starts here.

label start:

    play music "audio/bsCheshireCatTheme.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg saya

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show suka

    # These display lines of dialogue.

    k "hola, soy krisa, la hija de titivillus, y he venido a violarte"

    k ":v"

    # This ends the game.

    return
