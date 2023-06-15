from graphics import *

def drawFace(center, size, win):
    # Draw the head
    head = Circle(center, size)
    head.setFill("yellow")
    head.draw(win)

    # Draw the eyes
    eyeSize = size // 10
    leftEye = Circle(center, eyeSize)
    rightEye = Circle(center, eyeSize)
    leftEye.move(-size // 4, -size // 4)
    rightEye.move(size // 4, -size // 4)
    leftEye.setFill("black")
    rightEye.setFill("black")
    leftEye.draw(win)
    rightEye.draw(win)

    # Draw the mouth
    mouthWidth = size // 2
    mouthHeight = size // 3
    mouthLeft = Point(center.getX() - mouthWidth // 2, center.getY() + size // 3)
    mouthRight = Point(center.getX() + mouthWidth // 2, center.getY() + size // 3)
    mouthMid = Point((mouthLeft.getX() + mouthRight.getX()) / 2, center.getY() + size // 3 + mouthHeight)
    mouth = Oval(mouthLeft, mouthRight)
    mouth.setFill("black")
    mouth.draw(win)

    # Draw the smile lines
    lineLeft = Line(mouthLeft, mouthMid)
    lineRight = Line(mouthRight, mouthMid)
    lineLeft.draw(win)
    lineRight.draw(win)



def main():
    win = GraphWin("Smiley Faces", 500, 500)

    # Draw three faces with different sizes
    drawFace(Point(100, 100), 50, win)
    drawFace(Point(250, 250), 100, win)
    drawFace(Point(400, 400), 150, win)

    win.mainloop()

if __name__ == '__main__':
    main()
