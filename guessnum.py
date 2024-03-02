import random as rdm

def game(name="Player"):
    name = name.title()
    wins = 0
    rounds = 0
    def numguessGame():
        nonlocal wins, rounds
        rounds += 1

        print("What number am i thinking of? 1, 2 or 3?")
        numGuess = int(input("Enter your guess: "))
        
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







