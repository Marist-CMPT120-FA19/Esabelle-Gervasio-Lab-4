from graphics import *
import time
def main():
#box
    win=GraphWin("Traffic Light")
    shape = Rectangle(Point(20,20), Point(80,170))
    shape.setOutline("black")
    shape.setFill("white")
    shape.draw(win)

#red
    red = Circle(Point(50,45), 20)
    red.setOutline("black")
    red.setFill("red")
    red.draw(win)

#yellow
    yellow = Circle(Point(50,95), 20)
    yellow.setOutline("black")
    yellow.setFill("yellow")
    yellow.draw(win)

#green
    green = Circle(Point(50,145), 20)
    green.setOutline("black")
    green.setFill("green")
    green.draw(win)

main()

