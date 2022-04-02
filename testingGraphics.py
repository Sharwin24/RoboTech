from graphics import *

win = GraphWin('TestWindow', 1000, 800)  # give title and dimensions
#win.yUp() # make right side up coordinates!

img = Image(Point(500, 400), "starter_lake.png")
img.draw(win)

body = Circle(Point(40, 100), 25)
body.setFill("red")
body.draw(win)

message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
message.draw(win)
print(win.getKey())
win.close()
