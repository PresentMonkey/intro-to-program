import turtle as t
import math

# Named Constants
scrw = 600 #screen width
scrh = 600 #screen height
llx = 100 #target's lower-left X coordinate
lly = 250 #target's lower-left Y coordinate
tgtw = 25 #target width

# Set up Window
t.setup(scrw, scrh)

# move turtle to start of Target
t.hideturtle()
t.speed(0)
t.penup()
t.goto(llx, lly)

# Draw the Target
t.pendown()
t.forward(tgtw)
t.left(90)
t.forward(tgtw)
t.left(90)
t.forward(tgtw)
t.left(90)
t.forward(tgtw)

# Start Turtle at center of screen (origin)
t.penup()
t.goto(0, 0)
t.showturtle()

# Get angle and force for Turtle (user supplied)
angle = float(input("Enter turtle's angle: "))
force = float(input("Enter launch force (1 -200): "))

# Set the Turtle's heading (direction)
t.setheading(angle)
t.pendown()
t.forward(force)

# Launch turtle into outer space
maxangle = math.atan((lly+tgtw)/llx)*57.2958
minangle = math.atan(lly/(llx+tgtw))*57.2958
maxdistance = math.sqrt((llx+tgtw)**2 +(lly+tgtw)**2)
mindistance = math.sqrt(llx**2 + lly**2)

if (angle <=maxangle and angle >=minangle and force <=maxdistance and force >= mindistance):
  print("You hit the Target!")

if (angle > maxangle): #if angle is too great
  print("Lower the angle")

elif (angle < minangle): #if angle is too small
  print("Raise the angle")

elif (force < mindistance): #if force is too little
  print("Use more force")

elif (force > maxdistance): #if force is too great
  print("Use less force")

elif t.xcor() < llx:
  print("You're just off to the left")

elif t.xcor() > llx+tgtw:
  print("You're just off to the right")

elif t.ycor() < lly:
  print("You're just below it")

elif t.ycor() > lly+tgtw:
  print("You're just above it")