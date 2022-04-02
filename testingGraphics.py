from graphics import *

width = 1440
height = 810

win = GraphWin('TestWindow', width, height)  # give title and dimensions
#win.yUp() # make right side up coordinates!

img = Image(Point(width / 2, height / 2), "starter_lake75.png")
img.draw(win)

body = Circle(Point(40, 100), 25)
body.setFill("red")
body.draw(win)

message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
message.draw(win)
print(win.getKey())
win.close()
