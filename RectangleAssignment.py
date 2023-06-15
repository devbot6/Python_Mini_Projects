from graphics import *


def calculate_rectangle_information(x1, y1, x2, y2):
    length = abs(x2 - x1)
    width = abs(y2 - y1)
    perimeter = 2 * (length + width)
    area = length * width
    return length, width, perimeter, area


def draw_rectangle():
    win = GraphWin("Rectangle", 500, 500)
    message = Text(Point(win.getWidth() / 2, 20), "Click on two points to define the rectangle.")
    message.draw(win)

    p1 = win.getMouse()
    x1, y1 = p1.getX(), p1.getY()
    p2 = win.getMouse()
    x2, y2 = p2.getX(), p2.getY()

    length, width, perimeter, area = calculate_rectangle_information(x1, y1, x2, y2)
    r = Rectangle(p1, p2)
    r.draw(win)
    message.setText("Perimeter: {}\nArea: {}".format(perimeter, area))

    win.getMouse()
    win.close()


# Example usage:
draw_rectangle()

