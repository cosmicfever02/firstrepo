# -- Global Arrays/Lists --
studentInfo = []
allScores = []
print("normal version\n")
# studentInfo = ['john', 'joe', 'jake']
# allScores = [97, 76, 9]

# -- Functions/Procedures --
def displayMenu():
    
    while True:
        print("____________________")
        print("""
    Enter choice:
            1. Add new student
            2. Add student scores
            3. View student names and scores
            4. View highest, lowest and average marks
            5. Exit
    """)

        choice = input("    > ")

        print("____________________\n")
        match choice: # its like if else
            case "1":
                addNew()
            case "2":
                studentScore()
            case "3":
                displayNameScore()
            case "4": 
                highestLowest()
            case "5":
                return
            case _: # default response
                print("Invalid choice, try again")


def addNew(sInfo = studentInfo):

    name = input("Enter student name: ")
    while len(name) > 20 or len(name) < 1:
        print("Max 20 characters, try again")
        name = input("Enter student name: ")
    
    sInfo.append(name)


def studentScore(allScores = allScores):

    score = int(input("Enter scores in order: "))
    while score > 100 or score < 0:
        print("Must be 0-100")
        score = int(input("Enter score: "))
    
    allScores.append(score)


def displayNameScore(sInfo = studentInfo, allScores = allScores): # displays name and score like excel

    print(f"Names{' ' * 16}|Scores")
    print("-" * 30)
    for count in range(len(sInfo)):
        name = sInfo[count]
        score = allScores[count]
        if score == "":
            score = "N/A"

        print(f"{name}{' ' * (20 - len(name))} |{score}")


def highestLowest(allScores = allScores):

    highest = 0
    lowest = 999

    for score in allScores:
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")

# -- Main code --
displayMenu()