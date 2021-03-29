#Patrick Gawel


def kilogramsTopounds(kilos): #Function to convert kilos to pounds
    return kilos*2.2

userInput = float(input("Enter number of Kilograms: ")) #Asks user

userInputConverted = kilogramsTopounds(userInput) #Converts userinput
print(userInputConverted, " pounds ") #prints the result

if(userInputConverted >= 100 and userInputConverted <= 500): #Determins what else to print
    print("Weight is just right!")
elif(userInputConverted < 100):
    print("Weight is too light!")
elif(userInputConverted > 500):
    print("Weight is too heavy! ")