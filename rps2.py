import random as rdm

def game(name="Player"):
    name = name.title()
    wins = 0
    compWins = 0
    rounds = 0
    def rpsGame():
        nonlocal wins, compWins, rounds
        rounds += 1
        choices = {
            1 : "rock",
            2 : "paper",
            3 : "scissor"
        }
        while True:
            userInput = input("\nRock, paper or scissor? \n>")
            userInput = userInput.lower()
            if userInput in ["rock", "1", "paper", "2", "scissor", "3"]:
                break
            elif userInput == "stop": #<--- for testing
                from sys import exit
                exit("----Exited-----")
            else:
                print("Try again")


        compChoice = rdm.randint(1, 3)
        print(f"Computer chose {choices[compChoice]}\n")

        if userInput in ["Rock", "rock", "1"] and compChoice == 3:
            print(f"{name} won!")
            wins += 1
        elif userInput in ["Paper", "paper", "2"] and compChoice == 1:
            print(f"{name} won!")
            wins += 1
        elif userInput in ["Scissor", "scissor", "3"] and compChoice == 2:
            print(f"{name} won!")
            wins += 1
        elif userInput == choices[compChoice] or userInput == str(compChoice):
            print("Tie!")
        else:
            print("Computer wins!")
            compWins += 1

        print(f"\n{name} has {wins} wins\nComputer has {compWins} wins")
        print(f"Rounds played: {rounds}")
        print(f"Win percentage: {wins / rounds:.2%}")
        
        print("---------")

    return rpsGame


