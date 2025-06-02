import math 
import pygame, sys, random
from pygame.locals import QUIT

# OPEN TERMINAL TO TYPE STUFF IT IS NOT DISPLAYED IN THE PYTHON WINDOW

while True:
    try:
        num_input = input("Type first number (type exponent for exponents, ! for factorial, or quit to exit): ")
        if num_input.lower() == "quit":
            print("\nCALCULATOR PROGRAM: Initialize quit...\nProgram exited.")
            break
        if num_input.lower() == "exponent":
            try:
                number = float(input("Type number: "))
                power = float(input("Type power (ex. 2, 3): "))
                print(number ** power)
            except OverflowError:
                print("MATH ERROR: Number too large. Try again.", "\n")
            except ValueError:
                print("\nSYNTAX ERROR: Number or exponent may be wrong. Try again", "\n")
            continue
        
        if num_input.lower() == "!":
            try:
                factorial = int(input("Type number: "))
                print(math.factorial(factorial))
                continue
            except OverflowError:
                print("\nMATH ERROR: Number too large. Try again.", "\n")
                continue
            except ValueError:
                print("\nSYNTAX ERROR: Type in an non-negative whole number. Try again.", "\n")
                continue
        
        nums_input = input("Type second number or type quit to exit: ")
        if nums_input.lower() == "quit":
            print("CALCULATOR PROGRAM: Initialize quit...\nProgram exited.", "\n")
            break
        
        num = float(num_input)
        nums = float(nums_input)
        
    except ValueError: 
        print("\nSYNTAX ERROR: Numbers may be wrong. Try again.", "\n")
        continue
        
    operation = input("Type operation: ")
    print()
    try:
        if operation == "+":
            print(f"{num} + {nums} = {num + nums}\n")
        elif operation == "-":
            print(f"{num} - {nums} = {num - nums}\n")
        elif operation == "*":
            print(f"{num} x {nums} = {num * nums}\n")
        elif operation == "/":
            if nums == 0:
                print("\nMATH ERROR: No dividing by zero. Try again.")
            else:
                print(f"{num} / {nums} = {num / nums}\n")

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
            run=True
            paddlespeed=2
            s1=0
            s2=0
            winner=""
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
                else:
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
                    screens.blit(scoretext,(150,0))
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
                        balleft=False
                        ball.x=balleftboundary
                        run=False
                    if ball.x>=ballrightboundary:
                        ball.x=ballrightboundary
                        run=False
                    
                    # collide ball with paddles
                    if ball.colliderect(paddle):
                        balleft=False
                    if ball.colliderect(paddle2):
                        balleft=True
                    # score
                    if ball.x<=balleftboundary:
                        s2+=1
                    if ball.x>=ballrightboundary:
                        s1+=1       
                    if s1==10 or s2==10:
                        run=False
                    # winner
                else:
                    if s1>=10 and s1>s2:
                        winner="Player 1"
                        print(winner+" wins.")
                        winnertext=font.render(winner+" wins",False,(0,0,0))
                        screens.blit(winnertext,(100,40))

                    if s2>=10 and s2>s1:
                        winner="Player 2"
                        print(winner+" wins.")
                        winnertext=font.render(winner+" wins.",False,(0,0,0))
                        screens.blit(winnertext,(100,40))

                    screens.blit(scoretext,(150,0))
                    


                
                pygame.display.update()
                clock.tick(60) 

                
        def challenge():
            print("Hello, there. Welcome to the Land of Maybe. If you stumbled across here by accident, do not worry! Simply type 'no' into the next box. \n")
            cool = input("Would you like to continue?: ")
            
            if cool.lower() == "no":
                    print("Ha! You really thought it'd be that easy? Well, let me tell you something. IT'S NOT. Now you're stuck here forever. In 10 seconds I shall close these doors and lava will start flowing in, AND AFTER THAT, EVERYTHING IN THE ROOM WILL START BURNING! MWAHAHAHAHAHAHA! MWAHAHAHAHAHA!\nSHOULD DEATH AWAIT YOU.\n- FREDDIE MERCURY\n SEE YOU IN HECK YOU LITTLE FOOL!, \n")
                    return
            
            elif cool.lower() == "yes":
                print("\nYou have now ventured into unknown territory. There is no turning back. Now, you will participate in a geography challenge. If you win, you will get $5.6 trillion in strontium-90. If you lose, we will trap you here forever. \n")
                
                difficulty = input("Easy or hard: ").lower()
                
                if difficulty == "easy":
                    while True:
                        q1 = input("Capital of USA: ")
                        if q1.lower() in ["washington", "washington d.c.", "washington dc"]:
                            print("Good job!")
                            break
                        else:
                            print("Sorry, that was wrong. Try again!")
                            continue
                    while True:  
                        q2 = input("Capital of Mexico: ")
                        if q2.lower() == "mexico city":
                            print("Good job!")
                            break
                        else:
                            print("Sorry, that was wrong. Try again!")
                            continue
                    while True:   
                        q3 = input("Capital of Russia: ")
                        if q3.lower() == "moscow":
                            print("Good job! You have won the geography challenge. You can now go home happily with $1 in your pocket.")
                            break
                        else:
                            print("Sorry, that was wrong. Try again!")
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
                                print("Ha! You really thought it'd be that easy? Well, let me tell you something. IT'S NOT. Now you're stuck here forever. In 10 seconds I shall close these doors and lava will start flowing in, AND AFTER THAT, EVERYTHING IN THE ROOM WILL START BURNING! MWAHAHAHAHAHAHA! MWAHAHAHAHAHA!\nSHOULD DEATH AWAIT YOU.\n- FREDDIE MERCURY\n SEE YOU IN HECK YOU LITTLE FOOL!, \n")
                                return
                            else:
                                print("So you have chosen...death.\n")
                                return
                
        if operation.lower() == "magic":
            challenge()
            break
        if operation.lower() == "pong":
            print("I see you have found the game. To play it, simply go to your taskbar and click on the window that has the Python logo on it. Press space to start the game. Have fun!")
            game()
            break
            
        if operation.lower() not in ["+", "-", "*", "/", "magic"]:
            print("SYNTAX ERROR: Operations may be wrong. Try again.")
            
    except OverflowError:
        print("\nMATH ERROR: Number too large. Try again. \n")
        continue 
