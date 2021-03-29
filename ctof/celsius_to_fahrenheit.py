#celsius_to_fahrenheit.py
#Patrick Gawel
#2021/01/27
#Converts celcuis to fahrenheit and vice versa

#Utility function to convert celcuis to fahrenheit
def sqfeet_to_acres(celcuis):
    return (celcuis* 9/5) + 32

#Utility function to convert fahrenheit to celcuis 
def acres_to_sqfeet(fahrenheit):
    return (fahrenheit-32)* 5/9

#Main function to ask the user for imput and executes the commands
def ask():

    #Asks for which operation to do
    operation = input("Celsuis to Fahrenheit (1) \nFahrenheit to Celsuis (2) \nType in 1 or 2: ")
    if(operation == "1"): 
        a = float(input("How many degrees in Celsius? ")) #If it's the first option, ask for sqare feet
        print(a, " degrees Celsuis is equal to ", sqfeet_to_acres(a), "degrees Fahrenheit") #prints the calculation and calls the conversion function
    if(operation == "2"): 
        a = float(input("How many degrees in Fahrenheit? ")) #If it's the second option ask for acres
        print(a, "degrees Fahrenheit is equal to ", acres_to_sqfeet(a), "Celsuis") # the calculation and calls the conversion function

ask() #runs the ask() function