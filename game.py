from graphics import *

# Use the funtions from utils.py as part the solution.
from utils import *

def main():
    """
    The main function of the game.

    Side effects:
      Shows a splash screen.
      When the player clicks on the play button, lets the user play the game.
      If the user clicks on the quit button, close the window.
    """

    w = GraphWin("The Hunger Games", 500, 500)
    splash(w)
    game(w)

def splash(w):
    """
    Argument(s):
      w :: Graphical window.

    Side effects:
      Shows the splash screen with two buttons and a "hidden"
      Easter egg.

      Buttons:
        play -  play the game.
        quit - close the window w.

      Easter egg:
        When the user clicks on a "secret area" of the splash screen,
        the "secret area" changes to a random color.
    """

    w.setBackground("black")

    # TODO: Add code here.

    # We make function calls creating shapes and text return said things,
    # so that we can undraw them later

    play_button, play_text = playButton(w)
    quit_button, quit_text = quitButton(w)
    banner_text = banner(w)
    Ec = Easter(w)
    
    buttons = [play_button, quit_button, Ec, play_text, quit_text, banner_text]
    
    # loop until a function call makes something else happen
    while True:
        clicked_button = get_clicked_button(w, buttons)
        
        # get_clicked_button returns -1 if no button was clicked
        if clicked_button == -1:
            continue
        
        # button id 6 is the easter egg button :))))
        if clicked_button.id == 6:
            random_button_color(clicked_button)
        if clicked_button.id == 1:
            for button in buttons:
            	button.undraw()
            fade(w)
            # break out of the while loop so that the function can return
            # and we can execute game()
            break
            

    # Make use of the functions from utils.py as part of your solution.

    # Structure the code by creating new functions, for example one function
    # for each of the following tasks:
    #
    #    1) Create (and return) the Easter egg circle.
    #    2) Create (and return) the text "The Hunger Games".
    #    3) create (and return) a tuple with the play button circle and
    #       text.
    #    4) Create (and return) a tuple with the quit button rectangle
    #       and text.


def makeHero(p):
    """
    Argument(s):
      p :: Point.

    Return value: A circle with center p representing the hero.
    """

    h = Circle(p, 35)
    h.setWidth(10)
    h.setFill("yellow")

    return h

def makeFood(p):
    """
    Argument(s):
      p :: Point.

    Return value: A circle with center p representing the food.
    """

    f = Circle(p, 20)
    f.setWidth(10)
    f.setFill("red")

    return f

def gameOver(hero, food):
    """
    Argument(s):
      hero :: Circle
      food :: Circle

    Return value :: Bool
      Returns True if the center of the hero is the same as the center of the food,
      otherwise returns False.
    """

    return False # TODO: Change this.


def delta(hero, key):
    """
    Argument(s):
      hero :: Circle
      key  :: String ("Up", "Down", "Left" or "Right").

    Return value :: a tuple (dx, dy).
      dx - how much to move the hero circle in the x-direction.
      dy - how much to move the hero circle in the y-direction.
    """

    (dx, dy) = (0, 0)

    # TODO: Add code here.

    return (dx, dy)

def game(w):
    """
    Argument(s):
      w :: Graphical window.

    Side effects:
      Let the user play the game by moving the hero around on the grid.
    """

    grid = makeGrid()

    (h, f) = randomPoints()
    hero = makeHero(h)
    food = makeFood(f)

    objects = grid + [hero, food]
    show(objects, w)

    while True:
        if gameOver(hero, food):
            hide(objects)
            splash(w)

        key = w.getKey()

        (dx, dy) = delta(hero, key)

        hero.move(dx, dy)


if __name__ == "__main__":
    main()
