import math
import operator
import time
import random
import config
from pygame.locals import QUIT
from collections import deque
from fractions import Fraction


# Lists out all possible functions
def functions():
    print("\nHelpful functions:\nType 'exponent' to find the exponent of a number\nType 'factorial' to find the factorial of a number\nType 'frac decim' to convert a fraction to decimal or vice versa\nType 'prime' to see if a number is prime or composite\nType 'gcf lcm' to find the GCF or LCM of a number\nType 'percent decimal' to convert a decimal to percent or vice versa\nType 'square root' to find the square root of a number\nType 'hypotenuse' to find the hypotenuse of a right angle triangle\nType 'right angle' to see if the given lengths form a right triangle\nType 'area' to find the area of a shape (rectangle, square, trapezoid, triangle, circle)\nType 'scientific' for a scientific (base 10) calculator\nType 'sci convert' to convert a standardn number to scientific or vice versa\nType 'convert units' to convert between units\n\nMiscellaneous:\nType 'random number' to get a random number generatior\nType 'roll a die' to roll a die\nType 'flip a coin' to flip a coin\nType 'magic ball' to have your fortune told\n")

# Exponent calculations
def exponent():
    try:
        number = float(input("Type number: "))
        power = float(input("Type power (ex. 2, 3): "))
        print(f"\n{number ** power}")

    except OverflowError:
        print(config.matherror)

    except ValueError:
        print(config.syntaxerror)

# Factorial function
def factorial():
    try:
        factorial = int(input("Type number: "))
        print(math.factorial(factorial))
        print()

    except OverflowError:
        print(config.matherror)
    
    except ValueError:
        print(config.syntaxerror)
    

# Fraction to decimal
def frac_decim():
    try:
        conver = input("Fraction to decimal or decimal to fraction (type frac to decim or decim to frac): ")
        if conver.lower() == "frac to decim":
            fraction_input = input("Type fraction (i.e. 3/4): ")
            decimal = float(Fraction(fraction_input))
            print(f"\n{fraction_input} as a decimal {decimal}\n")
        elif conver.lower() == "decim to frac":
            decimal_input = input("Type decimal (i.e. 0.75): ")
            fraction = Fraction(float(decimal_input)).limit_denominator()
            print(f"\n{decimal_input} as a fraction is {fraction}.")
    
    except ValueError:
        print(config.syntaxerror)

           
# See if a number is prime or composite
def prime_composite():
    try:
        prime_input = input("Type number in a whole number: ")
        prime = int(prime_input)

        if prime in [0, 1]:
            print(f"\n{prime} is not a prime number.")
        else:
            for i in range(2, int(prime**0.5)+1):
                if prime%i == 0:
                    print(f"\n{prime} is not a prime number.")
                    break
            else:
                print(f"\n{prime} is a prime number.")
    
    except ValueError:
        print(config.syntaxerror)

# Find the GCF or LCM of two numbers
def factor():
    which = input("GCF or LCM (Type GCF or LCM): ")
    try:
        if which.lower() == "gcf":
            greatest = int(input("Type first num: "))
            greatest2 = int(input("Type second num: "))
            print(f"\nThe GCF of {greatest} and {greatest2} is {math.gcd(greatest, greatest2)}")
        elif which.lower() == "lcm":
            lowest = int(input("Type first num: "))
            lowest2 = int(input("Type second num: "))
            print(f"\nThe LCM of {lowest} and {lowest2} is {math.lcm(lowest, lowest2)}")
    
    except ValueError:
        print(config.syntaxerror)

        
# Convert decimal to percent and vice versa
def percent_decimal():
    per = input("Percent to decimal or decimal to percent (type per to dec or dec to per): ")
    try:
        if per.lower() == "per to dec":
            number = float(input("Type decimal: "))
            res = number * 100
            print(f"\n{number} as a percent is {res}%.")
        elif per.lower() == "dec to per":
            percent = float(input("Type percent (i.e.: 70, 80, 50, do not put a percent sign after): "))
            answer = percent/100
            print(f"\n{percent} as a decimal is {answer}.")
        
    except ValueError:
        print(config.syntaxerror)
        

# Find square root of a number
def square_root():
    try:
        x_input = input("Type number: ")
        x = float(x_input)
        sol = math.sqrt(x)
        print(f"\nThe square root of {x} is {sol}.")
    
    except OverflowError:
        print(config.matherror)
        
    except ValueError:
        print(config.syntaxerror)
        

# Find hypotenuse of a triangle given the lengths
def hypotenuse():
    try:
        a = float(input("Type length a: "))
        b = float(input("Type length b: "))
        c = a**2 + b**2
        hyp = math.sqrt(c)
        print(f"\nThe hypotenuse of length a, {a} and length b, {b} is {hyp}.")

    except ValueError:
        print(config.syntaxerror)
    except OverflowError:
        print(config.matherror)


# See if a triangle with the given lengths is a right triangle
def rightangle():
    try:
        num1 = float(input("Type length a: "))
        num2 = float(input("Type length b: "))
        num3 = float(input("Type length of hypotenuse: "))
        if (num1**2) + (num2**2) == (num3**2):
            print(f"A triangle with the lengths of {num1}, {num2}, {num3} does form a right triangle.")
        else:
            print(f"A triangle with the lengths of {num1}, {num2}, and {num3} does not form a right triangle.")
    
    except ValueError:
        print(config.syntaxerror)
    except OverflowError:
        print(config.matherror)


# 
def area():
    try:
        shape = input("Type shape (three options: triangle, rectangle/square, trapezoid, circle): ")
        if shape.lower() in ["rectangle", "square"]:
            length = float(input("Type length: "))
            wid = float(input("Type width: "))
            area = len*wid
            print(f"\nThe area of a {shape} with a length and width of {len} and {wid} is {area}.")
        elif shape.lower() == "trapezoid":
            length1 = float(input("Type length: "))
            length2 = float(input("Type second length: "))
            height = float(input("Type height: "))
            ans = ((length1 + length2) / 2)*height
            print(f"\nThe area of a trapezoid with a length of {length1}, a second length of {length2}, and a height of {height} is {ans}.")
        elif shape.lower() == "triangle":
            b = float(input("Type base length: "))
            h = float(input("Type height: "))
            a = 0.5*(b*h)
            print(f"\nThe area of a triangle with base and height of {b} and {h} is {a}.")
        elif shape.lower() == "circle":
            r = float(input("Type radius: "))
            ar = math.pi*(r**2)
            print(f"\nThe area of a circle with a radius of {r} is {ar}.")
        else:
            print("\nSYNTAX ERROR: Type in a name from the shapes provided. Try again.")
    
    except ValueError:
        print(config.syntaxerror)
    except OverflowError:
        print(config.matherror)
    

def scicalc():
    operations = {"+": operator.add, 
                        "-": operator.sub,
                        "*": operator.mul,
                        "/": operator.truediv}
    try:
        sci = float(input("Type number in scientific form (i.e. 3.5e+06): "))
        sci2 = float(input("Type second number here: "))
        operation = input("Type operation: ")
        result = operations[operation](sci, sci2)
        print(f"\n{result:.2e}")
        
    except ValueError:
        print(config.syntaxerror)

    except KeyError:
        print(config.syntaxerror)
    
    except ZeroDivisionError:
        print(config.zerodiv)

    except OverflowError:
        print(config.matherror)
        

def sci_convert():
    try:
        option = input("Scientific to standard or standard to scientific (Type 'sci to stan' or 'stan to sci'): ")
        if option.lower() == "sci to stan":
            sci_num = input("Type in number in scientific form (i.e. 3.5e+06): ")
            stan = float(sci_num)
            print(f"\n{sci_num} in standard form is {stan}.")
        elif option.lower() == "stan to sci":
            standard = float(input("Type number: "))
            sci = f"{standard:.2e}"
            print(f"\n{standard} in scientific form is {sci}.")

    except ValueError:
        print(config.config.syntaxerror)
    except OverflowError:
        print(config.matherror)

def unit_convert():
    conversions = {
        "celsius to fahrenheit": lambda c: c * 1.8 + 32,
        "fahrenheit to celsius": lambda f: (f - 32) * 5 / 9,
        "feet to miles": lambda ft: ft / 5280,
        "miles to feet": lambda mi: mi * 5280,
        "meters to kilometers": lambda m: m / 1000,
        "kilometers to meters": lambda km: km * 1000,
        "miles to kilometers": lambda miles: miles*1.609,
        "kilometers to miles": lambda kilometers: kilometers/1.609,
        "liters to gallons": lambda l: l / 3.785,
        "gallons to liters": lambda g: g * 3.785,
    }

    units = input("Type units you want to convert (e.g. 'celsius to fahrenheit'): ").lower().strip()
    if units in conversions:
        value = float(input(f"Type the value you want to convert from {units.split(' to ')[0]}: "))
        result = conversions[units](value)
        print(f"\n{value} {units.split(' to ')[0]} is {result} {units.split(' to ')[1]}.\n")
    else:
        print("\nSYNTAX ERROR: Conversion not found. Try again.")


def numgen():
    try:
        max_input = input("Type max number: ")
        maxnum = int(max_input)
        print(f"{random.randint(0, maxnum)}")

    except OverflowError:
        print(config.matherror)
    
    except ValueError:
        print(config.syntaxerror)
        

def rolldice():
    amount = int(input("\nHow many dice would you like to roll (3 is maximum)?: "))
    if amount == 1:
        result = random.randint(1,6)
        print(f"\nThe die landed on a {result}.\n")
    elif amount == 2:
        outcome1 = random.randint(1,6)
        outcome2 = random.randint(1,6)
        print(f"\nThe dice landed on a {outcome1} and {outcome2} for a total sum of {outcome1+outcome2}.")
    elif amount == 3:
        result1 = random.randint(1,6)
        result2 = random.randint(1,6)
        result3 = random.randint(1,6)
        print(f"\nThe dice landed on a {result1}, {result2}, {result3} for a total sum of {result1+result2+result3}.")
    else:
        print("\nSYNTAX ERROR: Type valid numbers.")    
    

def coinflip():
    result = random.choice(["Heads", "Tails"])
    print(f"\nThe coin landed on {result}.\n")

def fortune():
    question = input("\nAsk your question here: ")
    if question.lower() in ["will i die today?", "will i die today", "will i die tomorrow", "will i die tomorrow?"]:
        print("\nyes 100% no cap\nSession terminated. Think about the choices you have made today.\n")
        return
    else:
        result  = random.choice(["Yes", "No", "Maybe...", "Solve your own problems do I look like a magic 8 ball to you?", "I'm too lazy to answer ask me again sometime later", "Ask your pet fish I'm sleep deprived."])
        print(f"\nDrum roll please...\nAND the magic-8 ball says...\n{result}\n")
        return
