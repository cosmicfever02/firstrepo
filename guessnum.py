import random as rdm

def game(name="Player"):
    name = name.title()
    wins = 0
    rounds = 0
    def numguessGame():
        nonlocal wins, rounds
        rounds += 1

        #3-3-24, Improved guess input
        inputCheck = False
        while inputCheck == False:
            print("What number am i thinking of? 1, 2 or 3?")
            numGuess = input("Enter your guess: ")
            if numGuess not in ["1","2","3"]:
                print("\nGuess must be within 1, 2 and 3!")
                continue
            else:
                numGuess = int(numGuess)
                inputCheck = True
        
        num = rdm.randint(1, 3)

        if numGuess == num:
            print(f"{name}, you are correct!")
            wins += 1
        elif numGuess != num:
            print(f"{name}, you are incorrect! It was {num}")
        
        print(f"\nYour wins: {wins}")
        print(f"Rounds: {rounds}")
        print(f"Your win percentage: {wins / rounds:.2%}")
        print("--------")

    return numguessGame
