"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Bradshaw.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

goat_turtle = rg.SimpleTurtle('turtle')
goat_turtle.pen = rg.Pen('midnight blue', 4)
goat_turtle.speed = 10

fat_turtle = rg.SimpleTurtle('turtle')
fat_turtle.pen = rg.Pen('red', 2)
fat_turtle.speed = 10
size = 100

for k in range(14):
    goat_turtle.draw_circle(size)
    goat_turtle.pen_up()
    goat_turtle.right(90)
    goat_turtle.forward(20)
    goat_turtle.left(90)

    goat_turtle.pen_down()

    fat_turtle.draw_square(size)
    fat_turtle.pen_up()
    fat_turtle.right(90)
    fat_turtle.forward(10)
    fat_turtle.left(90)

    fat_turtle.pen_down()

    size = size + 12







window.close_on_mouse_click()



