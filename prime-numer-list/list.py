#Patrick Gawel

import math

def is_prime(number):
    '''Checks if a number is prime

        Returns boolean
    '''
    isPrime = True
    sqrtNum = int(math.sqrt(number))
    for i in range(2, sqrtNum + 1):
        remainder = number % i
        if(remainder == 0):
            isPrime = False
    
    return isPrime

    


printAll = bool(input("Enter whether or not you want to print all numbers(True) in range or just primes (Leave empty): "))
lowerBounds = int(input("Enter start of range to print out prime numbers from: "))
upperBounds = int(input("Enter end of range to print out prime numbers from: "))



for i in range(lowerBounds-1, upperBounds+1):
    if(printAll):
        print(i, is_prime(i))
    else:
        output = is_prime(i)
        if(output == True):
            print(i)
    
