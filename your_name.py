import random

def guessNumber():
    secretNumber = random.randint(1,20)
    print('I\'m thinking of a number between 1 and 20')
    
    for guesses in range(1,7):
        number = int(input("Enter the number: "))
        if number < secretNumber:
            print("You guessed too low")
        elif number > secretNumber:
            print("You guessed too high")
        else:
            break
    
    if number == secretNumber:
        print("Congrats! You guessed the number in " + str(guesses) + " guesses.")
    else:
        print("Hard luck! The number was " + str(secretNumber))
    

guessNumber()


