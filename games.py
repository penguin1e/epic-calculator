import pygame
from pygame.locals import QUIT
import sys


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