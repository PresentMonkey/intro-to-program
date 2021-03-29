#Patrick Gawel

import turtle


Vec2D = turtle.Vec2D #make it easier for us

turtle.speed(0) #Sets max speed
turtle.hideturtle()

#Constants
class constants:
    class screen:
        width= 600
        height= 600
    class checker:
        columns= 13
        rows= 13
        color1= "red"
        color2= "blue"

def isEven(num): #Function to check if a number is even
    if(num % 2) == 0:
        return True
    else:
        return False

def drawSquare(turtleObject, bottomLeftVec, width, height, color): #Draws a rectangle with width, height, and color arugments
    turtleObject.penup()
    turtleObject.fillcolor(color)
    turtleObject.goto(bottomLeftVec)
    turtleObject.pendown()
    turtleObject.begin_fill()
    turtleObject.setheading(0)


    for i in range(2): #draws rectangle
        turtleObject.forward(width)
        turtleObject.lt(90)
        turtleObject.forward(height)
        turtleObject.lt(90)
    turtleObject.end_fill()
    turtleObject.penup()

def drawRow(heightPos, offset): #Draws one row with arguments of how high is should be and the color offset
    colorAccumulator = 0 + offset #Adds the offset to the inital value of zero
    positionX = -(constants.screen.width / 2) #Calculates the inital X position we should start from by dividing the screen width by 2 and making it negative
    squareWidth = constants.screen.width / constants.checker.columns #Calcultates the square width by dividing the screen width by the number of desired colums
    squareHeight = constants.screen.height / constants.checker.rows #Calculates the square height by dividing the screen height by the number of desired colums
    for i in range(0, constants.checker.columns): #Loop to draw the squares
        if(isEven(colorAccumulator)): #Only if the accumulator is even do we draw color1
            drawSquare(turtle, Vec2D(positionX, heightPos), squareWidth, squareHeight, constants.checker.color1)
        else: #Else we draw color2
             drawSquare(turtle, Vec2D(positionX, heightPos), squareWidth, squareHeight, constants.checker.color2)
        #Increment the position by the square width and the color accumulator by 1
        positionX = positionX + squareWidth 
        colorAccumulator = colorAccumulator + 1


def drawBoard(): #Draws the full board
    turtle.tracer(100000000000) #we turn off turtle updates using a large tracer number and later turn them on so our checkboard renders instantly
    positionY = -(constants.screen.height / 2) #Calculates the initual X position by divinding the height by 2 and making it negative which means we start from the bottom drawing upwards
    squareHeight = constants.screen.height / constants.checker.rows 
    for i in range(0, constants.checker.rows): #Draws each row using the drawRow() function, we use i as the accumulator since it changes each time
        drawRow(positionY, i)
        positionY = positionY + squareHeight
    turtle.update() #Render screen

screen = turtle.Screen()
screen.setup(
    width=constants.screen.width,
    height=constants.screen.height,
    startx=-400 #needed for it to show on the second moniter, not in the middle of my 2 screens
)


drawBoard()

turtle.mainloop()