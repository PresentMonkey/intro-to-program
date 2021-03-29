#Patrick Gawel
#
#
#
import turtle 
import math
import random
import time

#Constants
screen_width = 600
screen_height = 600
target_width = 25

#Terminal Colors

class tcolors:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDCOLOR = '\033[0m'
    BOLD = '\033[1m'



targetCord = turtle.Vec2D(random.randint(0, 180), random.randint(50, 300)) #generatoes random vector(angle, force) that is limited between 180 degrees and between 50 and 300 to fit on screen

#for debugging
#print(targetCord)

def createObject(): #Utility function to easily create new objects with default parameters
    newObject = turtle.Turtle()
    newObject.hideturtle()
    newObject.penup()
    newObject.speed(0)
    return newObject

def angle_forceToCord(vector): #Converts angle,force vector to cartesion cords for rendering (this makes is an easier system to provide user feedback)
    force = vector[1]
    angle = vector[0]
    angleRad = math.radians(angle)
    yCord = force*math.sin(angleRad)
    xCord = force*math.cos(angleRad)
    return turtle.Vec2D(xCord, yCord)


def drawDot(vector, color): #Dot function that was used for debugging and to show inital point
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(vector)
    turtle.dot(10, color)
    turtle.penup()

class Target:
    def __init__(self, vector ,width): #Called when target is created
        self.vector = vector
        self.width = width
        self.angle = vector[0]
        self.force = vector[1]
        self.halfWidth = self.width/2 #just to make it easier for ourselfs later
        self.origin = angle_forceToCord(self.vector) #does this for us beforehand so we don't need to do it multiple times, returns vector in format: (x,y)
        self.topLeft = turtle.Vec2D(self.origin[0]-self.halfWidth, self.origin[1]+self.halfWidth) #Subracts halfwidth from x and adds halfwidth to y
        self.bottomRight = turtle.Vec2D(self.origin[0]+self.halfWidth, self.origin[1]-self.halfWidth) #Add halfwidth to x and Subracts halfwidth from y

        self.turtle = createObject()
        #Debugging lines
        #drawDot(self.topLeft, "blue")
        #drawDot(self.bottomRight, "green")
        #drawDot(self.origin, "red")

    def draw(self): #draws rectange 
        self.turtle.goto(self.topLeft) #We start drawing from the topleft
        self.turtle.pendown()
        self.turtle.setheading(0)
        for i in range(4): #draws rectangle
            self.turtle.forward(self.width)
            self.turtle.rt(90)
        self.turtle.penup()

    def checkifIn(self, userInput): #Method that checks if the userinputs are in the rectange
        userInputCords = angle_forceToCord(userInput)
        if((self.topLeft[0]< userInputCords[0] < self.bottomRight[0]) and (self.topLeft[1]> userInputCords[1] > self.bottomRight[1])):
            return True
        else:
            return False

    def suggestions(self, userInput): #Method that provides feedback to the user, returns a string with the feedback
        angleSuggestion = None
        forceSuggestion = None
        #First suggests angle
        if(userInput[0] > self.angle):
            angleSuggestion = "Your Angle is too high"
        elif(userInput[0] < self.angle):
            angleSuggestion = "Your Angle is too low"
        #Second suggests force
        if(userInput[1] > self.force):
            forceSuggestion = "Your Force is too strong"
        elif(userInput[1] < self.force):
            forceSuggestion = "Your force is too low"

        if(angleSuggestion and forceSuggestion):
            return angleSuggestion + " and " + forceSuggestion
        elif(angleSuggestion):
            return angleSuggestion + "!"
        elif(forceSuggestion):
            return forceSuggestion + "!"

            
    def clear(self):
        self.turtle.clear()

class Projectile: #projectice class
    def __init__(self, vector): #Creates projective with vector cords
        self.turtle = createObject()
        self.angle = vector[0]
        self.force = vector[1]
    def launch(self): #Launches the projective
        self.turtle.showturtle()
        self.turtle.pendown()
        self.turtle.seth(self.angle)
        self.turtle.forward(self.force)
    def clear(self):
        self.turtle.clear()


#Initial Setup Code
screen = turtle.Screen()
screen.setup(
    width=600,
    height=600,
    startx=-400 #needed for it to show on the second moniter, not in the middle of my 2 screens
)

#more setup code

target = Target(targetCord, target_width)
target.draw()

drawDot(turtle.Vec2D(0,0), "red") #Draws dot from where the line will start from

def ask(): #Function to ask the user, returns a vector with the userinput
    angle = float(input(f"{tcolors.YELLOW}Enter the angle (0-180): {tcolors.ENDCOLOR}"))
    force = float(input(f"{tcolors.YELLOW}Enter the force (50-360): {tcolors.ENDCOLOR}"))
    return turtle.Vec2D(angle, force)


def mainloop(): #the main loop that we run
    userInput = ask() #ask the user
    projectile = Projectile(userInput) #create a project with userinput and then launch it
    projectile.launch()
    if(target.checkifIn(userInput)): #Checks if the userinput (aka the projectile) is within the rectange
        print(f"{tcolors.GREEN}Congrats you have made it in! \nProgram will exit in 5 seconds{tcolors.ENDCOLOR}") #if it is then prints a success line and exits
        time.sleep(5)
        exit()
    else: # if user input is not correct that it provides suggestions, tells the user to try again and reruns the mainloop to repeat the process
        print(target.suggestions(userInput))
        print(f"{tcolors.RED}Try again! {tcolors.ENDCOLOR}")
        mainloop()
    

mainloop() #runs mainloop function for the first time
screen.mainloop() #required for turtle screen to not exit
    