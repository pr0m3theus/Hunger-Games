from graphics import *
import utils

"""
A collection of tests of the functions in the utils.py module.
"""

def randomColor():
    for _ in range(10):
        print utils.randomColor()

def randomColorFill():
    w = GraphWin("Test of randomColorFill()", 500, 500)
    c = Circle(Point(250, 250), 100)
    c.setWidth(10)
    c.setFill("yellow")
    c.draw(w)

    while True:
        point = w.checkMouse()
        key = w.checkKey()

        if point or key:
            utils.randomColorFill(c)

def randomPoints():
    for _ in range(10):
        print utils.randomPoints()


def showAndHide():
    w = GraphWin("Test of show() and hide", 500, 500)

    c = Circle(Point(150, 150), 100)
    c.setWidth(10)
    c.setFill("yellow")

    r = Rectangle(Point(250, 350), Point(350, 450))
    r.setWidth(10)
    r.setFill("red")

    l = Line(c.getCenter(), r.getCenter())
    l.setWidth(4)
    l.setArrow("both")
    l.setOutline("blue")

    objects = [c, r, l]

    n = 0

    print
    print "Click anywhere in the window."
    print
    print "Press any key or click anywhere in the window to show/hide all objects."
    print

    while True:
        point = w.checkMouse()
        key = w.checkKey()

        if point or key:

            n = n + 1

            if n % 2 == 1:
                utils.show(objects, w)
            else:
                utils.hide(objects)

def grow():
    w = GraphWin("Test of grow()", 500, 500)
    w.setBackground("black")
    t = Text(Point(250, 250), "The Hunger Games")
    t.setStyle("bold")
    t.setTextColor("yellow")
    t.draw(w)

    print
    print "Click anywhere in the window."
    print
    print "Press any key or click anywhere in the window to grow the text."
    print

    while True:
        point = w.checkMouse()
        key = w.checkKey()

        if point or key:
            utils.grow(t)

def fade():
    w = GraphWin("Test of fade()", 500, 500)
    w.setBackground("black")

    print
    print "Click anywhere in the window."
    print
    print "Press any key or click anywhere in the window to fade the background"
    print


    while True:
        point = w.checkMouse()
        key = w.checkKey()

        if point or key:
            utils.fade(w)

def inCircleOrInRectangle():
    w = GraphWin("Test of inCircle() and inRectangle()", 500, 500)

    c = Circle(Point(150, 150), 100)
    c.setWidth(10)
    c.setFill("yellow")
    c.draw(w)

    r = Rectangle(Point(350, 350), Point(450, 450))
    r.setWidth(10)
    r.setFill("red")
    r.draw(w)


    print
    print "Click anywhere in the window."
    print
    print "Try to click inside the circle and the square."
    print


    while True:
        point = w.getMouse()


        if utils.inCircle(point, c):
            print point, "INSIDE circle"
        elif utils.inRectangle(point, r):
            print point, "INSIDE rectangle"
        else:
            print point

def makeGrid():
    w = GraphWin("Test of makeGrid()", 500, 500)
    grid = utils.makeGrid()
    utils.show(grid, w)
    n = 0

    print
    print "Press any key or click anywhere in the window to hide/show the grid."
    print

    while True:
        point = w.checkMouse()
        key = w.checkKey()

        if point or key:
            n = n + 1

            if n % 2 == 1:
                utils.hide(grid)
            else:
                utils.show(grid, w)
