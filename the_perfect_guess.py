# Import Random Module
import random
# Genrate Random Number
randomNumber = random.randint(1, 100)
# print(randomNumber)
userInput = None
guesses = 0

# While loop for multiple guess input
while (userInput != randomNumber):

    # Enter number from user
    userInput = int(input("enter a number: "))
    guesses += 1

    # Condition1:
    if (randomNumber == userInput):
        print("You guess it correct")
    else:
        # Condition 2
        if(userInput > randomNumber):
            print("Enter a smaller number coz you enter larger number")
        else:
            print("Enter a larger number coz you enter smaller number")

print(f"Your total guesses is{guesses}")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses < hiscore):
    print("*** You broke the high score! ***")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))