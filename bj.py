import random

playerHold = 0

def Draw():
    return random.randint(1,13)

def Main(*args, **kwargs):
    global playerHold
    over = False
    playerHold += Draw()
    print(f"your first card is {playerHold}")
    while not over:
        drawAgain = input(f"draw again? your current hold is {playerHold} ").lower()
        if drawAgain[0] == "y":
            playerHold += Draw()
            if playerHold < 21:
                continue
        over = True


    botHold = random.randint(14,24)
    print("\n")
    if playerHold > 21:
        print(f"you lost bcs ur hold is {playerHold} and it is above 21 haha noob")
    elif playerHold == 21:
        print("you won bcs ur hold is 21")
    else:
        if botHold > 21:
            print(f"you won bcs your bots hold is {botHold} and it is above 21, your hold is {playerHold}")
        elif botHold > playerHold:
            print(f"you lost bcs bot hold is bigger than yours {botHold} > {playerHold}")
        elif playerHold > botHold:
            print(f"you won bcs your hold is bigger than bots {playerHold} > {botHold}")
        else:
            print(f"it is a draw {playerHold} = {botHold}")





Main()