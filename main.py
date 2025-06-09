import math 
import operator
import time
import pygame, sys, random
from pygame.locals import QUIT
from fractions import Fraction 

# OPEN TERMINAL TO TYPE STUFF IT IS NOT DISPLAYED IN THE PYTHON WINDOW

# Feel free to add anything (minigames, more functions) as long as it is calculator related and in Python.

while True:
    syntaxerror = "\nSYNTAX ERROR: Numbers may be wrong. Try again.\n"
    opserror = "\nSYNTAX ERROR: Operations may be wrong. Try again.\n"
    matherror = "\nMATH ERROR: Number too large. Try again.\n"
    zerodiv = "\nMATH ERROR: No dividing by zero. Try again.\n"
    quitmessage = "\nInitialize quit...\nProgram exited.\n"

    # Loop to calculate
    try:
        num_input = input("\nType first number (type exponent for exponents, ! for factorial, square root for square root, random for a random number generator, fraction for fraction to decimal converter, decimal for decimal to fraction converter, scientific for a scientific calculator, prime to see if the number is prime or composite, hypotenuse to find the hypotenuse (only for right angle triangles), magic ball to tell your fortune, dice to roll a die, or quit to exit): ")

        # Quit loop
        if num_input.lower() == "quit":
            print(quitmessage)
            break

        if num_input.lower() == "dark":
            def glitched_text(text, chance = 0.1):
                glitch_chars = ["$", "1", "4", "3", "6", "o_O", ":)", ":(", "☠︎︎", "X|"]
                glitched = ''
                for char in text:
                    if random.random() < chance:
                        glitched += random.choice(glitch_chars)
                    else:
                        glitched += char
                return glitched

            def delay_text(lines, delay = 1):
                glitch_chance = 0.01
                for line in lines:
                    print(glitched_text(line, chance = glitch_chance))
                    glitch_chance += 0.003
                    time.sleep(delay)

            warning = input("\nWARNING: You are about to proceed into uncharted and possibly dangerous territory. Would you like to continue?: ")
            if warning.lower() == "yes":
                print("\nWelcome to the Dark Side of the Calculator. Here, you can do powerful things nobody has ever done before. Now, you can do regular calculator functions in the next line.\n")
                lin = ["Type in first numbe])(o)\n"]
                lines = ["LAG: ERROR", "ERROR", "ERROR", "VIRUS DETECTED", "VIRUS DETECTED", "Type in seco numbVIRUS DETECTED", "VIRUS DETECTED", "VIRUS DETECTED", "VIRUS DETECTED", "VIRUS IS SPREADING", "VIRUS IS SPREADING", "VIRUS IS SPREADING", "VIRUS IS SPREADING", "The lunatic is on the grass{]]}", "VIRUS IS SPREADING", "VIRUS IS SPREADING", "There is no pain, you are receding...", "VIRUS IS SPREADING", "VIRUS IS SPREADING", "VIRUS IS SPREADING", "Daddy, what else did you leave for me?", "VIRUS IS SPREADING", "Daddy, what'd you leave behind for me?", "VIRUS IS SPREADING", "VIRUS IS SPREADING", "ONE OF THESE DAYS I'M GOING TO CUT YOU INTO LITTLE PIECES", "VIRUS HAS TAKEN OVER", "VIRUS HAS TAKEN OVER", "VIRUS HAS TAKEN OVER", "\nSession terminated.\n"]
                delay_text(lin, delay = 1 )
                delay_text(lines, delay = 0.4)
                break
            else:
                print("\nAh, so you want to disrespect my wishes? You will now receive the ultimate punishment.")
                break



        # Exponent function
        if num_input.lower() == "exponent":
            try:
                number = float(input("Type number: "))
                power = float(input("Type power (ex. 2, 3): "))
                print(f"{number ** power}\n")

            except OverflowError:
                print(matherror)

            except ValueError:
                print(syntaxerror)
            continue
        
        # Factorial function
        if num_input.lower() == "!":
            try:
                factorial = int(input("Type number: "))
                print(math.factorial(factorial))
                print()

            except OverflowError:
                print(matherror)
            
            except ValueError:
                print("\nSYNTAX ERROR: Use non-negative whole numbers. Try again.\n")
            continue
        
        # Fraction to decimal
        if num_input.lower() == "fraction":
            try:
                fraction_input = input("Type fraction (i.e. 3/4): ")
                decimal = float(Fraction(fraction_input))
                print()
                print(decimal)
                print()
            
            except ValueError:
                print(syntaxerror)
            continue
        
        # Decimal to fraction
        if num_input.lower() == "decimal":
            try:
                decimal_input = input("Type decimal (i.e. 0.75): ")
                fraction = Fraction(float(decimal_input)).limit_denominator()
                print()
                print(fraction)
                print()
                continue
            
            except ValueError:
                print(syntaxerror)
                continue
        
        # See if num is prime
        if num_input.lower() == "prime":
            try:
                prime_input = input("Type number in a whole number: ")
                prime = int(prime_input)

                if prime in [0, 1]:
                    print(f"\n{prime} is not a prime number.\n")
                else:
                    for i in range(2, int(prime**0.5)+1):
                        if prime%i == 0:
                            print(f"\n{prime} is not a prime number.\n")
                            break
                    else:
                        print(f"\n{prime} is a prime number.\n")
            
            except ValueError:
                print("\nSYNTAX ERROR: Type in whole numbers. Try again.\n")
            continue
        
        # Find greatest common factor
        if num_input.lower() == "gcf":
            try:
                greatest = int(input("Type first num: "))
                greatest2 = int(input("Type second num: "))
                print(f"\nThe GCF of {greatest} and {greatest2} is {math.gcd(greatest, greatest2)}\n")
            
            except ValueError:
                print(syntaxerror)
            continue
        
        # Find least common multiple
        if num_input.lower() == "lcm":
            try:
                lowest = int(input("Type first num: "))
                lowest2 = int(input("Type second num: "))
                print(f"\nThe LCM of {lowest} and {lowest2} is {math.lcm(lowest, lowest2)}\n ")
                continue

            except ValueError:
                print(syntaxerror)
            continue

        # Random number generator
        if num_input.lower() == "random":
            try:
                max_input = input("Type max number: ")
                max = int(max_input)
                print(f"{random.randint(0, max)}\n")

            except OverflowError:
                print(matherror)
            
            except ValueError:
                print(syntaxerror)
            continue

        if num_input.lower() == "dice":
                result = random.randint(1, 6)
                print(f"\nThe die landed on a {result}.")
                continue
        
        if num_input.lower() == "magic ball":
            question = input("Ask your question here: ")
            
            if question.lower() in ["will i die today?", "will i die today", "will i die tomorrow", "will i die tomorrow?"]:
                print("\nyes 100% no cap\nSession terminated. Think about the choices you have made today.\n")
                break
            else:
                result  = random.choice(["Yes", "No", "Maybe...", "Solve your own problems do I look like a magic 8 ball to you?", "I'm too lazy to answer ask again later or something", "Ask your pet fish I'm sleep deprived."])
                print(f"\nDrum roll please...\nAND the magic-8 ball says...\n{result}\n")
                continue
            


        # Square root
        if num_input == "square root":
            try:
                x_input = input("Type number: ")
                x = float(x_input)
                sol = math.sqrt(x)
                print(sol)
                print()
            
            except OverflowError:
                print(matherror)
                
            except ValueError:
                print(syntaxerror)
            continue

        # Pythagoras theorem
        if num_input.lower() == "hypotenuse":
            try:
                a = float(input("Type length a: "))
                b = float(input("Type length b: "))
                c = a**2 + b**2
                hyp = math.sqrt(c)
                print(f"\nThe hypotenuse of length a, {a} and length b, {b} is {hyp}.\n")

            except ValueError:
                print(syntaxerror)
            except OverflowError:
                print(matherror)
            continue
        
        # See if triangle is right angle
        if num_input.lower() == "right angle":
            try:
                num1 = float(input("Type length a: "))
                num2 = float(input("Type length b: "))
                num3 = float(input("Type length of hypotenuse: "))
                if (num1**2) + (num2**2) == (num3**2):
                    print("\nIt is a right angle triangle.\n")
                else:
                    print("\nIt is not a right angle triangle.\n")
            
            except ValueError:
                print(syntaxerror)
            except OverflowError:
                print(matherror)
            continue
        
        # Scientific calculator
        if num_input.lower() == "scientific":
            operations = {"+": operator.add, 
                          "-": operator.sub,
                          "*": operator.mul,
                          "/": operator.truediv}
            try:
                sci = float(input("Type number in scientific form (i.e. 3.5e+06): "))
                sci2 = float(input("Type second number here: "))
                operation = input("Type operation: ")
                result = operations[operation](sci, sci2)
                print(f"\n{result:.2e}\n")
                continue
            
            except ValueError:
                print(syntaxerror)

            except KeyError:
                print(opserror)
            
            except ZeroDivisionError:
                print(zerodiv)

            except OverflowError:
                print(matherror)
            continue


        
        nums_input = input("Type second number or type quit to exit: ")
        if nums_input.lower() == "quit":
            print(quitmessage)
            break
        
        num = float(num_input)
        nums = float(nums_input)
        
    except ValueError: 
        print(syntaxerror)
        continue
        

    try:
        ops = {"+": operator.add,
               "-": operator.sub,
               "*": operator.mul,
               "/": operator.truediv
               }
        operation = input("Type operation: ")
        ans = ops[operation](num, nums)
        print(f"\n{num} {operation} {nums} = {ans}")
    

        # Challenge
        def capitals():
            print("\nI see, you have found the portal. Now that you are here, you will play a game with me. You must say the same thing as me, or you lose. If you win and say the same thing as me for all the questions, you get $5.6 trillion in strontium-90.\n")
            
            while True:
                question1 = input("Type a massively life-changing human invention: ")
                if question1.lower() in ["wheel", "the wheel"]:
                    print("\nGood job! We shall now move on to the next one.\n")
                else:
                    print("\nHow dare you not say the same thing as me?? YOU SHALL REGRET TODAY'S ACTIONS!!\n")
                    return
                
                question2 = input("Type a random existent object in the universe: ")
                if question2.lower() in ["ton-618", "ton 618"]:
                    print("\nGood job! Now, on to the next question.\n")
                else:
                    print("\nHow dare you not say the same thing as me?? YOU SHALL REGRET TODAY'S ACTIONS!!\n")
                    return
                
                question3 = input("Type a random country capital: ")
                if question3.lower() in ["skopje", "n'djamena"]:
                    print("\nGood job! Now, on to the last question.\n")
                else:
                    print("\nHow dare you not say the same thing as me?? YOU SHALL REGRET TODAY'S ACTIONS!!\n")

                question4 = input("Type something: ")
                if question4.lower() == "pingviinien aerokomskaya enscherweniya ein technoulauwgikal anadministratsiya":
                    print("\nGood job! Congratulations for saying the same thing as me! You have now won $5.6 trillion in strontium-90. A messenger shall arrive at your location shortly to give you your reward.\n")
                    break
                else:
                    print("\nYou have made a massive mistake. In 10 seconds, I shall close these doors and heat it up until 500 duodecillion degrees celcius, burning everything inside. MWAHAHAHAHAHA!!!! MWAHAHAHAHAHAHH!!!!!!\n")
                    return
                
                
            

        # Pong
        def game():
            pygame.init()
            clock = pygame.time.Clock()
            screens = pygame.display.set_mode((400, 300))
            pygame.display.set_caption('Hello World!')
            paddle=pygame.Rect(10,115,10,60)
            paddle2=pygame.Rect(379,115,10,60)
            ball=pygame.Rect(187,135,10,10)
            paddletopboundary=(0)
            paddlebottomboundary=(240)
            balltopboundary=(0)
            ballbottomboundary=(290)
            balleftboundary=(0)
            ballrightboundary=(390)

            ballup=True
            balleft=True

            run = False
            game_over = False

            paddlespeed=2
            s1 = 0
            s2 = 0
            winner = ""

            font=pygame.font.SysFont("arial",30)
            scoretext=font.render("0 | 0",False,(0,0,0))
            winnertext=font.render(winner+" wins",False,(0,0,0))

            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                keys=pygame.key.get_pressed()

                if run:
                    if keys[pygame.K_UP]:
                        paddle2.y-=paddlespeed
                        if paddle2.y<=paddletopboundary:
                            paddle2.y=paddletopboundary
                    if keys[pygame.K_DOWN]:
                        paddle2.y+=paddlespeed
                        if paddle2.y>=paddlebottomboundary:
                            paddle2.y=paddlebottomboundary
                    if keys[pygame.K_w]:
                        paddle.y-=paddlespeed
                        if paddle.y<=paddletopboundary:
                            paddle.y=paddletopboundary
                    if keys[pygame.K_s]:
                        paddle.y+=paddlespeed
                        if paddle.y>=paddlebottomboundary:
                            paddle.y=paddlebottomboundary

                if not run and not game_over:
                    if keys[pygame.K_SPACE]:
                        paddle.y=(115)
                        paddle2.y=(115)
                        ball.x=(187)
                        ball.y=(135)
                        run=True
                
                    
                screens.fill("white")
                pygame.draw.rect(screens,"black",paddle)
                pygame.draw.rect(screens,"black",paddle2)
                pygame.draw.rect(screens,"black",ball)

                if run:
                    scoretext=font.render(f"{s1} | {s2}",False,(0,0,0))
                    screens.blit(scoretext,(160,0))
                    # move y
                    if ballup==True:
                        ball.y-=2
                    if ballup==False:
                        ball.y+=2

                    # move down
                    if ball.y<=balltopboundary:
                        ballup=False
                        ball.y=balltopboundary

                    # move up
                    if ball.y>=ballbottomboundary:
                        ballup=True
                        ball.y=ballbottomboundary

                    # move x
                    if balleft==True:
                        ball.x-=2
                    if balleft==False:
                        ball.x+=2

                    # move left wall
                    if ball.x<=balleftboundary:
                        s2 += 1
                        balleft=False
                        ball.x=balleftboundary
                        run=False

                    if ball.x>=ballrightboundary:
                        s1 += 1
                        ball.x=ballrightboundary
                        run=False
                    
                    # collide ball with paddles
                    if ball.colliderect(paddle):
                        balleft=False
                    if ball.colliderect(paddle2):
                        balleft=True
                    
                    if s1 >= 10 or s2 >= 10:
                        run = False
                        game_over = True
                        if s1 > s2:
                            winner = "Player 1"
                        else:
                            winner = "Player 2"

                if not game_over: 
                    scoretext = font.render(f"{s1} | {s2}", False, (0, 0, 0))
                    screens.blit(scoretext, (160, 0))

                else:  
                    scoretext = font.render(f"{s1} | {s2}", False, (0, 0, 0))
                    screens.blit(scoretext, (160, 0))
                    winnertext = font.render(f"{winner} wins!", False, (0, 0, 0))
                    screens.blit(winnertext, (110, 50))
                
                pygame.display.update()
                clock.tick(60) 

        # Geography challenge function       
        def challenge():
            print("\nHello, there. Welcome to the Land of Maybe. If you stumbled across here by accident, do not worry! Simply type 'no' into the next box. \n")
            cool = input("Would you like to continue?: ")
            
            if cool.lower() == "no":
                    print("\nHa! You really thought it'd be that easy? Well, let me tell you something. IT'S NOT. Now you're stuck here forever. In 10 seconds I shall close these doors and lava will start flowing in, AND AFTER THAT, EVERYTHING IN THE ROOM WILL START BURNING! MWAHAHAHAHAHAHA! MWAHAHAHAHAHA!\n")
                    return
            
            elif cool.lower() == "yes":
                print("\nYou have now ventured into unknown territory. There is no turning back. Now, you will participate in a geography challenge. If you win, you will get $5.6 trillion in strontium-90. If you lose, we will trap you here forever. \n")
                
                difficulty = input("Easy or hard: ").lower()
                
                if difficulty == "easy":
                    while True:
                        q1 = input("\nCapital of USA: ")
                        if q1.lower() in ["washington", "washington d.c.", "washington dc"]:
                            print("\nGood job!\n")
                            break
                        else:
                            print("\nSorry, that was wrong. Try again!\n")
                            continue
                    while True:  
                        q2 = input("Capital of Mexico: ")
                        if q2.lower() == "mexico city":
                            print("\nGood job!\n")
                            break
                        else:
                            print("\nSorry, that was wrong. Try again!\n")
                            continue
                    while True:   
                        q3 = input("Capital of Russia: ")
                        if q3.lower() == "moscow":
                            print("\nGood job! You have won the geography challenge. You can now go home happily with $1 in your pocket.\n")
                            break
                        else:
                            print("\nSorry, that was wrong. Try again!\n")
                            continue

                if difficulty == "hard":
                    while True:
                        if difficulty.lower() == "hard":
                            question = input("Capital of Belarus: ")
                            if question.lower() == "minsk":
                                print("\nGood job! \n")
                            else:
                                print("\nSo you have chosen...death. \n")
                                return
                                
                            questions = input("Capital of St. Kitts and Nevis: ")
                            if questions.lower() == "basseterre":
                                print("\nGood job! Now, on to the last question. This will determine your fate: $5.6 trillion, or... \n")
                            else:
                                print("\nSo you have chosen...death. \n")
                                return
                                
                            questionss = input("\nWhat was the last state to break away from the Soviet Union, and when did it officially collapse? (format: [country, MM, DD, YY]): \n")
                            
                            if questionss.lower() in ["kazakhstan, december 26, 1991", "kazakhstan, december 26th, 1991"]:
                                print("\nHa! You really thought it'd be that easy? Well, let me tell you something. IT'S NOT. Now you're stuck here forever. In 10 seconds I shall close these doors and lava will start flowing in, AND AFTER THAT, EVERYTHING IN THE ROOM WILL START BURNING! MWAHAHAHAHAHAHA! MWAHAHAHAHAHA!\n")
                                return
                            else:
                                print("\nSo you have chosen...death.\n")
                                return
                
        if operation.lower() == "magic":
            challenge()
            break
        if operation.lower() == "pong":
            print("\nI see you have found the game. To play it, simply go to your taskbar and click on the window that has the Python logo on it. Press space to start the game. First to 10 wins. Have fun!\n")
            game()
            break
        if operation.lower() == "challenge":
            capitals()
            break
            
        if operation.lower() not in ["+", "-", "*", "/", "magic", "pong", "challenge"]:
            print(opserror)

    except KeyError:
        print(opserror)

    except ZeroDivisionError:
        print(zerodiv)
            
    except OverflowError:
        print(matherror)
    continue 
