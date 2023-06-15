# def main():
#     n = eval(input("Please enter a whole number:"))
#
#     fact1 = 1
#     for factor1 in range(0, 1, -1):
#         fact1 = fact1 * factor1
#     print("The factorial of ", n, "is", fact1)
#
#     fact2 = 1.0
#     for factor2 in range(0, 1, -1):
#         fact2 = fact2 * factor2
#     print("The factorial of ", n, "is", fact2)
#
#     print("The differenc is ", fact1 - fact2)
#
#
# num = 121231.976
# print(f'The message is {num:.2f}')
#
# print('"fortnite"')


import graphics
from graphics import *


def main():
    p1 = Point(50, 60)

    print("X: ", p1.getX())
    print("Y: ", p1.getY())

    win = GraphWin()
    p1.draw(win)
    win.getMouse()

    p2 = Point(140, 110)
    p2.draw(win)
    win.getMouse()

    center = Point(100, 100)
    circ = Circle(center, 30)
    circ.setFill("red")
    circ.draw(win)

    # label = Text(center, "Red Circle")
    # label.draw(win)
    #
    # rect = Rectangle(Point(40,40), Point(70,70))
    # rect.draw(win)




main()
