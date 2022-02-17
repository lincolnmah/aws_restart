import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number and you will try and to guess it.")
number=random.randint(1,10)
isGuessRight=False
#if the user has not guessed the correct answer, enter the loop
while isGuessRight !=True:
    #ask the user for a guess
    guess=input ("Guess a number between 1 and 10: ")
    #is the guess the correct number?
    if int(guess)==number:
        #if the correct guess, tell the user it was the corrrect guess and exit the loop
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight=True
    else:
        #if the wrong guess, tell the user it was the wrong guess and continue the lopp
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))