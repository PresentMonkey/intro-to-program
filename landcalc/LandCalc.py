#LandCalc.py
#Patrick Gawel
#2021/01/25
#Converts sq feet to acres

#Utility function to convert sq feet to acres
def sqfeet_to_acres(feet):
    return feet/43560

#Utility function to convert acres to square feet
def acres_to_sqfeet(acres):
    return acres*43560

#Main function to ask the user for imput and executes the commands
def ask():

    #Asks for which operation to do
    operation = input("Sq Ft -> Acres (1) or Acres -> Sq Ft (2)? (Input 1 or 2): ")
    if(operation == "1"): 
        a = float(input("How many square feet? ")) #If it's the first option, ask for sqare feet
        print(a, " square feet is equal to ", sqfeet_to_acres(a), "acres") #prints the calculation and calls the conversion function
    if(operation == "2"): 
        a = float(input("How many acres? ")) #If it's the second option ask for acres
        print(a, "acres is equal to ", acres_to_sqfeet(a), "square feet") # the calculation and calls the conversion function

ask() #runs the ask() function