from graphics import *

win = GraphWin('TestWindow', 200, 150)  # give title and dimensions
# win.yUp() # make right side up coordinates!

body = Circle(Point(40, 100), 25)
body.setFill("red")
body.draw(win)

message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
message.draw(win)
print(win.getKey())
win.close()
