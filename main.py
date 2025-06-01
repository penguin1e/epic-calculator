import math 

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
            
        if operation.lower() not in ["+", "-", "*", "/", "magic"]:
            print("SYNTAX ERROR: Operations may be wrong. Try again.")
            
    except OverflowError:
        print("\nMATH ERROR: Number too large. Try again. \n")
        continue 
