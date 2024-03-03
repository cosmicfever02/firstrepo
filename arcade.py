import rps2 as rps
import guessnum as nguess
from sys import exit
#3-3-24, Improved inputs for name in arcade and guess in guessnum

nameCheck = False
while nameCheck == False:
    name = input("Enter your name: ")
    if len(name) < 3:
        print("Name must be at least 3 characters long!")
        continue
    elif len(name) > 25:
        print("Name can have a max of 25 characters!")
        continue
    else:
        name = name.title()
        print(f"Hello {name}!")
        nameCheck = True

def gameChoice():
    while True:
        gameChosen = input("Select game: \n[1] - Rock Paper Scissors\n[2] - Guess the Number \n[3] - Exit \n> ")

        if gameChosen not in ["1", "2", "3"]:
            print("Try again")
        elif gameChosen == "3":
            exit(f"Goodbye {name}!")
        else:
            gameChosen = int(gameChosen)
            break
    return gameChosen

def playGame(name, gameChosen):
    playAgain = "yes"
    if gameChosen == 1:
        rpsU = rps.game(name)
        while playAgain == "yes":
            rpsU()
            while True:
                playAgain = input("Do you want to play again?\n>")
                playAgain = playAgain.lower()
                if playAgain == "yes":
                    break
                elif playAgain == "no":
                    print("Returning to main menu...\n")
                    break
                else:
                    print("Try again")
    else:
        nguessU = nguess.game(name)
        while playAgain == "yes":
            nguessU()
            while True:
                playAgain = input("Do you want to play again?\n>")
                playAgain = playAgain.lower()
                if playAgain == "yes":
                    break
                elif playAgain == "no":
                    print("Returning to main menu...\n")
                    break
                else:
                    print("Try again")

x = True
while x == True:
    gameChosen = gameChoice()
    print("--------------------------")
    playGame(name, gameChosen)
