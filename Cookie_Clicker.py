# Import the Tkinter & Turtle Graphics Modules
import Tkinter
import turtle

# Create Game Window
screen = turtle.Screen()
screen.screensize(500, 500, "black")

# Create Sprite
screen.addshape("cookie.gif")
bigCookie = turtle.Turtle()
bigCookie.hideturtle() # hide turtle until the the duck image replaces the placeholder shape
bigCookie.penup() # prevent sprite from drawing on screen as it moves
bigCookie.left(90) # rotate sprite for proper placement on screen
bigCookie.shape("cookie.gif") # Set Image for Sprite
bigCookie.setposition(0, 0)
bigCookie.showturtle()

# Create Player Controls
def fire():
    print("FIRE! (space bar pressed)")

def makeCookie(x, y):
  print("making cookie...")
  print("x: " + str(x))
  print("y: " + str(y))

# Set Event Listeners for Player Controls
screen.onkey(fire, "space")
# screen.onclick(makeCookie)
bigCookie.onclick(makeCookie)
screen.listen()

# Main Game Loop (Keeps Game Window From Closing)
Tkinter.mainloop()
