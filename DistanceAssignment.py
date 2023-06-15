from graphics import *
import math

def main():
    win = GraphWin("Distance between 2 points", 400, 400)
    win.setCoords(-10, -10, 10, 10)

    message = Text(Point(0, 9), "Click on two points to find the distance between them.")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    distance = math.sqrt(dx**2 + dy**2)

    result = Text(Point(0, -9), "The distance between the points is {:.2f}.".format(distance))
    result.draw(win)
    print(result)

    win.getMouse()
    win.close()


main()