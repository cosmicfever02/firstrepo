import random as rdm

def game(name="Player"):
    name = name.title()
    wins = 0
    rounds = 0

    numMax = 10 #(for easier customizability) pick from 1 to (numMax) 3-3-24
    def numguessGame():
        nonlocal wins, rounds
        rounds += 1

        def numbers():
            nonlocal numMax
            numlist = []
            for x in range(1, numMax + 1):
                numlist.append(str(x))
            return numlist
        
        #improved input 3-3-24
        inputCheck = False
        while inputCheck == False:
            print(f"What number am i thinking of? Pick a number from 1 to {numMax}!")
            numGuess = input("Enter your guess: ")
            if numGuess not in numbers():
                print(f"\nGuess must be within 1-{numMax}!")
                continue
            else:
                numGuess = int(numGuess)
                inputCheck = True
        
        num = rdm.randint(1, numMax)

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

if __name__ == "__main__":
    nguess = game()
    nguess()

    return numguessGame
