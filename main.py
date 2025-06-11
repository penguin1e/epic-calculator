import math 
import operator
import time
from function import functions, exponent, factorial, frac_decim, prime_composite, factor, percent_decimal, square_root, hypotenuse, rightangle, area, scicalc, sci_convert, numgen, rolldice, fortune
from games import capitals, game, challenge
import config
import pygame, sys, random
from pygame.locals import QUIT
from collections import deque
from fractions import Fraction 

# OPEN TERMINAL TO TYPE STUFF IT IS NOT DISPLAYED IN THE PYTHON WINDOW

# Feel free to add anything (minigames, more functions) as long as it is calculator related and in Python.

commands = {"exponent": exponent,
            "functions": functions,
            "factorial": factorial,
            "frac decim": frac_decim,
            "prime": prime_composite,
            "gcf lcm": factor,
            "percent decimal": percent_decimal,
            "square root": square_root,
            "hypotenuse": hypotenuse,
            "right angle": rightangle,
            "area": area,
            "scientific": scicalc,
            "sci convert": sci_convert,
            "roll a die": rolldice,
            "random num": numgen,
            "magic ball": fortune
                }
        

while True:
    try:
        num_input = input("\nType first number, type functions to see all possible functions, or type quit to exit: ").lower().strip()
     
        if num_input.lower() == "quit":
            print(config.quitmessage)
            break

        try:
            num = float(num_input)

        except ValueError:
             func = commands.get(num_input)
             if func:
                func()
                continue
             else:
                print(config.syntaxerror)
                continue
        
        nums_input = input("Type second number or type quit to exit: ")

        if nums_input.lower() == "quit":
            print(config.quitmessage)
            break
        
        nums = float(nums_input)
        
    except ValueError:
        print(config.syntaxerror)
       
        
    operation = input("Type operation: ").lower().strip()
    try:
        if operation == "+":
            print(f"\n{num} + {nums} = {num+nums}")
        elif operation == "-":
            print(f"\n{num} - {nums} = {num-nums}")
        elif operation == "*":
            print(f"\n{num} x {nums} = {num*nums}")
        elif operation == "/":
            print(f"\n{num} / {nums} = {num/nums}")
    
        if operation == "magic":
            challenge()
            break
        elif operation == "pong":
            print("\nI see you have found the game. To play it, simply go to your taskbar and click on the window that has the Python logo on it. Press space to start the game. First to 10 wins. Have fun!\n")
            game()
            break
        elif operation == "challenge":
            capitals()
            break
        elif operation == "snake":
            pass
      
        if operation not in ["+", "-", "*", "/", "magic", "pong", "challenge", "snake"]:
            print(config.opserror)

    except ValueError:
        print(config.opserror)

    except ZeroDivisionError:
        print(config.zerodiv)
            
    except OverflowError:
        print(config.matherror)
    continue 
