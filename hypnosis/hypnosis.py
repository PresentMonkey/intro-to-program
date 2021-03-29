#Patrick Gawel

import turtle
from scipy.interpolate import interp1d

class Constants: #Constants class to store all of our constants, we want to avoid globals
    SPEED = 0
    START = 1 
    END = 700 #How long the loop will run for
    STEP = 1 #Step of 1 gives best results, the shape will be regardless of step because of functions. Think of STEP more like resolution
    class ANGLE:
        START = 90
        END = 91
    class LINE_LENGTH:
        START = 5
        END = 700 #Make sure this is large enough or it will be very small
    LINE_COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


dwg = turtle.Screen() #Creates screen object
dwg.setup(1280, 640, 0, 0) #Makes it bigger than default
dwg.bgcolor('black') #Makes the background black

pen = turtle.Turtle() #Create turtle object we will call pen
pen.hideturtle() 
pen.speed(Constants.SPEED)
pen.color('white') #Initial Color

#Find functions that will be used in the loop
angle_function = interp1d([Constants.START, Constants.END], [Constants.ANGLE.START, Constants.ANGLE.END], kind="linear") 
line_length_function = interp1d([Constants.START, Constants.END], [Constants.LINE_LENGTH.START, Constants.LINE_LENGTH.END], kind="linear") 
line_color_function = interp1d([Constants.START, Constants.END], [0, len(Constants.LINE_COLORS)], kind="linear")


#For loop to draw the shape
for i in range(Constants.START, Constants.END, Constants.STEP): 
    pen.forward(line_length_function(i)) #Uses the interpolation function to find the value of forward
    pen.left(angle_function(i)) #Uses the interpolation function to find the value of angle to turn
    pen.color(Constants.LINE_COLORS[int(line_color_function(i))]) #This causes a sharp contrast, in the future I would like to figure out how to make the transition smooth

dwg.mainloop()