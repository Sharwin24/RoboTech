from graphics import *

win = GraphWin('AquaSim', 1920, 1080)  # give title and dimensions
# win.yUp() # make right side up coordinates!

body = Circle(Point(40, 100), 25)
body.setFill("red")
body.draw(win)

message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
message.draw(win)
print(win.getKey())
win.close()